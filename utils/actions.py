from talon.voice import *
import time

class gen_repeated_action():
    def __init__(self, list_name):
        self.list_name = list_name

    def __call__(self, action):
        def f(m):
            try:
                rep = int(m[self.list_name][0])
            except KeyError:
                rep = 1
            for _ in range(rep):
                action(m)
        return f

def gen_alternating(list_name, lookup):
    def execute_command(m):
        c = lookup[m[list_name][0]]
        if isinstance(c, str):
            Str(c)(None)
        else:
            for i, key_or_text in enumerate(c):
                if i%2 == 0:
                    Str(key_or_text)(None)
                else:
                    Key(key_or_text)(None)
    return execute_command

def exec_str(list_name, lookup):
    return lambda m: Str(lookup[m[list_name][0]])(m)

def exec_key(list_name, lookup):
    return lambda m: Key(lookup[m[list_name][0]])(m)

class ContextAction:
    def __init__(self, default, alternatives):
        self.default = default
        self.alternatives = alternatives

    def __call__(self, m):
        current_exe = ui.active_app().exe.lower()
        for match, action in self.alternatives.items():
            if match in current_exe:
                action(m)
                return
        else:
            self.default(m)

def wait(n):
    return lambda m: time.sleep(n/1000)

def matches(matches, actual):
    for match in matches:
        if match in actual:
            return True
    return False

def context_matches(title=None, exe=None):
    if isinstance(title, str): title = [title]
    if isinstance(exe, str): exe = [exe]
    if title and exe:
        def f(app, win):
            if app is None or win is None:
                return False
            return matches(title, win.title.lower()) or matches(exe, app.exe.lower())
    elif title:
        def f(app, win):
            if win is None or win.title is None:
                return False
            return matches(title, win.title.lower())
    elif exe:
        def f(app, win):
            if app is None or app.exe is None:
                return False
            return matches(exe, app.exe.lower())
    else:
        def f(app, win):
            return True
    return f