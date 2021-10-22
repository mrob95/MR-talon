from talon import ui, Module, Context, registry, actions, imgui, cron
from user.lang.terraform.aws import DATA, RESOURCES

mod = Module()
ctx = Context()

ctx.matches = r"""
title: /.*\.tf/
"""

mod.list("tf_aws_data")
ctx.lists["user.tf_aws_data"] = DATA
mod.list("tf_aws_resources")
ctx.lists["user.tf_aws_resources"] = RESOURCES

ctx.lists["user.values"] = {
    "false": "false",
    "null": "null",
    "true": "true",
}

ctx.lists["user.logicals"] = {
    "and": " && ",
    "or": " || ",
    "in": " in ",
    "for": "for ",
    "if": " if ",
}

ctx.lists["user.functions"] = {
    # https://www.terraform.io/docs/language/functions
    # Numeric functions
    "absolute": "abs",
    "ceiling": "ceil",
    "floor": "floor",
    "log": "log",
    "min": "min",
    "max": "max",
    "parse int": "parseint",
    "power": "pow",
    "sign": "signum",
    # String functions
    "chomp": "chomp",
    "format": "format",
    "format list": "formatlist",
    "indent": "indent",
    "join": "join",
    "lower": "lower",
    "regex": "regex",
    "regex all": "regexall",
    "replace": "replace",
    "split": "split",
    "string reverse": "strrev",
    "substring": "substr",
    "title": "title",
    "trim": "trim",
    "trim prefix": "trimprefix",
    "trim suffix": "trimsuffix",
    "trim space": "trimspace",
    "upper": "upper",
    # Collections functions
    "all true": "alltrue",
    "any true": "anytrue",
    "chunk list": "chunklist",
    "coalesce": "coalesce",
    "coalesce list": "coalescelist",
    "compact": "compact",
    "concat": "concat",
    "contains": "contains",
    "distinct": "distinct",
    "element": "element",
    "flatten": "flatten",
    "index": "index",
    "keys": "keys",
    "length": "length",
    "list": "list",
    "lookup": "lookup",
    "map": "map",
    "match keys": "matchkeys",
    "merge": "merge",
    "one": "one",
    "range": "range",
    "reverse": "reverse",
    "set intersection": "setintersection",
    "set product": "setproduct",
    "set subtract": "setsubtract",
    "set union": "setunion",
    "slice": "slice",
    "sort": "sort",
    "sum": "sum",
    "transpose": "transpose",
    "values": "values",
    "zip map": "zipmap",
    # Encoding functions
    "base sixty four decode": "base64decode",
    "base sixty four encode": "base64encode",
    "base sixty four gee zip": "base64gzip",
    "csv decode": "csvdecode",
    "json decode": "jsondecode",
    "json encode": "jsonencode",
    "text decode base sixty four": "textdecodebase64",
    "text encode base sixty four": "textencodebase64",
    "url encode": "urlencode",
    "yaml decode": "yamldecode",
    "yaml encode": "yamlencode",
    # Filesystem functions
    "abs path": "abspath",
    "deer name": "dirname",
    "directory name": "dirname",
    "path expand": "pathexpand",
    "base name": "basename",
    "file": "file",
    "file exists": "fileexists",
    "file set": "fileset",
    "file base sixty four": "filebase64",
    "template file": "templatefile",
    # Date and Time Functions
    "format date": "formatdate",
    "time add": "timeadd",
    "time stamp": "timestamp",
    # Hash and Crypto Functions
    "base sixty four sha 256": "base64sha256",
    "base sixty four sha 512": "base64sha512",
    "be crypt": "bcrypt",
    "file base sixty four sha 256": "filebase64sha256",
    "file base sixty four sha 512": "filebase64sha512",
    "file M D five": "filemd5",
    "file sha 1": "filesha1",
    "file sha 256": "filesha256",
    "file sha 512": "filesha512",
    "M D five": "md5",
    "RSA decrypt": "rsadecrypt",
    "sha 1": "sha1",
    "sha 256": "sha256",
    "sha 512": "sha512",
    "UUID": "uuid",
    "UUID v5": "uuidv5",
    # IP Network Functions
    "cider host": "cidrhost",
    "cider net mask": "cidrnetmask",
    "cider subnet": "cidrsubnet",
    "cider subnets": "cidrsubnets",
    # Type Conversion Functions
    "can": "can",
    "defaults": "defaults",
    "non sensitive": "nonsensitive",
    "sensitive": "sensitive",
    "to bool": "tobool",
    "to list": "tolist",
    "to map": "tomap",
    "to number": "tonumber",
    "to set": "toset",
    "to string": "tostring",
    "try": "try",
}