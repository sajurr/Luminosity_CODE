from turtle import title
from manim import*
class displayEquations(Scene):
    def construct(self):
        # Create Tex objects
        title = Text('Welcome to', font_size=72)
        equation = Tex('$Luminosity$')
        VGroup(title, equation).arrange(DOWN)
        self.play(
            Write(title),
            FadeIn(equation, shift=DOWN))
        self.wait()
        # Position second line underneath first line
        equation.next_to(title, DOWN)
        
        # Displaying text and equation
        self.play(ReplacementTransform(title),(equation))
        self.wait(1)
        