import manim

from imports import *

__all__ = ['FruchtGraph']


class FruchtGraph(manim.Scene):
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
        self.add(graph.shift(LEFT * 3.5))
        v0 = RIGHT * 2.5 + DOWN * 2.5
        v1 = RIGHT * 2.5 + UP * 2.5
        v2 = LEFT * 2.5 + DOWN * 2.5
        v3 = LEFT * 2.5 + UP * 2.5
        w0 = v0 / 12
        w1 = v1 / 12
        w2 = v2 / 12
        w3 = v3 / 12
        r = RIGHT * 0.3
        e = LEFT * 0.3
        u = UP * 0.3
        d = DOWN * 0.3
        layout = {0: v0, 1: v1, 2: v2, 3: v3,
                  4: 6 * w0 + 6 * w1 + e, 5: 6 * w0 + 6 * w1 + 2 * e,
                  6: 6 * w1 + 6 * w0 + r, 7: 6 * w1 + 6 * w0 + 2 * r,
                  8: 6 * w2 + 6 * w3 + e, 9: 6 * w2 + 6 * w3 + 2 * e,
                  10: 6 * w3 + 6 * w2 + r, 11: 6 * w3 + 6 * w2 + 2 * r,
                  12: 8 * w0 + 4 * w2 + d, 13: 8 * w0 + 4 * w2 + 2 * d, 14: 4 * w0 + 8 * w2 + d,
                  15: 8 * w1 + 4 * w3 + d, 16: 8 * w1 + 4 * w3 + 2 * d, 17: 4 * w1 + 8 * w3 + d,
                  18: 8 * w2 + 4 * w0 + u, 19: 8 * w2 + 4 * w0 + 2 * u, 20: 4 * w2 + 8 * w0 + u,
                  21: 8 * w3 + 4 * w1 + u, 22: 8 * w3 + 4 * w1 + 2 * u, 23: 4 * w3 + 8 * w1 + u,
                  24: 9 * w0 + 3 * w3 + e + d, 25: 9 * w0 + 3 * w3 + 2 * e + 2 * d,
                  26: 6 * w0 + 6 * w3 + e + d, 27: 3 * w0 + 9 * w3 + e + d,
                  28: 9 * w1 + 3 * w2 + r + d, 29: 9 * w1 + 3 * w2 + 2 * r + 2 * d,
                  30: 6 * w1 + 6 * w2 + r + d, 31: 3 * w1 + 9 * w2 + r + d,
                  32: 9 * w2 + 3 * w1 + e + u, 33: 9 * w2 + 3 * w1 + 2 * e + 2 * u,
                  34: 6 * w2 + 6 * w1 + e + u, 35: 3 * w2 + 9 * w1 + e + u,
                  36: 9 * w3 + 3 * w0 + r + u, 37: 9 * w3 + 3 * w0 + 2 * r + 2 * u,
                  38: 6 * w3 + 6 * w0 + r + u, 39: 3 * w3 + 9 * w0 + r + u}
        frucht_graph = manim.Graph(list(range(40)),
                                   [(0, 4), (0, 5), (4, 5), (4, 1),
                                    (1, 6), (1, 7), (6, 7), (6, 0),
                                    (2, 8), (2, 9), (8, 9), (8, 3),
                                    (3, 10), (3, 11), (10, 11), (10, 2),
                                    (0, 12), (0, 13), (12, 13), (12, 14), (14, 2),
                                    (1, 15), (1, 16), (15, 16), (15, 17), (17, 3),
                                    (2, 18), (2, 19), (18, 19), (18, 20), (20, 0),
                                    (3, 21), (3, 22), (21, 22), (21, 23), (23, 1),
                                    (0, 24), (0, 25), (24, 25), (24, 26), (26, 27), (27, 3),
                                    (1, 28), (1, 29), (28, 29), (28, 30), (30, 31), (31, 2),
                                    (2, 32), (2, 33), (32, 33), (32, 34), (34, 35), (35, 1),
                                    (3, 36), (3, 37), (36, 37), (36, 38), (38, 39), (39, 0)],
                                   layout=layout)
        for t in [(0, 4), (0, 5), (4, 5), (4, 1),
                  (1, 6), (1, 7), (6, 7), (6, 0),
                  (2, 8), (2, 9), (8, 9), (8, 3),
                  (3, 10), (3, 11), (10, 11), (10, 2)]:
            frucht_graph.edges[t].set_stroke(color=manim.RED_A)
        for t in [(0, 12), (0, 13), (12, 13), (12, 14), (14, 2),
                  (1, 15), (1, 16), (15, 16), (15, 17), (17, 3),
                  (2, 18), (2, 19), (18, 19), (18, 20), (20, 0),
                  (3, 21), (3, 22), (21, 22), (21, 23), (23, 1)]:
            frucht_graph.edges[t].set_stroke(color=manim.BLUE_A)
        for t in [(0, 24), (0, 25), (24, 25), (24, 26), (26, 27), (27, 3),
                  (1, 28), (1, 29), (28, 29), (28, 30), (30, 31), (31, 2),
                  (2, 32), (2, 33), (32, 33), (32, 34), (34, 35), (35, 1),
                  (3, 36), (3, 37), (36, 37), (36, 38), (38, 39), (39, 0)]:
            frucht_graph.edges[t].set_stroke(color=manim.YELLOW_A)
        self.add(frucht_graph.shift(RIGHT * 3.5))
        self.add(manim.Arrow(graph.get_right(), frucht_graph.get_left(),
                             stroke_width=manim.DEFAULT_STROKE_WIDTH * 2, stroke_color=manim.GREEN))


if __name__ == '__main__':
    scene = FruchtGraph()
    scene.render(True)
