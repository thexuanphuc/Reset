from setuptools import find_packages
from setuptools import setup

setup(
    name='rbpler_interfaces',
    version='0.0.0',
    packages=find_packages(
        include=('rbpler_interfaces', 'rbpler_interfaces.*')),
)
