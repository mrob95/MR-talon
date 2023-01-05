tag: user.terminal
-

git {user.git_commands}: user.insert_fancy("git {git_commands}")

git add patch {user.git_status_items} [(and {user.git_status_items})+]:
		items = user.cat(git_status_items_list, "' '")
		user.paste("git add -p '{items}'")

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

# These commands depend on this tool:
# https://github.com/mrob95/talon-git-labeller
git {user.git_status_actions} {user.git_status_items} [(and {user.git_status_items})+]:
	items = user.cat(git_status_items_list, "' '")
	user.paste("git {git_status_actions} '{items}'")
git go {user.git_status_items}: user.cd_directory_of(git_status_items)
git file {user.git_status_items}: "'{git_status_items}'"

git {user.git_branch_actions} {user.git_branch_items} [(and {user.git_branch_items})+]:
	items = user.cat(git_branch_items_list, "' '")
	user.paste("git {git_branch_actions} '{items}'")
git copy branch {user.git_branch_items}:
	clip.set_text(git_branch_items)
	app.notify(git_branch_items)
