from manim import*
HOME1 = "C:\Z\YOUTUBE"
class SVG_FINAL(Scene):
    def construct(self):
        img = SVGMobject(f"{HOME1}\\image2vector (3).svg").scale(1.3)
        img2 = SVGMobject(f"{HOME1}\\image2vector (1).svg").scale(1.3)
        
        self.play(DrawBorderThenFill(img), run_time=4, rate_functions=smooth)
        self.play(Transform(img, img2), run_time=1.2, rate_functions=smooth)

        line_2 = Text("Luminosity", font_size=74, color=BLUE).set_opacity(0.4)
        line_3 = Text("Luminosity", font_size=72)
        
        line_2.next_to(img, DOWN)
        line_3.next_to(img, DOWN)

        self.play(DrawBorderThenFill(line_2), run_time=0.5)
        self.wait(0.3)
        self.play(Write(line_3), run_time=1.5)
        self.play(FadeOut(line_2, line_3, img))
        
        self.wait(1)