from .interface import ParserInterface
from ..models.environment import Environment
from ..models.package import CondaPackage, PipPackage

from conda.common.serialize import yaml_load_safe


class CondaEnvParser(ParserInterface):
    def __init__(self):
        pass

    def parse(self, env_file):
        with open(env_file, 'r') as f:
            env_yaml = yaml_load_safe(f)

        conda_packages = []
        pip_packages = []
        for dep in env_yaml.get("dependencies"):
            if type(dep) is str:
                conda_packages.append(CondaPackage(dep))
            elif type(dep) is dict and dep.get("pip"):
                for pip_dep in dep.get("pip"):
                    pip_packages.append(PipPackage(pip_dep))

        return Environment(
            conda_packages=conda_packages, pip_packages=pip_packages, config=None
        )
