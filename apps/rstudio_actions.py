from talon import Context, actions
ctx = Context()
ctx.matches = r"""
app: RStudio
"""

@ctx.action_class('edit')
class EditActions:
    def line_insert_down(): actions.key('end enter')
