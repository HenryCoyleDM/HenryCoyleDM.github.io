import manim

from imports import *

__all__ = ['CompositionOfDecorationsCayleyGraph']


class CompositionOfDecorationsCayleyGraph(manim.Scene):
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
        self.add(graph.shift(DOWN * 0.5 + RIGHT * 1.0))
        for a in [4, 6, 8, 10, 12, 14]:
            graph[a].set_stroke(opacity=0.2)
            graph[a][1].set_fill(opacity=0.2)
        self.add(manim.Circle(graph[1].radius + 0.05, color=manim.MAROON).move_to(graph[1]))
        self.add(manim.Circle(graph[3].radius + 0.05, color=manim.GOLD).move_to(graph[3]))
        label1_1 = manim.MathTex('{{1}}\\cdot{{1}}={{2}}\\cdot{{3}}\\cdot{{1}}').next_to(graph[5], RIGHT, -0.2)
        label1_1[0].set_fill(manim.MAROON)
        label1_1[2].set_fill(manim.RED)
        label1_1[4].set_fill(manim.GREEN_A)
        label1_1[6].set_fill(manim.GOLD)
        label1_1[8].set_fill(manim.RED)
        self.add(label1_1)
        label3_1 = manim.MathTex('{{3}}\\cdot{{1}}').next_to(graph[7], LEFT, 0.1)
        label3_1[0].set_fill(manim.GOLD)
        label3_1[2].set_fill(manim.RED)
        self.add(label3_1)
        label1_2 = manim.MathTex('{{1}}\\cdot{{2}}={{2}}\\cdot{{3}}\\cdot{{2}}').next_to(graph[9], UP, 0.1)
        label1_2[0].set_fill(manim.MAROON)
        label1_2[2].set_fill(manim.BLUE)
        label1_2[4].set_fill(manim.GREEN_A)
        label1_2[6].set_fill(manim.GOLD)
        label1_2[8].set_fill(manim.BLUE)
        self.add(label1_2)
        label3_2 = manim.MathTex('{{3}}\\cdot{{2}}').next_to(graph[11], DOWN, 0.1)
        label3_2[0].set_fill(manim.GOLD)
        label3_2[2].set_fill(manim.BLUE)
        self.add(label3_2)
        label1_3 = manim.MathTex('{{1}}\\cdot{{3}}={{2}}\\cdot{{3}}\\cdot{{3}}').next_to(graph[13], RIGHT + DOWN)\
            .shift(LEFT * 1.5 + UP * 3.5)
        label1_3[0].set_fill(manim.MAROON)
        label1_3[2].set_fill(manim.YELLOW)
        label1_3[4].set_fill(manim.GREEN_A)
        label1_3[6].set_fill(manim.GOLD)
        label1_3[8].set_fill(manim.YELLOW)
        self.add(label1_3)
        label3_3 = manim.MathTex('{{3}}\\cdot{{3}}').next_to(graph[15], LEFT + DOWN)\
            .shift(RIGHT * 3.2 + UP * 1.5)
        label3_3[0].set_fill(manim.GOLD)
        label3_3[2].set_fill(manim.YELLOW)
        self.add(label3_3)
        two_times_arrow = manim.CurvedArrow(dot3.get_critical_point(RIGHT + UP),
                                            dot1.get_critical_point(LEFT + UP), angle=-1.5, stroke_color=manim.GREEN_A)
        two_times_tex = manim.MathTex('{{2}}\\cdot').next_to(two_times_arrow, UP, 0.1)
        two_times_tex[0].set_fill(manim.GREEN_A)
        self.add(two_times_arrow, two_times_tex)
        explanation = manim.Tex('When you apply\\\\'
                                'the transformation\\\\'
                                '{{$2$}}$\\cdot$ to the\\\\'
                                'arrows coming out\\\\'
                                'of {{$3$}}, they match\\\\'
                                'the old arrows\\\\'
                                'coming out of {{$1$}}.',
                                tex_environment='flushleft').scale(0.8).shift(LEFT * 4.5)
        explanation[1].set_fill(manim.GREEN_A)
        explanation[3].set_fill(manim.GOLD)
        explanation[5].set_fill(manim.MAROON)
        self.add(explanation)


if __name__ == '__main__':
    scene = CompositionOfDecorationsCayleyGraph()
    scene.render(True)
