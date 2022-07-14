from re import L
from manim import*
import numpy as np
from colour import Color


class BasicAnimations(Scene):
    def construct(self):
        poly = VGroup(
            *[RegularPolygon(10, color=Color(hue=j/5, saturation=1, luminance=0.5), fill_opacity=0.5) for j in range(4)]
        ).arrange(RIGHT)
        self.play(DrawBorderThenFill(poly), run_time=2)
        self.play(
            Rotate(poly[0], PI, rate_func=smooth),
            Rotate(poly[1], PI, rate_func=linear),
            Rotate(poly[2], PI, rate_func=there_and_back),
            Rotate(poly[3], PI, rate_func=lambda t: np.sin(t*PI)),
            run_time=6
        )
        self.play(poly.animate.shift(RIGHT))

        self.wait(2)
        

class LaggedScene(Scene):
    def construct(self):
        square = VGroup(*[Square(color=Color(hue=j/20, saturation=1, luminance=0.5), fill_opacity=0.5) for j in range(20)])
        square.arrange_in_grid(4, 5).scale(0.6)
        self.play(AnimationGroup(*[FadeIn(s) for s in square], lag_ratio=0.15))


class LaggingGroup(Scene):
    def construct(self):
        squares = VGroup(*[Square(color=Color(hue=j/20, saturation=1, luminance=0.5), fill_opacity=0.8) for j in range(20)])
        squares.arrange_in_grid(4, 5).scale(0.75)
        self.play(AnimationGroup(*[FadeIn(s) for s in squares], lag_ratio=0.15))


class AnimationMechanism(Scene):
    def construct(self):
        c = Circle()

        c.generate_target()
        c.target.set_fill(color=BLUE, opacity=0.4)
        c.target.shift(UR*3).scale(0.2)

        self.add(c)
        self.wait()
        self.play(MoveToTarget(c))

        s = Square()
        s.save_state()
        self.play(FadeIn(s))
        self.play(s.animate.set_color(PINK).set_opacity(0.4).shift(LEFT*2).scale(3))
        self.play(s.animate.shift(DOWN*5).rotate(PI/2))
        self.wait()
        self.play(Restore(s), run_time=2)
        self.play(Transform(c, s))
        self.wait()



class SimpleCostumAnimation(Scene):
    def construct(self):
        def spiral_out(mobject, t):
            radius = 4*t
            angle = 2*t * 2*PI
            mobject.move_to(radius*(np.cos(angle)*RIGHT + np.sin(angle)*UP))
            mobject.set_color(Color(hue=t, saturation=1, luminance=0.5))
            mobject.set_opacity(1-t)

        d = Dot(color=WHITE)
        self.add(d)
        self.play(UpdateFromAlphaFunc(d, spiral_out, run_time=4))
        self.wait(2)


class Disperse(Animation):
    def __init__(self, mobject, dot_radius=0.05, dot_number=100, **kwargs):
        super().__init__(mobject, **kwargs)
        self.dot_radius = dot_radius
        self.dot_number = dot_number
    
    def begin(self):
        dots = VGroup(
            *[Dot(radius=self.dot_radius).move_to(self.mobject.point_from_proportion(p))
              for p in np.linspace(0, 1, self.dot_number)]
        )
        for dot in dots:
            dot.initial_position = dot.get_center()
            dot.shift_vector = 2*(dot.get_center() - self.mobject.get_center())
        dots.set_opacity(0)
        self.mobject.add(dots)
        self.dots = dots
        super().begin()
        
    def clean_up_from_scene(self, scene):
        super().clean_up_from_scene(scene)
        scene.remove(self.dots)

    def interpolate_mobject(self, alpha):
        alpha = self.rate_func(alpha)  # manually apply rate function
        if alpha <= 0.5:
            self.mobject.set_opacity(1 - 2*alpha, family=False)
            self.dots.set_opacity(2*alpha)
        else:
            self.mobject.set_opacity(0)
            self.dots.set_opacity(2*(1 - alpha))
            for dot in self.dots:
                dot.move_to(dot.initial_position + 2*(alpha-0.5)*dot.shift_vector)
            
            

class CustomAnimationExample(Scene):
    def construct(self):
        st = Star(color=YELLOW, fill_opacity=1).scale(3)
        self.add(st)
        self.wait()
        self.play(Disperse(st, dot_number=200, run_time=4))

