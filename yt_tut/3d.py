from cmath import sin
from manim import*

class ClassName(ThreeDScene):
    
    def construct(self):
      s_color=YELLOW
      t_color=GREEN
      
      axis=ThreeDAxes()
      self.set_camera_orientation(phi=75*DEGREES,theta=45*DEGREES)
      self.play(Create(axis),run_time=1)
     
      self.play(axis.animate.to_edge(UR),run_time=3)
      self.wait()



      plane=Rectangle(color=t_color,height=3,width=5).set_fill(color=t_color,opacity=0.6).move_to(axis.get_origin()+[0,0,1]).set_stroke(color=t_color)
      self.play(Create(plane,run_time=2))
      
      vector=Arrow3D(start=plane.get_center(),end=plane.get_center()+[0,0,4],color=s_color)
      self.move_camera(frame_center=axis.get_origin(),zoom=2)
      self.play(Create(vector),run_time=2)
      self.wait()