from .interface import EnvironmentProviderInterface


class PipEnvironmentProvider(EnvironmentProviderInterface):

    def install(self, prefix):
        raise NotImplementedError

    def freeze(self, subdir=None):
        if subdir:
            print("Warning: subdir setting does nothing with pip.  For OS-specific resolution, try conda instead.")

    def post_apply_steps(self):
        raise NotImplementedError
