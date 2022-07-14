from manim import*
class ValueTracker(Scene):
    def construct(self):
        
        k = ValueTracker(5)

        num = always_redraw(lambda: DecimalNumber(0).set_value(k.get_value()))
        
        self.play(FadeIn(num, k))
        self.wait(1)
        self.play(num.animate.set_value(0), runt_time=5, rate_functions=smooth)
        self.wait()