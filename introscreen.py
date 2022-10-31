import asciimatics.effects
from asciimatics.screen import *
from asciimatics.scene import *
from asciimatics.renderers import *
from asciimatics.effects import *




def demo(screen):
    effects = [
        Cycle(
            screen,
            FigletText("Welcome!!!", font='big'),
            screen.height // 2 - 3),
        Cycle(
            screen,
            FigletText("To The Game!", font='big'),
            screen.height // 2 + 3),
        Stars(screen, (screen.width + screen.height))
    ]
    screen.play([Scene(effects, 500)])

Screen.wrapper(demo)

