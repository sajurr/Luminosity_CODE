from pyclbr import Function
from turtle import fillcolor
from venv import create
from manim import*
import numpy as np
import colour as Color

Home = "C:\Z\YOUTUBE\P1"

class WritingProblem(Scene):
    def construct(self):

        prob_statement = Text("From point A located on a highway one has to get \n by car as soon as possible to point B located in the field at \n a distance l from the highway. \n It is known that the car moves in the \n field n times slower than on the highway, \n at what distance from point D one must turn off the highway?", font_size=25, color=YELLOW).to_edge(UP)
        prob_img = SVGMobject(f"{Home}\\image2vector.svg").next_to(prob_statement, DOWN, buff=0.6)
        cred = Text("Problem 17 (Chapter 1), 'Problems in General Physics'\n By: I.E. Irodov", font_size=11).to_edge(DOWN + RIGHT)
        box = SurroundingRectangle(prob_statement)

        self.play(Write(prob_statement), run_time=4)
        self.play(DrawBorderThenFill(box), run_time=3)
        self.play(DrawBorderThenFill(prob_img), run_time=3)
        self.wait()
        self.play(FadeIn(cred))
        self.wait() 


class MakingDiagram(Scene):
    def construct(self):
        
        dot_1 = Dot(color=BLUE).to_corner(LEFT)
        label_1 = Text("A", font_size=25, color=YELLOW).next_to(dot_1, UP)
        dot_2 = Dot(color=BLUE_A).next_to(dot_1, RIGHT, buff=2)
        label_2 = Text("C", font_size=25, color=YELLOW).next_to(dot_2, UP)
        dot_3 = Dot(color=BLUE_A).next_to(dot_2, RIGHT, buff=2)
        label_3 = Text("D", font_size=25, color=YELLOW).next_to(dot_3, UP)
        dot_4 = Dot(color=RED).next_to(dot_3, DOWN, buff=2)
        label_4 = Text("B", font_size=25, color=YELLOW).next_to(dot_4, RIGHT)
        line = Line(start=dot_1, end=dot_3)
        line2 = Line(start=dot_3, end=dot_4).set_color(BLUE)
        line3 = DashedLine(start=dot_2, end=dot_4).set_color(GREEN)
        line_above_CD = Line(dot_2, dot_3).set_color(BLUE)
        g1 = VGroup(dot_1, dot_2, dot_3, dot_4)
        g2 = VGroup(label_1, label_2, label_3, label_4)
        g_ = VGroup(g1, g2, line, line2, line3, line_above_CD)
        g_.save_state()



        self.add(g1)
        self.play(Write(g2))
        self.play(Create(line), Create(line2))
        self.wait()
        self.play(Create(line3))
        self.wait(2)
        self.play(g_.animate.shift(UP*5/2).scale(0.6))
        self.wait(2)
        self.play(Indicate(line))
        self.play(Indicate(line2))
        self.play(Indicate(line3))
        self.wait(2)
        
        arr1 = Arrow(dot_1, dot_2).set_color(RED)
        arr2 = Arrow(dot_2, dot_4).set_color(RED)
        self.play(DrawBorderThenFill(arr1))
        self.play(DrawBorderThenFill(arr2))
        self.wait(2)


        br1 = Brace(line_above_CD, direction=UP, buff=0.4)
        label_x = Text("x", font_size=20, color=BLUE).next_to(br1, UP)
        self.play(GrowFromCenter(br1))
        self.play(Write(label_x), run_time=3)
        self.wait(2)

        exp_1 = MathTex("t_1=\\frac{AD-x}{nv}").to_edge(UR).set_color(YELLOW)
        self.play(TransformFromCopy(line, exp_1))
        self.wait(2)
        exp_2 = MathTex("t_2=\\frac{\\sqrt {x^2 + l^2}}{v}").next_to(exp_1, DOWN).set_color(YELLOW)
        self.play(TransformFromCopy(line2, exp_2))
        self.wait(2)
        
        line5 = Text("The total time of the journey is then", font_size=16).next_to(exp_2, DOWN)
        self.play(FadeIn(line5))
        self.wait()
        exp_3 = MathTex("t=t_1 + t_2 = \\frac{AD-x}{nv}+\\frac{\sqrt {x^2 + l^2}}{v}").set_color(BLUE)
        self.play(Write(exp_3), run_time=2)
        self.wait()
        self.play(Indicate(exp_3))
        self.wait(2)


class Minima(Scene):
    def construct(self):
        ax = NumberPlane()
        plot1 = ax.plot(lambda x: x**2, color=YELLOW)
        dot = Dot()
        min = ax.get_secant_slope_group(x=0, graph=plot1, dx=0.001, secant_line_color=RED, secant_line_length=4)
        
        self.play(DrawBorderThenFill(ax), run_time=1)
        self.play(Create(plot1))
        self.wait()
        self.play(Create(min))
        self.add(dot)
        self.wait(3)


class TakingDerivative(Scene):
    def construct(self):
    
        exp = MathTex("t=t_1 + t_2 = \\frac{AD-x}{nv}+\\frac{\sqrt {x^2 + l^2}}{v}").set_color(BLUE).to_edge(UL)
        der1 = MathTex("\\frac{dt}{dx}\\ & = 0").scale(0.8).next_to(exp, DOWN)
        der2 = MathTex("\\Rightarrow \\frac{1}{v} (-\\frac{1}{n} + \\frac{x}{\\sqrt{x^2 + l^2}})").next_to(der1, DOWN).scale(0.8)
        der3 = MathTex("\\Rightarrow n^2 x^2=l^2 + x^2").next_to(der2, DOWN).scale(0.8)
        text = Text("Yielding:", font_size=18, color=GREEN).next_to(der3, DOWN)
        der4 = MathTex("x=\\frac{l}{\\sqrt{n^2 - 1}}").next_to(text, RIGHT + DOWN, buff=0.4).set_color(BLUE)
        box = SurroundingRectangle(der4, buff=0.2, color=BLUE)
        shortest_time = Text("path with minimum time", font_size=24).to_edge(RIGHT, buff=0.2)
        arr = Arrow(shortest_time, box, buff=SMALL_BUFF, color=BLUE)
        rect = SurroundingRectangle(shortest_time, corner_radius=0.15, color=YELLOW)

        self.play(Write(exp), run_time=1)
        self.play(DrawBorderThenFill(der1), run_time=1)
        self.play(DrawBorderThenFill(der2), run_time=1)
        self.play(DrawBorderThenFill(der3), run_time=1)
        self.play(FadeIn(text))
        self.play(DrawBorderThenFill(der4), run_time=1)
        self.play(DrawBorderThenFill(box), run_time=3)
        self.play(DrawBorderThenFill(arr), DrawBorderThenFill(shortest_time), DrawBorderThenFill(rect),run_time=4)
        self.wait(5)
        

class Snell(Scene):
    def construct(self):
        
        sq = Square().set_color(BLUE)
        sq.generate_target()
        sq.target.set_fill(BLUE, opacity=0.7)
        sq.target.scale(7).shift(DOWN*7)
        sq.save_state()
        
        self.add(sq)
        self.wait()
        self.play(MoveToTarget(sq))
        self.wait(3)

        #dot = Dot(UL)
        #traced_beam = TracedPath(dot.get_center, dissipating_time=0.9, stroke_opacity=[0, 1])
        #line = Line(start=sq, end=sq)
        #dot = Dot(line)
        #line2 = Line(start=dot, end=sq)
        #self.play(Create(line), Create(line2))
        #self.play(Create(dot))
        #self.play(traced_beam.animate(path_arc=PI / 6).shift(RIGHT * 8))
        #self.play(traced_beam.animate(path_arc=-PI / 6).shift(RIGHT * 2))
        #self.play(traced_beam.animate(path_arc=PI / 6).shift(RIGHT * 2))
        #self.play(traced_beam.animate(path_arc=-PI / 6).shift(RIGHT * 2))
        
        func1 = FunctionGraph(lambda x: -x, color=YELLOW, x_range=(-10, 0))
        func2 = FunctionGraph(lambda x: -1.4*x, color=YELLOW, x_range=(0, 10))
        dashed_line = DashedLine(start=(0,-4,0), end=(0,4,4))
        #theta_1 = MathTex("\\theta_1")
        #theta_1.add_updater(
        #    lambda m: m.move_to(func1).shift(.25*UL+1.5*LEFT)).set_color(RED_B)
        #theta_2 = MathTex("\\theta_2") 
        #theta_2.add_updater(
        #    lambda m: m.move_to(func2).shift(.25*UL+1.5*LEFT)).set_color(RED_C)
        label_1 = MathTex("\\theta_1").next_to(ORIGIN, UP + 2*LEFT).set_color(BLUE)
        label_2 = MathTex("\\theta_2").next_to(ORIGIN, DOWN + 2*RIGHT).set_color(GREEN)
        arc1 = ArcBetweenPoints(start=(0, 1, 0), end=(-1, 1, 0), angle=TAU/6)
        arc2 = ArcBetweenPoints(start=(0, -1, 0), end=(0.7, -1, 0))
        Snell = Text("Snell's Law:", font_size=18).to_edge(UP , buff=0.2).set_color(YELLOW)
        expr = MathTex("\\frac{\\sin \\left( \\theta _1 \\right)}{v_1}=\\frac{\\sin \\left( \\theta _2 \\right)}{v_2}", font_size=30).next_to(Snell, DOWN, buff=0.2)
        box = SurroundingRectangle(expr, buff=SMALL_BUFF)

        self.play(Create(dashed_line))
        self.play(FadeIn(func1))
        self.play(ApplyWave(func1, firection=RIGHT, amplitude=0.15, wave_func=smooth, ripples=5), run_time=3)
        self.play(Write(label_1), Create(arc1))
        #self.play(Write(theta_1))        
        self.play(FadeIn(func2))
        self.play(ApplyWave(func2, firection=RIGHT, amplitude=0.15, wave_func=smooth, ripples=5), run_time=3)
        self.play(Write(label_2), Create(arc2))
        #self.play(Write(theta_2))
        self.play(FadeIn(Snell), Write(expr), DrawBorderThenFill(box), run_time=2)
        self.wait(2)
        self.play(Uncreate(func1), Uncreate(func2), Uncreate(dashed_line), Uncreate(label_1), Uncreate(label_2), Uncreate(arc1), Uncreate(arc2), Uncreate(Snell), Uncreate(expr), Uncreate(box), Uncreate(sq) ,run_time=2)
        self.wait(2)

#class Snell2(Scene):
#   def construct(self):
#        theta = ValueTracker(np.arctan(1/3)) 
#        theta2 = ValueTracker((np.sin(0.75*np.sin(theta.get_value())))) # the refracted angle's value
#        midplane = Line(start = (-6,0,0), end = (6,0,0))
#        normal = Line(start = (0,-3,0), end = (0,3,0))
#        normal = DashedVMobject(normal)
 #       inc_start = (-6, 2, 0)
  #      inc_finish = (0,0, 0)
   #     refrac_start = (0,0,0)
    #    refrac_fin = (2, -3, 0) # magnitude of this matters but the coordinates really don't...
     #   in_arrow = Arrow(start = inc_start, end = inc_finish)
#        out_arrow = Arrow(start = refrac_start, end = refrac_fin)
#        # ... because the set_angle method effectively changes the coords here, before it is called onscreen
#        out_arrow.set_angle(3*PI/2 + np.sin(0.75*np.sin(theta.get_value())))
#        left_arc = Arc()
#        left_arc.add_updater(
#            lambda m: m.become(
#                Arc(
#            radius = 1.5,
#            start_angle = PI/2,
#            angle = PI/2 - theta.get_value()
#            )))
#        right_arc = Arc()
#        right_arc.add_updater(
#            lambda m: m.become(
#                Arc(
#            radius = 1.5,
#            start_angle = 3*PI/2,
#            angle = np.sin(0.75*np.sin(theta.get_value()))
###            )))
#        label_1 = MathTex('\\theta_{1}')
####        label_2 = MathTex('\\theta_{2#}')
#        label_1.add_updater(
#            lambda m: m.move_to(left_arc).shift(.165*LEFT+.8*UP))
#        label_2.add_updater(
#            lambda m: m.move_to(right_arc).shift(.165*RIGHT+.8*DOWN))
#        self.add(midplane, normal, in_arrow, left_arc, label_1)
#        self.wait()
#        self.play(GrowArrow(out_arrow))
#        in_arrow.add_updater(
#            lambda m: 
#            m.become(
#                # we use become here because I need to move the arrow's start, which would be fixed if we didn't redefine it like so
#                Arrow(start = (-(np.sqrt(40)*np.cos(theta.get_value())), (np.sqrt(40)*np.sin(theta.get_value())), 0), end = inc_finish)
#                ))
#        out_arrow.add_updater(
#            # but in this case we can use the set_angle method because all we have to do is rotate it.
#            lambda m: m.set_angle(3*PI/2 + np.sin(0.75*np.sin(theta.get_value()))))
#        self.play(Create(right_arc))
#        self.play(Write(label_2))
#        self.play(theta.animate, rotate = PI/3- np.arctan(1/3), rate_func = there_and_back, run_time = 2) 
#        self.wait()
#        self.play(ApplyMethod(in_arrow.rotate, PI))
#        self.wait()

class VehicleToBeam(Scene):
    def construct(self):
        
        dot = Dot(point=(-3,0,0)).set_color(BLUE)
        func = FunctionGraph(lambda x: 0, x_range=(1, 5), color=YELLOW)
        eq = MathTex("\\Leftrightarrow").next_to(dot, RIGHT)
        text1 = Text("vehicle/object", font_size=24).next_to(dot, 2*DOWN).set_color(YELLOW)
        arr1 = Arrow(start=dot, end=text1)
        text2 = Text("light beam", font_size=24).next_to(func, 2*DOWN).set_color(YELLOW)
        arr2 = Arrow(start=func, end=text2)
        #func2 = FunctionGraph(lambda x: x, x_range=(-0.5, -4), color=YELLOW)

        self.play(DrawBorderThenFill(dot))
        self.play(dot.animate.shift(RIGHT*3), rate_func=there_and_back, run_time=4)
        self.wait(0.5)
        self.play(TransformFromCopy(dot, func), Create(eq), Write(text1), Create(arr1), run_time=2)
        self.wait(0.3)
        self.play(ApplyWave(func, ripples=7, run_time=2.4), Write(text2), Create(arr2))
        self.wait(1.5)
        self.play(Uncreate(dot), Uncreate(eq), Uncreate(text1), Uncreate(text2), Uncreate(arr2), Uncreate(arr1), run_time=1)
        self.wait()

        sq = Square(side_length=5.2).to_corner(LEFT*2)
        sq.generate_target()
        sq.target.set_fill(BLUE, opacity=0.6)
        sq.save_state()
        
        self.add(sq)
        self.play(MoveToTarget(sq))
        self.play(sq.animate.rotate(PI/4).shift(DOWN))
        self.wait()
        self.play(func.animate.shift(LEFT*2))
        self.play(func.animate.shift(LEFT*4).rotate(PI/32), run_time=2)
        #self.play(FadeIn(func2))
        #self.play(TransformFromCopy(func, func2))
        self.wait(3)


class AtoB(Scene):
    def construct(self):
        dot_1 = Dot(color=BLUE).to_corner(LEFT)
        label_1 = Text("A", font_size=25, color=YELLOW).next_to(dot_1, UP)
        dot_2 = Dot(color=BLUE_A).next_to(dot_1, RIGHT, buff=2)
        label_2 = Text("C", font_size=25, color=YELLOW).next_to(dot_2, UP)
        dot_3 = Dot(color=BLUE_A).next_to(dot_2, RIGHT, buff=2)
        label_3 = Text("D", font_size=25, color=YELLOW).next_to(dot_3, UP)
        dot_4 = Dot(color=RED).next_to(dot_3, DOWN, buff=2)
        label_4 = Text("B", font_size=25, color=YELLOW).next_to(dot_4, RIGHT)
        line = Line(start=dot_1, end=dot_2)
        line__ = Line(start=dot_2, end=dot_3)
        line2 = Line(start=dot_3, end=dot_4).set_color(RED)
        line3 = DashedLine(start=dot_1, end=dot_4).set_color(GREEN)
        line_above_CD = Line(dot_2, dot_3).set_color(BLUE)
        g1 = VGroup(dot_1, dot_2, dot_3, dot_4)
        g2 = VGroup(label_1, label_2, label_3, label_4, line__)
        g_ = VGroup(g1, g2, line, line2, line3, line_above_CD)
        g_.save_state()
        cross = Cross(g2).scale(1.5)
        origin_point = (0,0,0)

        self.add(g1)
        self.play(Write(g2))
        self.play(Create(line), Create(line2))
        self.wait()
        self.play(Create(line3))
        self.wait(2)
        self.play(DrawBorderThenFill(cross))
        self.wait(2)
        self.play(Uncreate(cross), Uncreate(line3))
        self.wait(2)

        self.play(g_.animate.next_to(origin_point).scale(0.7))
        self.wait(1)

        
        arr = Arrow(start=dot_1, end=dot_2)
        lab1 = MathTex("\\text{Angle of incidence}=90^o").to_edge(UP).scale(0.6)
        group1 = VGroup(lab1)
        arr2 = Arrow(start=dot_2, end=dot_4).set_color(YELLOW)
        lab2 = MathTex("\\text{Angle of refraction}=\\theta").next_to(group1, DOWN).scale(0.6)
        group2 = VGroup(lab2)

        self.play(Create(group1), DrawBorderThenFill(arr))
        self.wait()
        self.play(Create(group2), DrawBorderThenFill(arr2))
        self.wait(2)

        snell = Text("From Snell's law, we have: ", font_size=20).to_edge(UL).set_color(BLUE)
        exp = MathTex("\\frac{\\sin \\left( {90^o} \\right)}{v_1}=\\frac{\\sin \\left( {\\theta }_{2} \\right)}{v_2}", font_size=30).next_to(snell, DOWN)
        self.play(GrowFromCenter(snell), GrowFromCenter(exp))
        self.wait()
        
        self.play(ApplyWave(line, direction=UP, rate_func=linear))
        self.play(ApplyWave(arr2, direction=UP, rate_func=linear), run_time=1)
        self.wait(2)

        exp2 = MathTex("\\frac{1}{n v_2}=\\frac{\\sin \\left( {\\theta _2} \\right)}{v_2}\\Rightarrow \\sin \\left( {\\theta _2} \\right)=\\frac{1}{n}", font_size=30).to_edge(LEFT+UP, buff=2).set_color(YELLOW)
        self.play(DrawBorderThenFill(exp2))
        self.wait(2)
        geo = MathTex("\\sin \\left( {\\theta _2} \\right), \\text{is}\\, \\frac{x}{\\sqrt{x^2 + l^2}", font_size=30).next_to(g_, DOWN)
        self.play(TransformFromCopy(g_, geo))
        self.wait(2)


        exp3 = MathTex("\\frac{x}{\\sqrt x^2 + l^2}=\\frac{1}{n}\\Rightarrow x^2 n^2 = x^2 + l^2 \\Rightarrow x=\\frac{l}{\sqrt n^2 - 1}", font_size=30).next_to(exp2, DOWN).set_color(YELLOW)
        self.play(TransformFromCopy(exp2, exp3))
        self.wait(2)
        box= SurroundingRectangle(exp3, buff =0.2).set_color(YELLOW)
        self.play(DrawBorderThenFill(box), run_time=3)
        self.wait(4)



class Thumbnail(Scene):
    def construct(self):
        
        t2 = ImageMobject(f"{Home}\\Screenshot 2022-06-24 094105.jpg").to_edge(DL, buff=1).scale(1.2)
        Head = Text("Shortest path between A and B ??", font_size=40).to_edge(UP, buff=1).set_color(YELLOW)
        
        Head[19].set_color(RED)
        Head[23].set_color(RED)
        
        
        self.add(t2)
        self.add(Head)

        dot_1 = Dot(color=BLUE).to_corner(LEFT)
        label_1 = Text("A", font_size=25, color=YELLOW).next_to(dot_1, UP)
        dot_2 = Dot(color=BLUE_A).next_to(dot_1, RIGHT, buff=2)
        label_2 = Text("C", font_size=25, color=YELLOW).next_to(dot_2, UP)
        dot_3 = Dot(color=BLUE_A).next_to(dot_2, RIGHT, buff=2)
        label_3 = Text("D", font_size=25, color=YELLOW).next_to(dot_3, UP)
        dot_4 = Dot(color=RED).next_to(dot_3, DOWN, buff=2)
        label_4 = Text("B", font_size=25, color=YELLOW).next_to(dot_4, RIGHT)
        line = DashedLine(start=dot_1, end=dot_2)
        line__ = Line(start=dot_2, end=dot_3)
        line2 = Line(start=dot_3, end=dot_4).set_color(RED)
        line3 = DashedLine(start=dot_2, end=dot_4).set_color(GREEN)
        line_above_CD = Line(dot_2, dot_3).set_color(BLUE)
        g1 = VGroup(dot_1, dot_2, dot_3, dot_4)
        g2 = VGroup(label_1, label_2, label_3, label_4, line__)
        g_ = VGroup(g1, g2, line, line2, line3, line_above_CD).to_edge(DR, buff=1.7).scale(1)
        g_.save_state()

        self.add(g_)

    

