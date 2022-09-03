from manim import*
import numpy as np
class Numpy(Scene):
    def construct(self):
        
        triangle = Triangle()
        triangle.set_color(RED)

        line = Text('Heluww :)')
        
        self.play(Create(triangle), run_time=3)
        self.play(triangle.animate.rotate(PI/3), run_time=3)
        self.play(triangle.animate.scale(2))
        self.play(triangle.animate.to_edge(UR).scale(0.4))
        self.wait()
        self.play(Transform(triangle, line))

        self.wait()