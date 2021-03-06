from subprocess import Popen
from talon import *
from talon import imgui
from win32gui import GetForegroundWindow, GetWindowText
from user.utils import utilities
import os
import time

mod = Module()
ctx = Context("mute")

@imgui.open(x=1300, y=1045)
def gui_mute(gui: imgui.GUI):
    if gui.button("Mute"):
        actions.key("alt-a")
        speech_system.engine_mimic("wake up")

@mod.action_class
class Actions:
    def mute_show():
        """"""
        if gui_mute.showing:
            gui_mute.hide()
        else:
            gui_mute.show()
