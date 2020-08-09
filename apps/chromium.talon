app: brave.exe
app: chrome.exe
-
<user.numberth> tab: key("ctrl-{numberth}")
new tab <user.n20>: key("ctrl-t:{n20}")
duplicate tab: key(alt-shift-d)
go <user.websites>:
    key(ctrl-l)
    sleep(20ms)
    insert(websites)
    key(enter)
new incognito window: key("ctrl-shift-n")
next tab <user.n20>: key("ctrl-tab:{n20}")
previous tab <user.n20>: key("ctrl-shift-tab:{n20}")
close tab <user.n20>: user.slow_key("ctrl-w:{n20}", "100ms")
reopen tab <user.n20>: key("ctrl-shift-t:{n20}")
page back <user.n20>: key("alt-left:{n20}")
page forward <user.n20>: key("alt-right:{n20}")
zoom reset: key(ctrl-0)
refresh: key(ctrl-f5)
[find] next match <user.n20>: key("ctrl-g:{n20}")
[find] previous match <user.n20>: key("ctrl-shift-g:{n20}")
[toggle] caret browsing: key(f7)
home page: key(alt-home)
show history:
    key(ctrl-t)
    "brave://history/"
    key(enter)
google search: key(ctrl-l)
copy path: key(ctrl-l ctrl-c escape)
image search:
    key(ctrl-l left)
    "https://www.google.com/searchbyimage?&image_url="
    key(enter)
science hub:
    key(ctrl-l left)
    sleep(20ms)
    "https://sci-hub.tw/"
    key(enter)
show downloads: key(ctrl-j)
add bookmark: key(ctrl-d)
bookmark all tabs: key(ctrl-shift-d)
[toggle] bookmark bar: key(ctrl-shift-b)
show bookmarks: key(ctrl-shift-o)
switch user: key(ctrl-shift-m)
brave task manager: key(shift-escape)
[toggle] full screen: key(f11)
focus notification: key(alt-n)
allow notification: key(alt-shift-a)
deny notification: key(alt-shift-a)
developer tools: key(f12)
view [page] source: key(ctrl-u)
