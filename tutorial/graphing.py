from pickle import TRUE
from manim import*
import numpy as np
class Graph(Scene):
    def construct(self):
        
        ax = Axes(x_range=(-4,4), y_range=(-4,4), x_length=4, y_length=5)
        
        pl = ax.plot(lambda x: np.log(x)*np.sin(x), x_range=(0,14) ,color=BLUE)
        area  = ax.get_riemann_rectangles(graph=pl, x_range=[0,PI], color=YELLOW, dx=0.5)
        self.play(Create(pl), run_time=5)
        self.play(Create(area))
        self.wait()
