from manim import*

class Example(Scene):
    def construct(self):
        
        ax = Axes(x_range=(-3, 3), y_range=(-3, 3))
        curve = ax.plot(lambda x: (x**2), color=YELLOW)
        curve2 = ax.plot(lambda x: (x**3), color=RED)
        scene = VGroup(ax, curve, curve)
        grid = NumberPlane()
        
        self.play(Create(grid))
        self.wait()
        self.play(Write(scene), run_time=2)
        self.wait()
        self.play(Write(curve2), run_time=3)
        self.wait()
        self.play(scene.animate.to_edge(UR).scale(0.2), FadeOut(curve2), run_time=2)
        self.wait()