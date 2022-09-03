from manim import*
HOME1 = "C:\Z\YOUTUBE\LOGO"

class SVGs(Scene):
    def construct(self):
        
        icon = ImageMobject(f"{HOME1}\\mhm.jpg")
        line_2 = Text("Luminosity", font_size=74, color=BLUE)
        line_3 = Text("Luminosity", font_size=72)
        
        line_2.next_to(icon, DOWN)
        line_3.next_to(icon, DOWN)

        self.play(FadeIn(icon), run_time=1)
        self.play(icon.animate.scale(0.5), run_time=1.4)
        
        self.play(DrawBorderThenFill(line_2), run_time=1.4)
        self.play(Write(line_3), run_time=2)
        self.wait()
        self.play(FadeOut(line_2, icon, line_3), run_time=1.4)
        
        self.wait(2)
