from re import X
import wave
from manim import*
import numpy as np
from pyparsing import line
from scipy.special import jv as besselj
from scipy.special import jn_zeros



class Scene2(Scene):
    def construct(self):
        

        #defining energy
        plane = NumberPlane()
        self.play(FadeIn(plane), run_time=0.5)
        self.play(plane.animate.set_opacity(0.6))
        self.wait(0.2)

        plane_graph = plane.plot(lambda x : np.sin(2*x), 
        x_range = [0,6*PI], color = BLUE)
        area = plane.get_riemann_rectangles(graph = plane_graph, x_range=[0,2.5*PI], dx=0.02)
        text = Text('Movement of kinetic energy along a pulse.', font_size=25)
        text.to_edge(UR, buff=1)
        self.play(Create(plane_graph), run_time=1.4)
        self.wait(0.5)
        self.play(Write(text))
        self.play(Create(area), run_time=5.6)
        self.wait(0.5)
        self.play(FadeOut(text, plane_graph))
        self.play(Uncreate(area), run_time=1)
        self.wait()
   
        


        #for a standing wave
        sine = plane.plot(lambda x: np.sin(x/2), x_range = [0,6*PI], color=RED)
        cos = plane.plot(lambda x: np.cos(x/2+PI/2), x_range = [0,6*PI], color=RED)
        area2 = always_redraw(lambda: plane.get_riemann_rectangles(graph = sine, x_range=[0,2.5*PI], dx=0.02))
        text2 = Text('Oscillation of potential energy in a standing wave.', font_size=20)
        text2.to_edge(UR, buff=1)
        self.play(Create(sine), run_func=smooth, run_time=2)
        self.play(Transform(sine, cos), run_time=1)
        self.play(Write(text2))
        self.play(FadeIn(area2), run_time=2.6)
        self.wait(0.5)
        self.play(FadeOut(sine, cos, text2))
        self.play(FadeOut(area2), run_time=1)
        self.wait(2)
