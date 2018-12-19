import os
import re

from setuptools import find_packages, setup

PACKAGE_NAME = 'acf'
REPOSITORY_URL = 'https://github.com/inspectorioinc/acf'


def read(*paths):
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), *paths)
    with open(path) as input_file:
        return input_file.read()


def get_version():
    """Get a version string from the source code"""

    return re.search(
        r"^__version__ = '(?P<version>.*?)'.*$",
        read(PACKAGE_NAME, '__init__.py'), re.MULTILINE
    ).group('version')


def get_long_description():
    """Generate a long description from the README file"""

    return read('README.md')


setup(
    name=PACKAGE_NAME,
    url=REPOSITORY_URL,
    version=get_version(),
    description='API Client Framework. '
                'The framework for building well structured '
                'API client libraries in Python.',
    long_description=get_long_description(),
    long_description_content_type='text/markdown',
    author='Inspectorio Developers',
    author_email='developer@inspectorio.com',
    license='MIT',
    install_requires=[
        'cached-property>=1.4,<2',
        'six>=1.9.0',
        'requests>=2.18,<3',
    ],
    python_requires='>=2.7',
    packages=find_packages(
        exclude=['tests', '*.tests', '*.tests.*', 'tests.*']
    ),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: ACF',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    project_urls={
        'Source': REPOSITORY_URL,
        'Tracker': REPOSITORY_URL + '/issues',
    },
)
