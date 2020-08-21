from talon import Context, Module
from user.utils import utilities

BRING = utilities.load_toml_relative("config/bringme.toml")


mod = Module()
ctx = Context()
mod.list("websites", desc="Websites")
ctx.lists["self.websites"] = BRING["website"]
