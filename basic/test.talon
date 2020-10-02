# test action: user.test_action("")
# test <phrase>: insert(user.formatted_text(phrase, 1, 2))

# test alphabet [{phabet}] {directions}:
#     alphabet = alphabet#     insert("ctrl-{alphabet}{directions}")
mouse test: user.mouse_move_relative(500, 500)