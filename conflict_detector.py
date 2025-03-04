import git
import re
from pathlib import Path

def get_conflicted_files(repo_path="."):
    repo = git.Repo(repo_path)
    conflicted_files = []

    for item in repo.index.unmerged_blobs().keys():
        conflicted_files.append(str(Path(repo_path) / item))

    return conflicted_files

def extract_conflicts(file_path):
    with open(file_path, "r") as file:
        content = file.read()

    conflict_pattern = r"<<<<< HEAD(.*?)=====.*?>>>>>>.*?"
    conflicts = re.findall(conflict_pattern, content, re.DOTALL)

    return conflicts
