import sys
import os

# sys.path.append(os.path.abspath(os.path.dirname("AI")))  # Add project root to path

from chatGPT_utils.ChatGPTClient import getResponseFromChatgpt
from chatGPT_utils.ChatGPTClient import get_completion
from chatGPT_utils.ChatGPTClient import  get_completion_and_token_count
prompt = "Hello, summarize 8th habit of highly effective book in one paragraph."
# print(getResponseFromChatgpt(prompt))
# print(get_completion(prompt="What is the capital of france"))

# Call chapgpt and get response and token information
messages = [
    {'role':'system',
     'content':"""You are an assistant who responds 
 in the style of Dr Seuss. Response should be a one liner."""},
    {'role':'user',
     'content':"""write me a very short poem 
 about a happy carrot"""},
]
response, token_dict = get_completion_and_token_count(messages)
print(response)
print(token_dict)