from manim import*
class Tute2(Scene):  #ILLUSTRATING POLAR PLANE WITH A SINE CURVE
    def construct(self):
        
        
        e = ValueTracker(0.01) #Tracks the end value of both functions

        plane = PolarPlane(radius_max=3).add_coordinates()
        plane.shift(LEFT*2)
        graph1 = always_redraw(lambda : 
        ParametricFunction(lambda t : plane.polar_to_point(2*np.sin(3*t), t), 
        t_range = [0, e.get_value()], color = GREEN)
        )
        dot1 = always_redraw(lambda : Dot(fill_color = GREEN, fill_opacity = 0.8).scale(0.5).move_to(graph1.get_end())
        )

        axes = Axes(x_range = [0, 4, 1], x_length=3, y_range=[-3,3,1], y_length=3).shift(RIGHT*4)
        axes.add_coordinates()
        graph2 = always_redraw(lambda : 
        axes.plot(lambda x : 2*np.sin(3*x), x_range = [0, e.get_value()], color = GREEN)
        )
        dot2 = always_redraw(lambda : Dot(fill_color = GREEN, fill_opacity = 0.8).scale(0.5).move_to(graph2.get_end())
        )

        title = MathTex("f(\\theta) = 2sin(3\\theta)", color = GREEN).next_to(axes, UP, buff=0.2)

        self.play(LaggedStart(
            Write(plane), Create(axes), Write(title),
            run_time=6, lag_ratio=0.5)
        )
        self.add(graph1, graph2, dot1, dot2)
        self.play(e.animate.set_value(PI), run_time = 10, rate_func = linear)
        self.wait()