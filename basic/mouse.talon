# mouse_click(button: int = 0, down: bool = None, up: bool = None, hold: int = None)
#   Click, hold, or release a mouse button
copy mouse position: user.copy_mouse_position()
copy mouse relative: user.copy_mouse_position_relative_window()

shifty:
    key(shift:down)
    mouse_click()
    key(shift:up)
colic:
    key(ctrl:down)
    mouse_click()
    key(ctrl:up)
mouse alt click:
    key(alt:down)
    mouse_click()
    key(alt:up)
millick:
    mouse_click(2)
kick:
    mouse_click()
kick double:
    mouse_click()
    mouse_click()
squat:
    user.mouse_drag()
bench:
    user.mouse_release()