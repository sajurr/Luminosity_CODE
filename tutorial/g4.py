from manim import* 
class Tute3(Scene): #Showing how to call 2 planes, put graphs on each and call elements to each
    def construct(self):

        backg_plane = NumberPlane(x_range=[-7,7,1], y_range=[-4,4,1]).add_coordinates()

        plane = NumberPlane(x_range = [-4,4,1], x_length = 4, 
        y_range= [0, 20, 5], y_length=4).add_coordinates()
        plane.shift(LEFT*3+DOWN*1.5)
        plane_graph = plane.plot(lambda x : x**2, 
        x_range = [-4,4], color = GREEN)
        area = plane.get_riemann_rectangles(graph = plane_graph, x_range=[-2,2], dx=0.005)

        axes = Axes(x_range = [-4,4,1], x_length = 4, 
        y_range= [-20,20,5], y_length=4).add_coordinates()
        axes.shift(RIGHT*3+DOWN*1.5)
        axes_graph = axes.plot(lambda x : 2*x, 
        x_range=[-4,4], color = YELLOW)
        v_lines = axes.get_vertical_lines_to_graph(
            graph = axes_graph, x_range=[-3,3], num_lines = 12)

       

        self.play(FadeIn(backg_plane), run_time=2)
        self.play(backg_plane.animate.set_opacity(0.3))
        self.play(Write(plane), Create(axes), run_time=4)
        self.wait()
        self.play(Create(plane_graph), Create(axes_graph), run_time = 4)
        self.add(area, v_lines)
        self.wait()