from user.imports import *

ctx = Context("lyx", func=actions.context_matches(exe="lyx.exe"))

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

ctx.keymap({
    #
    # LaTeX symbols
    #
    **{k: Str("\\" + v + " ")  for k, v in BINDINGS["tex_symbols1"].items()},
    **{k: Str("\\" + v + " ")  for k, v in BINDINGS["tex_symbols2"].items()},
    **{"greek " + k: Str("\\" + v + " ") for k, v in BINDINGS["greek_letters"].items()},
    **{"greek big " + k: Str("\\" + v.title() + " ") for k, v in BINDINGS["greek_letters"].items()},
    #
    # Misc maths
    #
    "{lyx.digits1}": lambda m: Key(m["lyx.digits1"][0])(m),
    "matrix {lyx.digits1} by {lyx.digits2}": matrix,
    "check"                          : Key("escape end enter ctrl-m"),
    "fraction"                       : Key("alt-m f"),
    "over"                           : Key("shift-left alt-m f down"),
    "(super script | to the power)"  : Key("^"),
    "sub script"                     : Key("_"),
    "squared"                        : Key("^ 2 right"),
    "cubed"                          : Key("^ 3 right"),
    "inverse"                        : Key("^ - 1 right"),
    "(prekris | parens | brackets)"  : Key("alt-m ("),
    "(brax | square brackets)"       : Key("alt-m ["),
    "curly [brackets]"               : Key("alt-m {"),
    "absolute"                       : Key("alt-m |"),
    "add matrix row"                 : Key("alt-m w i"),
    "(delete | remove) matrix row"   : Key("alt-m w d"),
    "add matrix column"              : Key("alt-m c i"),
    "(delete | remove) matrix column": Key("alt-m c d"),
    #
    "accent hat"        : Key("alt-m h"),
    "accent tilde"      : Key("alt-m &"),
    "accent dot"        : Key("alt-m ."),
    "accent double dot" : Key('alt-m "'),
    "accent bar"        : Key("alt-m -"),
    "accent vector"     : Key("alt-m v"),
    #
    # "summation"           : [Str("\\underset \\overset \\sum "), Key("down")],
    "blank summation"       : Str("\\sum "),
    "summation"             : [Str("\\stackrelthree "), Key("down"), Str("\\sum "), Key("down")],
    "(summation | sum) to N": [Str("\\stackrelthree "), Key("n, down"), Str("\\sum "), Key("down")],
    # "product"             : [Str("\\underset \\overset \\prod "), Key("down")],
    "blank product"         : Str("\\prod "),
    "product"               : [Str("\\stackrelthree "), Key("down"), Str("\\prod "), Key("down")],
    # "product to N"        : [Str("\\underset \\overset \\prod "), Key("up, n, down:2")],
    "product to N"          : [Str("\\stackrelthree "), Key("n down"), Str("\\prod "), Key("down")],
    "limit"                 : [Str("\\underset \\lim "), Key("down")],
    "blank limit"           : Str("\\lim "),
    "label above"           : Str("\\overset "),
    "label below"           : Str("\\underset "),
    "prime"                 : [Str("^\\prime "), Key("right")],
    "degrees"               : [Str("^\\circ "), Key("right")],
    "exponential"           : [Str("\\exp "), Key("alt-m (")],
    "expectation"           : [Str("E"), Key("alt-m (")],
    "variance"              : [Str("Var"), Key("alt-m (")],
    #
    "real numbers"          : [Str("\\mathbb R"), Key("right")],
    "complex numbers"       : [Str("\\mathbb C"), Key("right")],
    "integer numbers"       : [Str("\\mathbb Z"), Key("right")],
    "rational numbers"      : [Str("\\mathbb Q"), Key("right")],
    "natural numbers"       : [Str("\\mathbb N"), Key("right")],
    #
    # Program control
    #
    "math mode"                      : Key("ctrl-m"),
    "new file"    : Key("ctrl-n"),
    "open file"   : Key("ctrl-o"),
    "save as"     : Key("ctrl-shift-s"),
    "math mode"   : Key("ctrl-m"),
    "display mode": Key("ctrl-shift-m"),
    "normal mode" : Key("alt-p s"),
    "view PDF"    : Key("ctrl-r"),
    "update PDF"  : Key("ctrl-shift-r"),
    "next tab"              : Key("ctrl-pgdown"),
    "(prior | previous) tab": Key("ctrl-pgup"),
    "close tab"             : Key("ctrl-w"),
    "move line up"          : Key("alt-up"),
    "move line down"        : Key("alt-down"),
    #
    "insert (in line formula | in line)"            : Key("alt-i h i"),
    "insert (numbered formula)"                     : Key("alt-i h n"),
    "insert (display formula | display)"            : Key("alt-i h d"),
    "insert equation array"                         : Key("alt-i h e"),
    "insert (AMS align environment | AMS align)"    : Key("alt-i h a"),
    "insert AMS align at [environment]"             : Key("alt-i h t"),
    "insert AMS flalign [environment]"              : Key("alt-i h f"),
    "insert (AMS gathered environment | AMS gather)": Key("alt-i h g"),
    "insert (AMS multline [environment]| multiline)": Key("alt-i h m"),
    "insert array [environment]"                    : Key("alt-i h y"),
    "insert (cases [environment] | piecewise)"      : Key("alt-i h c"),
    "insert (aligned [environment] | align)"        : Key("alt-i h l"),
    "insert aligned at [environment]"               : Key("alt-i h v"),
    "insert gathered [environment]"                 : Key("alt-i h h"),
    "insert split [environment]"                    : Key("alt-i h s"),
    "insert delimiters"                             : Key("alt-i h r"),
    "insert matrix"                                 : Key("alt-i h x"),
    "insert macro"                                  : Key("alt-i h o"),
    #
    "insert [bulleted] list"            : Key("alt-p b"),
    "insert numbered list"              : Key("alt-p e"),
    "insert description"                : Key("alt-p d"),
    "insert part"                       : Key("alt-p 0"),
    "insert (section | heading)"        : Key("alt-p 2"),
    "insert sub (section | heading)"    : Key("alt-p 3"),
    "insert sub sub (section | heading)": Key("alt-p 4"),
    "insert paragraph"                  : Key("alt-p 5"),
    "insert sub paragraph"              : Key("alt-p 6"),
    "insert title"                      : Key("alt-p t"),
    "insert author"                     : Key("alt-p shift-a"),
    "insert date"                       : Key("alt-p shift-d"),
    "insert abstract"                   : Key("alt-p a"),
    "insert address"                    : Key("alt-p alt-a"),
    "insert bibliography"               : Key("alt-p shift-b"),
    "insert quotation"                  : Key("alt-p alt-q"),
    "insert quote"                      : Key("alt-p q"),
    "insert verse"                      : Key("alt-p v"),

})