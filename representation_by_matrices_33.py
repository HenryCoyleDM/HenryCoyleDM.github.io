import manim

import polyhedron_image_2d
from imports import *

__all__ = ['RepresentationByMatrices']


class RepresentationByMatrices(manim.Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOUR
        arrow0 = manim.Dot(color=manim.ORANGE).shift(LEFT * 6.5 + UP * 2.0)
        arrow1 = VGroup(manim.CurvedArrow(DOWN, UP, angle=PI, stroke_color=manim.RED),
                        manim.Dot(color=manim.RED)).shift(LEFT * 6.5 + DOWN * 2.0)
        arrow2 = VGroup(manim.CurvedArrow(DOWN, UP, angle=PI, stroke_color=manim.BLUE),
                        manim.Dot(color=manim.BLUE)).shift(RIGHT * 0.3 + UP * 2.0)
        arrow3 = VGroup(manim.CurvedArrow(DOWN, UP, angle=PI, stroke_color=manim.YELLOW),
                        manim.Dot(color=manim.YELLOW)).shift(RIGHT * 0.3 + DOWN * 2.0)
        matrix0 = manim.Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]]).shift(LEFT * 2.2).move_to(arrow0, coor_mask=UP)
        matrix1 = manim.Matrix([[1, 0, 0], [0, -1, 0], [0, 0, -1]]).shift(LEFT * 2.2).move_to(arrow1, coor_mask=UP)
        matrix2 = manim.Matrix([[-1, 0, 0], [0, -1, 0], [0, 0, 1]]).shift(RIGHT * 4.5).move_to(arrow2, coor_mask=UP)
        matrix3 = manim.Matrix([[-1, 0, 0], [0, 1, 0], [0, 0, -1]]).shift(RIGHT * 4.5).move_to(arrow3, coor_mask=UP)
        self.add(arrow0, arrow1, arrow2, arrow3,
                 matrix0, matrix1, matrix2, matrix3,
                 manim.DoubleArrow(arrow0.get_right(), matrix0.get_left(), buff=0.1,
                                   stroke_color=manim.GREEN, stroke_width=manim.DEFAULT_STROKE_WIDTH * 2),
                 manim.DoubleArrow(arrow1.get_right(), matrix1.get_left(), buff=0.1,
                                   stroke_color=manim.GREEN, stroke_width=manim.DEFAULT_STROKE_WIDTH * 2),
                 manim.DoubleArrow(arrow2.get_right(), matrix2.get_left(), buff=0.1,
                                   stroke_color=manim.GREEN, stroke_width=manim.DEFAULT_STROKE_WIDTH * 2),
                 manim.DoubleArrow(arrow3.get_right(), matrix3.get_left(), buff=0.1,
                                   stroke_color=manim.GREEN, stroke_width=manim.DEFAULT_STROKE_WIDTH * 2))


if __name__ == '__main__':
    scene = RepresentationByMatrices()
    scene.render(True)
