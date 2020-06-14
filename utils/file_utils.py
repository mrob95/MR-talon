from itertools import islice
# from git import Repo
import re

pattern = re.compile(r"[A-Z][a-z]*|[a-z]+|\d")
def create_spoken_forms(symbols, max_len=3):
    return [" ".join(list(islice(pattern.findall(s), max_len))) for s in symbols]
MAX = 100

# assert create_spoken_forms(["aTest"]) == ["a", "Test"]
# assert create_spoken_forms(["aTest_5"]) == ["a", "Test", "5"]

def get_directory_map(current_path):
    directories = [p.name for p in islice(current_path.iterdir(), MAX) if p.is_dir()]
    spoken_forms = create_spoken_forms(directories)
    return dict(zip(spoken_forms, directories))

def get_file_map(current_path):
    files = [p for p in islice(current_path.iterdir(), MAX) if p.is_file()]
    spoken_forms = create_spoken_forms([p.stem for p in files])
    return dict(zip(spoken_forms, [f.name for f in files]))


def get_children(mod):
    return [s for s in dir(mod) if not s.startswith("_")]

# import re

# print(get_children(re))
# children = get_children(re)
# re_spoken = dict(zip(create_spoken_forms(children), children))
# print(re_spoken)