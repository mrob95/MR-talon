tag: user.mouse_grid_enabled
-
M grid:
    user.grid_select_screen(1)
    user.grid_activate()

grid win:
    user.grid_place_window()
    user.grid_activate()

grid <user.digits>:
    user.grid_activate()
    user.grid_narrow_list(digits)
