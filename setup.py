"""Setup project."""
from setuptools import find_packages, setup

short_desc = "10 Pictures"
long_desc = "Show pictures from your Google Photo Library"

setup(
    name="ten_pics",
    description=short_desc,
    long_description=long_desc,
    author="Vincent Ketelaars",
    author_email="admin@vincentketelaars.nl",
    packages=find_packages(),
)
