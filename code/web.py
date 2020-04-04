from talon import Context, Module
from user.utils import utilities

BRING = utilities.load_toml_relative("config/bringme.toml")


mod = Module()
ctx = Context()
mod.list("websites", desc="Websites")
ctx.lists['websites'] = BRING["website"]

@mod.capture
def websites(m) -> str:
    "Websites I use often"

@ctx.capture(rule="{websites}")
def websites(m):
    return m["websites"]