# -*- coding: utf-8 -*-
from talon import *
import io, os, sys, time, re, datetime
import toml, webbrowser, json
try:
    from PIL import ImageGrab
except ImportError:
    print("Failed to import PIL")
    pass
from subprocess import Popen
from six import PY2
import requests


key_wait = 0.05


BASE_PATH = os.path.abspath(__file__).replace("\\", "/").rsplit("/utils/")[0]

def save_toml_file(data, path):
    try:
        formatted_data = toml.dumps(data)
        with io.open(path, "wt+", encoding="utf-8") as f:
            f.write(formatted_data)
    except Exception:
        raise

def load_toml_file(path):
    result = {}
    try:
        with io.open(path, "rt", encoding="utf-8") as f:
            result = toml.loads(f.read())
    except IOError as e:
        if e.errno == 2:  # The file doesn't exist.
            save_toml_file(result, path)
        else:
            print(e)
    except Exception as e:
        print(e)
    return result

def get_full_path(path):
    return BASE_PATH + "/" + path

def load_toml_relative(path):
    path = get_full_path(path)
    return load_toml_file(path)

def save_toml_relative(data, path):
    path = get_full_path(path)
    return save_toml_file(data, path)

def read_text_relative(path):
    path = get_full_path(path)
    with open(path, "r") as f:
        return f.read()


def kill_notepad():
    Popen(get_full_path("utils/bin/notepad_kill.bat"))

def browser_open(url):
    webbrowser.open_new_tab(url)

def terminal(dir):
    Popen(["C:/Program Files/Git/git-bash.exe", "--cd=" + dir.replace("\\", "/")])


def tinyurl():
    with clip.capture() as s:
        actions.edit.copy()
        text = s.get()
    url = "http://tinyurl.com/api-create.php?url=" + text
    tiny = requests.get(url)
    clip.set(tiny.text)


def image_name(dir=os.path.expandvars("%USERPROFILE%/Pictures/saved")):
    now = datetime.datetime.now()
    file_name = now.strftime("%Y-%m-%d %H%M%S")
    return "%s/%s" % (dir, file_name)

def save_clipboard_image(m=None):
    im = ImageGrab.grabclipboard()
    try:
        im.save('%s.png' % image_name(),'PNG')
    except AttributeError:
        print("Clipboard does not contain an image")
