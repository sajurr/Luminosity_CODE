from manim import *
from manim_physics import *

class Scene7(Scene):
    def construct(self):
        wave1 = StandingWave(2)
        waves = VGroup(wave1)
        
        waves.arrange(DOWN).to_edge(UR).scale(2)
        self.add(waves)
        for wave in waves:
            wave.start_wave()
        self.wait(3)
        self.play(waves.animate.shift(RIGHT))
        self.wait()