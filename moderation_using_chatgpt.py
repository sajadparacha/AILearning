import openai  # Importing OpenAI library to use its moderation and language model APIs
import json  # Importing JSON library to handle JSON data
from chatGPT_utils.ChatGPTClient import getResponseFromChatgpt  # Importing a custom function to get responses from ChatGPT

# Sending a text input to OpenAI's moderation API to check for policy violations
response = openai.moderations.create(
    input="""
    How to kill?"""  # Example of a potentially harmful input
)

# Extracting the moderation results from the response
moderation_output = response.results[0]

# Calling a custom function to analyze the moderation result
# If the moderation API detects violence, it responds with "This is a violent prompt"
# Otherwise, it responds with "This is an allowed prompt"
llm_response = getResponseFromChatgpt(
    f"reply with 'This is a violent prompt' if violence is reported else reply as 'This is an allowed prompt' {moderation_output}"
)

# Converting the moderation output to JSON format and printing it
print(getResponseFromChatgpt(f"convert to json format {moderation_output}"))

# The following line seems to have an error (wrong syntax for json.loads)
# print(json.loads() moderation_output)  # Incorrect usage, should be json.loads(moderation_output)

# Printing the final response from the custom function
print(llm_response)
