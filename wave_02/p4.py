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

class Scene4(Scene):
    def construct(self):
        eq1 = MathTex(
            "{y}_{n}\\left( x,t \\right)=\\sum\\limits_{n}{A}_{n}\\sin \\left( \\frac{n\pi x}{L} \\right)\\cos \\left( {\\omega }_{n}t \\right)}"
        )
        
        self.play(DrawBorderThenFill(eq1), run_time=1.5)
        self.play(eq1.animate.shift(UL*3).scale(0.5))
        self.wait()

        line1 = Text('Using the identity:', font_size=20)
        line1.next_to(eq1, DOWN)
        eq2 = MathTex(
            "\\sin \\left( a+b \\right)+\\sin \\left( a-b \\right)=2\\sin \\left( a \\right)\cos \\left( b \\right)"
        ).scale(0.5)
        eq2.set_color(YELLOW)
        eq2.next_to(line1, DOWN)
        box = SurroundingRectangle(eq2, buff=SMALL_BUFF, color=YELLOW)
        g1 = VGroup(line1, eq2)

        self.play(FadeIn(g1), run_time=1.5)
        self.play(DrawBorderThenFill(box), run_time=1)
        self.wait()

        line2 = Text('Applying this to the nth normal mode, we get the following result:', font_size=20)
        line2.next_to(g1, DOWN, buff=0.5)
        eq3 = MathTex(
            "{y}_{n}\\left( x,t \\right)=\\frac{A_n}{2}\\left( \\sin \\left( \\frac{n\pi x}{L}+{\\omega }_{n}t \\right)+\\cos \\left( \\frac{n\pi x}{L}-{\\omega }_{n}t \\right) \\right)"
        ).scale(0.7)
        eq3.set_color_by_gradient(BLUE, YELLOW, GREEN)
        eq3.next_to(line2, DOWN)
        g2 = VGroup(eq3)
        self.play(FadeIn(line2), run_time=0.2)
        self.play(Write(g2), run_time=4.5)
        self.wait(3)

        #arrow to standing wave eq3
        line3 = Text('superposition of two oppositely travelling waves', font_size=20)
        line3.next_to(g2, DOWN, buff=0.5)
        arrow = Arrow(g2, line3)
        self.play(Create(arrow))
        self.play(DrawBorderThenFill(line3))
        self.wait(2)

        groupALL = VGroup(eq1, g1, box, line2, g2, arrow, line3)
        self.play(Uncreate(groupALL), run_time=2.5)


        #superposition of travelling waves
        plot1 = Axes(x_range=[0,8], y_range=[0,6], x_length=7, y_length=4)
        
        stand1 = plot1.plot(lambda x: 2*np.sin(2*x), color=DARK_BLUE)
        standing = plot1.plot(lambda x: np.sin(2*x + PI), color=RED)
        g1 = VGroup(plot1, stand1, standing)
            
        plot3 = plot1.plot(lambda x: 2*np.sin(2*x) + np.sin(2*x + PI) + np.sin(3*x + PI) + np.sin(4*x + PI) + np.sin(4*x + PI/2))
        plot3.set_color_by_gradient(DARK_BLUE, RED)
    
        self.play(DrawBorderThenFill(g1), run_time=2)
        self.wait()
        
        self.play(Create(plot3), FadeOut(standing), run_time=0.6)
        self.play(Transform(stand1, plot3), run_time=1.7)
        
        self.wait()