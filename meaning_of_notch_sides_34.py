import manim

import polyhedron_image_2d
from imports import *

__all__ = ['MeaningOfNotchSides']


class MeaningOfNotchSides(manim.Scene):
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
        notched = VGroup(dashed_tetrahedron, tetrahedron).scale(2.5)
        vertex0 = dashed_tetrahedron[0][0].points[0]
        vertex1 = dashed_tetrahedron[0][0].points[4]
        vertex2 = dashed_tetrahedron[0][0].points[8]
        vertex3 = dashed_tetrahedron[0][1].points[8]
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
        notched.add(manim.Tex('$0$', fill_color=manim.ORANGE).scale(1.4).next_to(vertex0,
                                                                                 RIGHT + DOWN, buff=manim.SMALL_BUFF),
                    manim.Tex('$1$', fill_color=manim.RED).scale(1.4).next_to(vertex1,
                                                                              RIGHT + UP, buff=manim.SMALL_BUFF),
                    manim.Tex('$2$', fill_color=manim.BLUE).scale(1.4).next_to(vertex2,
                                                                               LEFT + DOWN, buff=manim.SMALL_BUFF),
                    manim.Tex('$3$', fill_color=manim.YELLOW).scale(1.4).next_to(vertex3,
                                                                                 LEFT + UP, buff=manim.SMALL_BUFF))
        self.add(notched)
        arrow0_3 = manim.Arrow(vertex0, notch0_3, stroke_width=manim.DEFAULT_STROKE_WIDTH * 2,
                               stroke_color=manim.YELLOW).set_z_index(10.0)
        arrow3_3 = manim.Arrow(vertex3, notch3_3, stroke_width=manim.DEFAULT_STROKE_WIDTH * 2,
                               stroke_color=manim.YELLOW).set_z_index(10.0)
        arrow1_3 = manim.Arrow(vertex1, notch1_3, stroke_width=manim.DEFAULT_STROKE_WIDTH * 2,
                               stroke_color=manim.YELLOW).set_z_index(-10.0)
        arrow2_3 = manim.Arrow(vertex2, notch2_3, stroke_width=manim.DEFAULT_STROKE_WIDTH * 2,
                               stroke_color=manim.YELLOW).set_z_index(-10.0)
        arrow0_1 = manim.Arrow(vertex0, notch0_1, stroke_width=manim.DEFAULT_STROKE_WIDTH * 2,
                               stroke_color=manim.RED, buff=0.0).set_z_index(10.0)
        arrow0_2 = manim.Arrow(vertex0, notch0_2, stroke_width=manim.DEFAULT_STROKE_WIDTH * 2,
                               stroke_color=manim.BLUE, buff=0.0).set_z_index(10.0)
        arrow1_1 = manim.Arrow(vertex1, notch1_1, stroke_width=manim.DEFAULT_STROKE_WIDTH * 2,
                               stroke_color=manim.RED, buff=0.0).set_z_index(10.0)
        arrow1_2 = manim.Arrow(vertex1, notch1_2, stroke_width=manim.DEFAULT_STROKE_WIDTH * 2,
                               stroke_color=manim.BLUE, buff=0.0).set_z_index(10.0)
        arrow2_1 = manim.Arrow(vertex2, notch2_1, stroke_width=manim.DEFAULT_STROKE_WIDTH * 2,
                               stroke_color=manim.RED, buff=0.0).set_z_index(10.0)
        arrow2_2 = manim.Arrow(vertex2, notch2_2, stroke_width=manim.DEFAULT_STROKE_WIDTH * 2,
                               stroke_color=manim.BLUE, buff=0.0).set_z_index(10.0)
        arrow3_1 = manim.Arrow(vertex3, notch3_1, stroke_width=manim.DEFAULT_STROKE_WIDTH * 2,
                               stroke_color=manim.RED, buff=0.0).set_z_index(10.0)
        arrow3_2 = manim.Arrow(vertex3, notch3_2, stroke_width=manim.DEFAULT_STROKE_WIDTH * 2,
                               stroke_color=manim.BLUE, buff=0.0).set_z_index(10.0)
        self.add(arrow0_3, arrow3_3, arrow1_3, arrow2_3, arrow0_1, arrow0_2,
                 arrow1_1, arrow1_2, arrow2_1, arrow2_2, arrow3_1, arrow3_2)


if __name__ == '__main__':
    scene = MeaningOfNotchSides()
    scene.render(True)
