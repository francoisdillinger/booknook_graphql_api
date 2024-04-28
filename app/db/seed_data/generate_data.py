from langchain.llms import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(
 openai_api_key=os.getenv('OPENAI_DATA_GENERATION_KEY')
)

result = llm("Write a very shourt poem")
print(result)