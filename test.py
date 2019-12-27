from talon.voice import Context, Key

ctx = Context('hello')
ctx.keymap({
    # 'talon hello world': 'hello world from talon',
    'talon hello world': 'hello from talon',
    'talon alt tab': Key('alt-tab'),
})