import manim

import polyhedron_image_2d
from imports import *

__all__ = ['IdentityDecoration']


class IdentityDecoration(manim.Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOUR
        vertex0 = LEFT * 1.0 + DOWN * 1.0 + IN * 1.0
        vertex1 = RIGHT * 1.0 + UP * 1.0 + IN * 1.0
        vertex2 = LEFT * 1.0 + UP * 1.0 + OUT * 1.0
        vertex3 = RIGHT * 1.0 + DOWN * 1.0 + OUT * 1.0
        notch1_1 = vertex1 * 0.4 + vertex0 * 0.6
        notch2_1 = vertex2 * 0.6 + vertex0 * 0.4
        notch3_1 = vertex3 * 0.8 + vertex0 * 0.2
        d_notch1 = manim.Polyhedron(vertex_coords=[vertex0, notch1_1, notch2_1, notch3_1],
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
        dashed_notch1 = polyhedron_image_2d.get_polyhedron_image(d_notch1, 1.3, -1.8)
        tetra1 = manim.Polyhedron(vertex_coords=[vertex1, vertex2, vertex3, notch1_1, notch2_1, notch3_1],
                                  faces_list=[[0, 1, 2],
                                              [0, 1, 4, 3],
                                              [0, 2, 5, 3],
                                              [1, 2, 5, 4],
                                              [3, 4, 5]],
                                  faces_config={'fill_color': manim.GREEN,
                                                'fill_opacity': 0.5,
                                                'stroke_opacity': 0.0},
                                  graph_config={'edge_config': {'stroke_opacity': 1.0, 'shade_in_3d': True},
                                                'vertex_config': {'fill_opacity': 0.0, 'stroke_opacity': 0.0}})
        tetrahedron1 = polyhedron_image_2d.get_polyhedron_image(tetra1, 1.3, -1.8)
        vertex0_1 = dashed_notch1[0][0].points[0]
        notch1_3 = notch1_1
        notch2_3 = notch2_1
        notch3_3 = notch3_1
        notch1_1 = dashed_notch1[0][0].points[4]
        notch2_1 = dashed_notch1[0][0].points[8]
        notch3_1 = dashed_notch1[0][1].points[8]
        rotation1 = VGroup(dashed_notch1.copy(), tetrahedron1,
                           manim.BraceLabel(manim.Line(vertex0_1, notch1_1), '1',
                                            (vertex0_1 - notch1_1)[1] * LEFT
                                            + (vertex0_1 - notch1_1)[0] * UP,
                                            buff=0.1).set_z_index(10.0),
                           manim.BraceLabel(manim.Line(vertex0_1, notch2_1), '2',
                                            (notch2_1 - vertex0_1)[1] * LEFT
                                            + (notch2_1 - vertex0_1)[0] * UP,
                                            buff=0.1).set_z_index(10.0),
                           manim.BraceLabel(manim.Line(vertex0_1, notch3_1), '3',
                                            (vertex0_1 - notch3_1)[1] * RIGHT
                                            + (vertex0_1 - notch3_1)[0] * DOWN,
                                            buff=0.1).set_z_index(10.0))
        rotation1[2].fill_color = manim.BLUE_A
        rotation1[2][1].shift(LEFT * 0.2)
        rotation1[3].fill_color = manim.BLUE_A
        rotation1[3][1].shift(UP * 0.2)
        rotation1[4].fill_color = manim.BLUE_A
        rotation1[4][1].shift(RIGHT * 0.2 + UP * 0.2)
        self.add(rotation1.scale(2.3, about_point=ORIGIN).shift(LEFT * 3.4))
        notch1_2 = vertex1 * 0.6 + vertex0 * 0.4
        notch2_2 = vertex2 * 0.8 + vertex0 * 0.2
        notch3_2 = vertex3 * 0.4 + vertex0 * 0.6
        d_notch2 = manim.Polyhedron(vertex_coords=[vertex0, notch1_2, notch2_2, notch3_2],
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
        dashed_notch2 = polyhedron_image_2d.get_polyhedron_image(d_notch2, 1.3, -1.8)
        tetra2 = manim.Polyhedron(vertex_coords=[vertex1, vertex2, vertex3, notch1_2, notch2_2, notch3_2],
                                  faces_list=[[0, 1, 2],
                                              [0, 1, 4, 3],
                                              [0, 2, 5, 3],
                                              [1, 2, 5, 4],
                                              [3, 4, 5]],
                                  faces_config={'fill_color': manim.GREEN,
                                                'fill_opacity': 0.5,
                                                'stroke_opacity': 0.0},
                                  graph_config={'edge_config': {'stroke_opacity': 1.0, 'shade_in_3d': True},
                                                'vertex_config': {'fill_opacity': 0.0, 'stroke_opacity': 0.0}})
        tetrahedron2 = polyhedron_image_2d.get_polyhedron_image(tetra2, 1.3, -1.8)
        tetra2_2 = manim.Polyhedron(vertex_coords=[vertex1, vertex2, vertex3, notch1_3, notch2_3, notch3_3],
                                    faces_list=[[0, 1, 2],
                                                [0, 1, 4, 3],
                                                [0, 2, 5, 3],
                                                [1, 2, 5, 4],
                                                [3, 4, 5]],
                                    faces_config={'fill_opacity': 0.0,
                                                  'stroke_opacity': 0.0},
                                    graph_config={'edge_config': {'stroke_opacity': 0.5, 'shade_in_3d': True,
                                                                  'stroke_color': manim.YELLOW},
                                                  'vertex_config': {'fill_opacity': 0.0, 'stroke_opacity': 0.0}})
        tetrahedron2_2 = polyhedron_image_2d.get_polyhedron_image(tetra2_2, 1.3, -1.8)
        tetrahedron2_2.set_z_index(-10.0)
        arrow = manim.Arc(radius=1.0, start_angle=3 * TAU / 4, angle=TAU / 3, stroke_color=manim.PURE_BLUE)
        arrow.rotate_about_origin(math.atan(math.sqrt(0.5)), axis=RIGHT + DOWN)
        arrow.shift(vertex0 * 0.4)
        arrow.add_tip()
        arrow_2d = polyhedron_image_2d.get_polyhedron_image(arrow, 1.3, -1.8)
        arrow_2d.set_z_index(10.0)
        rotation2 = VGroup(dashed_notch2.copy(), tetrahedron2, tetrahedron2_2, arrow_2d)
        self.add(rotation2.scale(2.3, about_point=ORIGIN).shift(RIGHT * 3.4))
        cross = manim.Union(manim.Rectangle(height=0.5, width=2.0).rotate(TAU / 8),
                            manim.Rectangle(height=2.0, width=0.5).rotate(TAU / 8)).set_stroke(opacity=0.0) \
            .set_fill(color=manim.PURE_RED, opacity=0.7)
        self.add(cross.move_to(rotation2).shift(UP * 2.8))


if __name__ == '__main__':
    scene = IdentityDecoration()
    scene.render(True)
