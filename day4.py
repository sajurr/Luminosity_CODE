from manim import*

class Errors(Scene):
    def construct(self):
        c = Circle(radius = 3)

        self.play(Write(c), run_time=4)
        self.wait()
