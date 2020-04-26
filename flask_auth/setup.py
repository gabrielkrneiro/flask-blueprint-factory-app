from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...

setup(
    name="Flask Auth",
    version="0.0.1",
    author="Gabriel Carneiro",
    author_email="carneiro.development@gmail.com",
    description=("Flask project to demonstrate the Factory App and Blueprint usage"),
    license="GNU",
    packages=["flask_auth", "tests"],
    install_requires=["poetry"],
    zip_safe=False,
)
