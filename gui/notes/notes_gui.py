import time
import shutil
import subprocess
from datetime import time, datetime
from typing import List, NamedTuple
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

mod = Module()
ctx = Context()

mod.tag("notes_showing")

counter = 0
notes: List[Note] = []

def occasional_update():
    global counter
    counter += 1
    return counter % 60 == 0

def update_notes():
    global notes
    notes = []
    for path in NOTES_DIR.glob("*.txt"):
        with open(path, "r") as f:
            lines = list(f.readlines())
        heading = lines[0].strip() if len(lines) > 0 else ""
        body = "\n".join(lines[1:]) if len(lines) > 1 else ""
        notes.append(Note(heading, body, path))

def maybe_update_notes():
    if occasional_update():
        update_notes()

extra_padding = 50

@imgui.open(x=0, y=600)
def notes_gui(gui: imgui.GUI):
    maybe_update_notes()
    global notes
    gui.text(f"| Notes {' '*extra_padding} |")
    for i, note in enumerate(notes, 1):
        if gui.button(f"{i: >2}. {note.heading}  |"):
            subprocess.Popen(["notepad", str(note.path)])


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

    def delete_note(n: int):
        """Delete note number n"""
        global notes
        assert n <= len(notes)
        note = notes[n-1]
        archive_name = f"{note.path.stem} - {note.heading}.txt"
        shutil.move(note.path, ARCHIVE_DIR / archive_name)
        notes[n-1].path.unlink()
        update_notes()

    def show_note(n: int):
        """Show note number n"""
        global notes
        assert n <= len(notes)
        subprocess.Popen(["notepad", str(notes[n-1].path)])
