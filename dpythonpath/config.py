"""
Dynamic Python Path Configuration Classes
"""
from typing import List

class PythonPath:
    """
    PythonPath
    Define a named pythonpath
    """
    def __init__(self, name: str, pythonpath: List[str]):
        """
        :param name: name of the pythonpath
        :param pythonpath: a list of python path strings, using "/" to separate path
        """
        self.name = name
        self.pythonpath = pythonpath

    def __repr__(self):
        return "%s(name=%r, pythonpath=%r)" % (self.__class__.__name__, self.name, self.pythonpath)


class Config:
    """
    Config
    """
    def __init__(self, dependencies: List[PythonPath]):
        self.dependencies = dependencies

    def __repr__(self):
        return "%s(dependencies=%r)" % (self.__class__.__name__, self.dependencies)
