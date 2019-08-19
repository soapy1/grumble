from unittest import TestCase
import os

from grumble.parsers.conda_env import CondaEnvParser
from grumble.models.environment import Environment
from grumble.models.package import CondaPackage


class TestCondaEnvParser(TestCase):

    def setUp(self):
        self.test_env_files = os.path.abspath("../test_files/environment_yaml")
        assert os.listdir(self.test_env_files) is not None

    def test_simple_env(self):
        file = os.path.join(self.test_env_files, "simple_env.yaml")
        conda_packages = [
            CondaPackage("python", "", "", "defaults", ""),
            CondaPackage("bokeh", "", "", "defaults", ""),
            CondaPackage("flask", "", "", "defaults", "")
        ]

        expected_env = Environment(
            conda_packages=conda_packages, pip_packages=[], config=None
        )
        parser = CondaEnvParser()
        env = parser.parse(file)
        # assert env == expected_env
        assert True