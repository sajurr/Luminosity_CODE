from __future__ import absolute_import
from manim import *

class ThreeDSurfacePlot(ThreeDScene):
    def construct(self):
        resolution_fa = 42
        self.set_camera_orientation(phi=75 * DEGREES, theta=-30 * DEGREES)

        def param_gauss(u, v):
            x = u
            y = v
            sigma, mu = 0.4, [0.0, 0.0]
            d = np.linalg.norm(np.array([x - mu[0], y - mu[1]]))
            z = np.exp(-(d ** 2 / (2.0 * sigma ** 2)))
            return np.array([x, y, z])

        gauss_plane = Surface(
            param_gauss,
            resolution=(resolution_fa, resolution_fa),
            v_range=[-2, +2],
            u_range=[-2, +2]
        )

        def param_gauss2(u, v):
            x = u
            y = v
            sigma, mu = 0.4, [0.0, 0.0]
            d = np.linalg.norm(np.array([x - mu[0], y - mu[1]]))
            z = np.exp(-(0.5*d ** 2 / (2.0 * sigma ** 2)))
            return np.array([x, y, z])

        gauss_plane2 = Surface(
            param_gauss2,
            resolution=(resolution_fa, resolution_fa),
            v_range=[-2, +2],
            u_range=[-2, +2]
        )

        gauss_plane.scale(2, about_point=ORIGIN)
        gauss_plane.set_style(fill_opacity=1,stroke_color=BLUE)
        gauss_plane.set_fill_by_checkerboard(ORANGE, BLUE, opacity=0.4)
        axes = ThreeDAxes()
        self.play(Create(axes))
        self.play(FadeIn(gauss_plane))
        self.begin_ambient_camera_rotation(rate=PI/10, about="theta")
        self.play(Transform(gauss_plane, gauss_plane2), run_time=4)
        self.wait(5)
        self.stop_ambient_camera_rotation()