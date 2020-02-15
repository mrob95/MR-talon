from ..imports import *

ctx = Context("mathcha", func=actions.context_matches(title="mathcha"))

BINDINGS = utilities.load_toml_relative("config/tex_data.toml")

ctx.set_list("digits1", [str(i) for i in range(10)])
ctx.set_list("digits2", [str(i) for i in range(10)])

def matrix(m):
    rows = int(m["lyx.digits1"][0])
    cols = int(m["lyx.digits2"][0])
    # create 1x1
    Str("\\matrix ")(m)
    # expand to reach the right size
    Key("alt-m w i " * (rows - 1))(m)
    Key("alt-m c i " * (cols - 1))(m)

def insert_tex(symbol):
    return [actions.wait(75), Key("\\"), actions.wait(75), Str(symbol), Key("enter")]

ctx.keymap({
    #
    # LaTeX symbols
    #
    **{k: insert_tex(v) for k, v in BINDINGS["tex_symbols1"].items()},
    **{k: insert_tex(v) for k, v in BINDINGS["tex_symbols2"].items()},
    **{f"greek {k}": insert_tex(v) for k, v in BINDINGS["greek_letters"].items()},
    **{f"big greek {k}": insert_tex(v.title()) for k, v in BINDINGS["greek_letters"].items()},
    "summation"       : insert_tex("sum"),
    "product"       : insert_tex("prod"),
    "product"       : insert_tex("lim"),
    #
    # Misc maths
    #
    "matrix {lyx.digits1} by {lyx.digits2}": matrix,
    # "check"                          : Key("escape end enter ctrl-m"),
    "fraction"                       : insert_tex("frac"),
    # "over"                           : Key("shift-left alt-m f down"),
    "(super script | to the power)"  : Key("^"),
    "sub script"                     : Key("_"),
    "squared"                        : Key("^ 2"),
    "cubed"                          : Key("^ 3"),
    "inverse"                        : Key("^ - 1"),
    # "(prekris | parens | brackets)"  : Key("alt-m ("),
    # "(brax | square brackets)"       : Key("alt-m ["),
    # "curly [brackets]"               : Key("alt-m {"),
    # "absolute"                       : Key("alt-m |"),
    # "add matrix row"                 : Key("alt-m w i"),
    # "(delete | remove) matrix row"   : Key("alt-m w d"),
    # "add matrix column"              : Key("alt-m c i"),
    # "(delete | remove) matrix column": Key("alt-m c d"),
    #
    "accent hat"        : insert_tex("hat"),
    "accent tilde"      : insert_tex("tilde"),
    "accent dot"        : insert_tex("dot"),
    "accent double dot" : insert_tex("ddot"),
    "accent bar"        : insert_tex("bar"),
    "accent vector"     : insert_tex("vec"),
    #
    "label above"           : Str("\\overset "),
    "label below"           : Str("\\underset "),
    # "prime"                 : [Str("^\\prime "), Key("right")],
    # "degrees"               : [Str("^\\circ "), Key("right")],
    # "exponential"           : [Str("\\exp "), Key("alt-m (")],
    # "expectation"           : [Str("E"), Key("alt-m (")],
    # "variance"              : [Str("Var"), Key("alt-m (")],
    # #
    # "real numbers"          : [Str("\\mathbb R"), Key("right")],
    # "complex numbers"       : [Str("\\mathbb C"), Key("right")],
    # "integer numbers"       : [Str("\\mathbb Z"), Key("right")],
    # "rational numbers"      : [Str("\\mathbb Q"), Key("right")],
    # "natural numbers"       : [Str("\\mathbb N"), Key("right")],
    #
    # Program control
    #
    "math mode"    : insert_tex("math-container"),
    "math mode"    : insert_tex("math-container"),
    # "new file"    : Key("ctrl-n"),
    # "open file"   : Key("ctrl-o"),
    # "save as"     : Key("ctrl-shift-s"),
    # "display mode": Key("ctrl-shift-m"),
    # "normal mode" : Key("alt-p s"),
    # "view PDF"    : Key("ctrl-r"),
    # "update PDF"  : Key("ctrl-shift-r"),
    # "next tab"              : Key("ctrl-pgdown"),
    # "(prior | previous) tab": Key("ctrl-pgup"),
    # "close tab"             : Key("ctrl-w"),
    # "move line up"          : Key("alt-up"),
    # "move line down"        : Key("alt-down"),
})