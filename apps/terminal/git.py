from talon import *


mod = Module()
ctx = Context()


mod.list("git_commands")
ctx.lists["user.git_commands"] = {
    "cherry pick abort": "cherry-pick --abort",
    "delete branch": "branch -D ",
    "new branch": "checkout -b ",
    "add": "add ",
    "add all": "add -A",
    "add force": "add -f ",
    "remove": "rm ",
    "remove cashed": "rm --cached ",
    "branch set upstream": "branch --set-upstream-to=",
    "branch": "branch ",
    "branch remotes": "branch -r ",
    "bisect start": "bisect start",
    "bisect good": "bisect good ",
    "bisect bad": "bisect bad ",
    "bisect reset": "bisect reset ",
    "bisect": "bisect ",
    "checkout develop": "checkout develop@",
    "checkout master": "checkout master@",
    "checkout upstream develop": "checkout upstream/develop@",
    "checkout": "checkout ",
    "checkout track": "checkout --track ",
    "cherry pick": "cherry-pick ",
    "commit amend": "commit --amend ",
    "commit all": 'commit -a -m "[|]"',
    "commit all and push": 'git commit -a -m "[|]" && git push',
    "commit": 'commit -m "[|]"',
    "commit fix up": "commit --fixup ",
    "diff": "diff ",
    "diff staged": "diff --staged ",
    "discard": "checkout -- ",
    "discard all": "reset --hard",
    "reset hard": "reset --hard",
    "fetch upstream": "fetch upstream ",
    "fetch upstream and pull": "fetch upstream && git pull",
    "fetch origin": "fetch origin ",
    "fetch origin and pull": "fetch origin && git pull",
    "fetch": "fetch ",
    "gooey blame": "gui blame PATH",
    "init": "init ",
    "log": "log ",
    "merge tool": "mergetool ",
    "merge": "merge ",
    "merge abort": "merge --abort ",
    "merge continue": "merge --continue ",
    "pull": "pull ",
    "publish": "push -u origin ",
    "push set upstream origin": "push --set-upstream origin ",
    "push": "push ",
    "push force": "push --force ",
    "rebase master": "rebase master",
    "rebase": "rebase",
    "rebase auto squash": "rebase -i --autosquash master",
    "rebase interactive": "rebase -i ",
    "remote": "remote ",
    "remote remove": "remote remove ",
    "remote prune origin": "remote prune origin ",
    "remote prune origin dry run": "remote prune origin --dry-run",
    "remote set url": "remote set-url ",
    "remote rename": "remote rename ",
    "remove branch": "branch -d ",
    "reset": "reset ",
    "show remotes": "remote -v @",
    "stash branch": "stash branch NAME",
    "stash list": "stash list",
    "stash": "stash ",
    "stash pop": "stash pop ",
    "subversion": "svn ",
    "subversion clone": "svn clone ",
    "subversion fetch": "svn fetch ",
    "subversion rebase": "svn rebase ",
    "status": "status@",
    "tag": "tag ",
    "unstage": "reset -- ",
}