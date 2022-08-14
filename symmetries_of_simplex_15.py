import polyhedron_image_2d
from imports import *

__all__ = ['SymmetriesOfSimplex']


class SymmetriesOfSimplex(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOUR
        vertex0 = LEFT * 1.0 + DOWN * 1.0 + IN * 1.0
        vertex1 = RIGHT * 1.0 + UP * 1.0 + IN * 1.0
        vertex2 = LEFT * 1.0 + UP * 1.0 + OUT * 1.0
        vertex3 = RIGHT * 1.0 + DOWN * 1.0 + OUT * 1.0
        tetra = manim.Polyhedron(vertex_coords=[vertex0, vertex1, vertex2, vertex3],
                                 faces_list=[[0, 1, 2],
                                             [0, 1, 3],
                                             [0, 2, 3],
                                             [1, 2, 3]],
                                 faces_config={'fill_color': manim.GREEN, 'fill_opacity': 0.5,
                                               'stroke_opacity': 0.0},
                                 graph_config={'edge_config': {'stroke_opacity': 1.0, 'shade_in_3d': True},
                                               'vertex_config': {'fill_opacity': 0.0, 'stroke_opacity': 0.0}})
        tetrahedron = polyhedron_image_2d.get_polyhedron_image(tetra, 1.3, -1.8)
        tetrahedron.scale(2.5).shift(LEFT * 1.2)
        vertex0 = tetrahedron[0][0].points[0]
        vertex1 = tetrahedron[0][0].points[4]
        vertex2 = tetrahedron[0][0].points[8]
        vertex3 = tetrahedron[0][1].points[8]
        tetrahedron.add(manim.Tex('0').next_to(vertex0, RIGHT + DOWN, buff=manim.SMALL_BUFF),
                        manim.Tex('1').next_to(vertex1, RIGHT + UP, buff=manim.SMALL_BUFF),
                        manim.Tex('2').next_to(vertex2, LEFT + DOWN, buff=manim.SMALL_BUFF),
                        manim.Tex('3').next_to(vertex3, LEFT + UP, buff=manim.SMALL_BUFF))
        tetrahedron.scale(0.8).shift(LEFT * 3.0)
        self.add(tetrahedron)
        self.add(manim.Tex('$S_4$', fill_color=manim.YELLOW).move_to(UP * 3.0 + LEFT * 0.5).scale(2.0))
        list1 = manim.Tex('''\
\\begin{align*}
0, 1, 2, 3\\rightarrow 0, 1, 2, 3\\\\
\\rightarrow 0, 1, 3, 2\\\\
\\rightarrow 0, 2, 1, 3\\\\
\\rightarrow 0, 2, 3, 1\\\\
\\rightarrow 0, 3, 1, 2\\\\
\\rightarrow 0, 3, 2, 1\\\\
\\rightarrow 1, 0, 2, 3\\\\
\\rightarrow 1, 0, 3, 2\\\\
\\rightarrow 1, 2, 0, 3\\\\
\\rightarrow 1, 2, 3, 0\\\\
\\rightarrow 1, 3, 0, 2\\\\
\\rightarrow 1, 3, 2, 0
\\end{align*}
''').scale(0.7).shift(RIGHT * 2.0 + UP * 0.5)
        list2 = manim.Tex('''\
\\begin{align*}
\\rightarrow 2, 0, 1, 3\\\\
\\rightarrow 2, 0, 3, 1\\\\
\\rightarrow 2, 1, 0, 3\\\\
\\rightarrow 2, 1, 3, 0\\\\
\\rightarrow 2, 3, 0, 1\\\\
\\rightarrow 2, 3, 1, 0\\\\
\\rightarrow 3, 0, 1, 2\\\\
\\rightarrow 3, 0, 2, 1\\\\
\\rightarrow 3, 1, 0, 2\\\\
\\rightarrow 3, 1, 2, 0\\\\
\\rightarrow 3, 2, 0, 1\\\\
\\rightarrow 3, 2, 1, 0
\\end{align*}
''').scale(0.7).next_to(list1, RIGHT, buff=manim.LARGE_BUFF)
        self.add(list1, list2)
        brace = manim.BraceText(manim.Brace(VGroup(list1, list2), DOWN).shift(UP * 0.5),
                                '4!=24\\textrm{ permutations}')
        self.add(brace)


if __name__ == '__main__':
    scene = SymmetriesOfSimplex()
    scene.render(True)
