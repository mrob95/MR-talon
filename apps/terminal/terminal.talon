app: mintty.exe
app: WindowsTerminal.exe
app: /.*/
and title: /MSYS:.*/

app: Visual Studio Code
and user.vs_terminal: True
-
tag(): user.terminal
tag(): user.command_mode
(CD | C D | see dee) {user.directories}:
    insert('cd "{directories}" && ls')
    key(enter)
file {user.files}:
    insert('{files} ')
folder {user.directories}:
    insert('{directories}/')
go {user.folders}:
    "cd {folders} && ls"
    key(enter)
dot {user.extensions}:
    ".{extensions}"
maker {user.makefile_targets}:
    "make {makefile_targets}"
#------------------------------------------------------
bash: "bash "
cancel: key(ctrl-c)
(history | page back): key(ctrl-r)
page forward: key(ctrl-s)
see dee up:
    "cd .."
    key(enter)
see dee: "cd "
curly: "curl "
greppy: "egrep "
greppy recursive: "egrep -R "
header: "head "
echo: "echo "
list: "ls "
remove: "rm "
remove recursive: "rm -rf "
line count: "wc -l "
make directory: "mkdir "
move file: "mv "
pipe: " | "
lodge and: " && "
to file: " > "
screen copy: "scrcpy "
android [list] devices: "adb devices -l"
android connect: "adb connect 192.168.0.65:5555"
android disconnect: "adb disconnect 192.168.0.65:5555"
sed replace:
    'sed -i -e "s///g"'
    key(left:4)
sumatra [PDF]: "SumatraPDF "
sublime: "subl -n "
sublime here:
    "subl -n ."
    key(enter)
jupiter notebook: "jupyter notebook"
jupiter lab: "jupyter lab"
youtube download: "youtube-dl -f best "
FFM peg: "ffmpeg "
W get: "wget "
catty: "cat "
explorer here:
    "explorer ."
    key(enter)
code here:
    "code ."
    key(enter)
#------------------------------------------------------
# options
option continue: " --continue "
option abort: " --abort "
option skip: " --skip "
option help: " --help"
option version: " --version"
option {user.alphabet}: " -{alphabet} "
#------------------------------------------------------
PDF LaTeX: "pdflatex "
bib TeX: "bibtex "
pan doc:
    'pandoc  -o '
    key(left:4)
pan doc beamer:
    "pandoc  -t beamer -o "
    key(left:14)
#------------------------------------------------------
# python
python: "python "
python debug: "python -m pdb -c c "
python pytest: "python -m pytest "
pip install: "pip install "
pip install editable: "pip install -e ."
upgrade pip: "--upgrade pip"
pie test: "pytest --pdb "
pie flakes: "pyflakes "
eye python: "ipython "
venv activate: "activate"
venv deactivate: "deactivate"
#------------------------------------------------------
# r
R script:
    "Rscript .r"
    key(left:2)
R markdown:
    "Rscript -e \"rmarkdown::render('.Rmd', clean=TRUE)\""
    key(left:19)
#------------------------------------------------------
# jekyll
jekyll serve watch: "jekyll serve --watch"
jekyll build: "jekyll build"
jekyll: "jekyll "
#------------------------------------------------------
# image
image [magic] trim:
    "convert  -fuzz 1% -trim +repage "
    key(left:24)
image [magic] transparent:
    "convert  -fuzz 1% -transparent white "
    key(left:29)
rename PNG large: "rename 'png_large' 'png' *.png_large"
rename jay peg large: "rename 'jpg_large' 'jpg' *.jpg_large"
# ------------------------------------------------
mux new: key(ctrl-b c)
mux next: key(ctrl-b n)
mux previous: key(ctrl-b p)
mux find: key(ctrl-b f)
mux close: key(ctrl-b &)
mux split: key(ctrl-b %)
mux split horizontal: key(ctrl-b ")
mux swap: key(ctrl-b o)
mux numbers: key(ctrl-b q)
mux kill: key(ctrl-b x)
mux layout: key(ctrl-b space)
mux page up: key(ctrl-b pgup)

complete: key(alt-?)
