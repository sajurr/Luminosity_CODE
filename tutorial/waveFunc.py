from __future__ import absolute_import
from manim import*

class Cosine(ThreeDScene):
    def construct(self):
        resolution_fa = 32
        ax = ThreeDAxes()
        self.set_camera_orientation(phi=75*DEGREES, theta=45*DEGREES)
        self.add(ax)

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
        

        def plane(s, t):
            x = s
            y = t
            z = 6 - s/3 + 2*t/3
            return np.array([x, y, z])

        plane = Surface(
            plane,
            resolution=(resolution_fa, resolution_fa)
        )
        
        gauss_plane.set_style(fill_opacity=0.5, fill_color=GREEN)
        gauss_plane.set_fill_by_checkerboard(ORANGE, BLUE, opacity=0.4)
        ax = ThreeDAxes()
        self.play(Create(ax))
        self.play(FadeIn(gauss_plane))
        self.begin_ambient_camera_rotation(rate=PI/10, about="theta")
        self.play(Transform(gauss_plane, plane), run_time=3)
        self.wait(2)
        self.stop_ambient_camera_rotation()
