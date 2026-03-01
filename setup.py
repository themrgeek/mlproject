'''
setup.py file is useful to use our project as a package and install it in other environments. It also helps to share our project with others.
In this file we are using setuptools to create a package for our project. 
We are also using a function get_requirements to read the requirements.txt file and return the list of requirements. 
This function will read the requirements.txt file and return the list of requirements. 
We are also using find_packages to find all the packages in our project and include them in our package. 
We are also specifying the name, version, author and author_email of our package. 
Finally we are using install_requires to specify the list of requirements for our package. 
This will help to install the required packages when we install our package using pip.
'''
from setuptools import find_packages, setup
from typing import List
HYPHEN_E_DOT = '-e .'
def get_requirements(file_path)-> List[str]:
    '''This function will return the list of requirements'''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n"," ")for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements
setup(
    name='mlflow-azureml',
    version='0.0.1',
    author='KATHAN PAREKH',
    author_email='parekhkathan8221@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('./requirements.txt'),
)