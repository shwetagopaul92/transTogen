'''
transTogen setup module
'''

from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='transTogen',
    version='0.1.0',
    description='Python command line tool to translate trancript coordinates \
                    genomic coordinates',
    author='Shweta Gopaulakrishnan',
    author_email='shwetagopaul92@gmail.com',
    keywords='Translate transcript coordintaes to genomic coordinates',
    packages=find_packages(),
    install_requires=['argparse'],
    extras_require={},
    package_data={},
    entry_points={
        'console_scripts': [
            'transTogen=transTogen.run_transTogen:main',
        ],
    }
)
