import os  # Importing the os module to interact with the operating system
import openai  # Importing the OpenAI library to interact with OpenAI's API
import json

# Get API Key from environment variable
api_key = os.getenv("OPENAI_API_KEY")  # Retrieving the OpenAI API key from environment variables

# Check if API key is not found and raise an error if missing
if not api_key:
    raise ValueError("API key not found. Please set the OPENAI_API_KEY environment variable.")

# Initialize OpenAI client with the retrieved API key
client = openai.Client(api_key=api_key)

# Initialize an empty response variable
llm_response = ""


def getResponseFromChatgpt(prompt: str) -> str:
    """
    Sends a prompt to OpenAI's GPT-4 model and retrieves a response.

    Args:
        prompt (str): The input prompt to send to the ChatGPT model.

    Returns:
        str: The generated response from the model.

    Raises:
        openai.OpenAIError: If there is an error with the OpenAI API.
        Exception: If an unexpected error occurs during execution.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4",  # Using the GPT-4 model for generating responses
            messages=[{"role": "user", "content": prompt}]  # Formatting the prompt for the API
        )

        # Extract response content
        llm_response = response.choices[0].message.content
        return llm_response  # Return the generated response

    except openai.OpenAIError as e:
        print(f"OpenAI API error: {e}")  # Print error if OpenAI API fails
    except Exception as e:
        print(f"Unexpected error: {e}")  # Print any other unexpected errors


def get_completion(prompt: str, model: str = "gpt-4") -> str:
    """
    Sends a prompt to OpenAI's GPT-4 model and retrieves a response with a fixed temperature setting.

    Args:
        prompt (str): The input prompt to send to the ChatGPT model.
        model (str, optional): The name of the model to use (default is "gpt-4").

    Returns:
        str: The generated response from the model.
    """
    messages = [{"role": "user", "content": prompt}]  # Prepare messages for the API request

    response = client.chat.completions.create(
        model=model,  # Specify the model to use
        messages=messages,  # Pass the user messages
        temperature=0  # Ensures deterministic output (less randomness)
    )

    return response.choices[0].message.content  # Return the generated response


def get_completion_and_token_count(messages: list,
                                   model: str = "gpt-4",
                                   temperature: float = 0,
                                   max_tokens: int = 500) -> tuple:
    """
    Sends a list of messages to OpenAI's GPT-4 model and retrieves a response along with token usage details.

    Args:
        messages (list): A list of message dictionaries (role-content pairs).
        model (str, optional): The name of the model to use (default is "gpt-4").
        temperature (float, optional): The randomness level of the model's output (default is 0).
        max_tokens (int, optional): The maximum number of tokens allowed in the response (default is 500).

    Returns:
        tuple: A tuple containing:
            - str: The generated response from the model.
            - dict: A dictionary with token usage details:
                - 'prompt_tokens': Number of tokens used in the input prompt.
                - 'completion_tokens': Number of tokens used in the response.
                - 'total_tokens': Total number of tokens used.
    """
    response = client.chat.completions.create(
        model=model,  # Specify the model
        messages=messages,  # Pass the messages for processing
        temperature=temperature,  # Set the temperature for randomness level
        max_tokens=max_tokens,  # Set the maximum response length
    )

    content = response.choices[0].message.content  # Extract the response content

    token_dict = {
        'prompt_tokens': response.usage.prompt_tokens,  # Get the number of tokens in the prompt
        'completion_tokens': response.usage.completion_tokens,  # Get the number of tokens in the response
        'total_tokens': response.usage.total_tokens,  # Calculate total tokens used
    }

    return content, token_dict  # Return response content and token usage details


def get_completion_from_messages(messages,
                                 model="gpt-4",
                                 temperature=0,
                                 max_tokens=500):
    """
    Sends a list of messages to OpenAI's GPT-4 model and retrieves a response.

    Args:
        messages (list): A list of message dictionaries (role-content pairs).
        model (str, optional): The name of the model to use (default is "gpt-4").
        temperature (float, optional): The randomness level of the model's output (default is 0).
        max_tokens (int, optional): The maximum number of tokens allowed in the response (default is 500).

    Returns:
        str: The generated response from the model.
    """
    response = client.chat.completions.create(
        model=model,  # Specify the model
        messages=messages,  # Pass the conversation history
        temperature=temperature,  # Control randomness
        max_tokens=max_tokens,  # Limit response length
    )
    return response.choices[0].message.content  # Return the generated response


def read_string_to_list(input_string):
    if input_string is None:
        return None

    try:
        input_string = input_string.replace("'", "\"")  # Replace single quotes with double quotes for valid JSON
        data = json.loads(input_string)
        return data
    except json.JSONDecodeError:
        print("Error: Invalid JSON string")
        return None


import ast  # Importing the 'ast' module for safe evaluation of expressions

def read_string_to_list_safe(input_string):
    """
    Safely converts a string representation of a list into an actual Python list.
    """
    if input_string is None:
        return None  # Return None if the input is None

    try:
        return ast.literal_eval(input_string)  # Safely evaluates the string as a Python literal
    except (SyntaxError, ValueError):  # Catch syntax errors or value errors if parsing fails
        print("Error: Invalid list format")  # Print an error message for invalid input
        return None  # Return None in case of failure


def get_moderation_response (input_string):
    response = client.moderations.create(
        input=input_string
    )
    moderation_output = response.results[0]
    return moderation_output

def get_completion_and_token_count(messages,
                                   model="gpt-4",
                                   temperature=0,
                                   max_tokens=500):

    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
    )

    content = response.choices[0].message.content

    token_dict = {
        'prompt_tokens':response.usage.prompt_tokens,
        'completion_tokens':response.usage.completion_tokens,
        'total_tokens':response.usage.total_tokens,
    }

    return content, token_dict