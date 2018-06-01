from setuptools import setup, find_packages


setup(
    python_requires='>=2.7',
    name='base-api-client',
    version='1.0.0',
    description='Base API Client',
    install_requires=[
        'cached-property==1.4.2',
        'requests==2.18.4',
    ],
    packages=find_packages(
        exclude=['tests', '*.tests', '*.tests.*', 'tests.*', ]
    )
)
