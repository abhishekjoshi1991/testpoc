
import torch
import pandas as pd
import os
from transformers import AutoModelForCausalLM, AutoTokenizer, AutoConfig
from torch.utils.data import Dataset, DataLoader
from tqdm import tqdm

import time
import pdb; pdb.set_trace()
excel_data = pd.read_excel('/mnt/data1/imai_phase_4new/testresume/train_data_without_resume_dataset.xlsx')
f_df = excel_data[excel_data['Question'] == "識別子が「kaifuku-tp-op」、モジュールが「docker-proxy応答(mysqld:3306)」、エージェントが「mansion-art-specialist」、障害状態が「障害状態」の場合、推奨される対応手順は何ですか?"]
def preprocess_function(examples, tokenizer):
    inputs = [q + " [SEP] " + a + "<|endoftext|>" for q, a in zip(examples["Question"], examples["Answer"])]
    model_inputs = tokenizer(inputs, max_length=1024, truncation=True, padding=True, return_tensors="pt")
    return model_inputs

# Save and load checkpoint functions
def save_checkpoint(model, optimizer, epoch, iteration, filepath):
    checkpoint = {
        'model_state_dict': model.state_dict(),
        'optimizer_state_dict': optimizer.state_dict(),
        'epoch': epoch,
        'iteration': iteration
    }
    torch.save(checkpoint, filepath)

def load_checkpoint(filepath, model, optimizer):
    checkpoint = torch.load(filepath)
    model.load_state_dict(checkpoint['model_state_dict'])
    optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
    epoch = checkpoint['epoch']
    iteration = checkpoint['iteration']
    return model, optimizer, epoch, iteration

def check_and_pause_training(start_time, stop_seconds, resume_seconds, model, optimizer, epoch, iteration, checkpoint_path):
    """
    Checks if the stop time has passed and handles pausing and resuming the training.

    Args:
        start_time (float): The start time of the training or last resume.
        stop_seconds (int): The number of seconds after which to stop.
        resume_seconds (int): The number of seconds to wait before resuming.
        model (torch.nn.Module): The model to be saved.
        optimizer (torch.optim.Optimizer): The optimizer to be saved.
        epoch (int): The current epoch number.
        iteration (int): The current iteration number.
        checkpoint_path (str): The path to save the checkpoint.

    Returns:
        float: The updated start time after resuming.
    """
    if (time.time() - start_time) >= stop_seconds:
        print("Stopping training for a break...")
        save_checkpoint(model, optimizer, epoch, iteration, checkpoint_path)
        print(f"Waiting for {resume_seconds / 60:.1f} minutes before resuming...")
        time.sleep(resume_seconds)  # Wait for resume duration
        print("Resuming training...")
        start_time = time.time()  # Reset the start time after resuming
    return start_time

# Integration into your training loop

def fine_tune_and_save_model_with_gpu(excel_data, model_save_path, epochs, learning_rate, batch_size):
    model_name = 'nlp-waseda/comet-gpt2-small-japanese'

    # Load the model
    model = AutoModelForCausalLM.from_pretrained(model_name, config=AutoConfig.from_pretrained(model_name))

    # Load the tokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    max_input_length = 1024

    # Set padding token
    tokenizer.pad_token = tokenizer.eos_token

    # Assuming `excel_data` is a DataFrame with 'Question' and 'Answer' columns
    first_100_rows_df = excel_data
    print("shape of the data: ", first_100_rows_df.shape)

    # Tokenize your data with a maximum length
    # tokenized_data = tokenizer(
    #     list(zip(first_100_rows_df['Question'], first_100_rows_df['Answer'])),
    #     return_tensors="pt",
    #     padding=True,
    #     truncation=True,
    #     max_length=max_input_length,
    # )
    tokenized_data = preprocess_function(excel_data, tokenizer)

    print(tokenized_data)

    # Create a custom dataset
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

    # Convert tokenized data to PyTorch dataset
    dataset = CustomDataset(tokenized_data)

    # Fine-tuning parameters (adjust as needed)
    num_epochs = epochs
    learning_rate = learning_rate

    # Set up your model and optimizer
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print("device: ", device)
    model.to(device)
    optimizer = torch.optim.AdamW(model.parameters(), lr=learning_rate)

    # Checkpoint interval
    stop_minutes = 15  # Time to run before stopping (in minutes)
    resume_minutes = 10  # Time to resume after stopping (in minutes)
    stop_seconds = stop_minutes * 60
    resume_seconds = resume_minutes * 60

    # Load checkpoint if exists
    checkpoint_path = '/mnt/data1/imai_phase_4new/testresume/checkpoint'
    try:
        model, optimizer, epoch, iteration = load_checkpoint(checkpoint_path, model, optimizer)
        print(f'Resuming from epoch {epoch}, iteration {iteration}')
    except FileNotFoundError:
        print('Starting training from scratch')
        epoch = 0
        iteration = 0

    start_time = time.time()

    while epoch < num_epochs:
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
            iteration += 1

            # Check if the stop time has passed
            start_time = check_and_pause_training(start_time, stop_seconds, resume_seconds, model, optimizer, epoch, iteration, checkpoint_path)

        average_loss = total_loss / len(dataloader)
        print(f"Epoch {epoch + 1}/{num_epochs}, Average Loss: {average_loss}")

        # Save checkpoint at the end of each epoch
        save_checkpoint(model, optimizer, epoch, iteration, checkpoint_path)
        epoch += 1

    # Save the fine-tuned model and tokenizer to the specified location
    model.save_pretrained(model_save_path)
    tokenizer.save_pretrained(model_save_path)
    print('Training complete')



model_save_path=r"/mnt/data1/imai_phase_4new/testresume/withpauseresume"
epochs=50
learning_rate=3.842858232584513e-05
batch_size=4
fine_tune_and_save_model_with_gpu(excel_data, model_save_path, epochs, learning_rate, batch_size)