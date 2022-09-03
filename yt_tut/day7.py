from manim import*
class Updater(Scene):
    def construct(self):
        
        num = MathTex("ln(2)")
        box = always_redraw(lambda: SurroundingRectangle(num, fill_color=BLUE, fill_opacity=0.4, color=YELLOW, buff=0.5)
        )
        name = always_redraw(lambda: Text("Sagarrr").next_to(box, DOWN, buff=0.25))

        self.play(Create(VGroup(num, box, name)), run_time=1)
        self.play(num.animate.shift(RIGHT * 2), run_time=3)
        self.wait(1)