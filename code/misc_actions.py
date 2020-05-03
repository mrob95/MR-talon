from talon import Module, Context, actions
import re

mod = Module()
ctx = Context()

@mod.action_class
class Actions:
    def slow_key(pattern: str):
        """Press some keys slowly"""
        print(pattern)
        keys = pattern.split(" ")
        keys2 = []
        for k in keys:
            chord_rep = k.split(":")
            if len(chord_rep) == 1:
                keys2.append(chord_rep[0])
            elif len(chord_rep) == 2:
                keys2.extend([chord_rep[0]]*int(chord_rep[1]))
        for k in keys2:
            actions.key(k)
            actions.sleep("50ms")
