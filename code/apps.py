from talon import Module

mod = Module()
apps = mod.apps

apps.chromium = """
app.exe: brave.exe
app.exe: chrome.exe
"""

apps.vscode = """
app.name: Visual Studio Code
app.exe: Code.exe
"""

apps.windows_explorer = """
os: windows
app.name: /.*/
and title: /(Save|Open|Browse|Select)/
app.name: Windows Explorer
app.exe: explorer.exe
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
