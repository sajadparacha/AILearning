import os
import sys
import openai

# Ensure the package path is added to Python's search path
# sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# Get API Key from environment variable
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("API key not found. Please set the OPENAI_API_KEY environment variable.")

# Initialize OpenAI client
client = openai.Client(api_key=api_key)

# Initialize response variable
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
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )

        # Extract response content
        llm_response = response.choices[0].message.content
        return llm_response

    except openai.OpenAIError as e:
        print(f"OpenAI API error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


def get_completion(prompt: str, model: str = "gpt-4") -> str:
    """
    Sends a prompt to OpenAI's GPT-4 model and retrieves a response with a fixed temperature setting.

    Args:
        prompt (str): The input prompt to send to the ChatGPT model.
        model (str, optional): The name of the model to use (default is "gpt-4").

    Returns:
        str: The generated response from the model.
    """
    messages = [{"role": "user", "content": prompt}]

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0  # Ensures deterministic output (less randomness)
    )

    return response.choices[0].message.content


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
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
    )

    content = response.choices[0].message.content

    token_dict = {
        'prompt_tokens': response.usage.prompt_tokens,
        'completion_tokens': response.usage.completion_tokens,
        'total_tokens': response.usage.total_tokens,
    }

    return content, token_dict

def get_completion_from_messages(messages,
                                 model="gpt-4",
                                 temperature=0,
                                 max_tokens=500):
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
    )
    return response.choices[0].message.content
