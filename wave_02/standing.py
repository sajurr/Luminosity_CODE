from manim import*
from manim_physics import*
import numpy as np

class StandingWaveExample(Scene):
    def construct(self):
        wave3 = StandingWave(8)
        wave4 = StandingWave(4)
        waves = VGroup(wave3, wave4)
        waves.arrange(DOWN).move_to(ORIGIN)
        self.add(waves)
        for wave in waves:
            wave.start_wave()
        self.wait(8)