from operator import length_hint
from manim import*
import numpy as np

class Nudging(Scene):
    def construct(self):
        func = lambda pos: np.sin(pos[1] / 2) * RIGHT + np.cos(pos[0] / 2) * UP 
        vector_field = ArrowVectorField(
            func, x_range=[-7, 7, 1], y_range=[-4, 4, 1], length_func=lambda x: x/2
        )
        self.play(DrawBorderThenFill(vector_field))
        
        circle = Circle(radius=2).shift(LEFT)
        self.add(circle.copy().set_color(GRAY))
        dot = Dot().move_to(circle)
        
        vector_field.nudge(circle, -2, 60, True)
        vector_field.nudge(dot, -2, 60)
        
        circle.add_updater(vector_field.get_nudge_updater(pointwise=True))
        dot.add_updater(vector_field.get_nudge_updater())
        self.play(DrawBorderThenFill(circle), DrawBorderThenFill(dot))
        self.wait(20)


class NudgeTwo(Scene):
    def construct(self):
        func = lambda pos: np.sin(pos[2]) * RIGHT + 2*np.cos(pos[1]) * UP - np.exp(pos[0]) * RIGHT
        vector_field = ArrowVectorField(func)
        self.add(vector_field)
        self.wait()
        
        func = VectorField.scale_func(func, 0.2)
        self.play(vector_field.animate.become(ArrowVectorField(func)))
        self.wait(2)
        
        func = VectorField.scale_func(func, 1.5)
        self.play(vector_field.animate.become(ArrowVectorField(func)))
        self.wait()
        
        func2 = lambda pos: np.sin(pos[1] / 2) * RIGHT + np.cos(pos[0] / 2) * UP 
        vector_field = ArrowVectorField(
            func, x_range=[-7, 7, 1], y_range=[-4, 4, 1], length_func=lambda x: x/2
        )
        
        self.play(vector_field.animate.become(ArrowVectorField(func2)))
        self.wait()
        
        
        
class ScaleVectorFieldFunction(Scene):
    def construct(self):
        func = lambda pos: np.sin(pos[1]) * RIGHT + np.cos(pos[0]) * UP
        vector_field = ArrowVectorField(func)
        self.add(vector_field)
        self.wait()

        func = VectorField.scale_func(func, 0.2)
        self.play(vector_field.animate.become(ArrowVectorField(func)))
        self.wait()
