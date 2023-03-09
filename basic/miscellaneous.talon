fix clipboard path:
    user.clip_replace("\\\\", "/")
close all notepads: user.kill_notepads()
(view | show) talon log: menu.open_log()

prekris deli: app.notify("lenny")
prekris lease deli: app.notify("penny")

type clipboard: insert(clip.text())

google that:
    text = edit.selected_text()
    user.browser_open("https://www.google.com/search?q={text}")

toggle list info: user.list_info_toggle()
