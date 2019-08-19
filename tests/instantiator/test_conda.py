from ..utils import package_is_installed

from grumble.models import environment, package
from grumble.instantiators import conda

import tempfile
import shutil
from unittest import TestCase
from conda_env import pip_util


class TestCondaInstatniator(TestCase):

    def setUp(self):
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_install_just_conda(self):
        conda_packages = [
            package.CondaPackage("imagesize", "1.1.0", "py37_0", "defaults", "osx-64"),
            package.CondaPackage("scikit-learn", "0.21.2", "py37hebd9d1a_0", "defaults", "osx-64")
        ]
        pip_packages = []
        config = environment.Config(channels=["defaults"], subdirs=["osx-64", "noarch"])
        env = environment.Environment(conda_packages, pip_packages, config)
        conda_instantiator = conda.CondaEnvironmentProvider(env)
        conda_instantiator.install(self.test_dir)
        for pkg in conda_packages:
            assert package_is_installed(self.test_dir, pkg.to_matchspec(), False)

    def test_install_conda_and_pip(self):
        conda_packages = [
            package.CondaPackage("imagesize", "1.1.0", "py37_0", "defaults", "osx-64"),
        ]
        pip_packages = [
            package.PipPackage("flask", "1.1.1")
        ]
        config = environment.Config(channels=["defaults"], subdirs=["osx-64", "noarch"])
        env = environment.Environment(conda_packages, pip_packages, config)
        conda_instantiator = conda.CondaEnvironmentProvider(env)
        conda_instantiator.install(self.test_dir)
        for pkg in conda_packages:
            assert package_is_installed(self.test_dir, pkg.to_matchspec(), False)
        for pkg in pip_packages:
            pip_list = pip_util.pip_subprocess(["list"], self.test_dir, None).lower()
            assert pkg.name in pip_list
            assert pkg.version in pip_list