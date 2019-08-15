from .interface import EnvironmentProviderInterface

import conda
import copy


class CondaEnvironmentProvider(EnvironmentProviderInterface):
    def __init__(self, *args, **kw):
        self.channels = kw.get('channels')
        self.pinned_packages = kw.get('pinned_packages')
        self.default_channels = kw.get('default_channels')
        self.channel_priority = kw.get('channel_priority')
        self.track_features = kw.get('track_features')
        self.subdirs = kw.get('subdirs')
        self.channel_alias = kw.get('channel_alias')
        self.frozen = kw.get('frozen', False)
        self.specs = kw.get('packages', tuple())

    def install(self, prefix):
        frozen_env = self
        if not self.frozen:
            frozen_env = self.freeze()
        conda.api.install(self.specs, prefix)
        return frozen_env

    def freeze(self, subdir=None):
        new_obj = copy.deepcopy(self.__dict__())
        # solve for specs with given info
        new_obj['packages'] = conda.api.solve()
        new_obj['frozen'] = True
        return CondaEnvironmentProvider(**new_obj)

    def merge(self, other):
        """Inheritance.

        Keys from other are inherited.
            * Any list values are extended, with the list from other appended to the list from self
            * Any string or numeric key from other is clobbered by the same key from self

        Only one level is allowed, but you can stack arbitrarily."""
        merged = copy.deepcopy(self.__dict__())
        for k, v in other.__dict__():
            if k in merged and getattr(self, k):
                if isinstance(v, (string_types, bool)):
                    pass
                else:
                    list_of_stuff = merged.get(k, [])
                    for entry in v:
                        if entry not in list_of_stuff:
                            list_of_stuff.append(entry)
                    merged[k] = list_of_stuff
            else:
                merged[k] = v
        return CondaEnvironmentProvider(**merged)

    def env_vars(self):
        pass
