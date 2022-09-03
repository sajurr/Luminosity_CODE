from manim import*
class Graphing(Scene):
    def construct(self):
        plane = NumberPlane(x_range=[-40,40,2], y_range=[10,16,4], x_length=9, y_length=9)
        
        
        self.play(DrawBorderThenFill(plane), run_time=4)
        
        self.wait(2)