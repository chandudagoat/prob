from openai import OpenAI
from dotenv import dotenv_values

config = dotenv_values(".env")
deepseek_key = config["DEEPSEEK_API_KEY"]

deepseek_client = OpenAI(api_key=deepseek_key, base_url="https://api.deepseek.com")
