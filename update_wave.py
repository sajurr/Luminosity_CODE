from xml.etree.ElementInclude import include
from cairo import TextExtents
from manim import*
from scipy import integrate
import numpy as np


class SimpleCosExpGraph(ThreeDScene):
    def construct(self):
        axes1, axes2, axes3 = all_axes = VGroup(*[
            self.get_three_d_axes(
                include=False,
            )
            for x in range(3)
        ])
        all_axes.scale(0.5)
        self.orient_three_d_mobject(all_axes)

        As = [1.5, 1.5]
        omegas = [1.5, 2.5]
        ks = [0.1, 0.1]
        quads = [
            (axes1, [As[0]], [omegas[0]], [ks[0]]),
            (axes2, [As[1]], [omegas[1]], [ks[1]]),
            (axes3, As, omegas, ks),
        ]

        for axes, As, omegas, ks in quads:
            graph = self.get_initial_state_graph(
                axes,
                lambda x: np.sum([
                    self.cos_exp(x, 0, A, omega, k)
                    for A, omega, k in zip(As, omegas, ks)
                ])
            )
            surface = self.get_surface(
                axes,
                lambda x, t: np.sum([
                    self.cos_exp(x, t, A, omega, k)
                    for A, omega, k in zip(As, omegas, ks)
                ])
            )
            surface.sort(lambda p: -p[2])

            axes.add(surface, graph)
            axes.graph = graph
            axes.surface = surface

        self.set_camera_orientation(distance=100)
        plus = Tex("+").scale(2)
        equals = Tex("=").scale(2)
        group = VGroup(
            axes1, plus, axes2, equals, axes3,
        )
        group.arrange(RIGHT, buff=SMALL_BUFF)

        for axes in all_axes:
            checkmark = Tex("\\checkmark")
            checkmark.set_color(GREEN)
            checkmark.scale(2)
            checkmark.next_to(axes, UP)
            checkmark.shift(0.7 * DOWN)
            axes.checkmark = checkmark

        self.add(axes1, axes2)
        self.play(
            LaggedStart(
                Write(axes1.surface),
                Write(axes2.surface),
            ),
            LaggedStart(
                FadeIn(axes1.checkmark, DOWN),
                FadeIn(axes2.checkmark, DOWN),
            ),
            lag_ratio=0.2,
            run_time=1,
        )
        self.wait()
        self.play(Write(plus))
        self.play(
            Transform(
                axes1.copy().set_fill(opacity=0),
                axes3
            ),
            Transform(
                axes2.copy().set_fill(opacity=0),
                axes3
            ),
            FadeIn(equals, LEFT)
        )
        self.play(
            FadeIn(axes3.checkmark, DOWN),
        )
        self.wait()