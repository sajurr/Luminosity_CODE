from pickle import TRUE
from turtle import width
from manim import*
class MATRIX(VectorScene):
    def construct(self):
        self.add_axes(animate=True)
        self.add_plane(animate=True)

        BasisVec = self.get_basis_vectors()
        self.add(BasisVec)

        self.wait(2)

        vec = Vector([3,2])
        vec.set_color(RED)
        self.add_vector(vec)
        self.wait(2)


class LinearTransform(LinearTransformationScene):
    def construct(self):
        plane = self.add_plane(animate=True).add_coordinates()
        vec = self.add_vector([-1,-1], color=YELLOW)

        basis = self.get_basis_vectors()
        self.add(basis)
        self.vector_to_coords(vector = vec)

        vec2 = self.add_vector([2,2])
        self.write_vector_coordinates(vector = vec2)
        self.wait(2)


class matrixLinear(LinearTransformationScene):
    def __init__(self):
            LinearTransformationScene.__init__(
                self,
                show_coordinates=True,
                leave_ghost_vectors=True,
                show_basis_vectors=True
            )
    
    def construct(self):
        matrix = [[1,2], [2,1]]

        matrix_tex = MathTex(
            "A=\\begin{bmatrix} 1&2 \\\ 2&1 \\end{bmatrix}"
        ).to_edge(UL).add_background_rectangle()

        unit_square = self.get_unit_square()
        text = always_redraw(lambda : Text("Det(A)").set(width=0.7).move_to(unit_square.get_center()))

        vect = self.get_vector([1,-2], color=PURPLE)

        rect1 = Rectangle(height=2, width=1, color=BLUE_D).shift(UP*2+LEFT*2)

        circ1 = Circle(radius=1, color=RED).shift(DOWN+LEFT)
        
        self.add_transformable_mobject(vect, unit_square, rect1, circ1)
        self.add_background_mobject(matrix_tex, text)
        self.apply_matrix(matrix)
        self.wait(2)
        