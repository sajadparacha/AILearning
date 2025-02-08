import os,sys
import openai
# Ensure the package path is added to Python's search path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# Get API Key from environment variable
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("API key not found. Please set the OPENAI_API_KEY environment variable.")

# Initialize OpenAI client
client = openai.Client(api_key=api_key)
# openai.api_key = api_key
llm_response=""
def getResponseFromChatgpt(prompt) :

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )

        # print(response.choices[0].message.content)
        llm_response=response.choices[0].message.content
        return llm_response
    except openai.OpenAIError as e:
        print(f"OpenAI API error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
#print(getResponseFromChatgpt('How are you?'));