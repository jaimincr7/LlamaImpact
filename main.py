from datasets import load_dataset

# Replace 'your-username/your-dataset' with the name of your uploaded dataset on Hugging Face
dataset = load_dataset("Jmv29/TaxesFAQs")

# Access the training data
train_data = dataset['train']

print(train_data[0])  # Print the first record in the train dataset
