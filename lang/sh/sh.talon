title: /.sh$/
-
standard header: "#!/bin/bash\nset -euo pipefail\n"
check argument count: user.insert_fancy('[ $# -ne [|] ] && {{ echo "Usage: "; exit 1; }}')

iffae:
    "if ; thenfi"
    key(left:2 enter up end left:6)
for loop:
    "for  in ; dodone"
    key(left:4 enter up end left:8)
while loop:
    "while ; dodone"
    key(left:4 enter up end left:4)
while read:
    "while read line; dodone"
    key(left:4 enter:2 up)
case when:
    "case  inesac"
    key(left:4 enter up end left:3)

create function [<phrase>]$:
    "{user.snake(phrase or '')}() {}"
    key(left enter)

lodge (folder | directory) exists: user.insert_fancy("[ -d [|] ]")
lodge file exists: user.insert_fancy("[ -f [|] ]")
lodge not file exists: user.insert_fancy("[ ! -f [|] ]")
lodge file executable: user.insert_fancy("[ -x [|] ]")
lodge file not executable: user.insert_fancy("[ ! -x [|] ]")

lodge file older: user.insert_fancy("[ [|] -ot  ]")
lodge file newer: user.insert_fancy("[ [|] -nt  ]")

lodge string zero: user.insert_fancy("[ -z [|] ]")
lodge string (exists | set | non zero): user.insert_fancy("[ -n [|] ]")

lodge equal: user.insert_fancy("[ [|] -eq  ]")
lodge not equal: user.insert_fancy("[ [|] -ne  ]")
lodge less than: user.insert_fancy("[ [|] -lt  ]")
lodge less equal: user.insert_fancy("[ [|] -le  ]")
lodge greater than: user.insert_fancy("[ [|] -gt  ]")
lodge greater equal: user.insert_fancy("[ [|] -ge  ]")

lodge three exists: user.insert_fancy("[ aws s3api head-object --bucket ${{S3_BUCKET}} --key ${{S3_KEY}} ]")
lodge not three exists: user.insert_fancy("[ ! aws s3api head-object --bucket ${{S3_BUCKET}} --key ${{S3_KEY}} ]")
