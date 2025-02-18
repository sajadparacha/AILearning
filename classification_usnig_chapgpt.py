from chatGPT_utils.ChatGPTClient import get_completion_from_messages  # Import function to interact with ChatGPT

# Define a delimiter to separate sections in the input message
delimiter = "####"

# System message to instruct ChatGPT on how to categorize customer service queries
system_message = f"""
You will be provided with customer service queries. \
The customer service query will be delimited with \
{delimiter} characters.

Classify each query into a primary category \
and a secondary category. 
Provide your output in json format with the \
keys: primary and secondary.

Primary categories: Billing, Technical Support, \
Account Management, or General Inquiry.

Billing secondary categories:
- Unsubscribe or upgrade
- Add a payment method
- Explanation for charge
- Dispute a charge

Technical Support secondary categories:
- General troubleshooting
- Device compatibility
- Software updates

Account Management secondary categories:
- Password reset
- Update personal information
- Close account
- Account security

General Inquiry secondary categories:
- Product information
- Pricing
- Feedback
- Speak to a human
"""

# Define a user message asking to reset a password
user_message = f"""
I want reset my password"""

# Create a list of messages to send to ChatGPT
messages =  [
    {'role': 'system', 'content': system_message},  # Provide system instructions to the AI
    {'role': 'user', 'content': f"{delimiter}{user_message}{delimiter}"},  # User input message formatted with delimiter
]

# Send messages to ChatGPT and get the classification response
response = get_completion_from_messages(messages)

# Print the AI's response in JSON format
print(response)
