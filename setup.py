from setuptools import find_packages, setup

setup(
    name="greta",
    packages=find_packages(),
    version="0.1.0",
    description="A library for green computing: execute code at low carbon intensity",
    author="Tom Titcombe",
    license="GPL-3",
    install_requires= ["requests"],
)
