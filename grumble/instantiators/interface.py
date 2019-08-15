class EnvironmentProviderInterface(object):
    def install(self, prefix):
        raise NotImplementedError

    def freeze(self, subdir=None):
        raise NotImplementedError

    def post_apply_steps(self):
        raise NotImplementedError

