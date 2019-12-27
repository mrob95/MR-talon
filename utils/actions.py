from talon.voice import *

class gen_repeated_action():
    def __init__(self, list_name):
        self.list_name = list_name

    def __call__(self, action):
        def f(m):
            try:
                rep = int(m[self.list_name])
            except KeyError:
                rep = 1
            for _ in range(rep):
                action(m)
        return f

def gen_alternating(list_name, lookup):
    def execute_command(m):
        c = lookup[m[list_name]]
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
    return lambda m: Str(lookup[m[list_name]])(None)

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


