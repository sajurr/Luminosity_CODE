from manim import*
import numpy as np
from manim_physics import*

class Scene10(Scene):
    def construct(self):
        line1 = Text("Direct relation between the transverse velocity and the phase velocity:", font_size=20, color=YELLOW).to_edge(UL)
        self.play(Write(line1),rate_func=smooth, run_time=2.5)

        eq1 = MathTex(
            "\\psi", "(x,t)", "=", "f(x-vt)"
        ).next_to(line1, DOWN).set_color(BLUE)
        self.play(Write(eq1))
        eq2 = MathTex(
            "\\psi \\left( x,t \\right)\\psi", "=\\left( z \\right)"
        ).next_to(eq1, DOWN).set_color(RED)

        self.play(LaggedStart(Transform(eq1[3].copy(), eq2), run_time=2))
        self.wait()
        self.play(Unwrite(eq1))
        self.wait()

        
        line2 = Text("Partial derivative of psi with respect to x will be the following:", font_size=16, color=YELLOW).next_to(eq2, DOWN)
        eq3 = MathTex(
            "\\frac{\\partial \\psi \\left( z \\right)}{\\partial x}=\\frac{\\partial \\psi }{\\partial z}\\times \\frac{\\partial z}{\\partial x}={\\psi ^1}\\left( z \\right)"
        ).next_to(line2, DOWN)
        self.play(Write(line2), run_time=2)
        self.play(Write(eq3), run_time=2)
        self.wait()

        line3 = Text("And the partial of psi with respect to time will be as follows:", font_size=16, color=YELLOW).next_to(eq3, DOWN)
        eq4 = MathTex(
            "\\frac{\\partial \\psi \\left( z \\right)}{\\partial t}=\\frac{\\partial \\psi }{\\partial z}\\frac{\\partial z}{\\partial t}=-v{{\\psi ^1}\\left( z \\right)"
        ).next_to(line3, DOWN)
        self.play(Write(line3), run_time=2)
        self.play(Write(eq4), run_time=2)
        self.wait()


        line4 = Text("Finally, the second partial derivatives of the two above equations yield our \n wave equation.", font_size=20, color=GREEN).next_to(eq4, DOWN)
        eq5 = MathTex(
            "\\frac{\\partial ^2 \\psi }{\\partial t^2}=v^2 \\frac{\\partial ^2 \\psi }{\\partial x^2}"
        ).next_to(line4, DOWN)
        box = SurroundingRectangle(eq5, color=BLUE, buff=SMALL_BUFF)
        self.play(Write(line4))
        self.play(Transform(eq3.copy(), eq5))
        self.play(Transform(eq4.copy(), eq5))
        self.play(Create(box))
        
        self.wait()
        self.play(Indicate(eq5))
        self.play(FadeOut(line1, eq1, eq2, line2, eq3, line3, eq4, line4, eq5, box), Unwrite(eq2))
        self.wait(2)
        