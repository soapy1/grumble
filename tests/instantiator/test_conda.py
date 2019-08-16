from grumble.models import environment, package
from grumble.instantiators import conda

import tempfile
import shutil
from unittest import TestCase

from conda.models.enums import PackageType
from conda.api import PrefixData
from conda.common.io import dashlist
from conda_env import pip_util


def package_is_installed(prefix, spec, pip=None):
    prefix_recs = tuple(PrefixData(prefix).query(spec))
    if len(prefix_recs) > 1:
        raise AssertionError("Multiple packages installed.%s"
                             % (dashlist(prec.dist_str() for prec in prefix_recs)))
    is_installed = bool(len(prefix_recs))
    if is_installed and pip is True:
        assert prefix_recs[0].package_type in (
            PackageType.VIRTUAL_PYTHON_WHEEL,
            PackageType.VIRTUAL_PYTHON_EGG_MANAGEABLE,
            PackageType.VIRTUAL_PYTHON_EGG_UNMANAGEABLE,
            PackageType.VIRTUAL_PYTHON_EGG_LINK,
        )
    if is_installed and pip is False:
        assert prefix_recs[0].package_type in (
            None,
            PackageType.NOARCH_GENERIC,
            PackageType.NOARCH_PYTHON,
        )
    return is_installed


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