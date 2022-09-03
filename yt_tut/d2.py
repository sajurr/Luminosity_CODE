from turtle import fillcolor
from manim import*

class Positioning(Scene):
     def construct(self):

        plane = NumberPlane()
        red_dot = Dot(color=RED)
        green_dot = Dot(color=GREEN).next_to(red_dot, RIGHT)

        # shit
        sq = Square(color = RED)
        sq.shift(2*DOWN + 4*LEFT)

        # move_to
        circ = Circle(color=RED)
        circ.move_to([-4,-2,0])

        #align_to
        c = Circle(radius=0.4, color=BLUE, fill_opacity=0.5)
        c2 = c.copy().set_color(YELLOW)
        c3 = c.copy().set_color(PURPLE_A)
        c.align_to(sq, UP)
        c3.align_to(sq, DOWN)
        c2.align_to(sq, UR)
        self.add(c,c2,c3)


        self.add(plane)
        self.add(red_dot, green_dot)
        self.add(sq)
        self.add(circ)