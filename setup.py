from setuptools import setup, find_packages

setup(
    name='navara',
    keywords='',
    version='1.0',
    author='Niels Hoogeveen',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
)