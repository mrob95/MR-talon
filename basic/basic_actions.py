from talon import Context, actions
ctx = Context()

@ctx.action_class('edit')
class EditActions:
    def undo(): actions.key('ctrl-z')
    def paste(): actions.key('ctrl-v')
    def copy(): actions.key('ctrl-c')
    def line_insert_down(): actions.key('ctrl-enter')
    def line_clone():
        actions.key('home shift-end ctrl-c end enter ctrl-v')
        actions.sleep('50ms')
