from pyclbr import Function
from manim import*
import numpy as np
import math
from colour import Color

def Sin_three_D(x, y):
    sin_cos = np.sin(x)*np.cos(y)

    return sin_cos

class SinThreeD(ThreeDScene):
    def construct(self):
        ax = ThreeDAxes(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            z_range=[-1, 1, 0.1]
        )
        x_label = ax.get_x_axis_label('x')
        y_label = ax.get_y_axis_label('y')
        
        axis_labels = VGroup(x_label, y_label)

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
        self.add(ax, axis_labels)
        self.set_camera_orientation(
            phi=75*DEGREES,
            theta=60*DEGREES,
            zoom=0.75
        )
        #Begin animation
        self.play(Create(surf))
        self.move_camera(theta=45*DEGREES, run_time=2)
        self.wait(2)

class Sin_TWO(ThreeDScene):
    def construct(self):
        ax = ThreeDAxes(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            z_range=[-1, 1, 0.1]
        )
        x_label = ax.get_x_axis_label('x')
        y_label = ax.get_y_axis_label('y')
        axis_labels = VGroup(x_label, y_label)

        surf = Surface(
            lambda u, v: np.array([u, v, Sin_three_D(u, v)]),
            resolution=(42, 42),
            u_range=[-4,4],
            v_range=[-4,4],
            fill_opacity=0.7
        )
        surf.set_color_by_gradient(RED, PURPLE)
        self.add(ax, axis_labels)
        self.set_camera_orientation(
            phi=75*DEGREES,
            theta=60*DEGREES,
            zoom=0.75
        )
        #Begin animation
        self.play(Create(surf))
        self.move_camera(theta=45*DEGREES, run_time=2)
        self.wait(2)

        x_value = ValueTracker(0)
        y_value = ValueTracker(0)

        x_tex = MathTex("x")
        x_tex_value = always_redraw(
            lambda: DecimalNumber(num_decimal_places=1, include_sign=True)
            .set_value(x_value.get_value())
            .next_to(x_tex, RIGHT)
        )

        y_tex = MathTex("x")
        y_tex_value = always_redraw(
            lambda: DecimalNumber(num_decimal_places=1, include_sign=True)
            .set_value(y_value.get_value())
            .next_to(y_tex, RIGHT)
        )

        surf = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    u, v, Sin_three_D(
                        u, v, x=x_value.get_value(), y=y_value.get_value(),
            resolution=(42, 42),
            u_range=[-4,4],
            v_range=[-4,4],
            fill_opacity=0.7
            )
        )))

        self.play(x_value.animate.set_value(-1), run_time=2, rate_func=rate_functions.smooth)
        self.wait(2)
