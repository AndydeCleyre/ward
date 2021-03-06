import platform

from setuptools import setup

description = "A modern Python 3 test framework for finding and fixing flaws faster."

# Work around encoding errors when installing on Windows.
with open("README.md", "r") as fh:
    if platform.system() != "Windows":
        long_description = fh.read()
    else:
        long_description = description

exec(open("ward/_ward_version.py").read())

setup(
    name="ward",
    version=__version__,  # noqa
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://github.com/darrenburns/ward",
    author="Darren Burns",
    author_email="darrenb900@gmail.com",
    license="MIT",
    packages=["ward"],
    python_requires=">=3.6",
    entry_points={"console_scripts": ["ward=ward.run:run"]},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Quality Assurance",
        "Topic :: Software Development :: Testing",
    ],
    install_requires=[
        "colorama>=0.3.3",
        "termcolor>=1.1.0",
        "dataclasses>=0.1; python_version < '3.7'",
        "click>=7.0",
    ],
)
