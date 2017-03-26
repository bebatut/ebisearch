import os
from setuptools import find_packages,setup

setup(
    name = "ebisearch",
    version = "0.0.1",
    author = "Bérénice Batut",
    author_email = "berenice.batut@gmail.com",
    description = ("A Python library for interacting with EBI Search's API"),
    license = "MIT",
    keywords = "api api-client ebi",
    url = "https://github.com/bebatut/ebisearch",
    packages=find_packages(),
    entry_points={
          'console_scripts': [
              'ebisearch = ebisearch.__main__:main'
          ]
      },
    install_requires=[
        'Click',
    ],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Web Environment",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering"
    ],
)