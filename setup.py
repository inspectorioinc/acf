import os
import re

from setuptools import find_packages, setup

PACKAGE_NAME = 'acf'


def get_version():
    init_path = os.path.join(
        os.path.abspath(os.path.dirname(__file__)), PACKAGE_NAME, '__init__.py'
    )
    with open(init_path) as init_file:
        return re.search(
            r"^__version__ = '(?P<version>.*?)'.*$",
            init_file.read(), re.MULTILINE
        ).group('version')


setup(
    python_requires='>=2.7',
    name=PACKAGE_NAME,
    version=get_version(),
    description='API Client Framework',
    install_requires=[
        'cached-property>=1.4,<2',
        'six>=1.9.0',
        'requests>=2.18,<3',
    ],
    packages=find_packages(
        exclude=['tests', '*.tests', '*.tests.*', 'tests.*']
    )
)
