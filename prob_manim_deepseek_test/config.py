from openai import OpenAI
from dotenv import dotenv_values

config = dotenv_values(".env")
openai_key = config["OPENAI_API_KEY"]

deepseek_client = OpenAI(api_key=openai_key)
