from manim import*

from colour import Color

class NameAnimation(Scene):
    def construct(self):
        
        sheet = NumberPlane()
        box = Rectangle(fill_color= RED, fill_opacity=0.5, height=1, width=1)

        self.play(Create(sheet), run_time=4)
        self.wait()
        self.play(Create(box))
        self.play(box.animate.shift(RIGHT*2), run_time=2)
        self.play(box.animate.shift(UP*3), run_time=3)
        self.play(box.animate.shift(DOWN + RIGHT), run_time=2)
        self.wait()


class Updater(Scene):
    def construct(self):

        rectangle = Rectangle(color=BLUE, height=2, width=2).shift(UP*2+RIGHT*3)
        eq = MathTex(
            "\\frac{3}{4}=0.75"
        ).set_color_by_gradient(GREEN_C, LIGHT_PINK)
        eq.move_to(rectangle.get_center())
        eq.add_updater(lambda x: x.move_to(rectangle.get_center()))

        self.play(FadeIn(rectangle), run_time=2)
        self.play(Write(eq), run_time=2)
        self.play(rectangle.animate.shift(DOWN*2+LEFT*1.5), run_time=3)
        self.wait()
        eq.clear_updaters()
        self.play(rectangle.animate.shift(DOWN*2+LEFT*1), run_time=4)
        self.wait()