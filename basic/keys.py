from user.imports import *

CORE = utilities.load_toml_relative("config/core.toml")

ctx = Context("basic_keys")

alphabet = CORE["letters_alt"]
digits = {str(i): str(i) for i in range(10)}
directions = CORE["directions"]
direction_modifiers = CORE["modifiers"]
repeat = {str(i): str(i) for i in range(20)}
punctuation = CORE["punctuation"]
punctuation.update(CORE["punctuation2"])
punctuation2 = CORE["punctuation2"]
simple_keys = CORE["keys"]
simple_keys_norepeat = CORE["misc_core_keys"]

def get_repeat(m, list_name):
  try:
    rep = int(m[list_name])
  except KeyError:
    rep = 1
  return rep


def direction(m):
  try:
    mod = m["direction_modifiers"]
  except KeyError:
    mod = ""
  try:
    dire = m["directions"]
  except KeyError:
    dire = "left"
  rep = get_repeat(m, "repeat")
  key = "-".join([mod, dire] if mod else [dire])
  for _ in range(rep):
    press(key)


def direction_extreme(m):
  try:
    mod = m["direction_modifiers"]
  except KeyError:
    mod = ""
  dire = m["directions"]
  if dire in ["up", "down"]:
    mod += "-ctrl"
  dire = "home" if dire in ["left", "up"] else "end"
  key = "-".join([mod, dire] if mod else [dire])
  print(key)
  press(key)

repeated_action = actions.gen_repeated_action("repeat")

ctx.commands = {
    # "{alphabet}": lambda m: Key(m["alphabet"])(m),
    # "big {alphabet}": lambda m: press(m["alphabet"].upper()),
    # "numb {digits}+": lambda m: Str("".join(m["digits_list"]))(m),
    # "{direction_modifiers} [{repeat}]": direction,
    # "[{direction_modifiers}] {directions} [{repeat}]": direction,
    # "[{direction_modifiers}] {directions} wally": direction_extreme,
    # "{punctuation}": lambda m: Key(m["punctuation"])(m),
    # "long {punctuation2}": [" ", lambda m: Key(m["punctuation2"])(m), " "],
    # "{simple_keys} [{repeat}]": repeated_action(lambda m: Key(m["simple_keys"])(m)),
    # "{simple_keys_norepeat}": lambda m: press(m["simple_keys_norepeat"]),

    # "stoosh": actions.ContextAction(Key("ctrl-c"), {
    #   "mintty.exe": Key("ctrl-insert"),
    #   # "windowsterminal.exe": Key("ctrl-shift-c"),
    #   }),
    # "spark": actions.ContextAction(Key("ctrl-v"), {
    #   "mintty.exe": Key("insert"),
    #   # "windowsterminal.exe": Key("ctrl-shift-v"),
    #   }),
    "check [{repeat}]": actions.ContextAction(
      repeated_action(Key("ctrl-enter")), {
      "notepad.exe": repeated_action(Key("end enter")),
      }),
    "duple [{repeat}]": actions.ContextAction(
      repeated_action(Key("home shift-end ctrl-c end enter c-v")), {
        "mintty.exe": lambda m: None,
        "code.exe": repeated_action(Key("shift-alt-down")),
      }),

    "hug prekris": Key("("),
    "hug curly": Key("{"),
    "hug brax": Key("["),
  }

ctx.lists["alphabet"] = alphabet
ctx.lists["digits"] = digits
ctx.lists["directions"] = directions
ctx.lists["direction_modifiers"] = direction_modifiers
ctx.lists["punctuation"] = punctuation
ctx.lists["punctuation2"] = punctuation2
ctx.lists["simple_keys"] = simple_keys
ctx.lists["repeat"] = repeat
ctx.lists["simple_keys_norepeat"] = simple_keys_norepeat