from manim import* 
from colour import Color
class Animation(Scene):
    def construct(self):
        polys = VGroup(
            *[RegularPolygon(5, radius=1, color=Color(hue=j/5, saturation=1, luminance=0.5), fill_opacity=0.5)
              for j in range(5)]
        ).arrange(RIGHT)
        self.play(DrawBorderThenFill(polys), run_time=5)
        self.play(
            Rotate(polys[0], PI, rate_func=lambda t: t), # rate_func=linear
            Rotate(polys[1], PI, rate_func=smooth),  # default behavior for most animations
            Rotate(polys[2], PI, rate_func=lambda t: np.sin(t*PI)),
            Rotate(polys[3], PI, rate_func=there_and_back),
            Rotate(polys[4], PI, rate_func=lambda t: 1 - abs(1-2*t)),
            run_time=2
        )
        self.wait(2)