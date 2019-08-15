import copy


class Environment(object):

    def __init__(self, path, conda_packages, pip_packages, config):
        self.path = path
        self.conda_packages = conda_packages
        self.pip_packages = pip_packages
        self.config = config

    def serialize(self, fn, filetype="yaml"):
        pass

    def load(self, fn):
        pass


class Config(object):
    def __init__(self, channels, channel_alias, pinned_packages, default_channels,
                 channel_priority, track_features, subdirs):
        self.channels = channels
        self.channel_alias = channel_alias
        self.pinned_packages = pinned_packages
        self.default_channels = default_channels
        self.channel_priority = channel_priority
        self.tracked_features = track_features
        self.subdirs = subdirs

