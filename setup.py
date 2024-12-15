from setuptools import setup
from typing import List

Hyphen_e_dot = "-e ."
def get_requirements(filepath)->List[str]:

    """
    This function takes in a filepath, reads lines from the file and returns a list.

    """

    with open(filepath, "r") as obj:
        requirements=obj.readlines()
        requirements=[line.replace("\n", "") for line in requirements]

    if Hyphen_e_dot in requirements:
        requirements.remove(Hyphen_e_dot)
    
    return requirements

    setup(
        name = "consumer_finance",
        version = "0.0.1",
        author = "mbali094",
        author_email = "mbalinene094@gmail.com",
        packages=find_packages(),
        install_requires = get_requirements("requirements.txt")
    )