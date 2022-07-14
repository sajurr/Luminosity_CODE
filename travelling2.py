from manim import *

class SineWave(Scene):
    def construct(self):
        # The ValueTracker functions as the constant `a` in `sin(ab)`.
        tracker = ValueTracker(0.1)

        # Create the graph
        sine_function = lambda x: np.sin(tracker.get_value() * x)
        sine_graph = always_redraw(lambda: FunctionGraph(
            sine_function,
            color=BLUE
        ))
        self.add(sine_graph)

        # Animate the sine wave from y=sin(0.1*x) to y=sin(10*x) over the course of 6 seconds.
        self.play(tracker.animate(run_time=6).set_value(tracker.get_value() * 100)),
