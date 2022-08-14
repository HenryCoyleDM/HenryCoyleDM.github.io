from imports import *

__all__ = ['GroupHomomorphism']


class GroupHomomorphism(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOUR
        line = manim.Line(RIGHT * 2.5 + UP * 1.5, LEFT * 1.5 + UP * 1.5)
        line.add_line_to(LEFT * 1.5 + DOWN * 2.5)
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
                                      radius=np.linalg.norm(RIGHT * 0.4 + UP * 2.9)) \
            .scale(0.5, about_point=ORIGIN)
        rhombus2 = VGroup(rhombus_s2, arrow_180)
        arrow_vertical = manim.CurvedDoubleArrow(start_point=LEFT * 1.8 + DOWN * 0.1,
                                                 end_point=RIGHT * 1.8 + DOWN * 0.1,
                                                 angle=0.5) \
            .scale(0.5, about_point=ORIGIN)
        rhombus3 = VGroup(rhombus_s3, arrow_vertical)
        arrow_horizontal = manim.CurvedDoubleArrow(start_point=LEFT * 0.1 + UP * 2.5,
                                                   end_point=LEFT * 0.1 + DOWN * 2.5,
                                                   angle=0.4) \
            .scale(0.5, about_point=ORIGIN)
        rhombus4 = VGroup(rhombus_s4, arrow_horizontal)
        rh1 = rhombus.copy().scale(0.3)
        rh2 = rhombus2.copy().scale(0.3, about_point=ORIGIN)
        rh3 = rhombus3.copy().scale(0.3)
        rh4 = rhombus4.copy().scale(0.3)
        for s in (rh1, rh2.submobjects[0], rh2.submobjects[1], rh3.submobjects[0], rh3.submobjects[1],
                  rh4.submobjects[0], rh4.submobjects[1]):
            s.stroke_width = manim.DEFAULT_STROKE_WIDTH * 0.4
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
                       tex0.copy().shift(RIGHT * 2.0 + DOWN * 2.0))
        table2 = VGroup(line.copy(),
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
        table.scale(0.7).shift(LEFT * 5.0 + UP * 2.0)
        table2.scale(0.7).shift(LEFT * 5.0 + DOWN * 2.0)
        mapping = VGroup(tex0.copy().shift(LEFT * 1.0 + UP * 1.5),
                         tex1.copy().shift(LEFT * 1.0 + UP * 0.5),
                         tex2.copy().shift(LEFT * 1.0 + DOWN * 0.5),
                         tex3.copy().shift(LEFT * 1.0 + DOWN * 1.5),
                         rh1.copy().shift(RIGHT * 1.0 + UP * 1.5),
                         rh2.copy().shift(RIGHT * 1.0 + UP * 0.5),
                         rh3.copy().shift(RIGHT * 1.0 + DOWN * 0.5),
                         rh4.copy().shift(RIGHT * 1.0 + DOWN * 1.5))
        for i in range(4):
            mapping.add(manim.DoubleArrow(mapping[i].get_right(), mapping[4 + i].get_left(),
                                          stroke_color=manim.GREEN_A,
                                          tip_length=manim.DEFAULT_ARROW_TIP_LENGTH * 0.5))
        mapping.shift(LEFT * 1.0)
        equation = manim.MathTex('{{1}}\\cdot{{2}}={{3}}').shift(RIGHT * 4.0 + UP * 1.0).scale(2.4)
        equation2 = equation.copy().shift(DOWN * 2.0)
        equation2.submobjects[0] = rh2.copy().move_to(equation.submobjects[0]).shift(DOWN * 2.0)
        equation2.submobjects[1] = manim.MathTex('+').move_to(equation.submobjects[1]).shift(DOWN * 2.0)
        equation2.submobjects[2] = rh3.copy().move_to(equation.submobjects[2]).shift(DOWN * 2.0)
        equation2.submobjects[4] = rh4.copy().move_to(equation.submobjects[4]).shift(DOWN * 2.0)
        equations = VGroup(equation, equation2,
                           manim.DoubleArrow(equation.submobjects[0].get_bottom(), equation2.submobjects[0].get_top(),
                                             stroke_color=manim.GREEN_A,
                                             tip_length=manim.DEFAULT_ARROW_TIP_LENGTH * 0.5),
                           manim.DoubleArrow(equation.submobjects[2].get_bottom(), equation2.submobjects[2].get_top(),
                                             stroke_color=manim.GREEN_A,
                                             tip_length=manim.DEFAULT_ARROW_TIP_LENGTH * 0.5),
                           manim.DoubleArrow(equation.submobjects[4].get_bottom(), equation2.submobjects[4].get_top(),
                                             stroke_color=manim.GREEN_A,
                                             tip_length=manim.DEFAULT_ARROW_TIP_LENGTH * 0.5))
        self.add(table, table2, mapping, equations,
                 manim.Text('Abstract Group', fill_color=manim.YELLOW)
                 .scale(0.4).next_to(table, UP, buff=0.1),
                 manim.Text('Representation by Symmetries', fill_color=manim.YELLOW)
                 .scale(0.4).next_to(table2, UP, buff=0.1))


if __name__ == '__main__':
    scene = GroupHomomorphism()
    scene.render(True)
