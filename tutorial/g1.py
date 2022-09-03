from tkinter import Scale
from manim import *

class GraphingIntro(Scene):
    def construct(self):

        backg_plane = NumberPlane(x_range=[-7,7,1], y_range=[-4,4,1]).add_coordinates()

        axes = Axes(x_range = [0,5,1], y_range = [0,3,1], 
        x_length = 5, y_length = 3,
        axis_config = {"include_tip": True, "numbers_to_exclude": [0]}
        ).add_coordinates()

        axes.to_edge(UR)
        axis_labels = axes.get_axis_labels(x_label = "x", y_label = "f(x)")

        graph = axes.plot(lambda x : x**0.5, x_range = [0,4], color = YELLOW)

        graphing_stuff = VGroup(axes, graph, axis_labels)

        self.play(FadeIn(backg_plane), run_time=6)
        self.play(backg_plane.animate.set_opacity(0.3))
        self.wait()
        self.play(DrawBorderThenFill(axes), Write(axis_labels), run_time = 2)
        self.wait()
        self.play(Create(graph), run_time = 2)
        self.play(graphing_stuff.animate.shift(DOWN*4), run_time = 3)
        self.wait()
        self.play(axes.animate.shift(LEFT*3), run_time = 3)
        self.wait()