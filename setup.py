from setuptools import find_packages, setup


setup(
    python_requires='>=2.7',
    name='acf',
    version='0.9.0',
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
