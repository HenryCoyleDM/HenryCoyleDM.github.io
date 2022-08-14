from imports import *

__all__ = ['BreakingSomeSymmetries']


class BreakingSomeSymmetries(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOUR
        rhombus1 = manim.Polygon(RIGHT * 2, UP * 3, LEFT * 2, DOWN * 3,
                                 fill_color=manim.BLUE,
                                 fill_opacity=0.5,
                                 stroke_color=manim.WHITE,
                                 stroke_opacity=1.0,
                                 stroke_width=manim.DEFAULT_STROKE_WIDTH)
        rhombus1.set_sheen(1.0, RIGHT * 1 + UP * 2).scale(0.5)
        rhombus_less_symmetric = rhombus1.copy()
        rhombus_less_symmetric.shift(LEFT * 5.0)
        square = manim.Square(math.sqrt(2) * np.linalg.norm(rhombus_less_symmetric.get_center()
                                                            - rhombus_less_symmetric.points[4]),
                              stroke_opacity=0.5)
        square.move_to(rhombus_less_symmetric).rotate(TAU / 8)
        dashed_square = manim.DashedVMobject(square, num_dashes=16, dash_offset=0.75)
        squish_arrow_1 = manim.Arrow(square.points[12], rhombus_less_symmetric.points[0], buff=manim.SMALL_BUFF)
        squish_arrow_2 = manim.Arrow(square.points[4], rhombus_less_symmetric.points[8], buff=manim.SMALL_BUFF)
        self.add(rhombus_less_symmetric, dashed_square, squish_arrow_1, squish_arrow_2)
        rhombus_s2 = rhombus1.copy().rotate(PI / 2)
        arrow_90 = manim.CurvedArrow(start_point=RIGHT * 0.4 + DOWN * 2.9,
                                     end_point=RIGHT * 2.9 + DOWN * 0.4,
                                     radius=np.linalg.norm(RIGHT * 0.4 + DOWN * 2.9)) \
            .scale(0.5, about_point=ORIGIN)
        rhombus2 = VGroup(rhombus_s2, arrow_90)
        rhombus_s3 = rhombus1.copy().rotate(PI)
        arrow_180 = manim.CurvedArrow(start_point=RIGHT * 0.4 + DOWN * 2.9,
                                      end_point=RIGHT * 0.4 + UP * 2.9,
                                      radius=np.linalg.norm(RIGHT * 0.4 + DOWN * 2.9)) \
            .scale(0.5, about_point=ORIGIN)
        rhombus3 = VGroup(rhombus_s3, arrow_180)
        rhombus_s4 = rhombus1.copy().rotate(3 * PI / 2)
        arrow_270_minor = manim.CurvedArrow(start_point=RIGHT * 0.4 + DOWN * 2.9,
                                            end_point=LEFT * 2.9 + UP * 0.4,
                                            radius=np.linalg.norm(RIGHT * 0.4 + DOWN * 2.9))
        arrow_270 = manim.CurvedArrow(start_point=RIGHT * 0.4 + DOWN * 2.9,
                                      end_point=LEFT * 2.9 + UP * 0.4,
                                      angle=TAU - arrow_270_minor.angle).scale(0.5, about_point=ORIGIN)
        rhombus4 = VGroup(rhombus_s4, arrow_270)
        rhombus_s5 = rhombus1.copy().flip()
        arrow_vertical = manim.CurvedDoubleArrow(start_point=LEFT * 1.8 + DOWN * 0.1,
                                                 end_point=RIGHT * 1.8 + DOWN * 0.1,
                                                 angle=0.5) \
            .scale(0.5, about_point=ORIGIN)
        rhombus5 = VGroup(rhombus_s5, arrow_vertical)
        rhombus_s6 = rhombus1.copy().flip(RIGHT + DOWN)
        arrow_right_up = manim.CurvedDoubleArrow(start_point=LEFT * 1.1 + DOWN * 1.1,
                                                 end_point=RIGHT * 1.1 + UP * 1.1,
                                                 angle=0.4) \
            .scale(0.5, about_point=ORIGIN)
        rhombus6 = VGroup(rhombus_s6, arrow_right_up)
        rhombus_s7 = rhombus1.copy().flip(RIGHT)
        arrow_horizontal = manim.CurvedDoubleArrow(start_point=LEFT * 0.1 + UP * 2.5,
                                                   end_point=LEFT * 0.1 + DOWN * 2.5,
                                                   angle=0.4) \
            .scale(0.5, about_point=ORIGIN)
        rhombus7 = VGroup(rhombus_s7, arrow_horizontal)
        rhombus_s8 = rhombus1.copy().flip(RIGHT + DOWN)
        arrow_right_down = manim.CurvedDoubleArrow(start_point=LEFT * 1.1 + UP * 1.1,
                                                   end_point=RIGHT * 1.1 + DOWN * 1.1,
                                                   angle=0.4) \
            .scale(0.5, about_point=ORIGIN)
        rhombus8 = VGroup(rhombus_s8, arrow_right_down)
        self.add(rhombus1.scale(0.7, about_point=ORIGIN).shift(UP * 1.5 + LEFT * 2.5),
                 rhombus2.scale(0.7, about_point=ORIGIN).shift(UP * 1.5),
                 rhombus3.scale(0.7, about_point=ORIGIN).shift(UP * 1.5 + RIGHT * 2.5),
                 rhombus4.scale(0.7, about_point=ORIGIN).shift(UP * 1.5 + RIGHT * 5.0),
                 rhombus5.scale(0.7, about_point=ORIGIN).shift(DOWN * 1.5 + LEFT * 2.5),
                 rhombus6.scale(0.7, about_point=ORIGIN).shift(DOWN * 1.5),
                 rhombus7.scale(0.7, about_point=ORIGIN).shift(DOWN * 1.5 + RIGHT * 2.5),
                 rhombus8.scale(0.7, about_point=ORIGIN).shift(DOWN * 1.5 + RIGHT * 5.0))
        dashed_rhombus = manim.DashedVMobject(rhombus1.copy().set_fill(opacity=0.0).set_stroke(opacity=0.5),
                                              num_dashes=16,
                                              dash_offset=0.75)
        self.add(dashed_rhombus.copy().shift(RIGHT * 2.5),
                 dashed_rhombus.copy().shift(RIGHT * 7.5),
                 dashed_rhombus.copy().shift(DOWN * 3.0 + RIGHT * 2.5),
                 dashed_rhombus.copy().shift(DOWN * 3.0 + RIGHT * 7.5))
        cross = manim.Union(manim.Rectangle(height=0.5, width=2.0).rotate(TAU / 8),
                            manim.Rectangle(height=2.0, width=0.5).rotate(TAU / 8)).set_stroke(opacity=0.0)\
            .set_fill(color=manim.PURE_RED, opacity=0.3)
        self.add(cross.copy().move_to(rhombus2),
                 cross.copy().move_to(rhombus4),
                 cross.copy().move_to(rhombus6),
                 cross.copy().move_to(rhombus8))


if __name__ == '__main__':
    scene = BreakingSomeSymmetries()
    scene.render(True)
