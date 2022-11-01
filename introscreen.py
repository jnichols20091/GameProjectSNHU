import asciimatics.effects
from asciimatics import screen, effects, scene
from asciimatics.screen import *
from asciimatics.scene import *
from asciimatics.renderers import *
from asciimatics.effects import *
from asciimatics.widgets import *
from asciimatics.event import MouseEvent
from asciimatics.exceptions import NextScene, StopApplication, InvalidFields
import sys
import re

button_options = {
    "FA": "Quit",
    "FB": "Continue"
}


class DemoFrame(Frame):
    def __init__(self, screen):
        super(DemoFrame, self).__init__(scene,
                                        int(screen.height * 2 // 3),
                                        int(screen.width * 2 // 3),
                                        has_border=True,
                                        x=10,
                                        y=10,
                                        data=button_options,
                                        has_shadow=True,
                                        name="My Form")
        boxes = Layout([1, 18, 1])
        self.add_layout(boxes)
        boxes.add_widget(RadioButtons([("FA", 1),
                                       ("FB", 2)],
                                      label="Please Make a Selection:",
                                      name="Start game",
                                      on_change=self._on_change), 1)
        self.fix()

    def _on_change(self):
        changed = False
        self.save()
        for key, value in self.data.items():
            if key not in button_options or button_options[key] != value:
                changed = True
                break
        self._reset_button.disabled = not changed


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


def demo(screen, scene):
    Screen.play([Scene([
        DemoFrame(Frame)
    ], -1)], stop_on_resize=True, start_scene=scene, allow_int=True)

last_scene = None
while True:
    try:
        Screen.wrapper(demo(screen, scene=DemoFrame), catch_interrupt=False, arguments=[last_scene])
        sys.exit(0)
    except ResizeScreenError as e:
        last_scene = e.scene





