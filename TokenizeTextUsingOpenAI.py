# Import the tiktoken library for tokenization
import tiktoken

# Load OpenAI's tokenizer for the GPT-4 model
tokenizer = tiktoken.encoding_for_model("gpt-4")

# Define an example text input for tokenization
text = "Can you help me find a SmartX ProPhone?"

# Tokenize the text into numerical token IDs
tokens = tokenizer.encode(text)

# Decode each token ID back to its corresponding text representation
decoded_tokens = [tokenizer.decode([t]) for t in tokens]

# Import pandas library for displaying the tokenized output in tabular format
import pandas as pd

# Create a DataFrame with token IDs and their corresponding decoded text
df = pd.DataFrame({"Token": tokens, "Decoded Text": decoded_tokens})

# Print the DataFrame to display the tokenized output
print(df)