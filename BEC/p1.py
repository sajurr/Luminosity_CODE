from tkinter import Scale
from manim import*
from imports import*

HOME1= "C:\Z\YOUTUBE\BEC"
class SCENE1(Scene):
    def construct(self):
        s_helium = ImageMobject(f"{HOME1}\\Bose_Einstein_condensate.png").scale(0.5)

        self.play(GrowFromCenter(s_helium))
        
        self.wait(3)
        self.play(s_helium.animate.to_edge(UR).scale(0.35))
        self.wait(4)