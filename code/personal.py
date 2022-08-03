from talon import Module, Context, resource
from typing import Dict
import toml

mod = Module()
ctx = Context()


def load_toml(path: str) -> Dict:
    try:
        contents = resource.read(str(path))
    except FileNotFoundError:
        return {}
    return toml.loads(contents)

PERSONAL = load_toml("../config/personal.toml")

mod.list("personal", desc="...")
ctx.lists["user.personal"] = PERSONAL

FOLDERS = load_toml("../config/folders.toml")

mod.list("folders", desc="Commonly accessed folders")
ctx.lists["user.folders"] = FOLDERS
