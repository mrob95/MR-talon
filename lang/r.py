from user.imports import *
from subprocess import Popen

BINDINGS = utilities.load_toml_relative("config/r.toml")


ctx = Context("R")
ctx.matches = r"""
title: /.*\.r$/
title: /.*\.R$/
app: RStudio
"""

commands = BINDINGS["commands"]
functions = BINDINGS["r_functions"]
graphs = BINDINGS["r_graph"]
cheatsheets = BINDINGS["cheatsheets"]

def r_func(data):
    if isinstance(data, str):
        return [f"{data}()", Key("left")]
    else:
        return [f"{data[0]}({data[1]})", Key(("left "*int(data[2])).strip())]

ctx.commands = {
    # **{k: actions.Alternating(v) for k, v in commands.items()},
    # **{f"fun {k}": r_func(v) for k, v in functions.items()},
    # **{f"graph {k}": r_func(v) for k, v in graphs.items()},
    # **{f"library {k}": f"library({v})" for k, v in graphs.items()},
    **{f"cheatsheet {k}": lambda m: Popen(["SumatraPDF", f"%USERPROFILE%/Documents/cheatsheets/R/{v}.pdf"]) for k, v in cheatsheets.items()},
}

ctx.lists["functions"] = {
    "anti join": "anti_join",
    "arrange": "arrange",
    "as character": "as.character",
    "as date": "as.Date",
    "as data frame": "as.data.frame",
    "as tibble": "as_tibble",
    "as double": "as.double",
    "as factor": "as.factor",
    "as numeric": "as.numeric",
    "bind rows": "bind_rows",
    "cable": "kable",
    "case when": "case_when",
    "count": "count",
    "covariance": "cov",
    "correlation": "cor",
    "distinct": "distinct",
    "describe": "describe",
    "drop NA": "drop_na",
    "eigen": "eigen",
    "everything": "everything",
    "filter": "filter",
    "full join": "full_join",
    "gather": "gather",
    "get working directory": "getwd",
    "set working directory": "setwd",
    "glimpse": "glimpse",
    "group by": "group_by",
    "head": "head",
    "if else": "ifelse",
    "inner join": "inner_join",
    "install packages": "install.packages",
    "is NA": "is.na",
    "(isn't | is not) NA": "!is.na",
    "left join": "left_join",
    "length": "length",
    "library": "library",
    "list": "list",
    "(LM | linear model)": "lm",
    "log": "log",
    "M table": "mtable",
    "make directory": "dir.create",
    "map": "map",
    "margins": "margins",
    "max": "max",
    "min": "min",
    "mean": "mean",
    "mutate": "mutate",
    "names": "names",
    "nest": "nest",
    "paste": "paste0",
    "print": "print",
    "read CSV": "read_csv",
    "read E views": "readEViews",
    "read excel": "read_xlsx",
    "read RDS": "read_rds",
    "rename": "rename",
    "rename all": "rename_all",
    "repeat": "rep",
    "reorder": "reorder",
    "right join": "right_join",
    "sequence": "seq",
    "semi join": "semi_join",
    "select": "select",
    "select all": "select_all",
    "scale": "scale",
    "starts with": "starts_with",
    "string contains": "str_detect",
    "string detect": "str_detect",
    "string replace": "str_replace",
    "string replace all": "str_replace_all",
    "subset": "subset",
    "sum": "sum",
    "summarise": "summarise",
    "summary": "summary",
    "tail": "tail",
    "tidy": "tidy",
    "tibble": "tibble",
    "trim white space": "trimws",
    "type [of]": "typeof",
    "ungroup": "ungroup",
    "unique": "unique",
    "vector": "c",
    "view": "View",
    "vee table": "vtable",
    "write RDS": "write_rds",
    "write CSV": "write_csv",
    "ex table": "xtable",
    "un nest": "unnest",
}

ctx.lists["logicals"] = {
    "and": " & ",
    "in": " %in% ",
    "or": " | ",
}

ctx.lists["r_graph"] = {
    "(coordinates | coord) fixed": "coord_fixed",
    "[geom] column": "geom_col",
    "[geom] density": "geom_density",
    "[geom] histogram": "geom_histogram",
    "[geom] label": "geom_label",
    "[geom] line": "geom_line",
    "[geom] path": "geom_path",
    "[geom] point": "geom_point",
    "[geom] polygon": "geom_polygon",
    "[geom] smooth": "geom_smooth",
    "[geom] text": "geom_text",
    "[GG] plot": "ggplot",
    "aesthetics": "aes",
    "element blank": "element_blank",
    "error bar": "errorbar",
    "facet grid": "facet_grid",
    "facet wrap": "facet_wrap",
    "highlight": "gghighlight",
    "save": "ggsave",
    "scale colour continuous": "scale_color_continuous",
    "scale colour discrete": "scale_color_discrete",
    "scale ex continuous": "scale_x_continuous",
    "scale ex discrete": "scale_x_discrete",
    "scale why continuous": "scale_y_continuous",
    "scale why discrete": "scale_y_discrete",
    "theme minimal": "theme_minimal",
    "theme": "theme",
}

ctx.lists["r_graph_misc"] = {
    "labels": "labs(x = \"\",\ny = \"\",\ntitle = \"\",\nsubtitle = \"\",\ncaption = \"\")",
    "remove legend": "theme(legend.position = \"none\")",
    "viridis": "scale_color_viridis(discrete=TRUE)",
}

ctx.lists["r_libraries"] = {
    "cable": "kable",
    "car": "car",
    "dev tools": "devtools",
    "gap minder": "gapminder",
    "[gee] animate": "gganimate",
    "[gee] highlight": "gghighlight",
    "[gee] map": "ggmap",
    "[gee] repel": "ggrepel",
    "grid extra": "gridExtra",
    "knitter": "knitr",
    "LM test": "lmtest",
    "margins": "margins",
    "psych": "psych",
    "stargazer": "stargazer",
    "tidy verse": "tidyverse",
    "vee table": "vtable",
    "viridis": "viridis",
}