import manim

import polyhedron_image_2d
from imports import *

__all__ = ['CopyingDecoration']


class CopyingDecoration(manim.Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOUR
        vertex0 = LEFT * 1.0 + DOWN * 1.0 + IN * 1.0
        vertex1 = RIGHT * 1.0 + UP * 1.0 + IN * 1.0
        vertex2 = LEFT * 1.0 + UP * 1.0 + OUT * 1.0
        vertex3 = RIGHT * 1.0 + DOWN * 1.0 + OUT * 1.0
        notch0_1 = vertex1 * 0.1 + vertex0 * 0.9
        notch0_2 = vertex2 * 0.3 + vertex0 * 0.7
        notch0_3 = vertex3 * 0.5 + vertex0 * 0.5
        notch1_1 = vertex0 * 0.1 + vertex1 * 0.9
        notch1_2 = vertex3 * 0.3 + vertex1 * 0.7
        notch1_3 = vertex2 * 0.5 + vertex1 * 0.5
        notch2_1 = vertex3 * 0.1 + vertex2 * 0.9
        notch2_2 = vertex0 * 0.3 + vertex2 * 0.7
        notch2_3 = vertex1 * 0.5 + vertex2 * 0.5
        notch3_1 = vertex2 * 0.1 + vertex3 * 0.9
        notch3_2 = vertex1 * 0.3 + vertex3 * 0.7
        notch3_3 = vertex0 * 0.5 + vertex3 * 0.5
        d_tetra = manim.Polyhedron(vertex_coords=[vertex0, vertex1, vertex2, vertex3],
                                   faces_list=[[0, 1, 2],
                                               [0, 1, 3],
                                               [0, 2, 3],
                                               [1, 2, 3]],
                                   faces_config={'fill_opacity': 0.0,
                                                 'stroke_opacity': 0.0},
                                   graph_config={'edge_type': manim.DashedLine,
                                                 'edge_config': {'stroke_opacity': 1.0, 'shade_in_3d': True,
                                                                 'dash_length': 0.12 * math.sqrt(0.5),
                                                                 'dashed_ratio': 0.3},
                                                 'vertex_config': {'fill_opacity': 0.0, 'stroke_opacity': 0.0}})
        dashed_tetrahedron = polyhedron_image_2d.get_polyhedron_image(d_tetra, 1.3, -1.8)
        tetra = manim.Polyhedron(vertex_coords=[notch0_1, notch0_2, notch0_3,
                                                notch1_1, notch1_2, notch1_3,
                                                notch2_1, notch2_2, notch2_3,
                                                notch3_1, notch3_2, notch3_3],
                                 faces_list=[[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11],
                                             [0, 3, 5, 8, 7, 1],
                                             [1, 7, 6, 9, 11, 2],
                                             [2, 11, 10, 4, 3, 0],
                                             [5, 8, 6, 9, 10, 4]],
                                 faces_config={'fill_color': manim.GREEN,
                                               'fill_opacity': 0.5,
                                               'stroke_opacity': 0.0},
                                 graph_config={'edge_config': {'stroke_opacity': 1.0, 'shade_in_3d': True},
                                               'vertex_config': {'fill_opacity': 0.0, 'stroke_opacity': 0.0}})
        tetrahedron = polyhedron_image_2d.get_polyhedron_image(tetra, 1.3, -1.8)
        notched = VGroup(dashed_tetrahedron, tetrahedron).scale(2.0).shift(RIGHT * 2.5)
        vertex0 = dashed_tetrahedron[0][0].points[0]
        vertex1 = dashed_tetrahedron[0][0].points[4]
        vertex2 = dashed_tetrahedron[0][0].points[8]
        vertex3 = dashed_tetrahedron[0][1].points[8]
        notched.add(manim.Tex('$0$', fill_color=manim.ORANGE).scale(1.4).next_to(vertex0,
                                                                                 RIGHT + DOWN, buff=manim.SMALL_BUFF),
                    manim.Tex('$1$', fill_color=manim.RED).scale(1.4).next_to(vertex1,
                                                                              RIGHT + UP, buff=manim.SMALL_BUFF),
                    manim.Tex('$2$', fill_color=manim.BLUE).scale(1.4).next_to(vertex2,
                                                                               LEFT + DOWN, buff=manim.SMALL_BUFF),
                    manim.Tex('$3$', fill_color=manim.YELLOW).scale(1.4).next_to(vertex3,
                                                                                 LEFT + UP, buff=manim.SMALL_BUFF))
        self.add(notched)
        arrow_0_3 = manim.Arrow(vertex0, vertex3, stroke_color=manim.YELLOW,
                                stroke_width=manim.DEFAULT_STROKE_WIDTH * 1.5).set_z_index(10.0)
        arrow_2_3 = manim.Arrow(vertex2, vertex1, stroke_color=manim.YELLOW,
                                stroke_width=manim.DEFAULT_STROKE_WIDTH * 1.5).set_z_index(-10.0)
        arrow_0_2 = manim.CurvedArrow(vertex0, vertex2, stroke_color=manim.BLUE, angle=-1.4,
                                      stroke_width=manim.DEFAULT_STROKE_WIDTH * 1.5)
        arrow_3_2 = manim.CurvedArrow(vertex3, vertex1, stroke_color=manim.BLUE, angle=-1.3,
                                      stroke_width=manim.DEFAULT_STROKE_WIDTH * 1.5)
        label_0 = manim.MathTex('2\\cdot', fill_color=manim.BLUE).scale(1.3).next_to(arrow_0_2, DOWN, buff=0.1)
        label_3 = manim.MathTex('2\\cdot', fill_color=manim.BLUE).scale(1.3).next_to(arrow_3_2, UP, buff=0.1)
        self.add(arrow_0_3, arrow_2_3, arrow_0_2, arrow_3_2, label_0, label_3)
        line = manim.Line(RIGHT * 2.5 + UP * 1.5, LEFT * 1.5 + UP * 1.5)
        line.add_line_to(LEFT * 1.5 + DOWN * 2.5)
        tex0 = manim.Tex('$0$').scale(1.4)
        tex1 = manim.Tex('$1$').scale(1.4)
        tex2 = manim.Tex('$2$').scale(1.4)
        tex3 = manim.Tex('$3$').scale(1.4)
        table = VGroup(line,
                       tex0.copy().shift(LEFT * 1.0 + UP * 2.0),
                       tex1.copy().shift(UP * 2.0),
                       tex2.copy().shift(RIGHT * 1.0 + UP * 2.0),
                       tex3.copy().shift(RIGHT * 2.0 + UP * 2.0),
                       tex0.copy().shift(LEFT * 2.0 + UP * 1.0),
                       tex1.copy().shift(LEFT * 2.0),
                       tex2.copy().shift(LEFT * 2.0 + DOWN * 1.0),
                       tex3.copy().shift(LEFT * 2.0 + DOWN * 2.0),
                       tex0.copy().shift(LEFT * 1.0 + UP * 1.0),
                       tex1.copy().shift(UP * 1.0),
                       tex2.copy().shift(RIGHT * 1.0 + UP * 1.0),
                       tex3.copy().shift(RIGHT * 2.0 + UP * 1.0),
                       tex1.copy().shift(LEFT * 1.0),
                       tex0.copy(),
                       tex3.copy().shift(RIGHT * 1.0),
                       tex2.copy().shift(RIGHT * 2.0),
                       tex2.copy().shift(LEFT * 1.0 + DOWN * 1.0),
                       tex3.copy().shift(DOWN * 1.0),
                       tex0.copy().shift(RIGHT * 1.0 + DOWN * 1.0),
                       tex1.copy().shift(RIGHT * 2.0 + DOWN * 1.0),
                       tex3.copy().shift(LEFT * 1.0 + DOWN * 2.0),
                       tex2.copy().shift(DOWN * 2.0),
                       tex1.copy().shift(RIGHT * 1.0 + DOWN * 2.0),
                       tex0.copy().shift(RIGHT * 2.0 + DOWN * 2.0)).shift(LEFT * 3.5)
        self.add(table)


if __name__ == '__main__':
    scene = CopyingDecoration()
    scene.render(True)
