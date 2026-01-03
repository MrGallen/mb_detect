from setuptools import setup
import pathlib

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name='mb_detect', 
    version='0.1.2',
    description='A smart serial port detector for BBC micro:bit',
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/mrgallen/mb_detect", # Update this if you have a github
    author="Eoin Gallen",
    email="egallen@sainteunans.com"
    license="MIT",
    py_modules=['mb_detect'],
    install_requires=['pyserial'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
