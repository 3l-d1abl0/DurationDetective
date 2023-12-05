import pathlib
from setuptools import setup, find_packages 

from durationdetective import __version__

HERE = pathlib.Path().cwd()
DESCRIPTION = HERE.joinpath("README.md").read_text()
VERSION = __version__
REQUIREMENTS = HERE.joinpath("requirements.txt").read_text().splitlines()


setup(
    include_package_data=True,
    name="duration-detective",
    version=VERSION,
    description="A Tree like tool to generate directory tree diagrams for media files in folders and Subfolders",
    long_description=DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/3l-d1abl0/DurationDetective",
    author="Sameer Barha",
    author_email="sameer.barha12@gmail.com",
    maintainer="Sameer Barha",
    maintainer_email="sameer.barha12@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
    ],
    packages=find_packages(include=['durationdetective']),
    install_requires=REQUIREMENTS,
    entry_points={
        "console_scripts": [
            "DurationDetective=durationdetective.__main__:main",
        ]
    },
)