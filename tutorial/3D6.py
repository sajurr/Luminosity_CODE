import math
from idna import check_label
from manim import*
import numpy as np

class NumberLine(Scene):
    def construct(self):
        
        ax = Axes(x_range=[-4,9], y_range=[-4,4]).add_coordinates()        
        self.add(ax)
        

        func1 = ax.plot(lambda x: x**2, x_range=[-math.sqrt(3), 4]).set_color(YELLOW)
        self.add(func1)        
        
        func2 = ParametricFunction(lambda t: np.array([
            np.sin(t), np.cos(t), 0
        ]), t_range=[-TAU, TAU])
        self.add(func2)


class THREED(ThreeDScene):
    def construct(self):
        
        ax = ThreeDAxes(x_range=[-5, 5], y_range=[-5, 5], z_range=[-5,5 ])
        self.set_camera_orientation(phi=70*DEGREES, theta=45*DEGREES)
        self.add(ax)
        
        surf1 = Surface(lambda u, v: np.array([
            u, v, u**2 + v**2
        ]), u_range=[-1, 1], v_range=[-1, 1], checkerboard_colors=[RED, BLUE], resolution=(10, 32)
        )

        surf2 = Surface(lambda u,v: np.array([
            u**2, v**3, np.sin(u*v)
        ]), u_range=[-1,1], v_range=[-1,1], resolution=(10,32), checkerboard_colors=[YELLOW, DARK_BROWN]
        )
        
        self.begin_ambient_camera_rotation(about="theta", rate=PI/12)
        
        self.play(Create(surf1), run_time=4)
        self.play(Transform(surf1, surf2))
        self.wait(2)
        self.stop_ambient_camera_rotation()
        self.wait(2)
        self.move_camera(phi=40*DEGREES)
        self.wait(2)


class ThreeDtoTwoD(ThreeDScene):
    
    def construct(self):
        
        ax = ThreeDAxes(x_range=[-10, 10], y_range=[-10, 10], z_range=[-10, 10], x_length=6, y_length=6, z_length=6)
        self.set_camera_orientation(phi=66*DEGREES, theta=50*DEGREES)

        surf1 = Surface(lambda u,v: np.array([
            np.sin(u)*np.cos(v), np.sin(u)*np.cos(v), np.sin(u)*np.cos(v)
        ]), color=RED, resolution=(10,32), u_range=[-TAU, TAU], v_range=[-TAU, TAU]
        )
        self.play(Create(ax))
        self.play(FadeIn(surf1))        
        self.wait()


class SimpleCosExpGraph(ThreeDScene):
    CONFIG = {
        "axes_config": {
            "x_min": 0,
            "x_max": TAU,
            "y_min": 0,
            "y_max": 10,
            "z_min": -3,
            "z_max": 3,
            "x_axis_config": {
                "tick_frequency": TAU / 8,
                "include_tip": False,
            },
            "num_axis_pieces": 1,
        },
        "default_graph_style": {
            "stroke_width": 2,
            "stroke_color": WHITE,
            "background_image_file": "VerticalTempGradient",
        },
        "default_surface_config": {
            "fill_opacity": 0.1,
            "checkerboard_colors": [GREY_B],
            "stroke_width": 0.5,
            "stroke_color": WHITE,
            "stroke_opacity": 0.5,
        },
        "temp_text": "Temperature",
    }
    def construct(self):
        axes = ThreeDAxes(x_range=[-10, 10], y_range=[-10, 10], z_range=[-10, 10], x_length=6, y_length=6, z_length=6)
        cos_graph = self.get_cos_graph(axes)
        cos_exp_surface = self.get_cos_exp_surface(axes)

        
        self.camera.frame_center.shift(3 * RIGHT)
        self.begin_ambient_camera_rotation(rate=0.01)

        self.add(axes)
        self.play(Create(cos_graph))
        self.play(UpdateFromAlphaFunc(
            cos_exp_surface,
            lambda m, a: m.become(
                self.get_cos_exp_surface(axes, v_max=a * 10)
            ),
            run_time=3
        ))

        self.add(cos_graph.copy())

        t_tracker = ValueTracker(0)
        get_t = t_tracker.get_value
        cos_graph.add_updater(
            lambda m: m.become(self.get_time_slice_graph(
                axes,
                lambda x: self.cos_exp(x, get_t()),
                t=get_t()
            ))
        )

        plane = Rectangle(
            stroke_width=0,
            fill_color=WHITE,
            fill_opacity=0.1,
        )
        plane.rotate(90 * DEGREES, RIGHT)
        plane.match_width(axes.x_axis)
        plane.match_depth(axes.z_axis, stretch=True)
        plane.move_to(axes.c2p(0, 0, 0), LEFT)

        self.add(plane, cos_graph)
        self.play(
            ApplyMethod(
                t_tracker.set_value, 10,
                run_time=10,
                rate_func=linear,
            ),
            ApplyMethod(
                plane.shift, 10 * UP,
                run_time=10,
                rate_func=linear,
            ),
            FadeIn(plane),
        )
        self.wait(10)

    #
    def cos_exp(self, x, t, A=2, omega=1.5, k=0.1):
        return A * np.cos(omega * x) * np.exp(-k * (omega**2) * t)

    def get_cos_graph(self, axes, **config):
        return self.get_initial_state_graph(
            axes,
            lambda x: self.cos_exp(x, 0),
            **config
        )

    def get_cos_exp_surface(self, axes, **config):
        return self.get_surface(
            axes,
            lambda x, t: self.cos_exp(x, t),
            **config
        )
    def get_initial_state_graph(self, axes, func, **kwargs):
        return self.get_time_slice_graph(
            axes,
            lambda x, t: func(x),
            t=0,
            **kwargs
        )

    def get_time_slice_graph(self, axes, func, t, **kwargs):
        config = dict()
        config.update(self.default_angled_camera_orientation_kwargs)
        config.update({
            "t_min": axes.x_range,
            "t_max": axes.x_range,
        })
        config.update(kwargs)
        return ParametricFunction(
            lambda x: axes.c2p(
                x, t, func(x, t)
            ),
            **config,
        )