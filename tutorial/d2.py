import math
from manim import*
import numpy as np 
from colour import Color
Home="C:\MikTex\SAVE\BACKUP SAVES\_SciAstra\IG"

class MovingDot(Scene):
    def construct(self):
        blue_dot = Dot(color=BLUE)
        blue_dot.save_state()
        dot_label = Text("Hello Dot!").next_to(blue_dot, UP)
        dot_label.add_updater(
            lambda mob: mob.next_to(blue_dot, UP)
        )

        self.add(blue_dot, dot_label)
        self.play(blue_dot.animate.shift(RIGHT))
        self.wait()
        self.play(blue_dot.animate.scale(8))
        self.wait(2)
        self.play(Restore(blue_dot))


class ElectroMagnetic(ThreeDScene):
    def construct(self):
        
        ax = ThreeDAxes()
        self.set_camera_orientation(phi=75*DEGREES, theta=45**DEGREES, distance=4)
        sin_x = ax.plot(lambda x: np.sin(x)).set_color(RED).set_opacity(0.6)
        sin_y = ax.plot(lambda y: np.sin(y)).set_color(BLUE).set_opacity(0.6)
        self.add(ax)
        self.play(Create(sin_x))
        self.play(Create(sin_y))
        self.wait()


        


class DotAndArrow(Scene):
    def construct(self):
        red_dot = Dot(color=RED).shift(LEFT)
        pointer = Arrow(ORIGIN, RIGHT).next_to(red_dot, LEFT)
        pointer.add_updater( # place the arrow next to the dot
            lambda mob : mob.next_to(red_dot, LEFT)
        )

        def shifter(mob, dt): # make the dot dot mmove  2 'munits' per second
            mob.shift(2*dt*RIGHT)
        red_dot.add_updater(shifter)

        def scene_scalar(dt): # scale mobjects depending on distance from origin
            for mob in self.mobjects:
                mob.set(width=2/(1 + np.linalg.norm(mob.get_center())))
        self.add_updater(scene_scalar)

        self.add(red_dot, pointer)
        self.update_self(0)
        self.wait(5)



class NewSVG(Scene):
    def construct(self):
        
        s1 = SVGMobject(f"{Home}\\sin_parabola.svg").scale(2)
        self.play(DrawBorderThenFill(s1, rate_func=smooth), run_time=4)
        self.wait()
        s2 = ImageMobject(f"{Home}\\1.png").scale(0.5).next_to(s1, DOWN)
        self.play(GrowFromCenter(s2, rate_func=smooth), run_time=4)
        self.wait()



class ThreeD(ThreeDScene):
    def construct(self):
        ax = ThreeDAxes(x_range=(-5, 5, 0), y_range=(-5, 5, 0), z_range=(-5, 5, 0))
        self.set_camera_orientation(phi=PI/3, theta=PI/4, distance=4)
        self.add(ax)

        

def PDF_normal(x, mu, sigma):
    '''
    General form of probability density function of univariate normal distribution
    '''
    return math.exp(-((x-mu)**2)/(2*sigma**2))/(sigma*math.sqrt(2*math.pi))
    
class AdjustMu(Scene):
    '''
    Scene to observe how adjustments to the mean of a normal distrubtion
    influences the shape of its probability density function
    '''

    def construct(self):
        ax = Axes(
            x_range = [-5, 5, 1],
            y_range = [0, 0.5, 0.1],
            axis_config = {'include_numbers':True}
        )

        # Initialize mu (distribution mean) ValueTracker to 0
        mu = ValueTracker(1)

        mu_text = MathTex("\\mu = ").next_to(ax, UP, buff=0.2).set_color(YELLOW)
        # Always redraw the decimal value for mu for each frame
        mu_value_text = always_redraw(
            lambda: DecimalNumber(num_decimal_places=2)
        .set_value(mu.get_value())
        .next_to(mu_text, RIGHT, buff=0.2)
        .set_color(YELLOW)
        )
        curve = always_redraw(
        lambda: ax.plot(
            lambda x: PDF_normal(x, mu.get_value(), 1), color=YELLOW)
    )
        self.add(ax, mu_text, mu_value_text)
        self.play(Create(curve))
        self.play(
            mu.animate.set_value(2), run_time=1,
            rate_func=rate_functions.smooth
        )
        self.wait()
        self.play(
            mu.animate.set_value(-2), run_time=1.5,
            rate_func=rate_functions.smooth
        )
        self.wait()
        self.play(
            mu.animate.set_value(0), run_time=1,
            rate_func=rate_functions.smooth
        )
        self.play(Uncreate(curve))



def PDF_bivariate_normal(x_1, x_2, mu_1=0, mu_2=0, sigma_1=1, sigma_2=1, rho=0):
    '''
    General form of probability density function of bivariate normal distribution
    '''
    normalizing_const = 1/(2 * math.pi * sigma_1 * sigma_2 * math.sqrt(1 - rho**2))
    exp_coeff = -(1/(2 * (1 - rho**2)))
    A = ((x_1 - mu_1)/sigma_1)**2
    B = -2 * rho * ((x_1 - mu_1)/sigma_1) * ((x_2 - mu_2)/sigma_2)
    C = ((x_2 - mu_2)/sigma_2)**2

    return normalizing_const * math.exp(exp_coeff*(A + B + C))

class StandardBivariateNormal(ThreeDScene):
    '''
    Plots the surface of the probability density function of the standard
    bivariate normal distribution
    '''

    def construct(self):
        ax = ThreeDAxes(
            x_range = [-4, 4, 1],
            y_range = [-4, 4, 1],
            z_range = [0, 0.2, 0.1]
        )
        x_label = ax.get_x_axis_label(r'x_1')
        y_label = ax.get_y_axis_label(r'x_2', edge=UP, buff=0.2)
        z_label = ax.get_z_axis_label(r'\phi(x_1, x_2)', buff=0.2)
        axis_labels = VGroup(x_label, y_label, z_label)


        distribution = Surface(
    lambda u, v: ax.c2p(u, v, PDF_bivariate_normal(u, v)),
    resolution=(42, 42),
    u_range=[-3.5, 3.5],
    v_range=[-3.5, 3.5],
    fill_opacity=0.7
)       
        distribution.set_color_by_gradient(RED, PURPLE)

        # Set up animation
        self.add(ax, axis_labels)
        self.set_camera_orientation(
            phi=75*DEGREES,
            theta=-70*DEGREES,
            frame_center=[0, 0, 2],
            zoom=0.75)
        # Begin animation
        self.play(Create(distribution))
        self.move_camera(theta=70*DEGREES, run_time=2)
        self.move_camera(theta=-70*DEGREES, run_time=2)
        self.play(Uncreate(distribution))


        mu_1 = ValueTracker(0)
        mu_2 = ValueTracker(0)

        mu_1_tex = MathTex(r'\mu_1 =')
        mu_1_value_text = always_redraw(
            lambda: DecimalNumber(num_decimal_places=2, include_sign=True)
            .set_value(mu_1.get_value())
            .next_to(mu_1_tex, RIGHT)
        )
        

        mu_2_tex = MathTex(r'\mu_2 =')
        mu_2_value_text = always_redraw(
            lambda: DecimalNumber(num_decimal_places=2, include_sign=True)
            .set_value(mu_2.get_value())
            .next_to(mu_2_tex, RIGHT)
        )

        # Define suface function of PDF, always redraw to allow for smooth
        # value adjustments to mu_1 and mu_2
        distribution = always_redraw(
            lambda: Surface(
                lambda u, v: ax.c2p(
                    u, v, PDF_bivariate_normal(
                        u, v, mu_1=mu_1.get_value(), mu_2=mu_2.get_value()
                    )
                ),
                resolution=(42, 42),
                u_range=[-4.5, 4.5],
                v_range=[-4.5, 4.5],
                fill_opacity=0.7
            )).set_color_by_gradient(RED, PURPLE_A)

        self.play(Create(distribution))
        self.play(
                mu_1.animate.set_value(2), run_time=2,
                rate_func=rate_functions.smooth
            )
        self.wait()
        self.play(
                mu_1.animate.set_value(0), run_time=1,
                rate_func=rate_functions.smooth
            )
        self.play(
                mu_2.animate.set_value(-2), run_time=2,
                rate_func=rate_functions.smooth
            )     
        self.wait()
        self.play(
                mu_2.animate.set_value(0), run_time=1,
                rate_func=rate_functions.smooth
            )
            # Top-down view
        self.move_camera(
                theta=-90*DEGREES,
                phi=0,
                frame_center=[0, 0, 0],
                zoom=0.5
            )
        self.play(
                mu_1.animate.set_value(-2),
                mu_2.animate.set_value(2),
                run_time=2,
                rate_func=rate_functions.smooth
            )
        self.wait()
        self.play(
                mu_1.animate.set_value(0),
                mu_2.animate.set_value(0),
                run_time=1,
                rate_fun=rate_functions.smooth
            )
            # Return camera to original position
        self.move_camera(
                theta=-70*DEGREES,
                phi=70*DEGREES,
                frame_center=[0, 0, 2],
                zoom=0.6
            )
        self.play(Uncreate(distribution))
        self.wait()


