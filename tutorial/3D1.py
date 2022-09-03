from manim import*
from manim_physics import*
import numpy as np

class TUT(ThreeDScene):
    def construct(self):

        ax = ThreeDAxes(
            x_range=[-6, 6, 1],
            y_range=[-6, 6, 1],
            z_range=[-6, 6, 1],
            x_length=8,
            y_length=6,
            z_length=6
        )

        graph = ax.plot(lambda x: x**2, x_range=[-2, 2,1], color = YELLOW)
        rect  = ax.get_riemann_rectangles(
            graph=graph, 
            x_range=[-2,2],
            dx=0.1,
            stroke_color=RED
        )

        graph2 = ax.plot_parametric_curve(
            lambda t: np.array([np.cos(t), np.sin(t), t]),
            t_range=[-2*PI, 2*PI]
        )

        self.add(ax, graph)
        self.wait()

        ## The camera is auto-set to phi=0 and theta=0

        self.move_camera(phi=60*DEGREES)
        self.wait()
        self.move_camera(theta=-45*DEGREES)
        self.play(Create(graph2))

        self.begin_ambient_camera_rotation(
            rate=PI / 10, about="theta" 
        )       ## rotates at a rate of radians per second
        self.play(Create(rect), run_time=3)
        self.wait(2)
        self.stop_ambient_camera_rotation()

        self.wait()
        self.begin_ambient_camera_rotation(
            rate=PI / 10, about="phi"
        )
        self.wait(2)
        self.stop_ambient_camera_rotation()

