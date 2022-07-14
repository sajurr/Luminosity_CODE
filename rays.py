from turtle import fillcolor
from manim import*
from imports import*

class Diss(Scene):
    def construct(self):

        a1 = [3, 3, 0]
        a2 = [-3, -3, 3]
        arcpol = ArcBetweenPoints(a1, a2, radius=5)
        arcpol2 = ArcBetweenPoints(a2, a1, radius=5)
        self.play(Create(arcpol), run_time=2)
        self.play(Create(arcpol2), run_time=2)
        self.wait(2)
       
        self.wait(2)