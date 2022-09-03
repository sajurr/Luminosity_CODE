from re import X
from tkinter import CENTER, ON, TOP
import wave
from manim import*
import numpy as np
from pyparsing import line
from scipy.special import jv as besselj
from scipy.special import jn_zeros



class Scene3(Scene):
    def construct(self):
        plane = NumberPlane()
        plot1 = Axes(x_range=[0,6], y_range=[0,5], x_length=3, y_length=2)
        plot1.to_edge(UP, buff=1)
        stand1 = plot1.plot(lambda x: np.sin(2*x), color=DARK_BLUE)
        g1 = VGroup(plot1, stand1)
        
        plot2 = Axes(x_range=[0,6], y_range=[0,5], x_length=3, y_length=2)
        plot2.to_edge(DOWN, buff=1)
        stand2 = plot2.plot(lambda x: np.sin(2*x + PI), color=RED)
        g2 = VGroup(plot2, stand2)

        g0 = VGroup(plane)
        
        self.play(Write(g0))
        self.play(DrawBorderThenFill(g1), run_time=1.5)
        self.play(DrawBorderThenFill(g2), run_time=1.5)
        self.wait()
        self.play(g1.animate.shift(DOWN).scale(2), run_time=1.5)
        self.play(g2.animate.shift(UP*2.82).scale(2), run_time=1.5)
        self.wait()