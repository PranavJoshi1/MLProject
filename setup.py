from setuptools import find_packages, setup
from typing import List


HYPEN_E_DOT = '-e .'
def get_requirements(file_path: str) -> List[str]:
    """This Function returns a list of requirements"""
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "")for req in requirements]  # as we do realines, it will add "\n" for every new line to remove it done this
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)   # as we will get error for -e as its not package which require in requirements file to connect setup.py
            
    return requirements 
        

setup(
name = "ML Project",
version= "0.0.1",
author= "Pranav",
author_email= "joshipranavc@gmail.com",
packages= find_packages(),
#install_requires = ['pandas', 'numpy', 'seaborn'] or as we require number of packages we create function

install_requires = get_requirements("requirements.txt")
)