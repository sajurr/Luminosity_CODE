from manim import*
class displayEquations(Scene):
    def construct(self):
        # Create Tex objects
        first_line = Text('Welcome')
        second_line = Text('to')
        equation = Tex('$Luminosity$')
        
        # Position second line underneath first line
        second_line.next_to(first_line, DOWN)

        # Displaying text and equation
        self.play(Write(first_line),Write(second_line))
        self.wait(1)
        self.play(ReplacementTransform(first_line, equation), FadeOut(second_line))
        self.wait(3)