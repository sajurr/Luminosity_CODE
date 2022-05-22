from manim import*
class Tute1(Scene): #ILLUSTRATING HOW TO PUT A NUMBER PLANE ON SCENE WITH A GRAPH, and a line using c2p
    def construct(self):

        backg_plane = NumberPlane(x_range=[-7,7,1], y_range=[-4,4,1])
        backg_plane.add_coordinates()
        

        my_plane = NumberPlane(x_range = [-6,6], x_length = 5,
        y_range = [-10,10], y_length=5)
        my_plane.add_coordinates()
        my_plane.shift(RIGHT*3)

        my_function = my_plane.plot(lambda x : 0.1*(x-5)*x*(x+5), 
        x_range=[-6,6], color = GREEN_B)

        label = MathTex("f(x)=0.1x(x-5)(x+5)").next_to(
            my_plane, UP, buff=0.2)

        area = my_plane.get_area(graph = my_function, 
        x_range = [-5,5], color = [BLUE,YELLOW])

        horiz_line = Line(
            start = my_plane.c2p(0, my_function.underlying_function(-2)),
        end = my_plane.c2p(-2, my_function.underlying_function(-2)),
        stroke_color = YELLOW, stroke_width = 2)

        self.play(FadeIn(backg_plane), run_time=6)
        self.play(backg_plane.animate.set_opacity(0.2))
        self.wait()
        self.play(DrawBorderThenFill(my_plane), run_time=2)
        self.wait()
        self.play(Create(my_function), Write(label), run_time=2)
        self.wait()
        self.play(FadeIn(area), run_time = 2)
        self.wait()
        self.play(Create(horiz_line), run_time = 2)
        self.wait()