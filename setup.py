from setuptools import find_packages, setup

setup(
    name="ebisearch",
    version="0.0.1",
    author="Berenice Batut",
    author_email="berenice.batut@gmail.com",
    description=("A Python library for interacting with EBI Search's API"),
    license="MIT",
    keywords="api api-client ebi",
    url="https://github.com/bebatut/ebisearch",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'ebisearch = ebisearch.__main__:main'
        ]
      },
    scripts=['ebi_metagenomics'],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Web Environment",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6"
    ],
    extras_require={
        'testing': ["pytest"],
    },
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    install_requires=[
        'requests',
        'Click',
        'flake8'],
    include_package_data=True,
    package_data={'ebisearch_data': ['ebisearch_data/*.json']}
)
