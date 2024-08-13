from transformers import AutoTokenizer, AutoModelForCausalLM, TrainingArguments, Trainer
from transformers import TrainerCallback
from ray import tune, init, shutdown, train
import torch
import pandas as pd
from datasets import Dataset
from sklearn.model_selection import train_test_split

# import pdb; pdb.set_trace()
result_df = pd.read_excel('/mnt/data1/imai_phase3_genAI_api/webservices/static/dataset_1562_records.xlsx')
print("result_df.columns  ",result_df.columns)
print("shape of resut_df  ",result_df.shape)


result_df = result_df.rename(columns={'question': 'Question', 'answer': 'Answer'})
print("result_df.columns  ",result_df.columns)
print("shape of resut_df  ",result_df.shape)

result_df = result_df[['Question', 'Answer']]
print("result_df.columns  ",result_df.columns)
train_data, test_data = train_test_split(result_df, train_size=0.8, random_state=42)
print("shape of train_data ", train_data.shape)
print("shape of test_data ", test_data.shape)

class TuneReportCallback(TrainerCallback):
    """Custom Callback for Hugging Face Trainer to report metrics to Ray Tune using ray.train.report."""
    def on_evaluate(self, args, state, control, metrics=None, **kwargs):
        train.report({"eval_loss": metrics["eval_loss"]})
        
def tokenize_and_prepare_datasets(tokenizer, data):
    try:
        def tokenize_function(examples):
            concatenated_texts = [q + tokenizer.eos_token + a for q, a in zip(examples['Question'], examples['Answer'])]
            return tokenizer(concatenated_texts, max_length=1024, truncation=True, padding="max_length", return_tensors="pt")

        tokenized_data = [tokenize_function(row) for _, row in data.iterrows()]
        dataset = Dataset.from_dict({
            "input_ids": [x["input_ids"][0] for x in tokenized_data],
            "attention_mask": [x["attention_mask"][0] for x in tokenized_data],
            "labels": [x["input_ids"][0] for x in tokenized_data]
        })
        return dataset
    except Exception as e:
        print(f"Failed to tokenize and prepare datasets: {e}")
        raise

def train_model(config):
    tokenizer = AutoTokenizer.from_pretrained("nlp-waseda/comet-gpt2-small-japanese")
    model = AutoModelForCausalLM.from_pretrained("nlp-waseda/comet-gpt2-small-japanese")


    train_dataset = tokenize_and_prepare_datasets(tokenizer, train_data)
    test_dataset = tokenize_and_prepare_datasets(tokenizer, test_data)

    training_args = TrainingArguments(
        output_dir='/mnt/data1/imai_phase_4/model_files/hpt_nlp_waseda',
        learning_rate=config["learning_rate"],
        per_device_train_batch_size=config["per_device_train_batch_size"],
        num_train_epochs=config["num_epochs"],
        do_eval=True,
        evaluation_strategy="epoch",
        logging_dir='/mnt/data1/imai_phase_4/model_files/logs_hpt_nlp_waseda',
        logging_steps=10,
        weight_decay=config["weight_decay"],
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=test_dataset,
        callbacks=[TuneReportCallback()]
    )

    trainer.train()
    
search_space = {
    "learning_rate": tune.loguniform(1e-5, 5e-5),
    "per_device_train_batch_size": tune.choice([2,4,8]),
    "num_epochs": tune.choice([1]),
    "weight_decay": tune.uniform(0.0, 0.3)
}

init(ignore_reinit_error=True)

analysis = tune.run(
    train_model,
    config=search_space,
    num_samples=3,
    resources_per_trial={'cpu': 1, 'gpu': 1},
    progress_reporter=tune.CLIReporter(parameter_columns=["learning_rate", "per_device_train_batch_size", "num_epochs"]),
    metric="eval_loss",
    mode="min",
    verbose=3,
)

best_config = analysis.get_best_config(metric="eval_loss", mode="min")
print("Best hyperparameters found were: ", best_config)
