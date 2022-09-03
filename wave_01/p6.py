from manim import*

class MoreEq(Scene):
    def construct(self):
        
        #getting to the wave eq
        reach = Text('We get the direct relation between', font_size=25)
        vec = MathTex("\\Delta\\theta")
        vec.next_to(reach, RIGHT)
        reach2 = Text("and the variation in transverse displacement y as follows:", font_size=25)
        reach2.next_to(reach, DOWN)
        vg = VGroup(reach, vec, reach2)

        self.play(Write(vg), run_time=4)
        self.wait(1)
        self.play(vg.animate.to_edge(UP).scale(0.6))
        self.wait(2)


        #the eq
        implies = MathTex(
            "\\Delta\\theta=\\frac{\\partial^2y}{\\partial x^2}\\Delta x}"
        ).next_to(vg, DOWN)
        implies.set_color(YELLOW)
        
        self.play(Write(implies))
        self.play(implies.animate.next_to(vg, DOWN).scale(0.6))
        self.wait(2)


        #plugging delta theta into force eq
        line2 = Text('Plugging this', font_size=25)
        vec2 = MathTex(
                "\\Delta\\theta"
                    )
        vec2.next_to(line2, RIGHT)
        line3 = Text('into', font_size=25)
        line3.next_to(vec2, RIGHT)
        eq4 = MathTex(
            "{a}_{y}=\\frac{T\\Delta\\theta}{\\mu(\\Delta x)}:")
        eq4.next_to(line3, RIGHT)
        vg2 = VGroup(line2, vec2, line3, eq4)

        self.play(Write(vg2), run_time=4)
        self.play(Indicate(implies), run_time=1.6)
        self.play(vg2.animate.next_to(implies, DOWN).scale(0.6))


        line4 = Text("We get the wave equation:")
        line4.next_to(vg2, DOWN)
        eq5 = MathTex(
            "\\frac{\\partial^2 y}{\\partial t^2}=\\frac{T}{\\mu}\\frac{\\partial^2 y}{\\partial x^2}"
        )
        eq5.set_color(YELLOW)
        eq5.next_to(line4, DOWN, buff=1)
        box = always_redraw(lambda: SurroundingRectangle(eq5, color=YELLOW, buff=MED_LARGE_BUFF))

        self.play(Write(line4), run_time=1.5)
        self.wait(2)
        self.play(line4.animate.scale(0.7).next_to(vg2, DOWN))
        self.play(Write(eq5), run_time=1.5)
        self.play(Create(box), run_time=1.5)
        self.wait(2)
        self.play(eq5.animate.scale(1.25))
        self.wait(4)
        self.play(Unwrite(vg), run_time=2)
        self.play(Unwrite(implies), run_time=2)
        self.play(Unwrite(vg2), run_time=2)
        self.play(Unwrite(line4), run_time=2)
        self.play(Unwrite(eq5), run_time=2)
        self.wait(3)