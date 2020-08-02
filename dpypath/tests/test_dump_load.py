# https://pyyaml.org/wiki/PyYAMLDocumentation

import sys
import os
import yaml

sys.path.append("..")
from config import PythonPath, Config
from utils import dump, load

os.makedirs("output", exist_ok=True)

filename = "output/config.yml"

def test_save_yaml():
    path_1 = [PythonPath("dep_1", ["lib/py_lib", "graph/ml/lib", "ml/bert/py_lib"]),]
    path_2 = [PythonPath("dep_2", ["simulation/py_lib", "torch/python/lib", "bert/py_lib", "demo/env/lib"]),]
    config = Config([path_1, path_2])
    dump(filename=filename, config=config)
    print("dump completed at %s" % filename)

def test_load_yaml():
    config: Config = load(filename)
    dep: PythonPath
    for dep in config.dependencies:
        print(dep)

    # print(config)

def test_get_pythonpath(id: str) -> str:
    config: Config = load(filename)
    dep: PythonPath
    for dep in config.dependencies:
        print(dep)

if __name__ == "__main__":
    if sys.argv[1] == '1':
        test_save_yaml()
    elif sys.argv[1] == '2':
        test_load_yaml()
    else:
        test_get_pythonpath("dep_1")
        print("---")
        test_get_pythonpath("dep_2")

