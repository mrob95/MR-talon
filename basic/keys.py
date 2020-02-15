from ..imports import *

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
    rep = int(m[list_name][0])
  except KeyError:
    rep = 1
  return rep


def direction(m):
  try:
    mod = direction_modifiers[m["basic_keys.direction_modifiers"][0]]
  except KeyError:
    mod = ""
  try:
    dire = directions[m["basic_keys.directions"][0]]
  except KeyError:
    dire = "left"
  rep = get_repeat(m, "basic_keys.repeat")
  key = "-".join([mod, dire] if mod else [dire])
  for _ in range(rep):
    press(key)


def direction_extreme(m):
  try:
    mod = direction_modifiers[m["basic_keys.direction_modifiers"][0]]
  except KeyError:
    mod = ""
  dire = directions[m["basic_keys.directions"][0]]
  if dire in ["up", "down"] and not mod:
    mod = "ctrl"
  dire = "home" if dire in ["left", "up"] else "end"
  key = "-".join([mod, dire] if mod else [dire])
  press(key)

repeated_action = actions.gen_repeated_action("basic_keys.repeat")

ctx.keymap(
  {
    "{basic_keys.alphabet}": lambda m: press(alphabet[m["basic_keys.alphabet"][0]]),
    "big {basic_keys.alphabet}": lambda m: press(alphabet[m["basic_keys.alphabet"][0]].upper()),
    "numb {basic_keys.digits}+": lambda m: Str("".join(m["digits_list"]))(m),
    "{basic_keys.direction_modifiers} [{basic_keys.repeat}]": direction,
    "[{basic_keys.direction_modifiers}] {basic_keys.directions} [{basic_keys.repeat}]": direction,
    "[{basic_keys.direction_modifiers}] {basic_keys.directions} wally": direction_extreme,
    "{basic_keys.punctuation}": lambda m: Key(punctuation[m["basic_keys.punctuation"][0]])(None),
    "long {basic_keys.punctuation2}": [" ", lambda m: Key(punctuation[m["basic_keys.punctuation2"][0]])(None), " "],
    "{basic_keys.simple_keys} [{basic_keys.repeat}]": repeated_action(lambda m: Key(simple_keys[m["basic_keys.simple_keys"][0]])(None)),
    "{basic_keys.simple_keys_norepeat}": lambda m: press(simple_keys_norepeat[m["basic_keys.simple_keys_norepeat"][0]]),

    "stoosh": actions.ContextAction(Key("ctrl-c"), {
      "mintty.exe": Key("ctrl-insert"),
      "windowsterminal.exe": Key("ctrl-shift-c"),
      }),
    "spark": actions.ContextAction(Key("ctrl-v"), {
      "mintty.exe": Key("insert"),
      "windowsterminal.exe": Key("ctrl-shift-v"),
      }),
    "check [{basic_keys.repeat}]": actions.ContextAction(
      repeated_action(Key("ctrl-enter")), {
      "notepad.exe": repeated_action(Key("end enter")),
      }),
    "duple [{basic_keys.repeat}]": actions.ContextAction(
      repeated_action(Key("home shift-end ctrl-c end enter c-v")), {
        "mintty.exe": lambda m: None,
        "code.exe": repeated_action(Key("shift-alt-down")),
      }),
    "volume up [{basic_keys.repeat}]": repeated_action(Key("volup")),
    "volume down [{basic_keys.repeat}]": repeated_action(Key("voldown")),
    "music next [{basic_keys.repeat}]": repeated_action(Key("next")),
    "music previous [{basic_keys.repeat}]": repeated_action(Key("previous")),
    "music play": Key("play"),

    "hug prekris": Key("("),
    "hug curly": Key("{"),
    "hug brax": Key("["),
  }
)

ctx.set_list("alphabet", alphabet.keys())
ctx.set_list("digits", digits.keys())
ctx.set_list("directions", directions.keys())
ctx.set_list("direction_modifiers", direction_modifiers.keys())
ctx.set_list("repeat", repeat.keys())
ctx.set_list("punctuation", punctuation.keys())
ctx.set_list("punctuation2", punctuation2.keys())
ctx.set_list("simple_keys", simple_keys.keys())
ctx.set_list("simple_keys_norepeat", simple_keys_norepeat.keys())

