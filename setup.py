import os
from setuptools import setup, find_packages

def get_version():
    version_file = os.path.join(os.path.dirname(__file__), 'DJA_Deployer', '__version__.py')
    with open(version_file) as f:
        exec(f.read())
    return locals()['__version__']


setup(
    name='djad',
    version=get_version(),
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'djad=DJA_Deployer.cli:main',
        ],
    },
)
