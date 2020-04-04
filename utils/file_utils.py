from itertools import islice
from git import Repo
import re

pattern = re.compile(r"[A-Z][a-z]*|[a-z]+|\d")
def create_spoken_forms(symbols, max_len=3):
    return [" ".join(list(islice(pattern.findall(s), max_len))) for s in symbols]
MAX = 100

def get_directory_map(current_path):
    directories = [p.name for p in islice(current_path.iterdir(), MAX) if p.is_dir()]
    spoken_forms = create_spoken_forms(directories)
    return dict(zip(spoken_forms, directories))

def get_file_map(current_path):
    files = [p for p in islice(current_path.iterdir(), MAX) if p.is_file()]
    spoken_forms = create_spoken_forms([p.stem for p in files])
    return dict(zip(spoken_forms, [f.name for f in files]))

def get_git_info(current_path):
    try:
        repo = Repo(current_path)
    except:
        return {}, {}, {}
    # git_dir = current_path / ".git"
    # if  not git_dir.is_dir():
    #     return {}, {}

    # remotes_dir = git_dir / "refs" / "remotes"
    # remote_names = [d.name for d in remotes_dir.iterdir() if d.is_dir()]
    remote_names = [r.name for r in repo.remotes]
    remotes = dict(zip(create_spoken_forms(remote_names), remote_names))

    # branches_dir = git_dir / "refs" / "heads"
    # branch_names = [d.name for d in branches_dir.iterdir()]
    branch_names = [h.name for h in repo.heads]
    branches = dict(zip(create_spoken_forms(branch_names), branch_names))

    file_names = [f.a_path for f in repo.index.diff(None)]
    file_names.extend(repo.untracked_files)
    files = dict(zip(create_spoken_forms(file_names), file_names))

    return branches, remotes, files