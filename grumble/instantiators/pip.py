class PipEnvironmentProvider(EnvironmentProviderInterface):
    def install(self):
        pass

    def freeze(self, subdir=None):
        if subdir:
            print("Warning: subdir setting does nothing with pip.  For OS-specific resolution, try conda instead.")
