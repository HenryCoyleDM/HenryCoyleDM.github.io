from imports import *

__all__ = ['GeneralGroupDefinition']


class GeneralGroupDefinition(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOUR
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
                       tex0.copy().shift(RIGHT * 2.0 + DOWN * 2.0))
        table.scale(0.6)
        table_cl = table.copy().shift(LEFT * 5.0 + UP * 1.8)
        closure_brace = manim.BraceText(VGroup(table_cl.submobjects[12], table_cl.submobjects[24]),
                                        '$0$, $1$, $2$,\\\\or $3$',
                                        brace_direction=RIGHT,
                                        fill_color=manim.BLUE_B)
        closure_brace.label.fill_color = closure_brace.fill_color
        closure = manim.Text('Closure', fill_color=manim.YELLOW).scale(0.8).next_to(table_cl, UP)
        table_closure = VGroup(table_cl, closure_brace, closure)
        self.add(table_closure)
        table_id = table.copy().shift(LEFT * 5.0 + DOWN * 2.2)
        identity_box = manim.SurroundingRectangle(VGroup(table_id.submobjects[1], table_id.submobjects[12]),
                                                  color=manim.RED_B)
        identity = manim.Text('Identity', fill_color=manim.YELLOW).scale(0.8).next_to(table_id, UP)
        table_identity = VGroup(table_id, identity_box, identity)
        self.add(table_identity)
        table_in = table.copy().shift(RIGHT * 2.0 + UP * 1.8)
        for i in range(9, 25):
            if not table_in.submobjects[i].tex_string == '$0$':
                table_in.submobjects[i].fill_color = manim.DARK_GRAY
        inverse_crosses = VGroup(manim.Line(table_in.submobjects[9].get_right() + RIGHT * 0.1,
                                            table_in.submobjects[12].get_right() + RIGHT * 0.1),
                                 manim.Line(table_in.submobjects[9].get_bottom() + DOWN * 0.1,
                                            table_in.submobjects[21].get_bottom() + DOWN * 0.1),
                                 manim.Line(table_in.submobjects[14].get_right() + RIGHT * 0.1,
                                            table_in.submobjects[16].get_right() + RIGHT * 0.1),
                                 manim.Line(table_in.submobjects[14].get_bottom() + DOWN * 0.1,
                                            table_in.submobjects[22].get_bottom() + DOWN * 0.1),
                                 manim.Line(table_in.submobjects[14].get_left() + LEFT * 0.1,
                                            table_in.submobjects[13].get_left() + LEFT * 0.1),
                                 manim.Line(table_in.submobjects[14].get_top() + UP * 0.1,
                                            table_in.submobjects[10].get_top() + UP * 0.1),
                                 manim.Line(table_in.submobjects[19].get_right() + RIGHT * 0.1,
                                            table_in.submobjects[20].get_right() + RIGHT * 0.1),
                                 manim.Line(table_in.submobjects[19].get_bottom() + DOWN * 0.1,
                                            table_in.submobjects[23].get_bottom() + DOWN * 0.1),
                                 manim.Line(table_in.submobjects[19].get_left() + LEFT * 0.1,
                                            table_in.submobjects[17].get_left() + LEFT * 0.1),
                                 manim.Line(table_in.submobjects[19].get_top() + UP * 0.1,
                                            table_in.submobjects[11].get_top() + UP * 0.1),
                                 manim.Line(table_in.submobjects[24].get_left() + LEFT * 0.1,
                                            table_in.submobjects[21].get_left() + LEFT * 0.1),
                                 manim.Line(table_in.submobjects[24].get_top() + UP * 0.1,
                                            table_in.submobjects[12].get_top() + UP * 0.1))
        for sub in inverse_crosses.submobjects:
            sub.set_stroke(opacity=0.7)
        inverse = manim.Text('Inverse', fill_color=manim.YELLOW).scale(0.8).next_to(table_in, UP)
        inverse_explainer = manim.Text('(Each row and\ncolumn has\none identity)', fill_color=manim.LIGHT_GRAY)\
            .scale(0.4).next_to(table_in, RIGHT)
        table_inverse = VGroup(table_in, inverse_crosses, inverse, inverse_explainer)
        self.add(table_inverse)
        table_as = table.copy().shift(RIGHT * 2.0 + DOWN * 2.2)
        associativity = manim.Text('Associativity', fill_color=manim.YELLOW).scale(0.8).next_to(table_as, UP)
        associativity_equation = manim.MathTex('{{1}}\\cdot({{2}}\\cdot{{3}})=({{1}}\\cdot{{2}})\\cdot{{3}}') \
            .move_to(table_as).shift(UP * 1.0)
        associativity_equation.submobjects[0].fill_color = manim.RED
        associativity_equation.submobjects[2].fill_color = manim.BLUE
        associativity_equation.submobjects[4].fill_color = manim.YELLOW
        associativity_equation.submobjects[6].fill_color = manim.RED
        associativity_equation.submobjects[8].fill_color = manim.BLUE
        associativity_equation.submobjects[10].fill_color = manim.YELLOW
        self.add(associativity, associativity_equation)


if __name__ == '__main__':
    scene = GeneralGroupDefinition()
    scene.render(True)
