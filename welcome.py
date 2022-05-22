from manim import*
HOME1 = "C:\Z\YOUTUBE\LOGO"

class SVGs(Scene):
    def construct(self):
        line = Text("Welcome to")
        icon = SVGMobject(f"{HOME1}\\ogo.svg")
        line_2 = Text("Luminosity", font_size=74, color=BLUE)
        line_3 = Text("Luminosity", font_size=72)
        line.next_to(icon, UP)
        line_2.next_to(icon, DOWN)
        line_3.next_to(icon, DOWN)

        self.play(Write(line),FadeIn(icon), run_time=1)
        self.play(icon.animate.scale(0.5), run_time=1.4)
        self.play(Unwrite(line), run_time=2)
        self.play(DrawBorderThenFill(line_2), run_time=1.4)
        self.play(Write(line_3), run_time=2)
        self.wait()
        self.play(Unwrite(line_3), run_time=1.4)
        self.wait()
