import manim

from imports import *

__all__ = ['CompositionOfTransformations']


class CompositionOfTransformations(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOUR
        rhombus = manim.Polygon(RIGHT * 2, UP * 3, LEFT * 2, DOWN * 3,
                                fill_color=manim.BLUE,
                                fill_opacity=0.5,
                                stroke_color=manim.WHITE,
                                stroke_opacity=1.0,
                                stroke_width=manim.DEFAULT_STROKE_WIDTH)
        rhombus.set_sheen(1.0, RIGHT * 1 + UP * 2)
        rhombus.scale(0.8)
        r1 = rhombus.copy().rotate(PI, UP)
        r2 = rhombus.copy()
        r3 = rhombus.copy()
        tex1 = manim.Tex('$+$').scale(1.4)
        tex2 = manim.Tex('$=$').scale(1.4)
        equation = VGroup(r1, tex1, r2, tex2, r3)
        equation.arrange()
        self.add(equation,
                 manim.Text('Composing Transformations', fill_color=manim.YELLOW).scale(1.4).next_to(equation, UP))
        self.wait(1.0)
        arrow2 = manim.CurvedDoubleArrow(start_point=LEFT * 1.8 + DOWN * 0.1,
                                         end_point=RIGHT * 1.8 + DOWN * 0.1,
                                         angle=0.5).scale(0.8, about_point=ORIGIN).shift(r2.get_center())
        arrow_tip2 = arrow2.submobjects.pop(0)
        arrow_tip2_2 = arrow2.submobjects.pop(0)
        arrow_animation2 = manim.AnimationGroup(manim.Succession(manim.Wait(0.7), Create(arrow2, run_time=1.1)),
                                                manim.Succession(manim.Wait(1.5), Create(arrow_tip2, run_time=0.5)),
                                                manim.Succession(manim.Wait(0.8), Create(arrow_tip2_2, run_time=0.5)))
        rhombus_animation_2 = rotate_sheen_direction_too(Rotate(r2, PI, UP, run_time=2.0))
        self.play(arrow_animation2, rhombus_animation_2)
        self.wait(0.5)
        arrow1 = manim.CurvedArrow(start_point=RIGHT * 0.4 + DOWN * 2.9,
                                   end_point=RIGHT * 0.4 + UP * 2.9,
                                   radius=np.linalg.norm(RIGHT * 0.4 + UP * 2.9)) \
            .scale(0.8, about_point=ORIGIN).shift(r1.get_center())
        arrow_tip1 = arrow1.submobjects.pop(0)
        arrow_animation1 = manim.AnimationGroup(manim.Succession(manim.Wait(0.4), Create(arrow1, run_time=1.4)),
                                                manim.Succession(manim.Wait(1.5), Create(arrow_tip1, run_time=0.5)))
        rhombus_animation_1 = rotate_sheen_direction_too(Rotate(r1, PI, run_time=2.0))
        self.play(arrow_animation1, rhombus_animation_1)
        self.wait(0.5)
        dashed_r3 = manim.DashedVMobject(r3, 16, dash_offset=0.75)
        for sub in dashed_r3.submobjects:
            sub.set_stroke(opacity=0.8).set_fill(opacity=0.0)
        self.add(dashed_r3)
        dashed_animation = manim.Succession(Rotate(dashed_r3, PI, UP, run_time=2.0),
                                            Rotate(dashed_r3, PI, run_time=2.0))
        arrow3 = manim.CurvedDoubleArrow(start_point=LEFT * 0.1 + UP * 2.5,
                                         end_point=LEFT * 0.1 + DOWN * 2.5,
                                         angle=0.4).scale(0.8, about_point=ORIGIN).shift(r3.get_center())
        arrow_tip3 = arrow3.submobjects.pop(0)
        arrow_tip3_2 = arrow3.submobjects.pop(0)
        arrow_animation3 = manim.AnimationGroup(manim.Succession(manim.Wait(1.4), Create(arrow3, run_time=2.2)),
                                                manim.Succession(manim.Wait(3.0), Create(arrow_tip3, run_time=1.0)),
                                                manim.Succession(manim.Wait(1.6), Create(arrow_tip3_2, run_time=1.0)))
        rhombus_animation_3 = rotate_sheen_direction_too(Rotate(r3, PI, RIGHT, run_time=4.0))
        self.play(dashed_animation, arrow_animation3, rhombus_animation_3)
        self.wait(1.5)


if __name__ == '__main__':
    manim.config.quality = 'low_quality'
    scene = CompositionOfTransformations()
    scene.render(True)
