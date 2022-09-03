from re import X
import wave
from manim import*
import numpy as np
from pyparsing import line
HOME1 = "C:\Z\YOUTUBE\LOGO"
class Scene1(Scene):
    def construct(self):

        #intro
        icon = ImageMobject(f"{HOME1}\\mhm.jpg")
        line_2 = Text("Luminosity", font_size=74, color=BLUE)
        line_3 = Text("Luminosity", font_size=72)
        
        line_2.next_to(icon, DOWN)
        line_3.next_to(icon, DOWN)

        self.play(FadeIn(icon), run_time=1)
        self.play(icon.animate.scale(0.5), run_time=1.4)
        
        self.play(DrawBorderThenFill(line_2), run_time=1.4)
        self.play(Write(line_3), run_time=2)
        self.play(FadeOut(line_3, icon), run_time=0.4)
        
        self.wait(1)
        
        #transforming the intro
        waveEq = MathTex(
            "\\frac{\\partial^2 y}{\\partial{t^2}}="+"{v^2}(\\frac{{\\partial^2}y }{\\partial x^2})"
            )
        waveEq.set_color_by_tex("y", YELLOW)
        self.play(ReplacementTransform(line_2, waveEq))
        self.wait()
        self.play(waveEq.animate.to_edge(UL), run_time=1.5)
        self.wait(1.5)

        #making arrow to solutions
        sol1 = MathTex(
            "y(x,t)=f(xt)"
        )
        sol1.to_edge(UP)
        arrow = Line(start=waveEq.get_right(), end=sol1.get_left()).add_tip()
        sol2 = MathTex(
            "y(x,t)=f(x\\pm vt)"
        )
        sol2.next_to(sol1, DOWN, buff=1)
        arrow2 = Line(start=waveEq.get_right(), end=sol2.get_left()).add_tip()
        g1 = VGroup(sol1, arrow, arrow2, sol2)

        self.play(Write(g1), run_time=5)
        self.wait(1)

        #standing wave
        trav = Tex("\\text{Standing wave:}")
        trav.next_to(waveEq, DOWN, buff = 2)
        self.play(FadeIn(trav))
        ax = Axes(x_range=[0,5,1], y_range=[0,3,1], x_length=3, y_length=2)
        ax.next_to(trav, RIGHT, buff = 0.5)
        sin = ax.plot(lambda x: np.sin(2*x), color=DARK_BLUE)
        sin2 = ax.plot(lambda x: np.sin(PI + 2*x), color = DARK_BLUE)
        ax_group = VGroup(ax)

        self.play(FadeIn(ax_group), run_time=0.3)
        self.play(Create(sin), run_time=1.5)
        self.play(Transform(sin, sin2), run_time=2)
        
        
        #travelling wave
        trav2 = Tex("\\text{Travelling wave:}")
        trav2.next_to(trav, DOWN, buff = 2)
        self.play(FadeIn(trav2))
        ax2 = Axes(x_range=[0,5,1], y_range=[0,3,1], x_length=3, y_length=2)
        ax2.next_to(trav2, RIGHT, buff = 0.5)
        sine = ax2.plot(lambda x: np.sin(x/2), color=RED)
        cos = ax2.plot(lambda x: np.cos(x/2), color=RED)
        ax_group2 = VGroup(ax2)
        self.play(Create(ax_group2), run_time=1)
        self.play(Create(sine), run_func=smooth ,run_time=2)
        self.play(Transform(sine, cos), run_time=1)
        self.wait(2)
        
    
   