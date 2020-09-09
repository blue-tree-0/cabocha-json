#!/usr/bin/env python

from setuptools import setup, find_packages


def load_requires(filename):
    return open(filename).read().splitlines()


setup(
    name="cabocha-json",
    packages=find_packages(),
    install_requires=load_requires("requirements.txt"),
    version="0.1.0",
    license="MIT",
    description="Cabocha-json saves the output of cabocha to a json file.",
    author="blue",
    url="https://github.com/blue-tree-0",
)
