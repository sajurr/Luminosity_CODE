from pyclbr import Function
from manim import*
import math
import numpy as np

def func_cos(x, n):
    cos_approx = 0
    for i in range(n):
        coef = (-1)**i
        num = x**(2*i)
        denom = math.factorial(2*i)
        cos_approx += ( coef ) * ( (num)/(denom) )

class TaylorSeries(ThreeDScene):
    def construct(self):
        ax = ThreeDAxes().set_color(BLUE)
        self.set_camera_orientation(phi=70*DEGREES, theta=45*DEGREES)
        ax_label = ax.get_x_axis_label("x")
        text = Text("This is a 3D text.").to_corner(UL)
        text2 = Text("WOW.").to_corner(UR)
        self.add_fixed_in_frame_mobjects(text)
        

        self.add(ax, ax_label)
        self.wait(2)
        self.play(TransformFromCopy(text, text2))
        self.wait()