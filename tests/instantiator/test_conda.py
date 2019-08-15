from grumble.models import environment, package
from grumble.instantiators import conda
from tempfile import gettempdir
from unittest import TestCase

import os
import shutil


class TestCondaInstatniator(TestCase):

    def setUp(self):
        self.prefix = gettempdir()
        os.makedirs(self.prefix)

    def tearDown(self):
        shutil.rmtree(self.prefix)

    def test_install(self):
        conda_packages = [
            package.CondaPackage("imagesize", "1.1.0", "py37_0", "pkgs/main", "osx-64"),
            package.CondaPackage("scikit-learn", "0.21.2", "py37hebd9d1a_0", "pkgs/main", "osx-64")

        ]

        pip_packages = []
        config = environment.Config(channels="defaults")
        env = environment.Environment(conda_packages, pip_packages, config)

        conda_instantiator = conda.CondaEnvironmentProvider(env)
        conda_instantiator.install(self.prefix)