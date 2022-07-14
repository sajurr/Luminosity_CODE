from manim import*
from manim_physics import*

class RadialWaveExampleScene(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(60 * DEGREES, -45 * DEGREES)
        wave = RadialWave(
            LEFT * 2 + DOWN * 5, # Two source of waves
            RIGHT * 2 + DOWN * 5,
            checkerboard_colors=[BLUE_D],
            stroke_width=0,
        )
        self.add(wave)
        wave.start_wave()
        self.wait(3)
        wave.stop_wave()