import math

import asciimatics.effects
from asciimatics.paths import Path
from asciimatics.screen import *
from asciimatics.scene import *
from asciimatics.renderers import *
from asciimatics.effects import *
from asciimatics.sprites import *
import sys


def background(screen):
    effects = [
        Cycle(
            screen,
            FigletText("Welcome", font='ogre'),
            screen.height // 4 - 3),
        Cycle(
            screen,
            FigletText("To The Game!", font='ogre'),
            screen.height // 4 + 3),
        Stars(screen, (screen.width + screen.height)),
        Matrix(
            screen,
        ),
    ]

    screen.play([Scene(effects, 500)])


Screen.wrapper(background)
