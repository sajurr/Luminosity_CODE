from manim import*
from imports import*
import random

HOME1 = "C:\Z\YOUTUBE"

class RandomNumbers(Scene):
    def construct(self):
        
        numbers = VGroup()
        for x in range(28):
            num = DecimalNumber()
            numbers.add(num)

        def randomize_numbers(numbers):
            for num in numbers:
                value = random.uniform(0, 1)
                num.set_value(value)
                if value > 0.1:
                    num.set_color(GREEN)
                else:
                    num.set_color(RED)
        
        randomize_numbers

        numbers.set(width = 0.38)
        numbers.arrange(RIGHT, buff=0.1)
        numbers.to_edge(UR)


        def get_results(numbers):
            results = VGroup()
            for num in numbers:
                if num.get_value() > 0.1:
                    result = (
                        SVGMobject(f"{HOME1}\\Ryan-Taylor-Green-Tick.svg")
                        .set_color(GREEN_C)
                        .set(width=0.3)
                    )
                else:
                    result = (
                        SVGMobject(f"{HOME1}\\milker_X_icon.svg")
                        .set_color(RED)
                        .set(width=0.3)
                    )

                result.next_to(num, DOWN, buff=0.2)
                results.add(result)
            return results

        for k in range(10):
            self.play(UpdateFromFunc(numbers, randomize_numbers))
            self.wait()
            result = get_results(numbers)
            self.play(Write(result))
            self.wait()
            box = SurroundingRectangle(result)
            self.play(Create(box))
            self.play(FadeOut(box), FadeOut(result))

        self.wait()



class Move(Scene):
    def construct(self):
        sq = Square()
        sq.shift(UR)
        self.play(GrowFromEdge(sq, UL))
        self.wait(2)
