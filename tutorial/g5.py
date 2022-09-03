from manim import*
class Tute4(Scene):
    def construct(self):

        plane = ComplexPlane(axis_config = {"include_tip": True, "numbers_to_exclude": [0]}).add_coordinates()

        labels = plane.get_axis_labels(x_label = "Real", y_label="Imaginary")

        quest = MathTex("Plot \\quad 2-3i").add_background_rectangle().to_edge(UL)
        dot = Dot()
        vect1 = plane.get_vector((2,0), stroke_color = YELLOW)
        vect2 = Line(start = plane.c2p(2,0),
        end = plane.c2p(2,-3), stroke_color = YELLOW).add_tip()

        self.play(DrawBorderThenFill(plane), Write(labels))
        self.wait()
        self.play(FadeIn(quest))
        self.play(GrowArrow(vect1), dot.animate.move_to(plane.c2p(2,0)), rate_func = linear, run_time = 2)
        self.wait()
        self.play(GrowFromPoint((vect2), point = vect2.get_start()),
        dot.animate.move_to(plane.c2p(2,-3)), run_time = 2, rate_func = linear)
        self.wait()