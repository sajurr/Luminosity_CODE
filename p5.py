from isosurfaces import plot_isoline
from manim import*

class Equations(Scene):
    def construct(self):
        
        #writing the equations of force
        eq1 = Text('acceleration along +y is:', font_size=20).to_edge(UL)
        self.play(Write(eq1))
        self.wait()

        eq2 = MathTex(
                "{a}_{y}=\\frac{T\\Delta\\theta}{\\mu(\\Delta x)}"
        ).next_to(eq1, DOWN)
        self.play(Write(eq2))
        self.wait()

        #defining axes/element
        axes = Axes(x_range=[0,2,1], y_range=[0,2,1], 
        x_length=3, y_length=3,
        axis_config={"include_tip": True, "numbers_to_exclude": [0]}
        )
        #adding plot
        axes.to_edge(UR)
        axis_labels = axes.get_axis_labels(x_label="x", y_label="y")
        curve_1 = axes.plot(lambda x: x**2, color=RED_A)
        curve_2 = axes.plot(lambda x: x)
        
        #defining theta
        line2 = Text('What is theta?')
        self.play(Write(line2))
        self.wait(1.5)
        self.play(Unwrite(line2))

        theta = MathTex(
            "tan\\theta=\\frac{\\partial y}{\\partial x}"
        ).next_to(eq2, DOWN)
        theta.set_color(BLUE)

        #taking derivative
        line3 = Text('-->Taking the first partial derivative:', font_size=20)
        line3.next_to(theta, DOWN, buff=0.3)

        der = MathTex(
            "{sec}^{2}\\theta\\frac{\\Delta\\theta}{\\Delta x}=\\frac{\\partial^2y}{\\partial x^2}"
        ).next_to(line3, DOWN)
        
        implies = MathTex(
            ">\\Rightarrow \\Delta\\theta=\\frac{\\partial^2y}{\\partial x^2}\\times\\frac{\\Delta x}{sec^2\\theta}"
        ).next_to(der, DOWN)
        implies.set_color(YELLOW)
        
        #defining a few things
        sm = Text('Delta theta is small.', font_size=25)
        why = Text('Since, delta x is effectively a straight line.', font_size=25).next_to(sm, DOWN)
        gr = VGroup(sm, why).to_edge(RIGHT)
        
        scene = VGroup(axes, axis_labels, curve_1)
        self.play(Write(scene), run_time=3)
        self.play(Transform(curve_1, curve_2), run_time=2)
        self.play(Indicate(curve_2), run_time=1.5)
        self.wait(3)
        self.play(Write(theta))
        self.wait(1)
        self.play(Write(line3))
        self.wait(1)
        self.play(Write(der))
        self.wait(2)
        self.play(Write(implies))
        self.wait(4)
        self.play(DrawBorderThenFill(gr), Indicate(curve_2), run_time=4)
        self.wait(3)