from manim import *

class displayEquations(Scene):
    def construct(self):
        
        first_line = Text('What do the wave equations mean?')
        
        # Wave eq in 1d
        eq1=MathTex(
            "1D: \\frac{d^2y}{d{t^2}}="+"{v^2}(\\frac{{d^2}y }{dx^2})"
            )
        eq1.set_color_by_tex("y", YELLOW)

        # wave eq in 2d
        eq2=MathTex(
            "2D: \\frac{d^2z}{dt^2}={v^2}(\\frac{d^2z}{d{x^2}}+\\frac{d^2z}{d{y^2}})"
            )
        eq2.set_color_by_tex("2", BLUE)

        # wave eq in 3d
        eq3=MathTex(
            "3D: \\frac{d^2g(x,y,z)}{dt^2}={v^2}(\\frac{d^2g(x,y,z)}{d{x^2}}+\\frac{d^2g(x,y,z)}{d{y^2}}+\\frac{d^2g(x,y,z)}{d{z^2}})")
        eq3.set_color_by_tex("2", WHITE)

        self.play(Write(first_line))
        self.wait(1)
        self.play(ReplacementTransform(first_line, eq1))
        self.wait(2)
        self.play(eq1.animate.to_edge(UL, buff=1))
        self.wait(1)
        self.play(Write(eq2))
        self.wait()
        self.play(eq2.animate.to_edge(UR, buff=1))
        self.wait()
        self.play(Write(eq3))
        self.wait(7)
        
        
