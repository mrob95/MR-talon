from user.imports import *
from subprocess import Popen
from talon import *
from talon import imgui
from win32gui import GetForegroundWindow, GetWindowText
import os
import time

PERSONAL = utilities.load_toml_relative("config/personal.toml")
CORE = utilities.load_toml_relative("config/core.toml")

mod = Module()
ctx = Context("misc")

def winfo(t):
    print(t)
    print(f"\t-- Shadow app: {ui.active_app()}")
    print(f"\t-- Shadow app exe: {ui.active_app().exe}")
    print(f"\t-- Shadow window title: {ui.active_window().title}")
    print(f"\t-- Actual window title: {GetWindowText(GetForegroundWindow())}")
    print(f"\t-- To check: {talon.windows.winevents.monitor.last_foreground}")
    print(f"\t-- Shadow hwnd: {ui.active_window().id}")
    print(f"\t-- Actual hwnd: {GetForegroundWindow()}")

# def ginfo(w):
#     print(hash(str(speech_system.engine.engine.grammar_blobs['talon_main'][2])))

# ui.register('post:app_activate', winfo)

@imgui.open(x=700, y=0, software=False)
def gui_wheel(gui: imgui.GUI):
    gui.text("This is a test")
    gui.line()
    if gui.button("Wheel Stop [stop scrolling]"):
        print("test")

@mod.action_class
class Actions:
    def test_gui():
        """"""
        gui_wheel.hide()