from manim import*
import numpy as np

class CameraPosition(ThreeDScene):
	def construct(self):
	
		self.set_camera_orientation(phi=80 * DEGREES) #camera starting position
		axis=ThreeDAxes()
		self.add(axis)

		def para(t):
			return np.array((t, 2*np.sin(t),0))

		def para2(t):
			return np.array((t, 0,2*np.sin(t)))


		E_wave = ParametricFunction(para,t_range=[-TAU, TAU], color = PINK) 
		B_wave = ParametricFunction(para2,t_range=[-TAU, TAU], color = BLUE)
		
		n = 70     #number of ticks
		n_frames = 10 #Used 500 for the animation I posted 
		pos = -2*PI   #first tick
		r = 0.2    #rate of ticks
		#Tried with arrows, but it bugs, used lines instead
		arrows = VGroup(  *[Line([pos + r*i,0,0], [pos + r*i , 2*np.sin(pos + r*i) , 0], color = RED)    for i in range(n+ 1 ) ] ) 
		arrows2 = VGroup(  *[Line([pos + r*i,0,0], [pos + r*i ,   0 ,  2*np.sin(pos + r*i)], color = BLUE)    for i in range(n+ 1 ) ] ) 


		self.begin_ambient_camera_rotation(rate=0.3)

		for v in range(n_frames):
			self.set_camera_orientation(phi=80 * DEGREES, theta = -PI/2, rate=PI/10)
            
			def para3(t):
				return np.array((t, 2*np.sin(t - self.rate),0))

			def para4(t):
				return np.array((t, 0, 2*np.sin(t - self.rate)))

			E_wave_new = ParametricFunction(para3,t_range=[-TAU, TAU], color = RED)
			B_wave_new = ParametricFunction(para4,t_range=[-TAU, TAU], color = BLUE)

			new_arrow = VGroup(  *[Line([pos + r*i , 0,0 ], [pos + r*i   ,   2*np.sin(pos + r*i - self.rate  ),0] , color = RED) for i in range(n+ 1) ] ) 
			new_arrow2 = VGroup(  *[Line([pos + r*i , 0,0 ], [pos + r*i   ,  0, 2*np.sin(pos + r*i - self.rate  )] , color = BLUE) for i in range(n+ 1) ] ) 
			self.play(   Transform(arrows, new_arrow) , Transform(B_wave_new, B_wave_new) ,Transform(arrows2, new_arrow2) , Transform(E_wave, E_wave_new) ,run_time = 0.01       )