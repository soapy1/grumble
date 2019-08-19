from abc import ABC, abstractmethod
from conda.models.match_spec import MatchSpec


class Package(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def to_matchspec(self):
        return MatchSpec(self.name)


class CondaPackage(Package):

    def __init__(self, name, version=None, build_string=None, channel=None, subdir=None):
        super(CondaPackage, self).__init__(name)
        self.version = version
        self.build_string = build_string
        self.channel = channel
        self.subdir = subdir

    def to_matchspec(self):
        match_spec_dict = {}
        if self.version:
            match_spec_dict['version'] = self.version
        if self.build_string:
            match_spec_dict['build_string'] = self.build_string
        if self.channel:
            match_spec_dict['channel'] = self.channel
        if self.subdir:
            match_spec_dict['subdir'] = self.subdir

        return MatchSpec(name=self.name, **match_spec_dict)


class PipPackage(Package):

    def __init__(self, name, version=None):
        super(PipPackage, self).__init__(name)
        self.version = version

    def to_matchspec(self):
        match_spec_dict = {}
        if self.version:
            match_spec_dict['version'] = self.version
        return MatchSpec(name=self.name, **match_spec_dict)