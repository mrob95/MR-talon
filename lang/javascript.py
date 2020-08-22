from user.imports import *

BINDINGS = utilities.load_toml_relative("config/javascript.toml")


ctx = Context("JavaScript")
ctx.matches = r"title: /.*\.js$/"

commands = BINDINGS["commands"]
ctx.lists["user.functions"] = BINDINGS["functions"]

# ctx.commands = {
#     **{k: actions.Alternating(v) for k, v in commands.items()},
#     # **{f"fun {k}": [f"{v}()", Key("left")] for k, v in functions.items()},
#     # "function [<dgndictation>]": ["fn ", textformat.insert_text(0, 3), "(){}", Key("left left")],
# }
# print(dir(talon.actions.list()))
# print(talon.actions.list())
