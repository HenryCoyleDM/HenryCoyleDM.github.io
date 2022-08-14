import manim

import polyhedron_image_2d
from imports import *

__all__ = ['CompositionOfDecorations']


class CompositionOfDecorations(manim.Scene):
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
        dashed_tetrahedron.add(manim.Tex('$0$', fill_color=manim.YELLOW).next_to(dashed_tetrahedron[0][0].points[0],
                                                                                 RIGHT + DOWN, buff=manim.SMALL_BUFF),
                               manim.Tex('$1$', fill_color=manim.YELLOW).next_to(dashed_tetrahedron[0][0].points[4],
                                                                                 RIGHT + UP, buff=manim.SMALL_BUFF),
                               manim.Tex('$2$', fill_color=manim.YELLOW).next_to(dashed_tetrahedron[0][0].points[8],
                                                                                 LEFT + DOWN, buff=manim.SMALL_BUFF),
                               manim.Tex('$3$', fill_color=manim.YELLOW).next_to(dashed_tetrahedron[0][1].points[8],
                                                                                 LEFT + UP, buff=manim.SMALL_BUFF))
        tetra0 = manim.Polyhedron(vertex_coords=[notch0_1, notch0_2, notch0_3,
                                                 vertex1, vertex2, vertex3],
                                  faces_list=[[0, 1, 2], [3, 4, 5],
                                              [0, 1, 4, 3],
                                              [1, 2, 5, 4],
                                              [0, 2, 5, 3]],
                                  faces_config={'fill_color': manim.GREEN,
                                                'fill_opacity': 0.5,
                                                'stroke_opacity': 0.0},
                                  graph_config={'edge_config': {'stroke_opacity': 1.0, 'shade_in_3d': True},
                                                'vertex_config': {'fill_opacity': 0.0, 'stroke_opacity': 0.0}})
        tetrahedron0 = VGroup(dashed_tetrahedron.copy(), polyhedron_image_2d.get_polyhedron_image(tetra0, 1.3, -1.8))
        tetra1 = manim.Polyhedron(vertex_coords=[notch1_1, notch1_2, notch1_3,
                                                 vertex0, vertex3, vertex2],
                                  faces_list=[[0, 1, 2], [3, 4, 5],
                                              [0, 1, 4, 3],
                                              [1, 2, 5, 4],
                                              [0, 2, 5, 3]],
                                  faces_config={'fill_color': manim.GREEN,
                                                'fill_opacity': 0.5,
                                                'stroke_opacity': 0.0},
                                  graph_config={'edge_config': {'stroke_opacity': 1.0, 'shade_in_3d': True},
                                                'vertex_config': {'fill_opacity': 0.0, 'stroke_opacity': 0.0}})
        tetrahedron1 = VGroup(dashed_tetrahedron.copy(), polyhedron_image_2d.get_polyhedron_image(tetra1, 1.3, -1.8))
        tetra3 = manim.Polyhedron(vertex_coords=[notch3_1, notch3_2, notch3_3,
                                                 vertex2, vertex1, vertex0],
                                  faces_list=[[0, 1, 2], [3, 4, 5],
                                              [0, 1, 4, 3],
                                              [1, 2, 5, 4],
                                              [0, 2, 5, 3]],
                                  faces_config={'fill_color': manim.GREEN,
                                                'fill_opacity': 0.5,
                                                'stroke_opacity': 0.0},
                                  graph_config={'edge_config': {'stroke_opacity': 1.0, 'shade_in_3d': True},
                                                'vertex_config': {'fill_opacity': 0.0, 'stroke_opacity': 0.0}})
        tetrahedron3 = VGroup(dashed_tetrahedron.copy(), polyhedron_image_2d.get_polyhedron_image(tetra3, 1.3, -1.8))
        tetrahedron0[0][2].set_fill(manim.BLUE)
        tetrahedron1[0][3].set_fill(manim.BLUE)
        tetrahedron3[0][5].set_fill(manim.BLUE)
        self.add(tetrahedron0.shift(LEFT * 4.5 + DOWN * 1.5).scale(1.4),
                 tetrahedron1.shift(RIGHT * 4.0 + DOWN * 1.5).scale(1.4),
                 tetrahedron3.shift(UP * 1.5 + LEFT * 0.5).scale(1.4))
        arrow_0_3 = manim.CurvedArrow(tetrahedron0.get_top() + DOWN * 0.5,
                                      tetrahedron3.get_left() + RIGHT * 0.5 + UP * 0.5,
                                      angle=-1.3)
        arrow_3_1 = manim.CurvedArrow(tetrahedron3.get_right() + LEFT * 0.5 + UP * 0.5,
                                      tetrahedron1.get_top() + DOWN * 0.5,
                                      angle=-2.0)
        arrow_0_1 = manim.CurvedArrow(tetrahedron0.get_right() + DOWN * 0.5,
                                      tetrahedron1.get_left() + DOWN * 0.5,
                                      angle=0.7)
        self.add(arrow_0_3, arrow_3_1, arrow_0_1,
                 manim.Tex('$3\\cdot$').scale(1.4)
                 .next_to(arrow_0_3, LEFT + UP, buff=-0.7),
                 manim.Tex('$2\\cdot$').scale(1.4)
                 .next_to(arrow_3_1, RIGHT + UP, buff=-0.5),
                 manim.Tex('$1\\cdot$').scale(1.4)
                 .next_to(arrow_0_1, UP, buff=-0.3),
                 manim.Tex('$3\\cdot2\\cdot$').scale(1.4)
                 .next_to(arrow_0_1, DOWN, buff=0.2))


if __name__ == '__main__':
    scene = CompositionOfDecorations()
    scene.render(True)
