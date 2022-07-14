from tkinter import Scale
from manim import*

IMG1 = "C:\Z\YOUTUBE\What does the wave equation mean"

class String(Scene):
    def construct(self):

        #defining the intials, like tension, density, etc.
        density = MathTex(
            "density(linear)=\\mu"
            )
        density.set_color_by_tex("density", YELLOW)
        density.to_edge(UL, buff=1)
        tension = MathTex(
            "Tension(T)"
        )
        tension.set_color_by_tex("tension", BLUE)
        tension.to_edge(UL, buff=1.6)

        #making the axes for reference
        axes = Axes(x_range=[0,1,1], y_range=[0,1,1], 
        x_length=1, y_length=1,
        axis_config={"include_tip": True, "numbers_to_exclude": [0]}
        )
        axes.to_edge(UR)
        axis_labels = axes.get_axis_labels(x_label="x", y_label="y")

        #adding image/photo of the string
        image1 = ImageMobject(f"{IMG1}\\opeg.jpg")
        eq1 = Text('Analysing the forces:')
        eq1.to_edge(LEFT)
        
        #analysing the forces(eq2, eq3)
        eq2 = MathTex(
            "{F}_{x}=0"
        )
        eq2.next_to(eq1, DOWN)
        eq3 = MathTex(
            "{F}_{y}=T\\Delta\\theta"
        )
        eq3.next_to(eq2, DOWN)
        line = Text('Force along y is obtained using Taylor series expansion.', font_size=16)
        line.next_to(eq3, DOWN)

        self.play(FadeIn(image1))
        self.play(image1.animate.to_edge(DR).scale(0.75))
        self.wait(2)
        self.play(Write(density))
        self.wait()
        self.play(Write(tension))
        self.wait()
        self.play(DrawBorderThenFill(axes), Write(axis_labels), run_time=2)
        self.wait(1)
        self.play(Write(eq1))
        self.wait()
        self.play(Write(eq2))
        self.wait()
        self.play(Write(eq3))
        self.wait()
        self.play(Write(line), run_time=2)
        self.wait(4)