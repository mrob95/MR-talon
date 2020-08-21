tag: terminal
-
git cherry pick abort: "git cherry-pick --abort"
git delete branch: "git branch -D "
git new branch: "git checkout -b "
git add: "git add "
git add all: "git add -A"
git add force: "git add -f "
git remove: "git rm "
git remove cashed: "git rm --cached "
git branch set upstream: "git branch --set-upstream-to="
git branch: "git branch "
git branch remotes: "git branch -r "
git bisect start: "git bisect start"
git bisect good: "git bisect good "
git bisect bad: "git bisect bad "
git bisect reset: "git bisect reset "
git bisect: "git bisect "
git checkout develop:
	"git checkout develop"
	key(enter)
git checkout master:
	"git checkout master"
	key(enter)
git checkout upstream develop:
	"git checkout upstream/develop"
	key(enter)
git checkout: "git checkout "
git checkout track: "git checkout --track "
git cherry pick: "git cherry-pick "
git clone:
	"git clone "
	user.insert_git_url()
git commit amend: "git commit --amend "
git commit all:
	'git commit -a -m ""'
	key(left)
git commit all and push:
	'git commit -a -m "" && git push'
	key(left:13)
git commit:
	'git commit -m ""'
	key(left)
git commit fix u: "git commit --fixup "
git create ignore: "curl https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore > .gitignore"
git diff: "git diff "
git diff staged: "git diff --staged "
git discard: "git checkout -- "
git (discard all | reset hard): "git reset --hard"
git fetch upstream: "git fetch upstream "
git fetch upstream and pull: "git fetch upstream && git pull"
git fetch origin: "git fetch origin "
git fetch origin and pull: "git fetch origin && git pull"
git fetch: "git fetch "
git gooey blame: "git gui blame PATH"
git hub: "git https://github.com/"
git init: "git init "
git log: "git log "
git merge tool: "git mergetool "
git merge: "git merge "
git merge abort: "git merge --abort "
git merge continue: "git merge --continue "
git pull: "git pull "
git publish: "git push -u origin "
git push set upstream origin: "git push --set-upstream origin "
git push: "git push "
git push force: "git push --force "
git rebase master: "git rebase master"
git rebase: "git rebase"
git rebase auto squash: "git rebase -i --autosquash master"
git rebase interactive: "git rebase -i "
git remote: "git remote "
git remote remove: "git remote remove "
git remote add:
	"git remote add "
	user.insert_git_url()
	key(home right:15)
git remote add origin:
	"git remote add origin "
	user.insert_git_url()
git remote add upstream:
	"git remote add upstream "
	user.insert_git_url()
git remote prune origin: "git remote prune origin "
git remote prune origin dry run: "git remote prune origin --dry-run"
git remote set url: "git remote set-url "
git remote rename: "git remote rename "
git remove branch: "git branch -d "
git reset: "git reset "
git show remotes:
	"git remote -v "
	key(enter)
git stash branch: "git stash branch NAME"
git stash list: "git stash list"
git stash: "git stash "
git stash pop: "git stash pop "
git subversion: "git svn "
git subversion clone: "git svn clone "
git subversion fetch: "git svn fetch "
git subversion rebase: "git svn rebase "
git status:
	"git status"
	key(enter)
git tag: "git tag "
git unstage: "git reset -- "
