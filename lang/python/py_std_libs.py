from talon import *

mod = Module()
ctx = Context("python")
ctx.matches = r"""
tag: user.python
"""

mod.list("py_lib_re")
ctx.lists["user.py_lib_re"] = {
    "ascii": "re.ASCII!",
    "debug": "re.DEBUG!",
    "dotall": "re.DOTALL!",
    "ignorecase": "re.IGNORECASE!",
    "locale": "re.LOCALE!",
    "multiline": "re.MULTILINE!",
    "match": "re.Match",
    "pattern": "re.Pattern",
    "regex flag": "re.RegexFlag",
    "scanner": "re.Scanner",
    "template": "re.TEMPLATE!",
    "unicode": "re.UNICODE!",
    "verbose": "re.VERBOSE!",
    "compile": "re.compile",
    "copyreg": "re.copyreg!",
    "enum": "re.enum!",
    "error": "re.error",
    "escape": "re.escape",
    "find all": "re.findall",
    "find iter": "re.finditer",
    "full match": "re.fullmatch",
    "func tools": "re.functools!",
    "match": "re.match",
    "purge": "re.purge",
    "search": "re.search",
    "split": "re.split",
    "SRE compile": "re.sre_compile!",
    "SRE parse": "re.sre_parse!",
    "sub": "re.sub",
    "sub N": "re.subn",
    "template": "re.template",
}

mod.list("py_lib_sys")
ctx.lists["user.py_lib_sys"] = {
    "api version": "sys.api_version!",
    "arg vee": "sys.argv!",
    "base exec prefix": "sys.base_exec_prefix!",
    "base prefix": "sys.base_prefix!",
    "breakpoint hook": "sys.breakpointhook",
    "builtin module names": "sys.builtin_module_names!",
    "byte order": "sys.byteorder!",
    "call tracing": "sys.call_tracing",
    "callstats": "sys.callstats",
    "copyright": "sys.copyright!",
    "display hook": "sys.displayhook",
    "DLL handle": "sys.dllhandle!",
    "dont write bytecode": "sys.dont_write_bytecode!",
    "exception info": "sys.exc_info",
    "except hook": "sys.excepthook",
    "exec prefix": "sys.exec_prefix!",
    "executable": "sys.executable!",
    "exit": "sys.exit",
    "flags": "sys.flags!",
    "float info": "sys.float_info!",
    "float repr style": "sys.float_repr_style!",
    "get async gen hooks": "sys.get_asyncgen_hooks",
    "get coroutine origin tracking depth": "sys.get_coroutine_origin_tracking_depth",
    "get coroutine wrapper": "sys.get_coroutine_wrapper",
    "get allocated blocks": "sys.getallocatedblocks",
    "get check interval": "sys.getcheckinterval",
    "get default encoding": "sys.getdefaultencoding",
    "get filesystem encode errors": "sys.getfilesystemencodeerrors",
    "get filesystem encoding": "sys.getfilesystemencoding",
    "get profile": "sys.getprofile",
    "get recursion limit": "sys.getrecursionlimit",
    "get ref count": "sys.getrefcount",
    "get size of": "sys.getsizeof",
    "get switch interval": "sys.getswitchinterval",
    "get trace": "sys.gettrace",
    "get windows version": "sys.getwindowsversion",
    "hash info": "sys.hash_info!",
    "hex version": "sys.hexversion!",
    "implementation": "sys.implementation!",
    "int info": "sys.int_info!",
    "intern": "sys.intern",
    "is finalizing": "sys.is_finalizing",
    "max size": "sys.maxsize!",
    "max unicode": "sys.maxunicode!",
    "meta path": "sys.meta_path!",
    "modules": "sys.modules!",
    "path": "sys.path!",
    "path hooks": "sys.path_hooks!",
    "path importer cache": "sys.path_importer_cache!",
    "platform": "sys.platform!",
    "prefix": "sys.prefix!",
    "set async gen hooks": "sys.set_asyncgen_hooks",
    "set coroutine origin tracking depth": "sys.set_coroutine_origin_tracking_depth",
    "set coroutine wrapper": "sys.set_coroutine_wrapper",
    "set check interval": "sys.setcheckinterval",
    "set profile": "sys.setprofile",
    "set recursion limit": "sys.setrecursionlimit",
    "set switch interval": "sys.setswitchinterval",
    "set trace": "sys.settrace",
    "standard error": "sys.stderr!",
    "standard in": "sys.stdin!",
    "standard out": "sys.stdout!",
    "thread info": "sys.thread_info!",
    "version": "sys.version!",
    "version info": "sys.version_info!",
    "warn options": "sys.warnoptions!",
    "win version": "sys.winver!",
}

mod.list("py_lib_os")
ctx.lists["user.py_lib_os"] = {
    "dir entry": "os.DirEntry",
    "f ok": "os.F_OK!",
    "mutable mapping": "os.MutableMapping",
    "O append": "os.O_APPEND!",
    "O binary": "os.O_BINARY!",
    "O creat": "os.O_CREAT!",
    "O excl": "os.O_EXCL!",
    "O noinherit": "os.O_NOINHERIT!",
    "O random": "os.O_RANDOM!",
    "O rdonly": "os.O_RDONLY!",
    "O rdwr": "os.O_RDWR!",
    "O sequential": "os.O_SEQUENTIAL!",
    "O short lived": "os.O_SHORT_LIVED!",
    "O temporary": "os.O_TEMPORARY!",
    "O text": "os.O_TEXT!",
    "O trunc": "os.O_TRUNC!",
    "O wronly": "os.O_WRONLY!",
    "p detach": "os.P_DETACH!",
    "p no wait": "os.P_NOWAIT!",
    "p no waito": "os.P_NOWAITO!",
    "p overlay": "os.P_OVERLAY!",
    "p wait": "os.P_WAIT!",
    "path like": "os.PathLike",
    "r ok": "os.R_OK!",
    "seek cur": "os.SEEK_CUR!",
    "seek end": "os.SEEK_END!",
    "seek set": "os.SEEK_SET!",
    "tmp max": "os.TMP_MAX!",
    "w ok": "os.W_OK!",
    "x ok": "os.X_OK!",
    "abc": "os.abc!",
    "abort": "os.abort",
    "access": "os.access",
    "altsep": "os.altsep!",
    "chdir": "os.chdir",
    "chmod": "os.chmod",
    "close": "os.close",
    "closerange": "os.closerange",
    "cpu count": "os.cpu_count",
    "curdir": "os.curdir!",
    "defpath": "os.defpath!",
    "device encoding": "os.device_encoding",
    "devnull": "os.devnull!",
    "dup": "os.dup",
    "dup two": "os.dup2",
    "environ": "os.environ!",
    "error": "os.error",
    "execl": "os.execl",
    "execle": "os.execle",
    "execlp": "os.execlp",
    "execlpe": "os.execlpe",
    "execv": "os.execv",
    "execve": "os.execve",
    "execvp": "os.execvp",
    "execvpe": "os.execvpe",
    "extsep": "os.extsep!",
    "FD open": "os.fdopen",
    "FS decode": "os.fsdecode",
    "FS encode": "os.fsencode",
    "FS path": "os.fspath",
    "F stat": "os.fstat",
    "F sync": "os.fsync",
    "F truncate": "os.ftruncate",
    "get exec path": "os.get_exec_path",
    "get handle inheritable": "os.get_handle_inheritable",
    "get inheritable": "os.get_inheritable",
    "get terminal size": "os.get_terminal_size",
    "get cwd": "os.getcwd",
    "get cwdb": "os.getcwdb",
    "get env": "os.getenv",
    "get login": "os.getlogin",
    "get pid": "os.getpid",
    "get P pid": "os.getppid",
    "is atty": "os.isatty",
    "kill": "os.kill",
    "linesep": "os.linesep!",
    "link": "os.link",
    "listdir": "os.listdir",
    "L seek": "os.lseek",
    "L stat": "os.lstat",
    "make dirs": "os.makedirs",
    "make dir": "os.mkdir",
    "name": "os.name!",
    "open": "os.open",
    "par dir": "os.pardir!",
    "path": "os.path!",
    "path sep": "os.pathsep!",
    "pipe": "os.pipe",
    "P open": "os.popen",
    "put env": "os.putenv",
    "read": "os.read",
    "read link": "os.readlink",
    "remove": "os.remove",
    "remove dirs": "os.removedirs",
    "rename": "os.rename",
    "renames": "os.renames",
    "replace": "os.replace",
    "rmdir": "os.rmdir",
    "scandir": "os.scandir",
    "sep": "os.sep!",
    "set handle inheritable": "os.set_handle_inheritable",
    "set inheritable": "os.set_inheritable",
    "spawnl": "os.spawnl",
    "spawnle": "os.spawnle",
    "spawnv": "os.spawnv",
    "spawnve": "os.spawnve",
    "st": "os.st!",
    "start file": "os.startfile",
    "stat": "os.stat",
    "stat result": "os.stat_result",
    "stat vfs result": "os.statvfs_result",
    "string error": "os.strerror",
    "supports bytes environ": "os.supports_bytes_environ!",
    "supports dir fd": "os.supports_dir_fd!",
    "supports effective ids": "os.supports_effective_ids!",
    "supports fd": "os.supports_fd!",
    "supports follow symlinks": "os.supports_follow_symlinks!",
    "symlink": "os.symlink",
    "sys": "os.sys!",
    "system": "os.system",
    "terminal size": "os.terminal_size",
    "times": "os.times",
    "times result": "os.times_result",
    "truncate": "os.truncate",
    "U mask": "os.umask",
    "U name result": "os.uname_result",
    "unlink": "os.unlink",
    "U random": "os.urandom",
    "U time": "os.utime",
    "wait pid": "os.waitpid",
    "walk": "os.walk",
    "write": "os.write",
}