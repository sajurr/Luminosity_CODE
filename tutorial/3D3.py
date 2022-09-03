from tokenize import group
from manim import*
from manim_physics import*
import numpy as np
import random


class ElectricFieldExampleScene(Scene):
    def construct(self):
        charge1 = Charge(5, LEFT + DOWN)
        charge2 = Charge(2, RIGHT + DOWN*2)
        charge3 = Charge(-0.1, UP)
        field = ElectricField(charge1, charge2, charge3)
        self.add(charge1, charge2, charge3)
        self.play(Create(field), run_time=3)
        self.wait()