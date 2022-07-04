from manim import *
class rose(Scene):
    def construct(self):
        '''defining the superposition'''

        a = ValueTracker(-2 * PI) #value of "a"
        axis = Axes()
        sin = axis.plot(lambda x : np.sin(x)).set_color(BLUE) #f(x) = sin(x)
        sin2 = always_redraw(lambda : axis.plot(lambda x : np.sin(x + a.get_value())).set_color(RED)) #f(x) = sin(x + a)
        sin3 = always_redraw(lambda : axis.plot(lambda x : np.sin(x + a.get_value()) + np.sin(x)).set_color(YELLOW)) #f(x) = sin(x + a + sin(x))
        sin_label = Tex("$f(x) = sin(x)$").set_color(BLUE).to_corner(UL) #label for "f(x) = sin(x)"
        sin2_label = Tex("$f(x) = sin(x +  $").set_color(BLUE).to_edge(UP) #label for "f(x) = sin(x + a)"
        sin3_label = Tex("$f(x) = sin(x + sin(x) + $").set_color(BLUE).to_edge(DOWN).shift(LEFT) #label for f(x) = sin(x + a + sin(x))
        a_value = always_redraw(
            lambda : DecimalNumber(num_decimal_places=2).set_value(a.get_value()).set_color(BLUE).next_to(sin2_label, RIGHT)
        ) #Writes the value of "a" and is constantly updating
        a_copy = always_redraw(
            lambda : DecimalNumber(num_decimal_places=2).set_value(a.get_value()).set_color(YELLOW).next_to(sin3_label, RIGHT)
        ) #Writes the value of "a" and is constantly updating
        sin2_brac = Tex("$)$").next_to(a_value, RIGHT).set_color(BLUE)
        sin3_brac = Tex("$)$").next_to(a_copy, RIGHT).set_color(YELLOW)

        '''Scenes'''

        self.play(Create(axis),
        Write(VGroup(sin_label, sin2_label, sin3_label)),
        Write(VGroup(a_value, a_copy, sin2_brac, sin3_brac)),
        DrawBorderThenFill(VGroup(sin, sin2, sin3)))
        self.wait()
        self.play(a.animate.set_value(3 * PI), rate_func=linear ,run_time=6) #Value of "a" becomes (3 * PI)
        self.wait()
        self.play(a.animate.set_value(-3 * PI), rate_func=linear, run_time=6) #Value of "a" becomes (-3 * PI)
        self.wait()
      