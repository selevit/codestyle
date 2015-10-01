# coding: utf-8

from distutils.core import setup

setup(
    name='codestyle',
    version='0.0.1',
    author=u'Sergey Levitin',
    author_email='selevit@gmail.com',
    packages=['codestyle'],
    package_dir={'codestyle': 'codestyle'},
    url='https://github.com/selevit/codestyle',
    license='GPL licence, see LICENCE.txt',
    description='Extendable codestyle checker and fixer',
    long_description=open('README.md').read(),
    scripts=['codestyle/codestyle.py']
)
