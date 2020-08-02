"""
Dynamic Python Path Configuration Classes
"""
from typing import List

PROJECT_ROOT_MARKER = ".git"  # an unique directory name or a file name as project root marker

class PythonPath:
    """
    PythonPath
    Define pythonpaths identified by id
    """
    def __init__(self, id: str, pythonpath: List[str]):
        """
        :param id: id to the list of the pythonpaths
        :param pythonpath: a list of python paths, relative to the project root.
                           use "/" or "\" to separate paths on Unix or Windows
        """
        self.id = id
        self.pythonpath = pythonpath

    def __repr__(self):
        return "%s(id=%r, pythonpath=%r)" % (self.__class__.__name__, self.id, self.pythonpath)


class Config:
    """
    Config
    """
    def __init__(self, dependencies: List[PythonPath], project_root_marker: str = PROJECT_ROOT_MARKER):
        self.dependencies = dependencies
        self.project_root_marker = project_root_marker

    def __repr__(self):
        return "%s(project_root_marker=%r, dependencies=%r)" % \
               (self.__class__.__name__, self.project_root_marker, self.dependencies)
