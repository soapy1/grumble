import copy


class Environment(object):

    def __init__(self, path, packages):
        self.path = path
        self.packages = packages

    def serialize(self, fn, filetype="yaml"):
        pass

    def load(self, fn):
        pass

