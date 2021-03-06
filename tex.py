from manim import*
class ColoringEquations(Scene):
#Grouping and coloring parts of equations
    def construct(self):
        line1=Text("\\text{The vector }", "\\vec{F}_{net}", "\\text{ is the net force on object of mass }")
        line1.set_color_by_tex("force", BLUE)
        line2=Text("m", "\\text{ and acceleration }", "\\vec{a}", ". ")
        line2.set_color_by_tex_to_color_map({
        "m": YELLOW,
        "{a}": RED
        })
        sentence=VGroup(line1,line2)
        sentence.arrange_submobjects(DOWN, buff=MED_LARGE_BUFF)
        self.play(Write(sentence))