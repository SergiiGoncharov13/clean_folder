from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version= '1.0.1',
    description='tools for clean folder',
    long_description=open('README.md').read(),
    url='p',
    autor='sergii',
    license='MIT',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['clean-folder=clean_folder.main:clean_folder']}
)



