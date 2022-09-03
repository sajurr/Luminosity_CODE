from manim import*
class Updaters(Scene):
    def construct(self):
        
        rect = Rectangle(width=2, height=1, color=RED, fill_color=BLUE, fill_opacity=0.5).to_edge(UL)

        circ = Circle(radius=1).to_edge(DOWN)

        arrow = always_redraw(lambda: Line(
            start=rect.get_bottom(), end=circ.get_top(), buff=0.1
            ).add_tip()
        )

        self.play(Create(VGroup(rect, circ, arrow)), run_time=4)
        self.wait(1)
        self.play(rect.animate.to_edge(UR).scale(1.3), circ.animate.scale(0.6), run_time=2)