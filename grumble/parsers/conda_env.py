from .interface import ParserInterface
from ..models.environment import Environment


class CondaEnvParser(ParserInterface):
    def __init__(self):
        pass

    def parse(self, env_file):
        return Environment(path=None, conda_packages=None, pip_packages=None)
