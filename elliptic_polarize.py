from manim import *
import numpy as np
import math

class Condition(Scene):
    def construct(self):
        eq = MathTex(
            "\\vec{E}=E_x \\sin (kz - \\omega t + \\phi_{o_x} ) \\hat {x} + E_y \\sin (kz - \\omega t + \\phi_{o_y} ) \\hat {y}"
        ).set_color(YELLOW)
        eq2 = MathTex(
            "\\vec{E}=E_x \\sin ( - \\omega t ) \\hat {x} + E_y \\sin ( - \\omega t - \\pi \\over 4 ) \\hat {y}"
        ).set_color(YELLOW)
        
        case_cond_1 = Text(" Under the condition", font_size=25).next_to(eq2, DOWN).set_color(BLUE)
        case_cond_2 = MathTex("E_x = 2 E_y,", " and, ", "\\phi_{o_x}=0, ","\\phi_{o_y}=\\frac{\\pi}{4} ", "becomes").next_to(case_cond_1, DOWN).set_color(BLUE)
        
        self.play(Write(eq))
        self.wait(0.5)
        self.play(Transform(eq, case_cond_1))
        self.wait(0.5)
        self.play(Write(case_cond_2))
        self.wait(0.5)
        self.play(Transform(eq, eq2))
        self.wait(0.5)
        self.play(FadeOut(eq), FadeOut(case_cond_2))

class FromThreeDToTwoD(ThreeDScene):
    def construct(self):
        ax = ThreeDAxes().set_color(BLUE)
        self.set_camera_orientation(phi=75*DEGREES, theta=-45*DEGREES)
    
        self.play(Create(ax))
        self.move_camera(phi=0*DEGREES, theta=-90*DEGREES)
        self.wait(1)
        


class SineCurveUnitCircle(Scene):
    '''I had written/referenced the intial code for the dot tracing a circle which I have modified to an ellipse for this assignment.'''
    def construct(self):
        self.show_axis()
        self.show_circle()
        self.move_dot_and_draw_curve()
        self.wait()

    def show_axis(self):
        x_start = np.array([-6,0,0])
        x_end = np.array([6,0,0])

        y_start = np.array([-4,-2,0])
        y_end = np.array([-4,2,0])

        x_axis = Line(x_start, x_end)
        y_axis = Line(y_start, y_end)

        ax_group = VGroup(x_axis, y_axis)

        self.add(ax_group)
        self.add_x_labels()

        self.origin_point = np.array([-4,0,0])
        self.curve_start = np.array([-3,0,0])

    def add_x_labels(self):
        x_labels = [
            MathTex("\pi"), MathTex("2 \pi"),
            MathTex("3 \pi"), MathTex("4 \pi"),
        ]

        for i in range(len(x_labels)):
            x_labels[i].next_to(np.array([-1 + 2*i, 0, 0]), DOWN)
            self.add(x_labels[i])

    def show_circle(self):
        circle = Ellipse(width=2, height=1)
        circle.move_to(self.origin_point)
        self.add(circle)
        self.circle = circle

    def move_dot_and_draw_curve(self):
        orbit = self.circle
        origin_point = self.origin_point

        dot = Dot(radius=0.06, color=YELLOW)
        dot.move_to(orbit.point_from_proportion(0))
        self.t_offset = 0
        rate = 0.25

        def go_around_circle(mob, dt):
            self.t_offset += (dt * rate)
            # print(self.t_offset)
            mob.move_to(orbit.point_from_proportion(self.t_offset % 1))

        def get_line_to_circle():
            return Line(origin_point, dot.get_center(), color=BLUE)

        def get_line_to_curve():
            x = self.curve_start[0] + self.t_offset * 4
            y = dot.get_center()[1]
            return Line(dot.get_center(), np.array([x,y,0]), color=YELLOW_A, stroke_width=1.4 )


        self.curve = VGroup()
        self.curve.add(Line(self.curve_start,self.curve_start))
        def get_curve():
            last_line = self.curve[-1]
            x = self.curve_start[0] + self.t_offset * 4
            y = dot.get_center()[1]
            new_line = Line(last_line.get_end(),np.array([x,y,0]), color=YELLOW_D)
            self.curve.add(new_line)

            return self.curve

        dot.add_updater(go_around_circle)

        origin_to_circle_line = always_redraw(get_line_to_circle)
        dot_to_curve_line = always_redraw(get_line_to_curve)
        sine_curve_line = always_redraw(get_curve)

        self.add(dot)
        self.add(orbit, origin_to_circle_line, dot_to_curve_line, sine_curve_line)
        self.wait(14)

        dot.remove_updater(go_around_circle)