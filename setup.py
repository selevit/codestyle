#!/usr/bin/env python
# coding: utf-8

from setuptools import setup, find_packages

setup(
    name='codestyle',
    version='0.0.9',
    author=u'Sergey Levitin',
    author_email='selevit@gmail.com',
    packages=find_packages(),
    url='https://github.com/selevit/codestyle',
    license='GPL licence, see LICENCE',
    description='Extendable codestyle checker and fixer',
    long_description=open('README.md').read(),
    scripts=['scripts/codestyle'],
    install_requires=['pep8', 'autopep8', 'pylint']
)
