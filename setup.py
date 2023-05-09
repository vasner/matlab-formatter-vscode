from setuptools import find_packages, setup

setup(
    name="matlab-formatter",
    version="0.1.0",
    packages=find_packages(exclude=["contrib", "docs", "tests"]),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "matlab-formatter = matlab_formatter.matlab_formatter:main",
        ],
    },
)