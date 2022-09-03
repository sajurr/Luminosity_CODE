from manim import*
HOME1 = "C:\Z\YOUTUBE\LOGO"

class SVGs(Scene):
    def construct(self):

        icon = SVGMobject(f"{HOME1}\\wolff.svg")

        self.play(DrawBorderThenFill(icon), run_time=2)
        self.wait(1)
        
