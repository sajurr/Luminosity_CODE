from manim import*
from imports import*
import itertools as it



class Lens(Arc):
    CONFIG = {
        "radius" : 2,
        "angle" : np.pi/2,
        "color" : BLUE_B,
    }
    def __init__(self, **kwargs):
        config(self, kwargs)
        Arc.__init__(self, self.angle, **kwargs)

    def init_points(self):
        Arc.init_points(self)
        self.rotate(-np.pi/4)
        self.shift(-self.get_left())
        self.add_points(self.copy().rotate(np.pi).points)
        

class ShowMultiplePathsThroughLens(Scene):
    def construct(self):
        lens = Lens()
        self.add(lens)
        Scene.construct(self)

    def generate_start_and_end_points(self):
        self.start_point = 3*LEFT + UP
        self.end_point = 2*RIGHT

    def get_paths(self):
        alphas = [0.25, 0.4, 0.58, 0.75]
        lower_right, upper_right, upper_left, lower_left = list(map(
            self.lens.point_from_proportion, alphas
        ))
        return [
            Mobject(
                Line(self.start_point, a),
                Line(a, b),
                Line(b, self.end_point)
            ).set_color(color)
            for (a, b), color in zip(
                [
                    (upper_left, upper_right),
                    (upper_left, lower_right),
                    (lower_left, lower_right),
                    (lower_left, upper_right),
                ],
                color(YELLOW).range_to(WHITE, 4)
            )
        ]

    
