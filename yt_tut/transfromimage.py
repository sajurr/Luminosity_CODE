from turtle import home
from manim import*
HOME1 = "C:\IMAGES\HAI YE KUCH"
class Transfrom(Scene):
    def construct(self):
        
        img = ImageMobject(f"{HOME1}\\2021-09-20 02.06.53 1.jpg")
        
        img2 = ImageMobject(f"{HOME1}\\2021-09-20 02.06.54 1.jpg")

        self.play(FadeIn(img), run_time=2)
        self.wait()
        self.play(Transform(img,img2))
        self.wait()