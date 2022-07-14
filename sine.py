from cmath import sin
from manim import*

class Sine(Scene):
    def construct(self):

        plane = NumberPlane()
        ax = Axes(x_range=(0,4), y_range=(0,6))
        curve1 = ax.plot(lambda x: x^2, x_range=[0,1])
        
        self.play(Create(plane), run_time=2)
        self.wait(Create(ax))
        self.play(Create(curve1), run_time=2)
        self.wait()