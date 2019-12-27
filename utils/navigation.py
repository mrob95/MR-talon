# # from dragonfly import *
# # from dragonfly.actions.action_mouse import get_cursor_position
# import time, struct
# # import utilities

# from voice.utils import utilities

# key_wait = 0.05

# def duple(n, esc=True):
#     cb = Clipboard(from_system=True)
#     if esc: Key("escape").execute()
#     Key("home, s-end, c-c, end").execute()
#     time.sleep(key_wait)
#     for _ in range(n):
#         Key("enter, c-v").execute()
#         time.sleep(key_wait)
#     cb.copy_to_system()

# def splat(splatdir, n, extreme, manual=False):
#     if extreme and splatdir == "left":
#         key = "s-home, delete"
#     elif extreme and splatdir == "right":
#         key = "s-end, delete"
#     elif manual:
#         key = "cs-%s:%s, delete" % (splatdir, n)
#         print(key)
#     elif splatdir == "left":
#         key = "c-backspace:%s" % n
#     elif splatdir == "right":
#         key = "c-delete:%s" % n
#     Key(key).execute()

# def text_nav(modifier, direction, n, extreme):
#     k = ""
#     if extreme:
#         if direction in ["left", "up"]:
#             k = "home"
#         else:
#             k = "end"
#         if direction in ["up", "down"]:
#             k = "c-" + k
#     else:
#         k = str(direction) + ":" + str(n)
#     if modifier:
#         if "c-" in k:
#             k = str(modifier).replace("c", "") + k
#         else:
#             k = str(modifier) + "-" + k.replace("c-", "")
#     Key(k).execute()

# '''
# function for performing an action on one or more lines in a text editor.
# E.g.: "cut 128 by 148"

# action: key combination to be pressed once the body of text has been highlighted, could be an empty string
# ln1, ln2: line numbers, usually ShortIntegerRef, the default for ln2 should be an empty string
# go_to_line: key combo to navigate by line number
# select_line_down: key combo to select the line below
# wait: some applications are slow and need a pause between keystrokes, e.g. wait="/10"
# '''
# def action_lines(action, ln1, ln2, go_to_line="c-g", select_line_down="s-down", wait=""):
#     num_lines = max(int(ln2)-int(ln1)+1, int(ln1)-int(ln2)+1) if ln2 else 1
#     top_line = min(int(ln2), int(ln1))                        if ln2 else int(ln1)
#     command = Key(go_to_line) + Text(str(top_line)) + Key("enter%s, home%s, %s%s:%s, %s" % (wait, wait, select_line_down, wait, str(num_lines), action))
#     command.execute()

# actions = {"select" : "",
#             "comment": "c-slash",
#            "copy"   : "c-c",
#            "cut"    : "c-x",
#            "insert" : "c-enter",
#            "remove" : "backspace",
#            "replace": "c-v"}

# def enclose_selected(enclosure):
#     '''
#     Encloses selected text in the appropriate enclosures
#     By using the system Clipboard as a buffer ( doesn't delete previous contents)
#     '''
#     selected_text = utilities.read_selected(True)
#     if selected_text:
#         opener = enclosure.split('~')[0]
#         closer = enclosure.split('~')[1]
#         enclosed_text = opener + selected_text + closer
#         # Attempt to paste enclosed text without altering clipboard
#         if not utilities.paste_string(enclosed_text):
#             print("failed to paste {}".format(enclosed_text))
