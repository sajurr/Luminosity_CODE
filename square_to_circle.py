from manim import *


class SquareToCircle(Scene):
    def construct(self):
        s = Square()
        c = Circle()
        self.add(s)
        self.play(Transform(s, c))


with tempconfig({"quality": "medium_quality", "disable_caching": True}):
    scene = SquareToCircle()
    scene.render()