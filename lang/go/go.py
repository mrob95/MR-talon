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
    "sprint": 'fmt.Sprint',
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
    "require Caller Info": "require.CallerInfo(t, [|])",
    "require Condition": "require.Condition(t, [|])",
    "require Contains": "require.Contains(t, [|])",
    "require Elements Match": "require.ElementsMatch(t, [|])",
    "require Empty": "require.Empty(t, [|])",
    "require Equal": "require.Equal(t, [|])",
    "require Equal Error": "require.EqualError(t, [|])",
    "require Equal Values": "require.EqualValues(t, [|])",
    "require Error": "require.Error(t, [|])",
    "require Error Contains": "require.ErrorContains(t, [|])",
    "require Eventually": "require.Eventually(t, [|])",
    "require False": "require.False(t, [|])",
    "require File Exists": "require.FileExists(t, [|])",
    "require Greater": "require.Greater(t, [|])",
    "require Greater Or Equal": "require.GreaterOrEqual(t, [|])",
    "require Is Decreasing": "require.IsDecreasing(t, [|])",
    "require Is Increasing": "require.IsIncreasing(t, [|])",
    "require Is Non Decreasing": "require.IsNonDecreasing(t, [|])",
    "require Is Non Increasing": "require.IsNonIncreasing(t, [|])",
    "require Is Type": "require.IsType(t, [|])",
    "require jason Equal": "require.JSONEq(t, [|])",
    "require Length": "require.Len(t, [|])",
    "require Less": "require.Less(t, [|])",
    "require Less Or Equal": "require.LessOrEqual(t, [|])",
    "require Negative": "require.Negative(t, [|])",
    "require Never": "require.Never(t, [|])",
    "require Nil": "require.Nil(t, [|])",
    "require No Error": "require.NoError(t, [|])",
    "require Not Empty": "require.NotEmpty(t, [|])",
    "require Not Equal": "require.NotEqual(t, [|])",
    "require Not Nil": "require.NotNil(t, [|])",
    "require Not Regexp": "require.NotRegexp(t, [|])",
    "require Not Zero": "require.NotZero(t, [|])",
    "require Positive": "require.Positive(t, [|])",
    "require Regexp": "require.Regexp(t, [|])",
    "require Same": "require.Same(t, [|])",
    "require Subset": "require.Subset(t, [|])",
    "require True": "require.True(t, [|])",
    "require Within Duration": "require.WithinDuration(t, [|])",
    "require Within Range": "require.WithinRange(t, [|])",
    "require Zero": "require.Zero(t, [|])",
    #
    "errors new closed": "ocerrors.NewClosed",
    "errors new conflicts": "ocerrors.NewConflicts",
    "errors new already exists": "ocerrors.NewAlreadyExists",
    "errors new not allowed":   "ocerrors.NewNotAllowed",
    "errors new internal"   :   "ocerrors.NewInternal",
    "errors new invalid input"  :   "ocerrors.NewInvalidInput",
    "errors new not found"  :   "ocerrors.NewNotFound",
    "errors new invalid request"    :   "ocerrors.NewInvalidRequest",
    "errors new multiple": "ocerrors.NewMultiple",
    "errors new unauthenticated": "ocerrors.NewUnauthenticated",
    "errors new unauthorized": "ocerrors.NewUnauthorized",
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
    # OC
    "mission ID": "mission.ID",
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
