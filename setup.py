from setuptools import setup, find_packages

def get_requirements(file_path: str) -> list[str]:
    '''
    This function will return the list of requirements.
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]
        
    return requirements

setup(
    name='machine learning',
    version='0.0.1',
    author='Abutalha Shaikh',
    author_email='abutalha11503@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)