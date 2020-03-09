from talon import Context, Module

repeat = {str(i): str(i) for i in range(1, 20)}
digits = {str(i): str(i) for i in range(10)}
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
# print(inspect.signature(mod.list))
mod.list('repeat', 'Number one to twenty')
ctx.lists['repeat'] = repeat