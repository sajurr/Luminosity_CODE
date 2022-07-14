from manim import*
class ThreeScene(ThreeDScene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def construct(self):
        def param_surface(u, v):
            x = u
            y = v
            z = np.sin(2*x) * np.cos(y)
            return z

        self.axes = ThreeDAxes()
        self.space = VGroup(self.axes,NumberPlane())
        surface_plane = Surface(
               lambda u, v: 
               self.axes.c2p(u, v, param_surface(u, v)),
               resolution=(15, 15), v_range=[0, 5], u_range=[0, 5],
               z_index=3)
        

        self.play(Create(self.space), run_time=4)
        self.wait()
        self.play(FadeIn(surface_plane), run_time=3)
        surface_plane.set_z_index(10, True)
        self.wait(2)
        self.play(surface_plane.animate.set_z_index(10, True),
        run_time=2)
        self.wait(2)