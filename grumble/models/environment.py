import copy


class Environment(object):

    def __init__(self, path, conda_packages, pip_packages):
        self.path = path
        self.conda_packages = conda_packages
        self.pip_packages = pip_packages

    def serialize(self, fn, filetype="yaml"):
        pass

    def load(self, fn):
        pass

