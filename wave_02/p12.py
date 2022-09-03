from cProfile import label
from manim import*
import numpy as np
from manim_physics import*

class Scene11(Scene):
    def construct(self):
        line1 = Text("Combine two waves that are travelling in different directions,", font_size=20).to_corner(UL)
        plane = NumberPlane().to_edge(DL)
        sine_wave = plane.plot(lambda x: np.sin(x) / np.e ** 2 * x, x_range=[0, 10] ,stroke_width=4, color=BLUE)

        self.play(Write(line1))
        self.play(DrawBorderThenFill(plane))
        self.play(DrawBorderThenFill(sine_wave))
        
        cos_wave = plane.plot(lambda x: x**3, x_range=[-1, 0] ,stroke_width=4, color = RED).rotate(PI)
        self.play(ApplyWave(sine_wave, ripples=5, amplitude=0.5, run_time=3, rate_func=smooth))
        
        self.play(Transform(sine_wave, cos_wave))
        self.play(ApplyWave(cos_wave, ripples=5, amplitude=0.5, run_time=3, rate_func=smooth))
        self.wait()

        self.play(FadeOut(plane, sine_wave, cos_wave))
        self.wait()


        line2 = Text("the result is a standing wave:", font_size=20, color=YELLOW).next_to(line1, DOWN)
        eq1 = MathTex(
            "y=A\\left\\{ \\sin \\left[ \\frac{2\pi }{\\lambda }\\left( x-vt \\right) \\right]+\\sin \\left[ \\frac{2\\pi }{\\lambda }\\left( x+vt \\right) \\right] \\right\\}"
        )
        self.play(Write(line2))
        self.play(Write(eq1))
        self.play(eq1.animate.next_to(line2, DOWN, buff=0.2).scale(0.6))
        eq2 = MathTex(
            "\\Rightarrow y=2A\\left\{ \\cos \\left[ \\frac{4\\pi vt}{\\lambda } \\right]+\\sin \\left[ \\frac{4\pi x}{\\lambda } \\right] \\right\\}"
        )
        box= always_redraw(lambda : SurroundingRectangle(eq2))
        self.play(Write(eq2))
        self.play(Create(box))
        self.play(eq2.animate.scale(1.4))
        self.wait(3)

        self.play(FadeOut(line1, line2, eq1, box, eq2))

        first_line = Text('Created by: Sagar Rathore', font_size=72)
        second_line = Text('..')
        third_line = Text('Please consider subscribing :)', color=BLUE)

        # Position second line underneath first line
        second_line.next_to(first_line, DOWN)

        # Displaying text
        self.play(DrawBorderThenFill(first_line), run_time=3)
        self.play(Write(second_line))
        self.wait(2)
        self.play(ReplacementTransform(first_line, third_line), FadeOut(second_line))
        self.wait(5)
