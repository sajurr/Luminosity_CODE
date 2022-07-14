from manim import*
from manim_physics import*
HOME1 = 'C:\Z\YOUTUBE\_SVGs'

class Waving(Scene):
    def construct(self):
        stick_man = SVGMobject(f"{HOME1}\\stickman_.svg").set_color(WHITE)
        wave_man = SVGMobject(f"{HOME1}\\stickman_WAVE.svg").set_color(WHITE)
        stick_man2 = SVGMobject(f"{HOME1}\\stickman_WAVE_2.svg").set_color(WHITE)
        stick_man3 = SVGMobject(f"{HOME1}\\stickman_WAVE_3.svg").set_color(WHITE)


        self.add(stick_man)
        self.wait()
        self.play(ReplacementTransform(stick_man, wave_man))
        self.play(ReplacementTransform(wave_man, stick_man2))
        self.play(ReplacementTransform(stick_man2, stick_man3))
        self.wait()
        self.play(stick_man3.animate.to_edge(UR))
        self.wait(2)