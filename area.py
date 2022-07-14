from turtle import fillcolor
from manim import*
from numpy import place

class Example(Scene):
    def construct(self):
        
        ax = Axes(x_range=(-6, 6), y_range=(-6, 6))
        curve = ax.plot(lambda x: (x**3), color=YELLOW)
        area = ax.get_area(curve, x_range=(-2, 0 ), color=BLUE)
        area2 = ax.get_area(curve, x_range=(0, 1 ), color=RED)

        self.play(Create(ax), Create(curve), run_time=4)
        self.wait()
        self.play(Create(area), run_time=2)
        self.play(FadeIn(area2), run_time=1)
        self.wait()


class SquareToCircle(Scene):
    def construct(self):
        square = Square(side_length=2, color=RED, fill_opacity=0.5)
        circle = Circle(radius=1, color=BLUE, fill_opacity=0.3)

        self.play(DrawBorderThenFill(square), run_time=2)
        self.wait()
        self.play(Transform(square, circle), run_time=1)
        self.play(Indicate(circle), run_time=1.4)
        self.wait()
        self.play(FadeOut(square, circle))
        self.wait()