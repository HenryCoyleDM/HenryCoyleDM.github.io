import polyhedron_image_2d
from imports import *

__all__ = ['ElementVertexRotation']


class ElementVertexRotation(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOUR
        tex1 = manim.Tex('$2$', fill_color=manim.BLUE).scale(2.0).move_to(LEFT * 6.0)
        vertex0 = LEFT * 1.0 + DOWN * 1.0 + IN * 1.0
        vertex1 = RIGHT * 1.0 + UP * 1.0 + IN * 1.0
        vertex2 = LEFT * 1.0 + UP * 1.0 + OUT * 1.0
        vertex3 = RIGHT * 1.0 + DOWN * 1.0 + OUT * 1.0
        tetra = manim.Polyhedron(vertex_coords=[vertex0, vertex1, vertex2, vertex3],
                                 faces_list=[[0, 1, 2],
                                             [0, 1, 3],
                                             [0, 2, 3],
                                             [1, 2, 3]],
                                 faces_config={'fill_color': manim.GREEN,
                                               'fill_opacity': 0.5,
                                               'stroke_opacity': 0.0},
                                 graph_config={'edge_config': {'stroke_opacity': 1.0, 'shade_in_3d': True},
                                               'vertex_config': {'fill_opacity': 0.0, 'stroke_opacity': 0.0}})
        tetrahedron = polyhedron_image_2d.get_polyhedron_image(tetra, 1.3, -1.8)
        tetrahedron.scale(1.5)
        t1 = tetrahedron.copy().move_to(LEFT * 2.0)
        t1.add(manim.Tex('$0$', fill_color=manim.ORANGE).next_to(t1[0][0].points[0],
                                                                 RIGHT + DOWN, buff=manim.SMALL_BUFF),
               manim.Tex('$1$', fill_color=manim.RED).next_to(t1[0][0].points[4],
                                                              RIGHT + UP, buff=manim.SMALL_BUFF),
               manim.Tex('$2$', fill_color=manim.BLUE).next_to(t1[0][0].points[8],
                                                               LEFT + DOWN, buff=manim.SMALL_BUFF),
               manim.Tex('$3$', fill_color=manim.YELLOW).next_to(t1[0][1].points[8],
                                                                 LEFT + UP, buff=manim.SMALL_BUFF))
        t2 = tetrahedron.copy().move_to(RIGHT * 3.5)
        t2.add(manim.Tex('$2$', '$\\cdot$', '$2$').next_to(t2[0][0].points[0], RIGHT + DOWN, buff=manim.SMALL_BUFF),
               manim.Tex('$2$', '$\\cdot$', '$3$').next_to(t2[0][0].points[4], RIGHT + UP, buff=manim.SMALL_BUFF),
               manim.Tex('$2$', '$\\cdot$', '$0$').next_to(t2[0][0].points[8], LEFT + DOWN, buff=manim.SMALL_BUFF),
               manim.Tex('$2$', '$\\cdot$', '$1$').next_to(t2[0][1].points[8], LEFT + UP, buff=manim.SMALL_BUFF))
        t2[2][0].fill_color = manim.BLUE
        t2[2][2].fill_color = manim.BLUE
        t2[3][0].fill_color = manim.BLUE
        t2[3][2].fill_color = manim.YELLOW
        t2[4][0].fill_color = manim.BLUE
        t2[4][2].fill_color = manim.ORANGE
        t2[5][0].fill_color = manim.BLUE
        t2[5][2].fill_color = manim.RED
        self.add(tex1, t1, t2,
                 manim.DoubleArrow(tex1.get_right(), t1.get_left() + RIGHT * 0.5, stroke_color=manim.GREEN,
                                   stroke_width=manim.DEFAULT_STROKE_WIDTH * 2),
                 manim.DoubleArrow(t1.get_right() + LEFT * 0.5, t2.get_left() + RIGHT * 1.0, stroke_color=manim.GREEN,
                                   stroke_width=manim.DEFAULT_STROKE_WIDTH * 2))
        arrow_0 = manim.CurvedArrow(t2[0][0].points[0], t2[0][0].points[8], angle=0.8,
                                    stroke_color=manim.ORANGE, tip_length=manim.DEFAULT_ARROW_TIP_LENGTH * 0.5)\
            .set_z_index(10.0)
        arrow_1 = manim.CurvedArrow(t2[0][0].points[4], t2[0][1].points[8], angle=0.9,
                                    stroke_color=manim.RED, tip_length=manim.DEFAULT_ARROW_TIP_LENGTH * 0.5)\
            .set_z_index(10.0)
        arrow_2 = manim.CurvedArrow(t2[0][0].points[8], t2[0][0].points[0], angle=1.1,
                                    stroke_color=manim.BLUE, tip_length=manim.DEFAULT_ARROW_TIP_LENGTH * 0.5)\
            .set_z_index(10.0)
        arrow_3 = manim.CurvedArrow(t2[0][1].points[8], t2[0][0].points[4], angle=1.2,
                                    stroke_color=manim.YELLOW, tip_length=manim.DEFAULT_ARROW_TIP_LENGTH * 0.5)\
            .set_z_index(10.0)
        box2 = manim.SurroundingRectangle(t1[4], stroke_color=manim.BLUE)
        text1 = manim.Text('Element', fill_color=manim.YELLOW).move_to(tex1, UP).shift(RIGHT * 0.5)
        text2 = manim.Text('Vertex', fill_color=manim.YELLOW).move_to(t1, UP)
        text3 = manim.Text('Transformation', fill_color=manim.YELLOW).move_to(t2, UP).shift(UP * 1.0)
        text1.move_to(text3, coor_mask=np.array([0, 1, 0]))
        text2.move_to(text3, coor_mask=np.array([0, 1, 0]))
        self.add(arrow_0, arrow_1, arrow_2, arrow_3, box2, text1, text2, text3)


if __name__ == '__main__':
    scene = ElementVertexRotation()
    scene.render(True)
