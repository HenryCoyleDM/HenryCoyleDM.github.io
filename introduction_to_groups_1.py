from imports import *

__all__ = ['IntroductionToGroups']


class IntroductionToGroups(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOUR
        rhombus = manim.Polygon(RIGHT * 2, UP * 3, LEFT * 2, DOWN * 3,
                                fill_color=manim.BLUE,
                                fill_opacity=0.5,
                                stroke_color=manim.WHITE,
                                stroke_opacity=1.0,
                                stroke_width=manim.DEFAULT_STROKE_WIDTH)
        rhombus.set_sheen(1.0, RIGHT * 1 + UP * 2)
        rhombus.scale(0.5)
        rhombus_s2 = rhombus.copy().rotate(PI)
        rhombus_s3 = rhombus.copy().flip()
        rhombus_s4 = rhombus.copy().flip(RIGHT)
        arrow_180 = manim.CurvedArrow(start_point=RIGHT * 0.4 + DOWN * 2.9,
                                      end_point=RIGHT * 0.4 + UP * 2.9,
                                      radius=np.linalg.norm(RIGHT * 0.4 + UP * 2.9))\
            .scale(0.5, about_point=ORIGIN)
        rhombus2 = VGroup(rhombus_s2, arrow_180)
        arrow_vertical = manim.CurvedDoubleArrow(start_point=LEFT * 1.8 + DOWN * 0.1,
                                                 end_point=RIGHT * 1.8 + DOWN * 0.1,
                                                 angle=0.5)\
            .scale(0.5, about_point=ORIGIN)
        rhombus3 = VGroup(rhombus_s3, arrow_vertical)
        arrow_horizontal = manim.CurvedDoubleArrow(start_point=LEFT * 0.1 + UP * 2.5,
                                                   end_point=LEFT * 0.1 + DOWN * 2.5,
                                                   angle=0.4)\
            .scale(0.5, about_point=ORIGIN)
        rhombus4 = VGroup(rhombus_s4, arrow_horizontal)
        self.add(rhombus.copy().shift(LEFT * 5.5 + UP * 1.5),
                 rhombus2.copy().shift(LEFT * 2.5 + UP * 1.5),
                 rhombus3.copy().shift(LEFT * 5.5 + DOWN * 2.0),
                 rhombus4.copy().shift(LEFT * 2.5 + DOWN * 2.0))
        line = manim.Line(RIGHT * 2.5 + UP * 1.5, LEFT * 1.5 + UP * 1.5)
        line.add_line_to(LEFT * 1.5 + DOWN * 2.5)
        rh1 = rhombus.copy().scale(0.3)
        rh2 = rhombus2.copy().scale(0.3, about_point=ORIGIN)
        rh3 = rhombus3.copy().scale(0.3)
        rh4 = rhombus4.copy().scale(0.3)
        for s in (rh1, rh2.submobjects[0], rh2.submobjects[1], rh3.submobjects[0], rh3.submobjects[1],
                  rh4.submobjects[0], rh4.submobjects[1]):
            s.stroke_width = manim.DEFAULT_STROKE_WIDTH * 0.6
        table = VGroup(line,
                       rh1.copy().shift(LEFT * 1.0 + UP * 2.0),
                       rh2.copy().shift(UP * 2.0),
                       rh3.copy().shift(RIGHT * 1.0 + UP * 2.0),
                       rh4.copy().shift(RIGHT * 2.0 + UP * 2.0),
                       rh1.copy().shift(LEFT * 2.0 + UP * 1.0),
                       rh2.copy().shift(LEFT * 2.0),
                       rh3.copy().shift(LEFT * 2.0 + DOWN * 1.0),
                       rh4.copy().shift(LEFT * 2.0 + DOWN * 2.0),
                       rh1.copy().shift(LEFT * 1.0 + UP * 1.0),
                       rh2.copy().shift(UP * 1.0),
                       rh3.copy().shift(RIGHT * 1.0 + UP * 1.0),
                       rh4.copy().shift(RIGHT * 2.0 + UP * 1.0),
                       rh2.copy().shift(LEFT * 1.0),
                       rh1.copy(),
                       rh4.copy().shift(RIGHT * 1.0),
                       rh3.copy().shift(RIGHT * 2.0),
                       rh3.copy().shift(LEFT * 1.0 + DOWN * 1.0),
                       rh4.copy().shift(DOWN * 1.0),
                       rh1.copy().shift(RIGHT * 1.0 + DOWN * 1.0),
                       rh2.copy().shift(RIGHT * 2.0 + DOWN * 1.0),
                       rh4.copy().shift(LEFT * 1.0 + DOWN * 2.0),
                       rh3.copy().shift(DOWN * 2.0),
                       rh2.copy().shift(RIGHT * 1.0 + DOWN * 2.0),
                       rh1.copy().shift(RIGHT * 2.0 + DOWN * 2.0))
        table.shift(RIGHT * 3.5 + DOWN * 0.5).scale(1.4)
        self.add(table)
        self.add(manim.Text('Symmetries', fill_color=manim.YELLOW).shift(LEFT * 4.0 + UP * 3.5),
                 manim.Text('Composition', fill_color=manim.YELLOW).shift(RIGHT * 3.5 + UP * 3.5))


if __name__ == '__main__':
    scene = IntroductionToGroups()
    scene.render(True)
