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

class Scene8(Scene):
    def construct(self):
        line1 = Text(('First partial derivative of the test function with respect to x:'), font_size=20).to_corner(UL, buff=0.3)
        self.play(GrowFromCenter(line1))
        self.wait(0.4)

        eq1 = MathTex(
            "\\frac{\\partial y}{\\partial x}=\\frac{2\pi }{\\lambda }A\\sin \\left( \\frac{2\pi }{\\lambda }\\left( x-vt \\right) \\right)", color=YELLOW
        ).next_to(line1, DOWN, buff=0.2)
        self.play(Write(eq1), run_time=1.2)
        self.wait(1.4)

        line2 = Text('And the partial derivative of ', font_size=20).to_corner(UL, buff=2.3)
        line0 = Text('displacement y with respect to time is:', font_size=20).next_to(line2, DOWN, buff=0.1)
        self.play(GrowFromCenter(line2))
        self.play(GrowFromCenter(line0))
        eq2 = MathTex(
            "\\frac{\\partial y}{\\partial t}=-\\frac{2\pi v}{\\lambda }A\\sin \\left( \\frac{2\pi }{\\lambda }\\left( x-vt \\right) \\right)", color=YELLOW
        ).next_to(line0, DOWN)
        self.play(Write(eq2), run_time=1)
        self.wait(1.5)

        line3 = Text('partial w.r.t. x and t', font_size=24).to_edge(UR)
        line4 = Text('WHY?', color=RED).next_to(line3, DOWN, buff=0.3)
        self.play(DrawBorderThenFill(line3))
        self.play(FadeIn(line4))
        arrow = Arrow(line3, eq1)
        arrow2 = Arrow(line3, eq2)
        g1 = VGroup(arrow2, arrow)
        self.play(Create(g1), run_time=1.5)
        self.wait(2)

        eq3 = MathTex(
            "\\frac{\\partial y}{\\partial \\lambda}\\ne\\frac{2\pi }{\\lambda }A\\sin \\left( \\frac{2\pi }{\\lambda }\\left( x-vt \\right) \\right)=0"
        ).next_to(g1, DOWN, buff=1.7)
        eq3.set_color(BLUE)
        self.play(DrawBorderThenFill(eq3), run_time=1.2)
        self.wait()
        cross = Cross(eq3)
        self.play(Create(cross), run_time=1.2)
        self.wait()

        






