import torch
import datetime
import pandas as pd
from datasets import Dataset
from transformers import (
    AutoTokenizer, 
    GPT2LMHeadModel,
    TrainingArguments,
    Trainer,
    DataCollatorForLanguageModeling
)
from sklearn.model_selection import KFold
# from preprocess_wiki_content import PrepareModelDataset

# dataset_obj = PrepareModelDataset()

timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

# Load the dataset
dataset_path = '/mnt/data1/imai_phase3_genAI_api/webservices/static/dataset_1200_records.xlsx'
dataset = pd.read_excel(dataset_path)
dataset = dataset[:100]

# df = dataset_obj.preprocess_data()
# dataset = df[['question', 'final_processed_content_x0001']].rename(columns={'final_processed_content_x0001': 'answer'})

import pdb; pdb.set_trace()
print("shape of the data set ",dataset.shape)
print("dataset.column  ",dataset.columns)

hf_dataset = Dataset.from_pandas(dataset)
print('shape of hf_dateset', hf_dataset.shape)

MODEL_NAME = 'nlp-waseda/comet-gpt2-small-japanese'
model = GPT2LMHeadModel.from_pretrained(
    MODEL_NAME,
    device_map="auto",
    trust_remote_code=True
)
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
tokenizer.pad_token = tokenizer.eos_token

def preprocess_function(examples):
    inputs = [q + " [SEP] " + a + "<|endoftext|>" for q, a in zip(examples["question"], examples["answer"])]
    model_inputs = tokenizer(inputs, max_length=1024, truncation=True, padding=True, return_tensors="pt")
    return model_inputs

n_splits = 5
kf = KFold(n_splits=n_splits, shuffle=True, random_state=42)

# Placeholder for fold results
fold_results = []

common_training_args = {
    "evaluation_strategy": "epoch",  # Evaluation at the end of each epoch
    "save_strategy": "epoch",  # Save at the end of each epoch to match evaluation_strategy
    "learning_rate": 3.842858232584513e-05,
    "per_device_train_batch_size": 8,
    "per_device_eval_batch_size": 8,
    "num_train_epochs":60,
    "weight_decay": 0.058649705990444265,
    "logging_steps": 10,
    "load_best_model_at_end": True,  # Ensure the save strategy matches evaluation_strategy
    "metric_for_best_model": "eval_loss",  # Correct metric name?
    "greater_is_better": False,
    "report_to": "none",
    "save_total_limit": 3
}

for fold, (train_idx, val_idx) in enumerate(kf.split(hf_dataset)):
    print(f"\nTraining on fold {fold+1}")

    hf_dataset = hf_dataset.shuffle(seed=42)
    
    # Select train/validation split
    train_dataset = hf_dataset.select(train_idx)
    val_dataset = hf_dataset.select(val_idx)

    print("shape of train_dataset", train_dataset.shape)
    print("shape of val dataset", val_dataset.shape)
    
    # Tokenize datasets
    tokenized_train_dataset = train_dataset.map(preprocess_function, batched=True)
    tokenized_val_dataset = val_dataset.map(preprocess_function, batched=True)

    # Update training arguments for this fold
    training_args = TrainingArguments(
        output_dir=f"/mnt/data1/imai_phase_4/model_files/{timestamp}/{fold+1}",
        # logging_dir=f'/mnt/data1/imai_phase_4/model_files/fold_log{timestamp}/{fold+1}',
        **common_training_args,
    )

    # Initialize Trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_train_dataset,
        eval_dataset=tokenized_val_dataset,
        tokenizer=tokenizer,
        data_collator=DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False),
    )
    model.config.use_cache = False
    trainer.train()

    best_ckpt_path = trainer.state.best_model_checkpoint
    print('best_ckpt_path =============', best_ckpt_path)
    
    torch.save(model.state_dict(), f"{best_ckpt_path}/model_state_dict.pth")
    
    
    # Evaluate the model on the validation set
    eval_results = trainer.evaluate()
    fold_results.append(eval_results)

    # Extract training loss from log history
    training_loss = [log['loss'] for log in trainer.state.log_history if 'loss' in log][-1]
    print(f"Fold {fold+1} Training Loss: {training_loss}")
    print(f"Fold {fold+1} Evaluation Results: {eval_results}")
    
    
print(f"Number of entries in fold_results: {len(fold_results)}")
print("Evaluation losses for each fold:", [result['eval_loss'] for result in fold_results])

best_fold_index = fold_results.index(min(fold_results, key=lambda x: x['eval_loss']))
print(f"Best Fold: {best_fold_index + 1} with eval_loss: {fold_results[best_fold_index]['eval_loss']}")

best_ckpt_path2 = trainer.state.best_model_checkpoint
print('best_ckpt_path 2=============', best_ckpt_path2)