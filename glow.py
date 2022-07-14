from manim import*

class GlowCircle(VGroup):
    def __init__(self,point=ORIGIN,radius=2,color=GREEN,stretch=0.6,no_of_rings=80,**kwargs):        
        glowouter=VGroup()
        glowinner=VGroup()

        for i,s_w in zip(np.linspace(radius,radius+stretch,no_of_rings),np.linspace(1,0,no_of_rings)):     
            glowouter.add(Circle(radius=i,color=color,stroke_opacity=s_w*0.2).move_to(point))
            
        for i,s_w in zip(np.linspace(radius,radius-stretch,no_of_rings),np.linspace(1,0,no_of_rings)):
            glowinner.add(Circle(radius=i,color=color,stroke_opacity=s_w*0.2).move_to(point))
        
        super().__init__(glowouter,glowinner)


class glowc(Scene):
    def construct(self):
        GlowGroup=VGroup()
        x=[-3, -3, 3, 3]
        y=[-2, 2, 2, -2]
        col=[RED,GREEN,BLUE,YELLOW]
        for c,(i,j) in enumerate(zip(x,y)):
            gc=GlowCircle(point=[i,j,0],radius=1,color=col[c],stretch=0.5)
            self.add(gc)
            GlowGroup.add(gc)
        self.play(AnimationGroup(*[Rotating(gc,radians=2*TAU,axis=Y_AXIS) for gc in GlowGroup],lag_ratio=0.5,run_time=10,rate_func=linear))
        self.wait()