from manim import*
from manim_physics import*
from typing import Iterable

class StandingWave(ParametricFunction):
    def __init__(
        self,
        n: int = 2,
        length: float = 4,
        period: float = 1,
        amplitude: float = 1,
        **kwargs
    ) -> None:
        """A 2D standing wave.

        Parameters
        ----------
        n
            Harmonic number.
        length
            The length of the wave.
        period
            The time taken for one full oscillation.
        amplitude
            The maximum height of the wave.
        kwargs
            Additional parameters to be passed to :class:`~ParametricFunction`.

        Examples
        --------
        .. manim:: StandingWaveExampleScene

            from manim_physics import *

            class StandingWaveExampleScene(Scene):
                def construct(self):
                    wave1 = StandingWave(1)
                    wave2 = StandingWave(2)
                    wave3 = StandingWave(3)
                    wave4 = StandingWave(4)
                    waves = VGroup(wave1, wave2, wave3, wave4)
                    waves.arrange(DOWN).move_to(ORIGIN)
                    self.add(waves)
                    for wave in waves:
                        wave.start_wave()
                    self.wait()
        """
        self.n = n
        self.length = length
        self.period = period
        self.amplitude = amplitude
        self.time = 0
        self.kwargs = {**kwargs}

        super().__init__(
            lambda t: np.array([t, amplitude * np.sin(n * PI * t / length), 0]),
            t_range=[0, length],
            **kwargs,
        )
        self.shift([-self.length / 2, 0, 0])

    def _update_wave(self, mob: Mobject, dt: float) -> None:
        self.time += dt
        mob.become(
            ParametricFunction(
                lambda t: np.array(
                    [
                        t,
                        self.amplitude
                        * np.sin(self.n * PI * t / self.length)
                        * np.cos(2 * PI * self.time / self.period),
                        0,
                    ]
                ),
                t_range=[0, self.length],
                **self.kwargs,
            ).shift(self.wave_center + [-self.length / 2, 0, 0])
        )

    def start_wave(self):
        self.wave_center = self.get_center()
        self.add_updater(self._update_wave)

    def stop_wave(self):
        self.remove_updater(self._update_wave)