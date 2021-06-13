tag: user.python
and app: vscode
-
for mouse:
    "for  in {user.vscode_grab_mouse()}:"
    key(home right:4)

selfie {user.vscode_members}: "self.{vscode_members}"
selfie {user.vscode_methods}: user.insert_function("self.{vscode_members}")