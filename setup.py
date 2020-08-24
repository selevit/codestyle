#!/usr/bin/env python
"""Setup."""
from setuptools import find_packages, setup

setup(
    name='codestyle',
    version='2.1.0',
    author=u'Sergey Levitin',
    author_email='selevit@gmail.com',
    packages=find_packages(),
    package_data={
        'codestyle': ['standards/*'],
    },
    include_package_data=True,
    zip_safe=False,
    url='https://github.com/webpp-studio/codestyle',
    license='GPLv3',
    description='Extendable codestyle checker and fixer',
    long_description=open('README.rst').read(),
    scripts=['scripts/codestyle'],
    install_requires=[
        'future~=0.17.1',
        'pep8~=1.7.1',
        'pyflakes~=2.1.1',
        'autopep8~=1.4.4',
        'flake8~=3.7.9',
        'flake8-annotations-complexity~=0.0.2',
        'flake8-broken-line~=0.1.1',
        'flake8-bugbear~=19.8.0',
        'flake8-comprehensions~=2.2.0',
        'flake8-debugger~=3.1.0',
        'flake8-docstrings~=1.5.0',
        'pydocstyle~=4.0.1',
        'flake8-eradicate~=0.2.2',
        'flake8-executable~=2.0.3',
        'flake8-print~=3.1.0',
        'flake8-string-format~=0.2.3',
        'flake8_builtins~=1.4.1',
        'flake8_commas~=2.0.0',
        'flake8_pep3101~=1.2.1',
        'flake8_quotes~=2.1.0',
        'flake8-bandit~=2.1.2',
        'flake8-logging-format~=0.6.0',
        'mccabe~=0.6.1',
        'pep8-naming~=0.8.2',
        'pycodestyle~=2.5.0',
        'pyflakes~=2.1.1',
        'radon~=2.4.0',
        'flake8-rst-docstrings~=0.0.11',
        'autoflake~=1.3.1',
    ],
    test_suite='tests',
    tests_require=[
        'mock~=3.0.5',
        'six~=1.12.0',
    ],
    classifiers=[
        'Development Status :: 6 - Beta',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Quality Assurance',

        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
