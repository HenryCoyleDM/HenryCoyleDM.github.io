from imports import *

__all__ = ['CayleyGraph']


class CayleyGraph(manim.Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOUR
        dot0 = manim.LabeledDot('0', fill_color=manim.ORANGE).shift(RIGHT * 2.5 + DOWN * 2.5)
        dot1 = manim.LabeledDot('1', fill_color=manim.RED).shift(RIGHT * 2.5 + UP * 2.5)
        dot2 = manim.LabeledDot('2', fill_color=manim.BLUE).shift(LEFT * 2.5 + DOWN * 2.5)
        dot3 = manim.LabeledDot('3', fill_color=manim.YELLOW).shift(LEFT * 2.5 + UP * 2.5)
        dot0[1].fill_color = manim.WHITE
        dot1[1].fill_color = manim.WHITE
        dot2[1].fill_color = manim.WHITE
        graph = VGroup(dot0, dot1, dot2, dot3,
                       manim.CurvedArrow(dot0.get_top(), dot1.get_bottom(), stroke_color=manim.RED, angle=0.3)
                       .shift(RIGHT * 0.1),
                       manim.CurvedArrow(dot1.get_bottom(), dot0.get_top(), stroke_color=manim.RED, angle=0.3)
                       .shift(LEFT * 0.1),
                       manim.CurvedArrow(dot2.get_top(), dot3.get_bottom(), stroke_color=manim.RED, angle=0.3)
                       .shift(RIGHT * 0.1),
                       manim.CurvedArrow(dot3.get_bottom(), dot2.get_top(), stroke_color=manim.RED, angle=0.3)
                       .shift(LEFT * 0.1),
                       manim.CurvedArrow(dot0.get_left(), dot2.get_right(), stroke_color=manim.BLUE, angle=0.3)
                       .shift(UP * 0.1),
                       manim.CurvedArrow(dot1.get_left(), dot3.get_right(), stroke_color=manim.BLUE, angle=0.3)
                       .shift(UP * 0.1),
                       manim.CurvedArrow(dot2.get_right(), dot0.get_left(), stroke_color=manim.BLUE, angle=0.3)
                       .shift(DOWN * 0.1),
                       manim.CurvedArrow(dot3.get_right(), dot1.get_left(), stroke_color=manim.BLUE, angle=0.3)
                       .shift(DOWN * 0.1),
                       manim.CurvedArrow(dot0.get_critical_point(LEFT + UP), dot3.get_critical_point(RIGHT + DOWN),
                                         stroke_color=manim.YELLOW, angle=0.2).shift(RIGHT * 0.1 + UP * 0.1),
                       manim.CurvedArrow(dot1.get_critical_point(LEFT + DOWN), dot2.get_critical_point(RIGHT + UP),
                                         stroke_color=manim.YELLOW, angle=0.2).shift(LEFT * 0.1 + UP * 0.1),
                       manim.CurvedArrow(dot2.get_critical_point(RIGHT + UP), dot1.get_critical_point(LEFT + DOWN),
                                         stroke_color=manim.YELLOW, angle=0.2).shift(RIGHT * 0.1 + DOWN * 0.1),
                       manim.CurvedArrow(dot3.get_critical_point(RIGHT + DOWN), dot0.get_critical_point(LEFT + UP),
                                         stroke_color=manim.YELLOW, angle=0.2).shift(LEFT * 0.1 + DOWN * 0.1))
        self.add(graph.shift(RIGHT * 3.0))
        line = manim.Line(RIGHT * 2.5 + UP * 1.5, LEFT * 1.5 + UP * 1.5)
        line.add_line_to(LEFT * 1.5 + DOWN * 2.5)
        tex0 = manim.Tex('$0$', fill_color=manim.ORANGE).scale(1.4)
        tex1 = manim.Tex('$1$', fill_color=manim.RED).scale(1.4)
        tex2 = manim.Tex('$2$', fill_color=manim.BLUE).scale(1.4)
        tex3 = manim.Tex('$3$', fill_color=manim.YELLOW).scale(1.4)
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
                       tex0.copy().shift(RIGHT * 2.0 + DOWN * 2.0)).scale(1.2)
        self.add(table.shift(LEFT * 3.5))
        self.add(manim.Text('Cayley Graph').next_to(graph, UP))


if __name__ == '__main__':
    scene = CayleyGraph()
    scene.render(True)
