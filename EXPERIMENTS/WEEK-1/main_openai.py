import os
from dotenv import load_dotenv
from openai import OpenAI

# Load variables from the .env file
load_dotenv()

# Read the API key securely from the environment
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError(
        "OPENAI_API_KEY was not found. Check that .env exists "
        "and contains OPENAI_API_KEY=your_key."
    )

# Create the OpenAI client
client = OpenAI(api_key=api_key)

# Send a prompt to the model
response = client.responses.create(
    model="gpt-5.5",
    input="What is Artificial Intelligence? Explain in simple words."
)

# Display the generated answer
print("\nLLM Response:")
print(response.output_text)
