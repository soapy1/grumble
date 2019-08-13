from setuptools import setup
import versioneer

requirements = [
    # package requirements go here
]

setup(
    name='grumble',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="Grand Unified Model of Base Level Environments",
    author="Anaconda, Inc.",
    author_email='conda@anaconda.com',
    url='https://github.com/msarahan/grumble',
    packages=['grumble'],
    entry_points={
        'console_scripts': [
            'grumble=grumble.cli:cli'
        ]
    },
    install_requires=requirements,
    keywords='grumble',
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
    ]
)
