from manim import *


class SquareToCircle(Scene):
    def construct(self):
        square = Square()
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)
        square.rotate(PI / 4)
        square.set_fill(RED, opacity=0.5)

        self.play(Create(circle))
        self.play(Transform(circle, square))
        self.play(FadeOut(square))
