from talon import ui, Module, Context, registry, actions, imgui, cron

mod = Module()
ctx = Context()

ctx.matches = r"""
title: /\.go$/
"""

@ctx.action_class("user")
class Actions:
    def lang_print(s: str):
        actions.insert(f'fmt.Println("{s}: ", {s})')
    def get_type_regex() -> str:
        return r"type ([A-Za-z]+)"
    def get_var_regex() -> str:
        return r"(\s|,|\()([A-Za-z_]+?)(,|:|\)|\s*=|\(|\.|\n)"

ctx.lists["user.functions"] = {
    "close": "close",
    "error": "fmt.Errorf",
    "int": "int",
    "length": "len",
    "make": "make",
    "print F": 'fmt.Printf("[|]")',
    "print": "fmt.Println",
    "sprint F": 'fmt.Sprintf("[|]")',
    "string": "string",
    "to integer": "strconv.Atoi",
    "to string": "strconv.Itoa",
    # logging
    "log debug": 'log.Debugf("[|]")',
    "log info": 'log.Infof("[|]")',
    "log error": 'log.Errorf("[|]")',
    "log context debug": 'log.WithContext(ctx).Debugf("[|]")',
    "log context info":  'log.WithContext(ctx).Infof("[|]")',
    "log context error": 'log.WithContext(ctx).Errorf("[|]")',
    #
    "must": "functional.Must",
    "slice map": "slice.Map",
    "slice map with error": "slice.MapWithError",
    "slice filter": "slice.Filter",
    "slice any": "slice.Any",
    "slice all": "slice.All",
    #
    "assert Caller Info": "assert.CallerInfo(t, [|])",
    "assert Condition": "assert.Condition(t, [|])",
    "assert Contains": "assert.Contains(t, [|])",
    "assert Elements Match": "assert.ElementsMatch(t, [|])",
    "assert Empty": "assert.Empty(t, [|])",
    "assert Equal": "assert.Equal(t, [|])",
    "assert Equal Error": "assert.EqualError(t, [|])",
    "assert Equal Values": "assert.EqualValues(t, [|])",
    "assert Error": "assert.Error(t, [|])",
    "assert Error Contains": "assert.ErrorContains(t, [|])",
    "assert Eventually": "assert.Eventually(t, [|])",
    "assert False": "assert.False(t, [|])",
    "assert File Exists": "assert.FileExists(t, [|])",
    "assert Greater": "assert.Greater(t, [|])",
    "assert Greater Or Equal": "assert.GreaterOrEqual(t, [|])",
    "assert Is Decreasing": "assert.IsDecreasing(t, [|])",
    "assert Is Increasing": "assert.IsIncreasing(t, [|])",
    "assert Is Non Decreasing": "assert.IsNonDecreasing(t, [|])",
    "assert Is Non Increasing": "assert.IsNonIncreasing(t, [|])",
    "assert Is Type": "assert.IsType(t, [|])",
    "assert jason Equal": "assert.JSONEq(t, [|])",
    "assert Length": "assert.Len(t, [|])",
    "assert Less": "assert.Less(t, [|])",
    "assert Less Or Equal": "assert.LessOrEqual(t, [|])",
    "assert Negative": "assert.Negative(t, [|])",
    "assert Never": "assert.Never(t, [|])",
    "assert Nil": "assert.Nil(t, [|])",
    "assert No Error": "assert.NoError(t, [|])",
    "assert Not Empty": "assert.NotEmpty(t, [|])",
    "assert Not Equal": "assert.NotEqual(t, [|])",
    "assert Not Nil": "assert.NotNil(t, [|])",
    "assert Not Regexp": "assert.NotRegexp(t, [|])",
    "assert Not Zero": "assert.NotZero(t, [|])",
    "assert Positive": "assert.Positive(t, [|])",
    "assert Regexp": "assert.Regexp(t, [|])",
    "assert Same": "assert.Same(t, [|])",
    "assert Subset": "assert.Subset(t, [|])",
    "assert True": "assert.True(t, [|])",
    "assert Within Duration": "assert.WithinDuration(t, [|])",
    "assert Within Range": "assert.WithinRange(t, [|])",
    "assert Zero": "assert.Zero(t, [|])",
}

ctx.lists["user.logicals"] = {
    "and": " && ",
    "or": " || ",
}

ctx.lists["user.values"] = {
    "false": "false",
    "nil": "nil",
    "none": "nil",
    "null": "nil",
    "true": "true",
}

mod.list("go_types")
ctx.lists["user.go_types"] = {
    # builtins
    "integer": "int",
    "inter eight": "int8",
    "inter sixteen": "int16",
    "inter thirty two": "int32",
    "inter sixty four": "int64",
    "you inter eight": "uint8",
    "you inter sixteen": "uint16",
    "you inter thirty two": "uint32",
    "you inter sixty four": "uint64",
    "boolean": "bool",
    "string": "string",
    "empty interface": "interface{}",
    "error": "error",
    "rune": "rune",
    "byte": "byte",
    "float thirty two": "float32",
    "float sixty four": "float64",
    # common
    "time duration": "time.Duration",
    "time time": "time.Time",
    "HTTP client": "http.Client",
    "UUID": "uuid.UUID",
    "testing": "testing.T",
    "sequel DB": "sql.DB",
    "Context": "context.Context",
    # external
    "cobra command": "cobra.Command",
}

@mod.capture(rule="""[ref] (
             {user.go_types} |
              <user.go_map> |
              <user.go_slice> |
              <user.go_chan> |
              {user.file_types}
            )""")
def go_type(m) -> str:
    """A Go type"""
    if m[0] == "ref":
        return "*" + m[1]
    return str(m)

@mod.capture(rule="map {user.go_types}*")
def go_map(m) -> str:
    """A Go map map, e.g. map int string"""
    d = {1: "map[[|]]", 2: "map[{m.go_types_1}][|]", 3: "map[{m.go_types_1}]{m.go_types_2}"}
    return d[len(m)].format(m=m)

@mod.capture(rule="slice [<number>] [{user.go_types}]")
def go_slice(m) -> str:
    """A Go map slice, e.g. slice string"""
    number = getattr(m, "number", "")
    type = getattr(m, "go_types", "")
    return f"[{number}]{type}"

@mod.capture(rule="channel {user.go_types}")
def go_chan(m) -> str:
    """A Go map slice, e.g. slice string"""
    type = getattr(m, "go_types", "")
    return f"chan {type}"
