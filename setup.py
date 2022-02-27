import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="Topsis-Archit-101903054",
    version="1.1.0",
    description="Calculates TOPSIS on the given dataset!",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Snehil-21/Topsis-Snehil-101903064",
    author="Archit Kapoor",
    author_email="architkapoor13@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    packages=["Topsis"],
    include_package_data=True,
    install_requires=['pandas'],
    entry_points={
        "console_scripts": [
            "Topsis=Topsis.__main__:main",
        ]
    },
)