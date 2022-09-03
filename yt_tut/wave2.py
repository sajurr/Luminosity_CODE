from manim import *
import numpy as np
from scipy.special import jv as besselj
from scipy.special import jn_zeros

EIGENFUNCTION_COLORS = [
    ("#08FF94", -1.00 +  1.0 / 7.0),
    ("#37A0FF", -1.00 +  3.0 / 7.0),
    ("#496FFF", -1.00 +  5.0 / 7.0),
    ("#8A42FF", -1.00 +  7.0 / 7.0),
    ("#FF58FF", -1.00 +  9.0 / 7.0),
    ("#F62EA6", -1.00 + 11.0 / 7.0),
    ("#DC143C", -1.00 + 13.0 / 7.0),
]

class Drum_Skins_Function(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=60 * DEGREES, theta = -45 * DEGREES)
        axes = ThreeDAxes()
        surface = Surface(
            lambda u, v : axes.c2p(u * np.cos(v), u * np.sin(v), 2.0 * besselj(3.0, 2.0 * u) * np.sin(2.0 * v)),
            u_range = [0.00001, jn_zeros(3, 1)[-1]],
            v_range = [0, 2.0 * np.pi],
            resolution = 64
        )
        surface.set_fill_by_value(axes=axes, colors = EIGENFUNCTION_COLORS)
        self.add(axes, surface)

class Stretching_Flat(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=60 * DEGREES, theta = -45 * DEGREES)
        axes = ThreeDAxes(x_range=[-2.0, 2.0], y_range=[-2.0, 2.0], z_range=[-4.0, 4.0])
        surface = Surface(
            lambda u, v : axes.c2p(u * np.cos(v), u * np.sin(v), 0),
            u_range = [0.00001, 2.0],
            v_range = [0, 2.0 * np.pi],
            resolution = 64
        )
        surface.set_fill_by_value(axes=axes, colors = EIGENFUNCTION_COLORS)
        self.add(axes, surface)

class Stretching_Flat_Constant_Offset(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=60 * DEGREES, theta = -45 * DEGREES)
        axes = ThreeDAxes(x_range=[-2.0, 2.0], y_range=[-2.0, 2.0], z_range=[-2.0, 2.0])
        surface = Surface(
            lambda u, v : axes.c2p(u * np.cos(v), u * np.sin(v), 1.0),
            u_range = [0.00001, 2.0],
            v_range = [0, 2.0 * np.pi],
            resolution = 64
        )
        surface.set_fill_by_value(axes=axes, colors = EIGENFUNCTION_COLORS)
        self.add(axes, surface)

class Stretching_Plane(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=60 * DEGREES, theta = -45 * DEGREES)
        axes = ThreeDAxes(x_range=[-2.0, 2.0], y_range=[-2.0, 2.0], z_range=[-2.0, 2.0])
        surface = Surface(
            lambda u, v : axes.c2p(u * np.cos(v), u * np.sin(v), -0.5 * u * np.cos(v) - 0.25 * u * np.sin(v)),
            u_range = [0.00001, 2.0],
            v_range = [0, 2.0 * np.pi],
            resolution = 64
        )
        surface.set_fill_by_value(axes=axes, colors = EIGENFUNCTION_COLORS)
        self.add(axes, surface)

class Stretching_Bell_Curve(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=60 * DEGREES, theta = -45 * DEGREES)
        axes = ThreeDAxes(x_range=[-2.0, 2.0], y_range=[-2.0, 2.0], z_range=[-2.0, 2.0])
        surface = Surface(
            lambda u, v : axes.c2p(u * np.cos(v), u * np.sin(v), 2.0 * np.exp(-16.0 * u ** 2) - 1.0),
            u_range = [0.00001, 2.0],
            v_range = [0, 2.0 * np.pi],
            resolution = 64
        )
        surface.set_fill_by_value(axes=axes, colors = EIGENFUNCTION_COLORS)
        self.add(axes, surface)

class Stretching_Bell_Curve_Plane(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=60 * DEGREES, theta = -45 * DEGREES)
        axes = ThreeDAxes(x_range=[-2.0, 2.0], y_range=[-2.0, 2.0], z_range=[-2.0, 2.0])
        surface = Surface(
            lambda u, v : axes.c2p(u * np.cos(v), u * np.sin(v), 1.5 * np.exp(-16.0 * u ** 2) - 0.5 * u * np.cos(v) - 0.25 * u * np.sin(v)),
            u_range = [0.00001, 2.0],
            v_range = [0, 2.0 * np.pi],
            resolution = 64
        )
        surface.set_fill_by_value(axes=axes, colors = EIGENFUNCTION_COLORS)
        self.add(axes, surface)

class Standing_Wave(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=60 * DEGREES, theta = -45 * DEGREES)
        axes = ThreeDAxes(x_range=[-1.0, 1.0], y_range=[-1.0, 1.0], z_range=[-1.0, 1.0])
        t = ValueTracker(0.0)
        surface = always_redraw(
            lambda : Surface(
                lambda u, v : axes.c2p(u, v, np.sin(np.pi * u) * np.cos(2.0 * np.pi * v) * np.cos(2.0 * np.pi * t.get_value())),
                u_range = [-1.0, 1.0],
                v_range = [-1.0, 1.0],
                resolution = [64, 128]
            ).set_fill_by_value(axes=axes, colors = EIGENFUNCTION_COLORS)
        )
        self.add(axes, surface)
        anim_runtime = 4.0
        self.play(t.animate.set_value(1.0), run_time=anim_runtime, rate_func = linear)

def partial_plane_wave(u, v, ku, kv, t, omega, phase):
    arg = ku * u + kv * v - omega * t + phase
    if np.abs(arg) > 8.0 * np.pi:
        return 0.0
    else:
        return np.sin(arg)

class Standing_Wave_from_Traveling_Waves(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=60 * DEGREES, theta = -45 * DEGREES)
        axes = ThreeDAxes(x_range=[-10.0, 10.0], y_range=[-10.0, 10.0], z_range=[-3.0, 3.0])
        t = ValueTracker(0.0)
        wave = lambda u, v, t : (partial_plane_wave(u, v, 0.0, 2.0, t, 1.0, 45.0) + partial_plane_wave(u, v, 0.0, 2.0, t, -1.0, -45.0)) / 2.0
        surface = always_redraw(
            lambda : Surface(
                lambda u, v : axes.c2p(u, v, wave(u, v, t.get_value())),
                u_range = [-8.0, 8.0],
                v_range = [-8.0, 8.0],
                resolution = [1, 256]
            ).set_fill_by_value(axes=axes, colors = EIGENFUNCTION_COLORS)
        )
        self.add(axes, surface)
        anim_runtime = 20.0
        self.play(t.animate.set_value(90), run_time=anim_runtime, rate_func = linear)