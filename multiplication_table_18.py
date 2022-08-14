from imports import *

__all__ = ['MultiplicationTable']


class MultiplicationTable(Scene):
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
                       tex0.copy().shift(RIGHT * 2.0 + DOWN * 2.0)).scale(1.4)
        self.add(table)


if __name__ == '__main__':
    scene = MultiplicationTable()
    scene.render(True)
