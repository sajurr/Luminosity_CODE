from cgitb import text
from re import X
from tkinter import CENTER, ON, TOP
from tracemalloc import start
import wave
from manim import*
import numpy as np
from pyparsing import line
from scipy.special import jv as besselj
from scipy.special import jn_zeros

class Scene6(Scene):
    def construct(self):
        wave = MathTex(
            "\\frac{d^2y}{d{t^2}}="+"{v^2}(\\frac{{d^2}y }{dx^2})",
            color=RED)
        wave.to_edge(RIGHT, buff=2)

        sol = Text('Solution to the wave equation', font_size=25)
        sol.next_to(wave, DOWN)

        eq = Tex(
            "y(x,t)", "=", "f(x)g(t)", color=YELLOW
        )
        eq.to_corner(UL, buff=2.5)

        eq2 = MathTex(
            "y(x,t)", "=", "f(x\\pm vt)", color=YELLOW
        )
        eq2.to_corner(DL, buff=2.5)

        self.add(wave)
        self.play(FadeIn(eq), run_time=1.5)
        self.play(ReplacementTransform(eq.copy(), sol), run_time=1.5)
        self.wait(0.4)
        self.play(FadeIn(eq2), run_time=0.5)
        self.play(ReplacementTransform(eq2.copy(), sol), run_time=1.5)
        self.wait(2)