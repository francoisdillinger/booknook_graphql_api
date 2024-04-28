from langchain.llms import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Create an OpenAI object with the API key
llm = OpenAI(
    model='gpt-3.5-turbo-instruct'
)

# Generate text using the generate method
result = llm("Write a very short poem")
print(result)


