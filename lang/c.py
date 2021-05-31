from talon import ui, Module, Context, registry, actions, imgui, cron

mod = Module()
ctx = Context("C")
ctx.matches = r"""
title: /.*\.c/
title: /.*\.cpp/
title: /.*\.h/
"""

@ctx.action_class("user")
class Actions:
    def lang_print(s: str):
        actions.insert(f'printf("{s}: %s", {s});')


ctx.lists["user.functions"] = {
    "file open": "fopen",
    "file seek": "fseek",
    "file seek end": "fseek([|], 0, SEEK_END);",
    "file close": "fclose",
    "file read": "fread",
    "rewind": "rewind",
    "free": "free",
    "exit": "exit",
    "mallock": "malloc",
    "mem copy": "memcpy",
    "mem char": "memchr",
    "mem compare":  "memcmp",
    "mem move": "memmove",
    "mem set": "memset",
    "print": 'printf("[|]\\n");',
    "size of": "sizeof",
    "string length": "strlen",
    "string copy": "strcpy",
    "string cat": "strcat",
    "string N cat": "strncat",
    "string char": "strchr",
    "string compare": "strcmp",
    "string N compare": "strncmp",
    "string N copy": "strncpy",
    "string string": "strstr",
    "string token": "strtok",
    "string transform": "strxfrm",
    # CPP stdlib

    # STB data structures
    "array length": "arrlen", # the length of the dynamic array
    "array length unsigned": "arrlenu", # the length of the dynamic array as an unsigned type
    "array put": "arrput", # copy an object into the dynamic array
    "array free": "arrfree", # free the entire array
    "array add N": "arraddn", # adds n uninitialized values to the dynamic array
    "array set length": "arrsetlen", # sets the length of the array (leaves new slots uninitialized)
    "array last": "arrlast", # the last item in the array as an lvalue
    "array insert": "arrins", # inserts an item in the middle of the array
    "array delete": "arrdel", # deletes an item from the middle of the array, moving the following items over
    "array swap delete": "arrswapdel", # deletes an item from the middle of the array, replacing it with the formerly last item
    "array capacity": "arrcap", # returns the internal capacity, the maximum length the array can be without reallocating it
    "array set capacity": "arrsetcap", # sets the internal capacity. it is not possible to shrink the capacity (currently)
    "hash length": "hmlen", # The length of the hashmap array data for iterating the hashmap contents
    "hash free": "hmfree", # The length of the hashmap array data for iterating the hashmap contents
    "hash length unsigned": "hmlenu", # As above, but unsigned
    "hash get": "hmget", # Get the value corresponding to a key, or return the default
    "hash gets": "hmgets", # Get the value corresponding to a key, or return the default
    "hash get index": "hmgeti", # Return the index into the array of a given key, or -1
    "hash put": "hmput", # Update an existing key,value pair, or add a new one if the key isn't present
    "hash puts": "hmputs", # Update an existing structure, or add a new one if the key isn't present
    "hash delete": "hmdel", # Delete a key,value pair if the key is present
    "hash default": "hmdefault", # Set the default value used by hmget
    "hash defaults": "hmdefaults", # Set the default struct used by hmget
    "hash string length": "shlen", # The length of the hashmap array data for iterating the hashmap contents
    "hash string length unsigned": "shlenu", # As above, but unsigned
    "hash string get": "shget", # Get the value corresponding to a key, or return the default
    "hash string gets": "shgets", # Get the value corresponding to a key, or return the default
    "hash string get index": "shgeti", # Return the index into the array of a given key, or -1
    "hash string put": "shput", # Update an existing key,value pair, or add a new one if the key isn't present
    "hash string puts": "shputs", # Update an existing structure, or add a new one if the key isn't present
    "hash string delete": "shdel", # Delete a key,value pair if the key is present
    "hash string default": "shdefault", # Set the default value used by hmget
    "hash string defaults": "shdefaults", # Set the default struct used by hmget
    "hash string new arena": "sh_new_arena", # Overwrites pointer with a new hashmap using a string arena for string management
    "hash string new string duplicate": "sh_new_strdup", # Overwrites pointer with a new hashmap using strdup for string management
    "hash string alloc": "stbds_stralloc", # Allocates a string in a string arena
    "hash string reset": "stbds_strreset", # Frees all the strings in a string arena
}

ctx.lists["user.logicals"] = {
    "and": " && ",
    "or": " || ",
}

mod.list("c_types")
ctx.lists["user.c_types"] = {
    # Ray tracing
    "vector three": "vec3",
    "point three": "point3",
    "colour": "colour",
    "ray": "ray",
    #
    "auto": "auto",
    "inline": "inline",
    "boolean": "bool",
    "constant": "const",
    "double": "double",
    "float": "float",
    "integer": "int",
    "file": "FILE",
    "unsigned": "unsigned",
    "void": "void",
    "struct": "struct",
    "size": "size_t",
    "enum": "enum",
    "char star": "char *",
}

mod.list("c_type_modifiers")
ctx.lists["user.c_type_modifiers"] = {
    "static": "static",
    "inline": "inline",
    "virtual": "virtual",
    "constant": "const",
}

@mod.capture(rule="[{user.c_type_modifiers}+] {user.c_types} [(star | value)]")
def c_type(m) -> str:
    """A C type, e.g. static inline int *"""
    result = m["c_types"]
    if hasattr(m, "c_type_modifiers_list"):
        modifiers = " ".join(m["c_type_modifiers_list"]) + " "
    else:
        modifiers = ""
    if m._words[-1] == "star":
        end = " *"
    elif m._words[-1] == "value":
        end = "& "
    else:
        end = " "
    return f"{modifiers}{result}{end}"

mod.list("cpp_std")
ctx.lists["user.cpp_std"] = {
    "C error": "cerr",
    "C out": "cout",
    "end line": "endl",
    "flush": "flush",
    "square root": "sqrt",
    "shared pointer": "shared_ptr",
    "make shared": "make_shared",
    "numerical limits": "numeric_limits",
    "oh stream": "ostream",
    "vector": "vector",
}