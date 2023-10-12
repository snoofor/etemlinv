from setuptools import find_packages, setup
from typing import List


const = '-e .'

def get_requirements(file_path:str)->List[str]:
    """
    returns list of requirements
    """
    requirements = []

    with open(file_path) as f_obj:
        requirements = f_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]

        if const in requirements:
            requirements.remove(const)

    return requirements


setup(
    name="invproject",
    version='0.0.1',
    author='Furkan',
    author_email='info@thinkdata.digital',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
    
    )
