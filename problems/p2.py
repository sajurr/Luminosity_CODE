from operator import not_
from pydoc import plainpager
from manim import*
import numpy as np
import math
from colour import Color

class DerivativeOne(ThreeDScene):
    def construct(self):
        
        plane = NumberPlane()
        ax = Axes()
        func_1 = plane.plot(lambda x: np.sin(x)).set_color(YELLOW)
        func_1_label = MathTex(r'f(x)=\sin(x)', font_size=40).next_to(func_1, UP).set_color(YELLOW)
        func_2 = plane.plot_derivative_graph(func_1, color=GREEN)
        func_2_label = MathTex(r'\frac{d f(x)}{dx}=\cos(x)', font_size=40).next_to(func_2, UP).set_color(GREEN)
        What = Text("But, what about dervatives in 3-dimensions?", font_size=30).next_to(func_2, DOWN, buff=0.4).set_color(BLUE)
        not_simple = Text("Taking the first derivate of the function, f(x)=sin(x)*cos(y), \n with respect to 'x'.", font_size=35).set_color(BLUE)
        g = VGroup(plane, ax, func_1, func_1_label, func_2, func_2_label, What)
        
        self.play(DrawBorderThenFill(plane), Create(ax), run_time=1.5)
        self.play(plane.animate.set_opacity(0.3))
        self.play(Create(func_1), DrawBorderThenFill(func_1_label), run_time=3)
        self.wait()
        self.play(Transform(func_1, func_2), Transform(func_1_label, func_2_label), run_time=2.4)
        self.wait()
        self.play(Transform(func_2_label, What), run_time=1.3)
        self.play(Uncreate(What), Uncreate(func_1), Uncreate(func_2))
        self.wait(2)
        self.play(Uncreate(g))
        self.wait(2)
        self.play(Write(not_simple), run_time=2)
        self.wait()


class ThreeDDerivative(ThreeDScene):
    def construct(self):
        ax = Axes()
        Three_D_ax = ThreeDAxes(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            z_range=[-2, 2, 0.2]
        )
        self.set_camera_orientation(phi=75*DEGREES, theta=60*DEGREES, zoom=0.75)
        surf = Surface(
            lambda u, v: np.array([
                u, v, np.sin(u)*np.cos(v)
            ]),
            resolution=(42, 42),
            u_range=[-4,4],
            v_range=[-4,4],
            fill_opacity=0.7
        )
        surf.set_color_by_gradient(RED, PURPLE)
        

        #Begin animation
        self.add(ax)
        self.play(Transform(ax, Three_D_ax), run_time=2)
        self.play(Create(surf), run_time=4)
        self.move_camera(theta=-45*DEGREES, run_time=3)
        self.wait(2)

        
        der_1 = Surface(
            lambda u, v: np.array([
                u, v, np.cos(u)*np.cos(v)
            ]),
            resolution=(42, 42),
            u_range=[-4,4],
            v_range=[-4,4],
            fill_opacity=0.7
        )
        #self.play(Write(not_simple))

        der_1.set_color_by_gradient(BLUE, PURPLE)
        
        self.play(Transform(surf, der_1), run_time=2.5)
        self.wait(2)

        not_simple_2 = Text("Now taking derivate of the function, f(x)=cos(x)*cos(y), \n with respect to 'y'.", font_size=25).next_to(surf, UP).set_color(BLUE)
        der_2 = Surface(
            lambda u, v: np.array([
                u, v, -np.cos(u)*np.sin(v)
            ]),
            resolution=(42, 42),
            u_range=[-4,4],
            v_range=[-4,4],
            fill_opacity=0.7
        )
        
        der_2.set_color_by_gradient(BLUE, GREEN)
        self.move_camera(phi=0*DEGREES, theta=-90*DEGREES, distance=10)
        self.play(Write(not_simple_2))
        self.play(Transform(surf, der_2), run_time=2.5)
        self.wait(3)

Home = "C:\MikTex\SAVE\BACKUP SAVES\_SciAstra"
class LogoOne(Scene):
    def construct(self):
        
        logo = SVGMobject(f"{Home}\\image2vector.svg")
        self.play(DrawBorderThenFill(logo, rate_func=smooth), run_time=3)
        self.wait(2)


class SmallTestCode(Scene):
    def construct(self):
        sq = Square()
        self.play(Create(sq))
        self.wait()



class ArrayMatrix(Scene):
    def costruct(self):
        a1 = Matrix([[3, 4], ["\pi", 4]])
        m0 = Matrix([[2, "\pi"], [-1, 1]])
        a1.get_brackets()
        self.add(m0)


class GetBracketsExample(Scene):
    def construct(self):
        m0 = Matrix([["\pi", 3], [1, 5]])
        bra = m0.get_brackets()
        colors = [BLUE, GREEN]
        for k in range(len(colors)):
            bra[k].set_color(colors[k])
        self.add(m0)
        