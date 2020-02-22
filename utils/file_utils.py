import speakit

def get_directory_map(current_path):
    directories = [p.name for p in current_path.iterdir() if p.is_dir()]
    spoken_forms = speakit.split_symbols(directories, max_len=3)
    return dict(zip(spoken_forms, directories))

def get_file_map(current_path):
    files = [p for p in current_path.iterdir() if p.is_file()]
    spoken_forms = speakit.split_symbols([p.stem for p in files], max_len=3)
    return dict(zip(spoken_forms, [f.name for f in files]))