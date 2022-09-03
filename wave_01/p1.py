from manim import*
HOME1 = "C:\Z\YOUTUBE\What does the wave equation mean"
class GraphingMovement(Scene):
    def construct(self):
        axes = Axes(x_range=[0,3,1], y_range=[0,3,1], 
        x_length=1, y_length=1,
        axis_config={"include_tip": True, "numbers_to_exclude": [0]}
        )
        icon1 = ImageMobject(f"{HOME1}\\Standing_wave.gif")
        icon2 = ImageMobject(f"{HOME1}\\rect_13.gif")
        axes.to_edge(UR)
        axis_labels = axes.get_axis_labels(x_label="x", y_label="y")
        


        self.play(DrawBorderThenFill(axes), Write(axis_labels), run_time=2)
        self.wait(1)
        self.play(FadeIn(icon1), run_time=1)
        self.wait(1)
        self.play(icon1.animate.to_edge(UL, buff=0.5).scale(1.1))
        self.wait(1)
        self.play(FadeIn(icon2), run_time=1)
        self.wait(1)
        self.play(icon2.animate.to_edge(DL, buff=1).scale(1.5))
        self.wait(1)
        
