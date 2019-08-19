from unittest import TestCase
import os

from grumble.parsers.conda_env import CondaEnvParser
from grumble.models.environment import Environment, Config
from grumble.models.package import CondaPackage, PipPackage


class TestCondaEnvParser(TestCase):

    def setUp(self):
        self.test_env_files = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "../test_files/environment_yaml"
        )
        assert os.listdir(self.test_env_files) is not None

    def test_simple_env(self):
        file = os.path.join(self.test_env_files, "simple_env.yaml")
        conda_packages = [
            CondaPackage("python", "", "", "defaults", ""),
            CondaPackage("bokeh", "", "", "defaults", ""),
            CondaPackage("flask", "", "", "defaults", "")
        ]
        config = Config(channels=["defaults"], subdirs=["osx-64", "noarch"])

        expected_env = Environment(
            conda_packages=conda_packages, pip_packages=[], config=config
        )
        parser = CondaEnvParser()
        env = parser.parse(file)
        import ipdb; ipdb.set_trace()
        assert env == expected_env

    def test_env_with_pip(self):
        file = os.path.join(self.test_env_files, "env_with_pip.yaml")
        conda_packages = [
            CondaPackage("python", "3.7", "", "defaults", ""),
            CondaPackage("imagesize", "", "", "defaults", "")
        ]
        pip_packages = [
            PipPackage("flask")
        ]
        config = Config(channels=["defaults"], subdirs=["osx-64", "noarch"])

        expected_env = Environment(
            conda_packages=conda_packages, pip_packages=pip_packages, config=config
        )
        parser = CondaEnvParser()
        env = parser.parse(file)
        assert env == expected_env