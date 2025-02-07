from manim import *
from dotenv import dotenv_values

config = dotenv_values(".env")
deepseek_key = config["DEEPSEEK_API_KEY"]


class CreateCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)
        self.play(Create(circle))
