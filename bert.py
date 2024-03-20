from transformers import BertTokenizer, BertForSequenceClassification
from transformers import Trainer, TrainingArguments
import torch
from nlp import number_of_intents, texts, labels

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=number_of_intents)

# Tokenising the dataset
inputs = tokenizer(texts, padding=True, truncation=True, return_tensors="pt")

# Dataset and DataLoader for training will need to be set (work in progress)
# Here we are assuming 'labels' is a list of integer labels for each text (however also under construction as I will need to convert the labels to integers first)
dataset = torch.utils.data.TensorDataset(inputs['input_ids'], inputs['attention_mask'], torch.tensor(labels))
train_loader = torch.utils.data.DataLoader(dataset, batch_size=16, shuffle=True)

# Define training arguments
training_args = TrainingArguments(output_dir='./results', num_train_epochs=3, per_device_train_batch_size=16)

# Initialising Trainer
trainer = Trainer(model=model, args=training_args, train_dataset=dataset)

# Train the model
trainer.train()

