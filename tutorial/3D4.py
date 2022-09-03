import fractions
from os import abort
from manim import*
import numpy as np


class ThreeD(ThreeDScene):
    def construct(self):
        

        ax = ThreeDAxes()
        self.set_camera_orientation(phi=80*DEGREES, theta=40*DEGREES, distance=6)
        ThreedText = Text("Hellow 3D world").scale(2)
        ThreedText.rotate(PI/2, axis=RIGHT)


        TwoDText = Text("Heloooo").scale(2)
        TwoDText.to_edge(UP+RIGHT)
        self.add_fixed_in_frame_mobjects(TwoDText)

        self.play(Create(ax))
        self.play(Write(ThreedText))
        self.play(FadeIn(TwoDText))
        self.wait()
        self.move_camera(phi=45*DEGREES, distance=3)
        self.wait(2)
        self.begin_ambient_camera_rotation(rate=PI/10)
        self.wait(4)
        self.stop_ambient_camera_rotation()
        self.wait()

class ThreeDCurve(ThreeDScene):
    def construct(self):
        
        ax = ThreeDAxes()
        self.set_camera_orientation(phi=75*DEGREES, theta=45*DEGREES, distance = 8)
        self.add(ax)

        curve = ParametricFunction(lambda t: np.array([
            np.cos(t), np.sin(3*t), np.cos(5*t)
        ]), color=YELLOW, t_range=[-TAU, TAU])
        self.begin_ambient_camera_rotation(rate=0.6)
        self.play(Create(curve), run_time=8)
        self.wait(10)



class ThreeDCurve2(ThreeDScene):
    def construct(self):
        
        ax = ThreeDAxes()
        self.set_camera_orientation(phi=75*DEGREES, theta=45*DEGREES, distance = 8)
        self.add(ax)

        curve1 = ParametricFunction(lambda t: np.array([
            np.cos(t), np.sin(3*t), np.cos(5*t)
        ]), color=YELLOW, t_range=[-TAU, TAU])
        
        curve2 = ParametricFunction(lambda t: np.array([
            np.exp(-0.1*t)*np.cos(t), np.exp(-0.1*t)*np.sin(t), 2*t 
        ]), color=GREEN, t_range=[-TAU, TAU])
        
        curve3 = ParametricFunction(lambda t: np.array([
            np.sin(t), np.sin(2*t), np.sin(3*t)
        ]), color=RED, t_range=[-TAU, TAU])

        self.begin_ambient_camera_rotation(rate=0.6)
        self.play(Create(curve1), run_time=4)
        self.play(Transform(curve1, curve2), run_time=4, rate_func=smooth)
        self.wait(10)
        self.play(DrawBorderThenFill(curve3))
        self.wait(3)


class ThreeDSurface(ThreeDScene):
    def construct(self):
        
        ax = ThreeDAxes()
        self.set_camera_orientation(phi=75*DEGREES, theta=45*DEGREES, distance = 8)
        self.add(ax)

        bowl = Surface(
            lambda u, v: np.array([
                np.cos(v)*u, np.sin(v)*u, u**2
            ]), v_range=[-TAU, TAU], resolution=(10, 32), checkerboard_colors=[MAROON_B, MAROON_A]
        )
        self.begin_ambient_camera_rotation(rate=0.5, about="theta")
        self.play(Create(bowl.scale(2)), run_time=5)
        self.wait(3)
        self.stop_ambient_camera_rotation()
        self.wait(2)


class Butterfly(ThreeDScene):
    def construct(self):
        
        ax = ThreeDAxes()
        self.set_camera_orientation(phi=75*DEGREES, theta=45*DEGREES, distance = 8)
        self.add(ax)

        butterfly = ParametricFunction(lambda t: np.array([
            np.exp(np.sin(t)), 2*np.cos(4*t), (np.sin(t/12 - PI/24))**5
        ]), t_range=[0, 12*PI], color=RED)

        
        self.begin_ambient_camera_rotation(rate=0.3, about="theta")
        self.play(Create(butterfly), run_time=12)
        self.wait(12)
        self.stop_ambient_camera_rotation()
        
     

        
