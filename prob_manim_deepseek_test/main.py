from dotenv import dotenv_values 

config = dotenv_values(".env")
deepseek_key = config["DEEPSEEK_API_KEY"]

