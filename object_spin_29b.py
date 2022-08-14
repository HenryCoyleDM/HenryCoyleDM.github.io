import manim

import polyhedron_image_2d
from imports import *

__all__ = ['ObjectSpin']


class ObjectSpin(manim.ThreeDScene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOUR
        vertex0 = LEFT * 1.0 + DOWN * 1.0 + IN * 1.0
        vertex1 = RIGHT * 1.0 + UP * 1.0 + IN * 1.0
        vertex2 = LEFT * 1.0 + UP * 1.0 + OUT * 1.0
        vertex3 = RIGHT * 1.0 + DOWN * 1.0 + OUT * 1.0
        notch0_1 = vertex1 * 0.1 + vertex0 * 0.9
        notch0_2 = vertex2 * 0.3 + vertex0 * 0.7
        notch0_3_3_3 = vertex3 * 0.5 + vertex0 * 0.5
        notch1_1 = vertex0 * 0.1 + vertex1 * 0.9
        notch1_2 = vertex3 * 0.3 + vertex1 * 0.7
        notch1_3_2_3 = vertex2 * 0.5 + vertex1 * 0.5
        notch2_1 = vertex3 * 0.1 + vertex2 * 0.9
        notch2_2 = vertex0 * 0.3 + vertex2 * 0.7
        notch3_1 = vertex2 * 0.1 + vertex3 * 0.9
        notch3_2 = vertex1 * 0.3 + vertex3 * 0.7
        d_tetra = manim.Polyhedron(vertex_coords=[vertex0, vertex1, vertex2, vertex3],
                                   faces_list=[[0, 1, 2],
                                               [0, 1, 3],
                                               [0, 2, 3],
                                               [1, 2, 3]],
                                   faces_config={'fill_opacity': 0.0,
                                                 'stroke_opacity': 0.0},
                                   graph_config={'edge_type': manim.DashedLine,
                                                 'edge_config': {'stroke_opacity': 1.0, 'shade_in_3d': True,
                                                                 'dash_length': 0.12 * math.sqrt(0.5),
                                                                 'dashed_ratio': 0.3},
                                                 'vertex_config': {'fill_opacity': 0.0, 'stroke_opacity': 0.0}})
        tetra = manim.Polyhedron(vertex_coords=[notch0_1, notch0_2, notch0_3_3_3,
                                                notch1_1, notch1_2, notch1_3_2_3,
                                                notch2_1, notch2_2,
                                                notch3_1, notch3_2],
                                 faces_list=[[0, 1, 2], [3, 4, 5], [6, 7, 5], [8, 9, 2],
                                             [0, 3, 5, 7, 1],
                                             [1, 7, 6, 8, 2],
                                             [2, 9, 4, 3, 0],
                                             [5, 6, 8, 9, 4]],
                                 faces_config={'fill_color': manim.GREEN,
                                               'fill_opacity': 0.5,
                                               'stroke_opacity': 0.0},
                                 graph_config={'edge_config': {'stroke_opacity': 1.0, 'shade_in_3d': True},
                                               'vertex_config': {'fill_opacity': 0.0, 'stroke_opacity': 0.0}})
        notched = VGroup(d_tetra, tetra)
        notched.add(manim.Line3D((vertex0 + vertex1) * 0.6, (vertex2 + vertex3) * 0.6,
                                 color=manim.RED),
                    manim.Line3D((vertex0 + vertex2) * 0.6, (vertex1 + vertex3) * 0.6,
                                 color=manim.BLUE),
                    manim.Line3D((vertex0 + vertex3) * 0.6, (vertex1 + vertex2) * 0.6,
                                 color=manim.YELLOW),
                    manim.Dot3D((vertex0 + vertex1) / 2, color=manim.RED,
                                radius=manim.DEFAULT_DOT_RADIUS / 2),
                    manim.Dot3D((vertex2 + vertex3) / 2, color=manim.RED,
                                radius=manim.DEFAULT_DOT_RADIUS / 2),
                    manim.Dot3D((vertex0 + vertex2) / 2, color=manim.BLUE,
                                radius=manim.DEFAULT_DOT_RADIUS / 2),
                    manim.Dot3D((vertex1 + vertex3) / 2, color=manim.BLUE,
                                radius=manim.DEFAULT_DOT_RADIUS / 2),
                    manim.Dot3D((vertex0 + vertex3) / 2, color=manim.YELLOW,
                                radius=manim.DEFAULT_DOT_RADIUS / 2),
                    manim.Dot3D((vertex1 + vertex2) / 2, color=manim.YELLOW,
                                radius=manim.DEFAULT_DOT_RADIUS / 2))
        notched.scale(2.5)
        self.add(notched)
        self.set_camera_orientation(1.3, -1.8, PI / 2)
        self.begin_ambient_camera_rotation(rate=TAU / 6.0, about='phi')
        self.wait(6.0)


if __name__ == '__main__':
    manim.config.quality = 'low_quality'
    scene = ObjectSpin()
    scene.render(True)
