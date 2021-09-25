from setuptools import find_packages, setup

from liquiditypy.version import __version__

setup(
    name="liquiditypy",
    author="J. Floth",
    version=__version__,
    url="https://github.com/flothjl/",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "web3",
        "click"
    ]
)
