from talon import speech_system, ui, cron, registry, Module

in_command_context = False

mod = Module()
mod.tag("command_mode")

def check_context():
    global in_command_context
    if speech_system.engine and speech_system.engine.name == "dragon":
        if "user.command_mode" in registry.tags:
            if in_command_context: return
            speech_system.engine_mimic("switch to command mode")
            in_command_context = True
        else:
            if not in_command_context: return
            speech_system.engine_mimic("switch to normal mode")
            in_command_context = False

cron.interval("1s", check_context)
