from talon import Context, Module

raw_digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]


repeat = {name: str(i) for i, name in enumerate(raw_digits[1:] + teens)}
numbers = {name: str(i+1) for i, name in enumerate(raw_digits[1:] + teens)}
digits_d = {name: str(i) for i, name in enumerate(raw_digits)}
tens_d = {name: str(i*10) for i, name in enumerate(tens, 2)}
numberth_d = {"first": "1","second": "2","third": "3","fourth": "4","fifth": "5","sixth": "6","seventh": "7","eighth": "8","last": "9","ninth": "9"}

mod = Module()
ctx = Context()
import inspect


mod.list("repeat20")
ctx.lists["user.repeat20"] = repeat

mod.list("numbers20")
ctx.lists["user.numbers20"] = numbers

mod.list("numberth")
ctx.lists["user.numberth"] = numberth_d

mod.list("digits10")
ctx.lists["user.digits10"] = digits_d

mod.list("spoken10")
ctx.lists["user.spoken10"] = raw_digits


@mod.capture(rule="[{user.repeat20}]")
def r20(m) -> int:
    "Repeat values up to twenty"
    return int(m["repeat20"]) if hasattr(m, "repeat20") else 0

@mod.capture(rule="[{user.numbers20}]")
def n20(m) -> int:
    "Numbers up to twenty"
    return int(m["numbers20"]) if hasattr(m, "numbers20") else 1

@mod.capture(rule="{user.digits10}+")
def digits(m) -> str:
    "A series of digits"
    return "".join(m["digits10_list"])

@mod.capture(rule="{user.digits10}+")
def digits_int(m) -> int:
    "A series of digits"
    return int("".join(m["digits10_list"]))

@mod.capture(rule="{user.numberth}")
def numberth(m) -> int:
    "Numberth"
    return m["numberth"]
