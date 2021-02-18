from talon import speech_system, ui, cron

command_exes = ["code.exe", "mintty.exe", "kindle.exe"]
command_titles = ["JupyterLab"]

in_command_context = False

def matches(matches, actual):
    for match in matches:
        if match is None: continue
        if match in actual: return True
    return False

def context_matches(title=None, exe=None):
    if isinstance(title, str): title = [title]
    if isinstance(exe, str): exe = [exe]
    app, win = ui.active_app(), ui.active_window()
    if app.exe is None or win.title is None:
        return False
    return matches(title, win.title.lower()) or matches(exe, app.exe.lower())

def context_matches_command():
    return context_matches(command_titles, command_exes)


def switch_command():
    global in_command_context
    if in_command_context: return
    speech_system.engine_mimic("switch to command mode")
    in_command_context = True

def switch_normal():
    global in_command_context
    if not in_command_context: return
    speech_system.engine_mimic("switch to normal mode")
    in_command_context = False

def check_context():
    if speech_system.engine and speech_system.engine.name == "dragon":
        switch_command() if context_matches_command() else switch_normal()

cron.interval("1s", check_context)
