from time import sleep
import shutil
import subprocess
from datetime import time, datetime
from typing import List, NamedTuple, Dict
from talon import ui, Module, Context, registry, actions, imgui, cron
import os
from pathlib import Path

NOTES_DIR = Path(__file__).parent / "notes"
NOTES_DIR.mkdir(exist_ok=True)
ARCHIVE_DIR = Path(__file__).parent / "archive"
ARCHIVE_DIR.mkdir(exist_ok=True)


class Note(NamedTuple):
    heading: str
    body: str
    path: Path
    mtime_seen: float

mod = Module()
ctx = Context()

mod.tag("notes_showing")

counter = 0
notes_by_filename: Dict[str, Note] = {}
notes_by_number: Dict[int, Note] = {}

def occasional_update():
    global counter
    counter += 1
    return counter % 60 == 0

def update_notes():
    global notes_by_filename
    all_notes = list(NOTES_DIR.glob("*.txt"))
    filenames = {p.name for p in all_notes}
    for k in list(notes_by_filename.keys()):
        if k not in filenames:
            del notes_by_filename[k]

    for path in all_notes:
        mtime = path.stat().st_mtime
        if path.name in notes_by_filename and mtime <= notes_by_filename[path.name].mtime_seen:
            continue # nothing new
        with open(path, "r") as f:
            lines = list(f.readlines())
        heading = lines[0].strip() if len(lines) > 0 else ""
        body = "\n".join(lines[1:]) if len(lines) > 1 else ""
        if not heading and not body:
            path.unlink()
            continue
        notes_by_filename[path.name] = Note(heading, body, path, mtime)

def maybe_update_notes():
    if occasional_update():
        update_notes()

extra_padding = 50

@imgui.open(x=0, y=600)
def notes_gui(gui: imgui.GUI):
    maybe_update_notes()
    global notes_by_filename
    gui.text(f"| Notes {' '*extra_padding} |")
    for i, note in enumerate(notes_by_filename.values(), 1):
        if gui.button(f"{i: >2}. {note.heading}  |"):
            subprocess.Popen(["notepad", str(note.path)])
        notes_by_number[i] = note


@mod.action_class
class Actions:
    def notes_gui_toggle():
        """Toggle the notes gui"""
        if notes_gui.showing:
            ctx.tags = []
            notes_gui.hide()
        else:
            update_notes()
            ctx.tags = ["user.notes_showing"]
            notes_gui.show()

    def create_note():
        """Create a new note"""
        curtime = datetime.now().strftime("%Y-%m-%d %H%M%S")
        file_path = NOTES_DIR / f"{curtime}.txt"
        file_path.touch()
        subprocess.Popen(["notepad", str(file_path)])
        update_notes()

    def delete_note(n:int):
        """Delete note number n"""
        global notes_by_number
        global notes_by_filename
        assert n <= len(notes_by_number)
        note = notes_by_number[n]
        archive_name = f"{note.path.stem} - {note.heading}.txt"
        shutil.move(note.path, ARCHIVE_DIR / archive_name)
        note.path.unlink()
        del notes_by_number[n]
        del notes_by_filename[note.path.name]

    def show_note(n: int):
        """Show note number n"""
        global notes_by_number
        assert n <= len(notes_by_number)
        subprocess.Popen(["notepad", str(notes_by_number[n].path)])
