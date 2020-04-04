from talon.engine import engine
from talon import ui
from talon import cron
from utils import actions

command_exes = ["code.exe", "mintty.exe", "kindle.exe"]
command_titles = ["JupyterLab"]

in_command_context = None

def switch_command():
    engine.mimic("switch to command mode")

def switch_normal():
    engine.mimic("switch to normal mode")

def check_context():
    global in_command_context
    if actions.context_matches(command_titles, command_exes)(ui.active_app(), ui.active_window()):
        if in_command_context is None or not in_command_context:
            switch_command()
            in_command_context = True
    else:
        if in_command_context is None or in_command_context:
            switch_normal()
            in_command_context= False

cron.interval("1s", check_context)