"""
Utilities
"""
import yaml

from config import PythonPath, Config

def load(filename: str) -> Config:
    config: Config
    with open(filename, "r") as f:
        obj_str = "".join(f.readlines())
        config = yaml.load(obj_str, yaml.FullLoader)

    return config


def dump(filename: str, config: Config) -> None:
    obj_str = yaml.dump(config)
    with open(filename, "w") as f:
        f.write(obj_str)
