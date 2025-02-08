from manim import *
from config import deepseek_client

response = deepseek_client.chat.completions.create(
    model="gpt-40",
    messages=[{"role": "user", "content": "write a poem about charisma"}],
    stream=False,
)

print(response.choices[0].message)
