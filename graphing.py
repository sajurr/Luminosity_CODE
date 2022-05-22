from pickle import TRUE
from manim import*
import numpy as np
class Graph(Scene):
    def construct(self):
        
        ax = Axes(x_range=(-4,4), y_range=(-4,4), x_length=4, y_length=5)
        
        graph = ax.plot(lambda x: np.log(x)*np.sin(x), x_range=(0,14) ,color=YELLOW)
        self.play(Create(graph), run_time=5)
        self.wait()
