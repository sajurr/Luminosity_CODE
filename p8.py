from cgitb import text
from cmath import sin
from re import X
from tkinter import CENTER, ON, TOP
from tracemalloc import start
import wave
from manim import*
import numpy as np

from scipy.special import jv as besselj
from scipy.special import jn_zeros
from manim_physics import*

class Scene7(Scene):
    def construct(self):
        line1 = Text('Consider a traveling wave given by the following function:', font_size=20).to_edge(UL)
        self.play(GrowFromCenter(line1))

        eq1 = MathTex(
            "y\\left( x,t \\right)=A\\sin \\left( \\frac{2\pi }{\\lambda }\\left( x-vt \\right) \\right)"
        )
        eq1.next_to(line1, DOWN)
        self.play(Write(eq1))
        self.wait(2)

        ax = Axes(x_range=[0,5], y_range=[0,4], x_length=4, y_length=2)
        ax.to_edge(UR).scale(0.5)
        self.play(Write(ax))

        graph1 = ax.plot(lambda x: 0)
        self.play(Create(graph1), run_time=0.4)
        self.play(ApplyWave(graph1, rate_functions=smooth, amplitude=0.4, ripples=3, run_time=4))
        self.wait()

        eq2 = MathTex(
            "\\frac{d^2y}{d{t^2}}="+"{v^2}(\\frac{{d^2}y }{dx^2})"
        )
        arrow = Arrow(eq1, eq2)
        line2 = Text('Solution??').next_to(arrow, RIGHT, buff=0.2)
        self.play(Write(eq2))
        self.play(Transform(eq1.copy(), eq2))
        self.play(Create(arrow))
        self.play(DrawBorderThenFill(line2))
        self.wait(3)

