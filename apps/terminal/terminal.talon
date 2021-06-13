app: mintty.exe
app: WindowsTerminal.exe
app: /.*/
and title: /MSYS:.*/

app: Visual Studio Code
and user.vs_terminal: True
-
tag(): user.terminal
tag(): user.command_mode
CD {user.directories}:
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
#------------------------------------------------------
bash: "bash "
cancel: key(ctrl-c)
CD up:
    "cd .."
    key(enter)
CD: "cd "
curly: "curl "
greppy: "grep "
greppy recursive: "grep -R "
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
SSH kali: "ssh -p 3022 mrob@172.30.1.3"
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
python 3: "python3 "
python 2: "python27 "
python 3 debug: "python3 -m pdb "
python 3 pytest: "python3 -m pytest "
python 2 pytest: "python27 -m pytest "
python 2 64: "C:/Python27-64/python.exe "
python 3 32: "C:/Python38-32/python.exe "
python 2 pip install: "python27 -m pip install "
python 3 pip install: "python3 -m pip install "
pip install: "pip install "
upgrade pip: "--upgrade pip"
pip two (install | build) package: "pip2 install -e ."
pie test: "pytest "
pie flakes: "pyflakes "
eye python: "ipython "
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
