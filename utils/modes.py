# from dragonfly import Mimic, Playback, AppContext, Window, get_engine
# import natlink

# class ModeManager():
#     def __init__(self):
#         self.mode = "normal"
#         self.frequency = 5
#         self.command_titles = ["sublime", "jupyter", "rstudio", "mingw64", "lyx", "scientific notebook"]
#         self.command_executables = ["code.exe", "kindle.exe"]
#         self.command_contexts = AppContext(title=self.command_titles) | AppContext(self.command_executables)
#         self.timer = get_engine().create_timer(self.check_context, self.frequency)

#     def switch_mode(self, mode="command"):
#         Playback([([mode, "mode", "on"], 0.0)]).execute()
#         self.mode = mode

#     def check_context(self):
#         if natlink.getMicState() == "on":
#             w = Window.get_foreground()
#             should_be_command = self.command_contexts.matches(w.executable, w.title, w.handle)
#             if should_be_command and self.mode == "normal":
#                 self.switch_mode("command")
#             elif not should_be_command and self.mode == "command":
#                 self.switch_mode("normal")
#             else:
#                 pass

# mm = ModeManager()
