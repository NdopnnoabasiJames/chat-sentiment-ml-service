from datasets import load_dataset

dataset = load_dataset("twitter_customer_support")

print(dataset)
print(dataset["train"][0])