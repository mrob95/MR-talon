from user.imports import *
import time
from talon import ctrl, tap
from talon_plugins import eye_mouse


ctx = Context("mouse")

x, y = ctrl.mouse_pos()

def click(m, button=0, times=1):
    ctrl.mouse_click(pos=(x, y), button=button, times=times, wait=16000)


def right_click(m):
    click(m, button=1)

def dubclick(m):
    click(m, button=0, times=2)
    click(m, button=0, times=2)

def mouse_drag(m):
    ctrl.mouse_click(pos=(x, y), down=True)

def mouse_release(m):
    ctrl.mouse_click(pos=(x, y), up=True)

def press_key_and_click(m, key, button=0, times=1):
    ctrl.key_press(key, down=True)
    ctrl.mouse_click(pos=(x, y), button=button, times=times, wait=16000)
    ctrl.key_press(key, up=True)

ctx.commands = {
    'shifty': lambda m: press_key_and_click(m, 'shift'),
    'colic': lambda m: press_key_and_click(m, 'ctrl'),
    'mouse alt click': lambda m: press_key_and_click(m, 'alt'),
    "millick": lambda m: click(m, 2),
    'kick': click,
    'kick double': dubclick,
    'squat': mouse_drag,
    'bench': actions.ContextAction(
        mouse_release, {
            "shellexperiencehost.exe": [lambda m: print("Saving screenshot"), mouse_release, actions.wait(100), utilities.save_clipboard_image]
        }
    ),
}
