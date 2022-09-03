from msilib.schema import IsolatedComponent
from pickle import FALSE
from manim import*

class String(Scene):
    def construct(self):

        line = Text('Hello world!')
        line.set_color_by_gradient(RED, GREEN, BLUE, LIGHT_PINK)
        self.play(Write(line), run_time=2)
        self.wait()

        lien2 = Tex("\\justifying {this is the first try ${\\int I}$}")
        lien2.next_to(line, DOWN)
        self.play(Write(lien2))
        

        eq = MathTex(
            r"W(s)&=\oint \vec{F}\cdot d\vec{s} \\ &=U", font_size=32,
            substrings_to_isolate="s"
            )
        eq.set_color(BLUE)
        eq.next_to(lien2, DOWN)
        eq.set_color_by_tex("s", WHITE)
        Br = Brace(eq, DOWN, buff=0.5)
        box = SurroundingRectangle(eq, buff=0.5)
        cross = Cross(lien2)

        self.play(Write(eq), run_time=2)
        self.play(Create(box), run_time=2)
        self.play(Write(cross))
        self.play(GrowFromCenter(Br))
        self.wait()