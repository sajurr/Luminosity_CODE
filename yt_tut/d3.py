# This magic command calls the animation and gets rid of any unecessary output
from manim import*

class TwoMinSingleDot(Scene):
  def construct(self):
      # Create the axes object and labels
      ax = Axes(x_range=[-4.5, 4.5], y_range=[0, 30, 10], axis_config={"include_tip": False})
      labels = ax.get_axis_labels(x_label="x", y_label="f(x)")
      
      # Example Function
      def func(x):
          return (0.1*(x**4)) - (x**2) + .5*x + 9 + 5*np.sin(x)
      
      # Plot the function on the axes
      graph = ax.plot(func, x_range=[-4, 4], color=GREEN)

      # Create a pair of ValueTracker objetcs, one to track the X coordinate and one to track the Y coord
      # Value Tracker objects can be animated
      xt = ValueTracker(-4)
      yt = ValueTracker(30)

      # Create the dot mobject to its initial point (the values of the ValueTrackers)
      initial_point = [ax.c2p(xt.get_value(), yt.get_value())]
      dot = Dot(point=initial_point)

      # Explicitly defining the updater fucntion in order to remove it later
      def updater_1(mobj):
          mobj.move_to(ax.c2p(xt.get_value(), yt.get_value()))

      # Add the updater to the object
      dot.add_updater(updater_1)

      # Add the (m)objects and animate changing the dot's y-value to the function line
      self.add(ax, labels, graph, dot)
      self.wait(1) # ** To add suspense **
      self.play(yt.animate.set_value(func(xt.get_value())))

      # Clear the first updater to add a new one
      dot.remove_updater(updater_1)

      # Because we wont have to remove this updater we can just define it in the method
      dot.add_updater(lambda x: x.move_to(ax.c2p(xt.get_value(), func(xt.get_value()))))
      xspace = np.linspace(-4, 1.32, 300)
      min_idx = func(xspace).argmin()

      # Second animation step: change the x value tracker to the minimum point, updater will move dot along line
      self.play(xt.animate.set_value(xspace[min_idx]), run_time=2)
      self.wait()
