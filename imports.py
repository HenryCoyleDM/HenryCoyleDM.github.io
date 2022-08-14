from abc import ABC
from functools import reduce
from typing import List, Optional, Sequence, Union, Callable, Any
import math
import operator
import manim
import numpy as np
from manim import Mobject, VMobject, Group, VGroup, Scene, Animation,\
    Rotate, Transform, Create, Uncreate, RIGHT, LEFT, UP, DOWN, OUT, IN, ORIGIN, PI, TAU
from manim.utils.paths import path_along_circles, straight_path
import animated_mobject
from animated_mobject import AnimatedSprite, VAnimatedSprite, AnimatedSpriteGroup, VAnimatedSpriteGroup,\
    animate_on_animated_sprite
import animation_utilities
from animation_utilities import rotate_sheen_direction_too, UpdateFromRawAlphaFunc

__all__ = ['ABC', 'reduce', 'List', 'Optional', 'Sequence', 'Union', 'Callable', 'Any', 'math', 'operator', 'manim',
           'np', 'Mobject', 'VMobject', 'Group', 'VGroup', 'Scene', 'Animation', 'Rotate', 'Transform',
           'Create', 'Uncreate', 'RIGHT', 'LEFT', 'UP', 'DOWN', 'OUT', 'IN', 'ORIGIN', 'PI', 'TAU',
           'path_along_circles', 'straight_path', 'animated_mobject', 'AnimatedSprite', 'VAnimatedSprite',
           'AnimatedSpriteGroup', 'VAnimatedSpriteGroup', 'animate_on_animated_sprite',
           'animation_utilities', 'rotate_sheen_direction_too', 'UpdateFromRawAlphaFunc',
           'BACKGROUND_COLOUR']

BACKGROUND_COLOUR = '#080808'
