import sys
import os

sys.path.append(os.path.abspath(os.path.dirname("AI")))  # Add project root to path

from chatGPT_utils.ChatGPTClient import getResponseFromChatgpt

prompt = "Hello, summarize 8th habit of highly effective book in one paragraph."
print(getResponseFromChatgpt(prompt))