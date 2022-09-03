from manim import*
class Getters(Scene):
    def construct(self):
        
        rect = Rectangle(color=RED, height = 3, width = 4).to_edge(UL)

        circ = Circle().to_edge(DOWN)

        arrow = Line(start=rect.get_bottom(), end=circ.get_top()).add_tip()

        self.play(Create(VGroup(rect, circ, arrow)))
        self.wait(2)

        self.play(rect.animate.to_edge(UR))
