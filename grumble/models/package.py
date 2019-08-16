from abc import ABC, abstractmethod
from conda.models.match_spec import MatchSpec


class Package(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def to_matchspec(self):
        return MatchSpec(self.name)


class CondaPackage(Package):

    def __init__(self, name, version, build_string, channel, subdir):
        super(CondaPackage, self).__init__(name)
        self.version = version
        self.build_string = build_string
        self.channel = channel
        self.subdir = subdir

    def to_matchspec(self):
        return MatchSpec(
            name=self.name, version=self.version, build=self.build_string,
            channel=self.channel, subdir=self.subdir
        )


class PipPackage(Package):

    def __init__(self, name, version):
        super(PipPackage, self).__init__(name)
        self.version = version

    def to_matchspec(self):
        return MatchSpec(name=self.name, version=self.version)