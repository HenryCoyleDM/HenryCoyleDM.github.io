import colour
import manim

from imports import *


def get_polyhedron_image(shape: VMobject, phi: float, theta: float):
    shape2 = shape.copy()
    shape2.set_shade_in_3d(True)
    scene = manim.ThreeDScene()
    light_pos = scene.camera.light_source.location
    max_distance_to_light = None
    min_distance_to_light = None
    for f in shape2.get_family():
        if isinstance(f, VMobject) and f.has_points():
            distance = math.sqrt(np.linalg.norm(f.get_center_of_mass() - light_pos))
            if max_distance_to_light is None or distance > max_distance_to_light:
                max_distance_to_light = distance
            if min_distance_to_light is None or distance < min_distance_to_light:
                min_distance_to_light = distance
    for f in shape2.get_family():
        if isinstance(f, VMobject) and not isinstance(f, manim.ArrowTip) and not isinstance(f, manim.Dot):
            norm_distance = (max_distance_to_light - math.sqrt(np.linalg.norm(f.get_center_of_mass() - light_pos)))\
                            / (max_distance_to_light - min_distance_to_light)
            color = f.get_fill_color()
            brightness = color.get_luminance()
            new_brightness = (norm_distance + brightness) / 2
            color.set_luminance(new_brightness)
            f.set_fill(color.get_hex(), family=False)
    shape2.rotate(-theta, axis=OUT, about_point=ORIGIN).rotate(-phi, axis=UP, about_point=ORIGIN)
    for f in shape2.get_family():
        f.set_z_index_by_z_coordinate()
        for p in f.points:
            p[2] = 0.0
    return shape2
