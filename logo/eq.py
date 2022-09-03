from manim import *


class displayEquations(Scene):
    def construct(self):
        # Create Tex objects
        first_line = Text('What does the wave equation mean?')
        second_line = Text('Consider y(x,t) as a function of')
        third_line = Text('position (x) and time (t).')
        text=MathTex(
            "\\frac{d^2y}{d{t^2}}="+"{v^2}\\frac{{d^2}y }{dx^2}"
            )
        # Position second line underneath first line
        first_line.next_to(first_line, DOWN)
        sentence=VGroup(second_line)
        sentence2=VGroup(third_line)
        third_line.next_to(second_line, DOWN)
        text.set_color_by_tex("y", YELLOW)

        # Displaying text and equation

        self.play(Write(first_line))
        self.wait(1)
        self.play(ReplacementTransform(first_line, text))
        self.wait(3)

        self.play(text.animate.to_edge(UL))
        self.wait(3)
        self.play(Write(sentence))
        self.wait()
        self.play(Write(sentence2))
        self.wait()