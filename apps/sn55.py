from user.imports import *


ctx = Context("sn55")
ctx.matches = r"""
app: scinoteb.exe
"""

BINDINGS = utilities.load_toml_relative("config/ScientificNotebook55.toml")

ctx.lists["digits1"] = [str(i) for i in range(10)]
ctx.lists["digits2"] = [str(i) for i in range(10)]

def control_hold(**kw):
    def f(m):
        ctrl.key_press("ctrl", **kw)
    return f

def TeX(symbol):
    return [control_hold(down=True), Str(symbol), control_hold(up=True)]

def matrix(m):
    rows = m["digits1"][0]
    cols = m["digits2"][0]
    Key("f10")(m)
    actions.wait(50)(m)
    Key("i " + "down "*8 + "enter")(m)
    actions.wait(50)(m)
    Key(rows + " tab " + cols + " enter")(m)

ctx.commands = {
    #
    # LaTeX symbols
    #
    **{k: TeX(v) for k, v in BINDINGS["tex_symbols"].items()},
    **{"greek " + k: Key("ctrl-g " + v) for k, v in BINDINGS["greek_letters"].items()},
    **{"big greek " + k: Key("ctrl-g " + v.title()) for k, v in BINDINGS["greek_letters"].items()},
    #
    # Misc maths
    #
    "{digits1}": lambda m: Key(m["digits1"][0])(m),
    "matrix {digits1} by {digits2}": matrix,
    "fraction"                      : Key("ctrl-f"),
    "over"                          : Key("ctrl-shift-left ctrl-f"),
    "(super script | to the power)" : Key("ctrl-h"),
    "sub script"                    : Key("ctrl-l"),
    "squared"                       : Key("ctrl-h 2 right"),
    "cubed"                         : Key("ctrl-h 3 right"),
    "inverse"                       : Key("ctrl-h - 1 right"),
    "inverse half"                  : Key("ctrl-h - ctrl-f 1 down 2) right right"),
    "(parens | parentheses | prens)": Key("ctrl-0"),
    "(squares | square brackets)"   : Key("ctrl-6"),
    "absolute"                      : Key("ctrl-\\"),
    "norma"                         : Key("ctrl-shift-\\"),
    "chi squared"                   : Key("ctrl-g q ctrl-h 2 right"),
    "(radical | square root)"       : Key("ctrl-r"),
    "summation"                     : Key("ctrl-7"),
    "accent hat"         : Key("ctrl-^"),
    "accent tilde"       : Key("ctrl-~"),
    "accent dot"         : Key("ctrl-."),
    "accent double dot"  : Key("ctrl-\""),
    "accent bar"         : Key("ctrl-_"),
    "accent arrow"       : Key("ctrl--"),
    #
    # Program control
    #
    "new file"                        : Key("f10 f enter"),
    "open file"                       : Key("ctrl-o"),
    "save file"                       : Key("f10 f s"),
    "save as"                         : Key("f10 f " + " down "*5 + "enter"),
    "print file"                      : Key("ctrl-p"),
    "export document"                 : Key("f10 f " + " down "*7 + "enter"),
    "page preview"                    : Key("f10 f " + " down "*17 + "enter"),
    "body math"                       : Key("alt-2 down enter"),
    "body text"                       : Key("alt-2 " + " down "*2 + "enter"),
    "(begin | insert) [bulleted] list": Key("alt-1 " + " down "*2 + "enter"),
    "(begin | insert) numbered list"  : Key("alt-1 " + " down "*4 + "enter"),
    "end [(bulleted | numbered)] list": Key("alt-1 up enter"),
    "insert normal text"              : Key("alt-3 down enter"),
    "insert big text"                 : Key("alt-3 " + " down "*2 + "enter"),
    "insert small text"               : Key("alt-3 " + " down "*9 + "enter"),
    "insert bold text"                : Key("alt-3 " + " down "*3 + "enter"),
    "insert italic text"              : Key("alt-3 " + " down "*6 + "enter"),
    "insert bold symbols"             : Key("alt-3 " + " down "*4 + "enter"),
    "insert centred text"             : Key("alt-2 " + " down "*3 + "enter"),
    "insert left text"                : Key("alt-2 " + " down "*4 + "enter"),
    "insert right text"               : Key("alt-2 " + " down "*5 + "enter"),
    "insert quotation"                : Key("alt-2 " + " down "*11 + "enter"),
    "insert (heading | title) [one]"  : Key("alt-2 " + " down "*6 + "enter"),
    "insert (heading | title) two"    : Key("alt-2 " + " down "*7 + "enter"),
    "insert (heading | title) three"  : Key("alt-2 " + " down "*8 + "enter"),
    "insert (heading | title) four"   : Key("alt-2 " + " down "*9 + "enter"),
    "insert (heading | title) five"   : Key("alt-2 " + " down "*10 + "enter"),
    "evaluate"                        : Key("ctrl-e"),
    "evaluate numerically"            : Key("f10 c down enter"),
    "toggle math"                   : Key("ctrl-m"),
    "toggle text"                   : Key("ctrl-t"),
    "label above"                    : Key("f10 i " + " down "*11 + "enter/25 a enter"),
    "label below"                    : Key("f10 i " + " down "*11 + "enter/25 b enter"),
    "add matrix row"                 : Key("f10 e up up enter/10 enter"),
    "add matrix column"              : Key("f10 e up enter/10 enter"),
}