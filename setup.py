from setuptools import find_packages, setup
from typing import List

HyphenEdot= '-e .'

def get_requirements(file_path:str)->List[str]:

    requirements=[]
    with open(file_path) as fileobj:
        requirements= fileobj.readlines()
        requirements= [req.replace('\n','') for req in requirements]
    
        if HyphenEdot in requirements:
            requirements.remove(HyphenEdot) # as this is only to trigger setup.py, not any package to be installed.
    return requirements

setup(
    name='mlproject',
    version= '0.0.1',
    author='Suraj',
    packages= find_packages(),
    install_requires= get_requirements('requirements.txt')
)