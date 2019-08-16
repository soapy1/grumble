from grumble.models import environment, package
from grumble.instantiators import conda
import tempfile
from unittest import TestCase

import shutil


class TestCondaInstatniator(TestCase):

    def setUp(self):
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_install(self):
        conda_packages = [
            package.CondaPackage("imagesize", "1.1.0", "py37_0", "defaults", "osx-64"),
            package.CondaPackage("scikit-learn", "0.21.2", "py37hebd9d1a_0", "defaults", "osx-64")
        ]
        pip_packages = []
        config = environment.Config(channels=["defaults"], subdirs=["osx-64", "noarch"])
        env = environment.Environment(conda_packages, pip_packages, config)
        conda_instantiator = conda.CondaEnvironmentProvider(env)
        conda_instantiator.install(self.test_dir)