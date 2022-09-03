from cgitb import text
from cmath import sin
from re import X
from tkinter import CENTER, ON, TOP
from tracemalloc import start
import wave
from manim import*
import numpy as np
from pyparsing import line
from scipy.special import jv as besselj
from scipy.special import jn_zeros

class Scene5(Scene):
    def construct(self):
        
        ax = Axes(x_range=[0,10], y_range=[0,5], x_length=8, y_length=4)
        plot2 = ax.plot(lambda x: 0)
        plot2.set_color(YELLOW)
        g = VGroup(plot2)

        self.play(GrowFromCenter(ax))
        self.play(ApplyWave(
            g,
            rate_func=smooth, amplitude=0.5,
            ripples=10, run_time=7
        ))
        self.wait()
        