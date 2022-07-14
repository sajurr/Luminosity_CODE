from cgitb import text
from cmath import sin
from csv import writer
from re import X
from tkinter import CENTER, ON, TOP
from tracemalloc import start
import wave
from manim import*
import numpy as np

from scipy.special import jv as besselj
from scipy.special import jn_zeros
from manim_physics import*

class Scene9(Scene):
    def construct(self):
        eq1 = MathTex(
            "\\frac{\\partial y}{\\partial t}=-v\\frac{\\partial y}{\\partial x}"
        )
        self.play(Write(eq1), run_time=2.4)
        self.play(eq1.animate.to_edge(UL).scale(0.7), run_time=1.5)
        self.wait(2)

        line1 = Text("If you take a traveling wave on another string that \n is moving in the negative x direction, you will get the \n same differential equation \n but without the minus sign.", font_size=20)
        eq2 = MathTex(
            "\\frac{\\partial y}{\\partial t}=v\\frac{\\partial y}{\\partial x}"
        ).next_to(line1, DOWN)

        g1 = VGroup(line1, eq2)
        self.play(Write(g1), run_time=5.5)
        self.wait()

        box = always_redraw(lambda: (SurroundingRectangle(g1, color= BLUE, buff=SMALL_BUFF)))
        self.play(Create(box))
        self.play(g1.animate.to_edge(UR).scale(0.8))
        self.wait(3)

        line2 = Text("Taking the second partial derivative of the differential equation(s) above:", font_size=20).to_edge(ORIGIN)
        self.play(Write(line2), run_time=0.5)
        eq3 = MathTex(
            "\\frac{\\partial ^2 y}{\\partial t^2}=","v^2","\\frac{\\partial ^2 y}{\\partial x^2}"
        ).next_to(line2, DOWN).set_color(YELLOW)
        box1 = SurroundingRectangle(eq3, color=YELLOW, buff=SMALL_BUFF)
        self.play(Write(eq3), run_time=4)
        self.play(Create(box1))
        self.wait(2)

        line4 = Text("'v' is the velocity of the phase and not the particles moving transversely.", font_size=18).to_corner(DR, buff=0.4)
        arrow = Arrow(eq3[1], line4)
        box = SurroundingRectangle(line4, color=BLUE, buff=SMALL_BUFF, corner_radius=0.1)
        g0 = VGroup(arrow, line4, box)
        self.play(Write(g0), run_time=2)
        self.wait(2)