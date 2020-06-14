from talon import *
from dragonfly import Key

mod = Module()
ctx = Context()

@mod.action_class
class Actions:
    def music_play():
        """"""
        Key("playpause").execute()

    def music_next(n: int):
        """"""
        Key(f"tracknext:{n}").execute()

    def music_prev(n: int):
        """"""
        Key(f"trackprev:{n}").execute()

    def music_volup(n: int):
        """"""
        Key(f"volup:{n}").execute()

    def music_voldown(n: int):
        """"""
        Key(f"voldown:{n}").execute()
