from .parsers import conda_env, conda_txt, pipfile


class CondaEnvironment(object):
    def __init__(self, file, parser, instantiator, modifier):
        self.parser = parser
        self.instantiator = instantiator
        self.modifier = modifier
        # TODO: choose parser
        self.environment_model = conda_env.CondaEnvParser().parse(file)

    def create_environment(self, prefix=None):
        if prefix is not None:
            self.environment_model.path = prefix
        self.instantiator.install(self.environment_model)
        self.modifier.run(self.environment_model.path)
