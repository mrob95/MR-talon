from talon import Module

mod = Module()
apps = mod.apps

apps.chromium = """
app.exe: brave.exe
app.exe: chrome.exe
"""

apps.firefox = """
os: windows
and app.name: Firefox
os: windows
and app.exe: firefox.exe
"""

# app.name: Visual Studio Code
apps.vscode = """
app.exe: Code.exe
"""

apps.windows_explorer = """
os: windows
and app.name: /.*/
and title: /(Save|Open|Browse|Select)/
os: windows
and app.exe: explorer.exe
os: windows
and app.name: Windows Explorer
"""

apps.windows_command_processor = """
os: windows
and app.name: Windows Command Processor
os: windows
and app.exe: cmd.exe
"""

apps.windows_terminal = """
os: windows
and app.exe: WindowsTerminal.exe
"""

apps.windows_power_shell = """
os: windows
and app.exe: powershell.exe
"""
