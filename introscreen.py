import asciimatics.effects
from asciimatics.screen import *
from asciimatics.scene import *
from asciimatics.renderers import *
from asciimatics.effects import *
from asciimatics.widgets import *
import sys





def background(screen):
    effects = [
        Cycle(
            screen,
            FigletText("Welcome!!!", font='ogre'),
            screen.height // 2 - 3),
        Cycle(
            screen,
            FigletText("To The Game!", font='ogre'),
            screen.height // 2 + 3),
        Stars(screen, (screen.width + screen.height)),
        Matrix(
            screen,
        )
    ]
    screen.play([Scene(effects, 500)])


def global_shortcuts(event):
    if isinstance(event, KeyboardEvent):
        c = event.key_code
        if c in (17, 24):
            raise StopApplication("User Terminated app")


Screen.wrapper(background)