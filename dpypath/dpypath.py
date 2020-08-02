import os
import sys
from pathlib import Path

from .utils import load

CONFIG_FILE = "dpypath.yml"

PROJECT_ROOT_MARKER = ".git"

def find_project_root() -> str:
    """
    Find project root directory identified by PROJECT_ROOT_MARKER, e.g. ".git"
    :return:
    """
    cwd = os.getcwd()
    path_0: str = Path(cwd).parts[0]
    while cwd != path_0:
        git_dir = os.path.join(cwd, PROJECT_ROOT_MARKER)
        if os.path.exists(git_dir):
            return cwd
        cwd = os.path.dirname(cwd)
    return None

class DPyPath:

    @staticmethod
    def get_python_path(key: str, filename=CONFIG_FILE):
        config = load(filename)
        pass
