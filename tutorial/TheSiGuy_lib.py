from imports import *
from manim import*
class SmoothGraphFromSetPoints(VMobject):
    def __init__(self, set_of_points, **kwargs):
        super().__init__(**kwargs)
        self.set_points_smoothly(set_of_points)


def list_c2p(list,ax=Axes()):
    pts=[ax.coords_to_point(*pt) for pt in list ]
    return pts

def vmobj_from_list(list):
    vmobj=VMobject().set_points_as_corners(list)
    return vmobj

def xy_plane(axis,color=BLUE):
    ax=axis
    xy_plane = Polygram([[ax.x_axis.get_start()[0], ax.y_axis.get_start()[1], ax.get_origin()[2]],
                         [ax.x_axis.get_start()[0], ax.y_axis.get_end()[1], ax.get_origin()[2]],
                         [ax.x_axis.get_end()[0], ax.y_axis.get_end()[1], ax.get_origin()[2]],
                         [ax.x_axis.get_end()[0], ax.y_axis.get_start()[1], ax.get_origin()[2]]], stroke_width=0,
                        fill_color=color, fill_opacity=0.1)
    return xy_plane



def xz_plane(axis,color=BLUE):
    ax=axis
    xz_plane = Polygram([[ax.x_axis.get_start()[0], ax.get_origin()[1], ax.z_axis.get_start()[2]],
                         [ax.x_axis.get_start()[0], ax.get_origin()[1], ax.z_axis.get_end()[2]],
                         [ax.x_axis.get_end()[0], ax.get_origin()[1], ax.z_axis.get_end()[2]],
                         [ax.x_axis.get_end()[0], ax.get_origin()[1], ax.z_axis.get_start()[2]]], stroke_width=0,
                        fill_color=color, fill_opacity=0.1)
    return xz_plane


def yz_plane(axis,color=BLUE):
    ax=axis
    yz_plane = Polygram([[ax.get_origin()[0], ax.y_axis.get_end()[1], ax.z_axis.get_start()[2]],
                         [ax.get_origin()[0], ax.y_axis.get_end()[1], ax.z_axis.get_end()[2]],
                         [ax.get_origin()[0], ax.y_axis.get_start()[1], ax.z_axis.get_end()[2]],
                         [ax.get_origin()[0], ax.y_axis.get_start()[1], ax.z_axis.get_start()[2]]], stroke_width=0,
                        fill_color=color, fill_opacity=0.1)

    return yz_plane


def ThreeGraphsFromCsv(ax, ax1, ax2,csvFile,stroke_width=1):
    d3 = []
    d21 = []
    d22 = []
    d = []
    df = pd.read_csv(csvFile, names=['x', 'y', 'z'])
    for ind, row in df.iterrows():
        d3List = [row.x, row.y, row.z]
        d21List = [row.z, row.x]
        d22List = [row.z, row.y]

        d3.append(d3List)
        d21.append(d21List)
        d22.append(d22List)

    pts3d = [ax.coords_to_point(*pt) for pt in d3]
    ptsd21 = [ax1.coords_to_point(*pt) for pt in d21]
    ptsd22 = [ax2.coords_to_point(*pt) for pt in d22]

    graph = VMobject(color=YELLOW, stroke_width=stroke_width).set_points_as_corners(pts3d)
    g1 = VMobject(color=YELLOW, stroke_width=stroke_width).set_points_as_corners(ptsd21)
    g2 = VMobject(color=YELLOW, stroke_width=stroke_width).set_points_as_corners(ptsd22)

    dot = Dot3D(graph.get_start()).scale(0.6)
    dot1 = Dot(g1.get_start()).scale(0.6)
    dot2 = Dot(g2.get_start()).scale(0.6)

    return graph, g1, g2, dot, dot1, dot2


def area_graph_of_points(ax,x_min,x_max,mobject,opacity=0.3,color=[BLUE, GREEN]):
    points = (
            [ax.c2p(x_min,0,0)]
            + [p for p in mobject.points if x_min <= ax.p2c(p)[0] <= x_max]
            + [ax.c2p(x_max,0,0)]
    )
    return Polygon(*points,).set_opacity(opacity).set_color(color)


def create_dot_headed_path(path, tracker, color=YELLOW, stroke_width=2):
    created_path = always_redraw(lambda: VMobject(color=color, stroke_width=stroke_width).set_points_as_corners(
        path.get_points()[:int(tracker.get_value())]))
    animated_dot = always_redraw(lambda: Dot3D(created_path.get_end()))
    return created_path, animated_dot



# copy this to the source code of manim library to get the area under y_coordinate
#     def get_area_y(
#             self,
#             graph: "ParametricFunction",
#             x_range: Optional[Tuple[float, float]] = None,
#             color: Union[Color, Iterable[Color]] = [BLUE, GREEN],
#             opacity: float = 0.3,
#             bounded_graph: "ParametricFunction" = None,
#             **kwargs,
#     ):
#         """Returns a :class:`~.Polygon` representing the area under the graph passed.
#
#         Examples
#         --------
#
#         .. manim:: GetAreaExample
#             :save_last_frame:
#
#             class GetAreaExample(Scene):
#                 def construct(self):
#                     ax = Axes().add_coordinates()
#                     curve = ax.plot(lambda x: 2 * np.sin(x), color=DARK_BLUE)
#                     area = ax.get_area(
#                         curve,
#                         x_range=(PI / 2, 3 * PI / 2),
#                         color=(GREEN_B, GREEN_D),
#                         opacity=1,
#                     )
#
#                     self.add(ax, curve, area)
#
#         Parameters
#         ----------
#         graph
#             The graph/curve for which the area needs to be gotten.
#         x_range
#             The range of the minimum and maximum x-values of the area. ``x_range = [x_min, x_max]``.
#         color
#             The color of the area. Creates a gradient if a list of colors is provided.
#         opacity
#             The opacity of the area.
#         bounded_graph
#             If a secondary :attr:`graph` is specified, encloses the area between the two curves.
#         kwargs
#             Additional parameters passed to :class:`~.Polygon`
#
#         Returns
#         -------
#         :class:`~.Polygon`
#             The :class:`~.Polygon` representing the area.
#
#         Raises
#         ------
#         :exc:`ValueError`
#             When x_ranges do not match (either area x_range, graph's x_range or bounded_graph's x_range).
#         """
#         if x_range is None:
#             a = graph.t_min
#             b = graph.t_max
#         else:
#             a, b = x_range
#         if bounded_graph is not None:
#             if bounded_graph.t_min > b:
#                 raise ValueError(
#                     f"Ranges not matching: {bounded_graph.t_min} < {b}",
#                 )
#             if bounded_graph.t_max < a:
#                 raise ValueError(
#                     f"Ranges not matching: {bounded_graph.t_max} > {a}",
#                 )
#             a = max(a, bounded_graph.t_min)
#             b = min(b, bounded_graph.t_max)
#
#         if bounded_graph is None:
#             points = (
#                     [self.c2p(0,a,0)]
#                     + [p for p in graph.points if a <= self.p2c(p)[1] <= b]
#                     + [self.c2p(0,b,0)]
#             )
#         else:
#             graph_points, bounded_graph_points = (
#                 [g.function(a)]
#                 + [p for p in g.points if a <= self.p2c(p)[0] <= b]
#                 + [g.function(b)]
#                 for g in (graph, bounded_graph)
#             )
#             points = graph_points + bounded_graph_points[::-1]
#         return Polygon(*points, **kwargs).set_opacity(opacity).set_color(color)