from talon import Context, Module

raw_digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

repeat = {name: str(i) for i, name in enumerate(raw_digits[1:] + teens)}
numbers = {name: str(i+1) for i, name in enumerate(raw_digits[1:] + teens)}
digits = {name: str(i) for i, name in enumerate(raw_digits)}

numberth = {
    "first": "1",
    "second": "2",
    "third": "3",
    "fourth": "4",
    "fifth": "5",
    "sixth": "6",
    "seventh": "7",
    "eighth": "8",
    "last": "9",
    "ninth": "9",
}

mod = Module()
ctx = Context()
import inspect

ctx.lists['repeat20'] = repeat
ctx.lists['numbers20'] = numbers
ctx.lists['numberth'] = numberth
ctx.lists['digits10'] = digits
ctx.lists['spoken10'] = raw_digits


@mod.capture
def r20(m) -> int:
    "Repeat values up to twenty"

@mod.capture
def n20(m) -> int:
    "Numbers up to twenty"

@mod.capture
def spoken10(m) -> str:
    "Numbers up to twenty"

@mod.capture
def digits(m) -> int:
    "A series of digits"

@mod.capture
def numberth(m) -> int:
    "Numberth"

@ctx.capture(rule="[{repeat20}]")
def r20(m):
    return int(m["repeat20"]) if hasattr(m, "repeat20") else 0

@ctx.capture(rule="[{numbers20}]")
def n20(m):
    return int(m["numbers20"]) if hasattr(m, "numbers20") else 1

@ctx.capture(rule="[{spoken10}]")
def spoken10(m):
    return m["spoken10"] if hasattr(m, "spoken10") else "one"

@ctx.capture(rule="{digits10}+")
def digits(m):
    return "".join(m["digits10_list"])

@ctx.capture(rule="{numberth}")
def numberth(m):
    return m["numberth"]
