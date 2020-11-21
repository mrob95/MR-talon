tag: user.terminal
-

git {user.git_commands}: user.insert_fancy("git {git_commands}")

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
git clone:
	"git clone "
	user.insert_git_url()
git create ignore: "curl https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore > .gitignore"