from manim import *
from config import deepseek_client

response = deepseek_client.chat.completions.create(
    model="deepseek-chat", messages=[{"role": "user", "content": "Hello"}], stream=False
)

print(response.choices[0].message.content)
