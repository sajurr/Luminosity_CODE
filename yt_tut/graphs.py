from manim import*
class SinInterface(VGroup):
    CONFIG = {
        "x_size": 16,
        "y_size": 6,
        "axes_config":{
            "x_min": -7,
            "x_max": 7,
            "y_min": -2.5,
            "y_max": 2.5,
            "axis_config": {
                "color": LIGHT_GREY,
                "include_tip": False,
                "exclude_zero_from_default_numbers": False,
                "decimal_number_config": {
                    "num_decimal_places": 1,
                },
            },
            "x_axis_config": {
                "unit_size":0.8,
            },
            "y_axis_config": {
                "label_direction": LEFT,
                "unit_size":0.8,
                # "x_min": -2.5,
                # "x_max": 2.5,
            },
            "center_point": ORIGIN,
        },
        "margin": 1,
        "x_margin": 1.2,
        "y_margin": None,
        "grid_kwargs": {
            "stroke_width": 0.5
        }
    }
    def __init__(self, **kwargs):
        digest_config(self, kwargs)
        super().__init__(**kwargs)
        if self.x_size != None:
            self.axes_config["x_max"] = self.x_size / 2
            self.axes_config["x_min"] = -self.x_size / 2
        if self.y_size != None:
            self.axes_config["y_max"] = self.y_size / 2
            self.axes_config["y_min"] = -self.y_size / 2
        axes = Axes(**self.axes_config)
        inner_margin = RoundedRectangle(
            width=axes.get_width(),
            height=axes.get_height(),
            fill_opacity=1,
            fill_color=BLACK,
            stroke_width=0,
            stroke_color=WHITE,
        )
        if self.x_margin == None:
            self.x_margin = self.margin
        if self.y_margin == None:
            self.y_margin = self.margin
        # print(self.y_margin)
        outer_margin = Rectangle(
            width=axes.get_width()+self.x_margin,
            height=axes.get_height()+self.y_margin,
            fill_opacity=1,
            fill_color="#AAAAAA",
            stroke_width=0,
            stroke_color=WHITE,
        )
        axes[0].add_numbers()
        axes[1].add_numbers()
        axes[0][-1].remove(axes[0][-1][0])
        axes[0][-1].set_y((inner_margin.get_bottom()[1]+outer_margin.get_bottom()[1])/2)
        axes[1][-1].remove(axes[1][-1][0])
        axes[1][-1].set_x((inner_margin.get_left()[0]+outer_margin.get_left()[0])/2)
        # left_side = axes[1][-1].get_right()
        # for n in axes[1][-1]:
        #     n[:].align_to(inner_margin,RIGHT)
        VGroup(axes[0][-1],axes[1][-1]).set_color(BLACK)
        for i in [*axes[0][-1],*axes[1][-1]]:
            i.scale(0.5)
        columns = self.x_size 
        rows = self.y_size
        grid = Grid(rows, columns,width=self.x_size,height=self.y_size,line_kwargs=self.grid_kwargs)
        grid.set_width(inner_margin.get_width())
        grid.move_to(inner_margin)
        self.axes = axes
        self.add(outer_margin,inner_margin,grid,axes)

class SinFunctionInterface(Scene):
    def construct(self):
        A_COLOR = YELLOW
        K_COLOR = RED
        W_COLOR = TEAL
        PHI_COLOR = BLUE
        X_COLOR = PURPLE
        T_COLOR = GREEN
        interface = SinInterface()
        interface.to_edge(DOWN,buff=0.2)
        axes = interface.axes
        # f(x,t) = A * sin(k*x + w*t + s)
        A = ValueTracker(1)
        k = ValueTracker(1)
        w = ValueTracker(1)
        s = ValueTracker(0)
        t = ValueTracker(0)
        graph = axes.get_graph(lambda t: np.sin(t),color=RED)
        graph.add_updater(lambda mob: mob.become(
            axes.get_graph(
                lambda x: A.get_value() * np.sin(
                    k.get_value() * x + w.get_value() * t.get_value() + s.get_value()
                ),
            color=RED)
        ))
        graph.t_offset = 0

        labels = VGroup(
            self.get_range_line(-2,2,A,"A",A_COLOR),
            self.get_range_line(-2,2,s,"\\phi",PHI_COLOR),
            self.get_range_line(-2,2,k,"k",K_COLOR),
            self.get_range_line(-2,2,w,"\\omega",W_COLOR),
        )
        max_tex_width = max(*[l[1].get_width() for l in labels])
        for l in range(len(labels)):
            line = labels[l][0]
            line.align_to(labels[l],LEFT)
            line.shift(RIGHT*max_tex_width+0.2*RIGHT)
            labels[l][-1].next_to(labels[l][0],RIGHT,0.3)

        labels.scale(0.8)
        labels.arrange(DOWN,buff=0.2,aligned_edge=LEFT)
        labels.to_edge(UP,buff=0.1)
        labels.to_edge(LEFT)
        # -----------------
        t_tex = TexMobject("t",color=T_COLOR)
        t_dig = DecimalTextNumber(0,num_decimal_places=3)
        t_dig.add_updater(lambda mob: mob.set_value(t.get_value()))
        tg = VGroup(t_tex,t_dig).arrange(RIGHT,buff=0.6)
        tg_r = Rectangle(width=tg.get_width()+0.3,height=tg.get_height()+0.3)
        tg.add(tg_r)
        tg.next_to(interface,UP)
        tg_l = Line(tg.get_corner(UL),tg.get_corner(DL))
        tg_l.next_to(t_tex,RIGHT,buff=abs(tg.get_left()-t_tex.get_left())[0])
        tg.add(tg_l)
        tg.shift(RIGHT*interface.get_width()/4)
        # -------------------
        formula = TexMobject(
            "y(x,t)=A\\ \\!{\\rm sin}(kx+\\omega t+\\phi)",
            tex_to_color_map={
                "A": A_COLOR, "k": K_COLOR, "\\omega": W_COLOR, "\\phi": PHI_COLOR,
                "x": X_COLOR, "t": T_COLOR
            },
        )
        formula.next_to(tg,UP)
        self.play(Write(interface))
        self.play(Write(labels),Write(graph))
        self.play(Write(tg),Write(formula))
        self.add(interface,graph,tg,formula,*labels)
        self.wait()
        # self.play(ChangeDecimalToValueText(t,1),run_time=2) 
        RUN_TIME = 4
        self.play(A.set_value,1.9,run_time=RUN_TIME)
        self.wait(4)
        self.play(s.set_value,0.5,run_time=RUN_TIME)
        self.wait(4)
        self.play(s.set_value,-1.5,run_time=RUN_TIME)
        self.wait(4)
        self.play(k.set_value,-0.4,run_time=RUN_TIME)
        self.wait(4)
        self.play(k.set_value,1.7,run_time=RUN_TIME)
        self.wait(4)
        self.play(Indicate(t_tex),FocusOn(t_tex.get_center()))
        self.wait(0.5)
        def update_t(mob,dt):
            graph.t_offset+= dt * 0.3
            mob.set_value(graph.t_offset)
        t.add_updater(update_t)
        self.add(t)
        self.wait(8)
        self.play(w.set_value,2,run_time=RUN_TIME)
        self.wait(7)
        self.play(w.set_value,-1.1,run_time=RUN_TIME)
        self.wait(7)
        self.play(
            A.set_value,-1.7,
            k.set_value,0.8,
            run_time=RUN_TIME,
        )
        self.wait(7)
        
        
    def get_range_line(self, 
                       start,
                       end,
                       vt,
                       tex="\\alpha",
                       color=WHITE,
                       tex_config={},
                       line_config={}
        ):
        line_config["numbers_with_elongated_ticks"] = []
        line = NumberLine(x_min=start,x_max=end,**line_config)
        tex_ = TexMobject(tex,**tex_config)
        tex_.next_to(line,LEFT)
        dot = Dot()
        dot.add_updater(lambda mob: mob.move_to(line.n2p(vt.get_value())))
        digital = DecimalTextNumber(0,num_decimal_places=3,include_sign=True)
        digital.add_updater(lambda mob: mob.set_value(vt.get_value()))
        digital.next_to(line,RIGHT)
        VGroup(line,tex_,digital).set_color(color)
        return VGroup(line,tex_,dot,digital)