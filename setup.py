from setuptools import find_packages, setup


setup(
    python_requires='>=2.7',
    name='base-api-client',
    version='1.1.0',
    description='Base API Client',
    install_requires=[
        'cached-property>=1.4,<2',
        'requests>=2.18,<3',
    ],
    packages=find_packages(
        exclude=['tests', '*.tests', '*.tests.*', 'tests.*']
    )
)
