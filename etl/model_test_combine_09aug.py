import torch
import os
import pandas as pd
from transformers import AutoModelForCausalLM, AutoTokenizer, AutoConfig
from torch.utils.data import Dataset, DataLoader
from tqdm import tqdm
from transformers import GPT2LMHeadModel, ReformerTokenizer


# excel_data_original = pd.read_excel(r"/content/12 mar/question_answer_3124_records.xlsx")
# print("shape of excel_data_original  :", excel_data_original .shape)
# print("columns of excel_data_original : ", excel_data_original .columns)

# excel_data_original = excel_data_original.sample(frac=1).reset_index(drop=True)

# selected_columns = ['Question', 'Answer']
# result_df = excel_data_original[selected_columns]
import pdb; pdb.set_trace()
def preprocess_function(examples, tokenizer):
    inputs = [q + " [SEP] " + a + "<|endoftext|>" for q, a in zip(examples["Question"], examples["Answer"])]
    model_inputs = tokenizer(inputs, max_length=1024, truncation=True, padding=True, return_tensors="pt")
    return model_inputs

# train_data = pd.read_excel(r'/mnt/data1/imai_phase_4new/testresume/train_data_without_resume.xlsx')
train_data = pd.read_excel(r'/mnt/data1/imai_phase_4new/testresume/train_data_without_resume_dataset.xlsx')

# train_data = train_data.rename(columns={
#     'question': 'Question',
#     'final_processed_content_x0001': 'Answer'
# })

# train_data = train_data[['Question', 'Answer']]
# train_data = train_data.sample(n=100, random_state=42)

# train_data.to_excel('/mnt/data1/imai_phase_4new/testresume/train_data_without_resume_dataset.xlsx')
model_name = 'nlp-waseda/comet-gpt2-small-japanese'

# Load the model and tokenizer
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
max_input_length = 1024

# Set padding token
tokenizer.pad_token = tokenizer.eos_token

tokenized_data = preprocess_function(train_data, tokenizer)


# tokenized_data = tokenizer(
#     list(zip(train_data['Question'], train_data['Answer'])),
#     return_tensors="pt",
#     padding=True,
#     truncation=True,
#     max_length=max_input_length,
# )

class CustomDataset(Dataset):
    def __init__(self, tokenized_data):
        self.input_ids = tokenized_data['input_ids']
        self.attention_mask = tokenized_data['attention_mask']

    def __len__(self):
        return len(self.input_ids)

    def __getitem__(self, idx):
        return {
            'input_ids': self.input_ids[idx],
            'attention_mask': self.attention_mask[idx],
        }
    
dataset = CustomDataset(tokenized_data)


model_save_path=r"/mnt/data1/imai_phase_4new/testresume/withoutresume12aug/"
num_epochs= 50
learning_rate=3.842858232584513e-05
batch_size=4


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
optimizer = torch.optim.AdamW(model.parameters(), lr=learning_rate)



for epoch in range(num_epochs):
        dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)
        total_loss = 0.0

        for batch in tqdm(dataloader, desc=f"Epoch {epoch + 1}/{num_epochs}"):
            input_ids = batch['input_ids'].to(device)
            attention_mask = batch['attention_mask'].to(device)

            labels = input_ids.clone()
            labels[labels == tokenizer.pad_token_id] = -100  # Mask the padding tokens

            outputs = model(input_ids, attention_mask=attention_mask, labels=labels)
            loss = outputs.loss

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            total_loss += loss.item()
        average_loss = total_loss / len(dataloader)
        print(f"Epoch {epoch + 1}/{num_epochs}, Average Loss: {average_loss}")

# Save the fine-tuned model and tokenizer to the specified location
model.save_pretrained(model_save_path)
tokenizer.save_pretrained(model_save_path)
