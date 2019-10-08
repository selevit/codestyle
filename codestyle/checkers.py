#!/usr/bin/env python
from __future__ import absolute_import
from builtins import object

import os
import subprocess
from subprocess import STDOUT
from abc import ABCMeta, abstractmethod

from .result import Result, ResultSet
from .settings import parser
from future.utils import with_metaclass


DEVNULL = open(os.devnull, 'wb')


class BaseChecker(with_metaclass(ABCMeta, object)):
    """
    Base codestyle checker
    """

    def __init__(self, application, **kwargs):
        self.application = application
        self.extra = kwargs

    @abstractmethod
    def get_check_commands(self):
        """
        List of check commands
        """

        return []

    def get_fix_commands(self):
        """
        List of fix commands
        """

        raise NotImplementedError('')

    def exe(self, alias):
        """
        Get checker executable name
        """

        return self.application.settings.CHECKER_EXE[alias]

    def cfg(self, checker):
        """
        Get checker config path
        """

        return self.application.get_config_path(
            self.application.settings.CHECKER_CFG[checker]
        )

    def make_result(self, command, files):
        """
        Make checking result from command
        """

        if not isinstance(files, (list, tuple)):
            files = [files]
        command_args = list(command) + list(files)
        kwargs = {'stderr': STDOUT}
        if self.application.params.compact:
            kwargs['stdout'] = DEVNULL
        p = subprocess.Popen(command_args, **kwargs)
        output = p.communicate()[0]
        return Result(files, p.returncode, output)

    def check(self, files):
        """
        Check files
        """

        results = ResultSet()
        for command in self.get_check_commands():
            result = self.make_result(command, files)
            results.add(result)
        return results

    def fix(self, files):
        """
        Fix files
        """

        results = ResultSet()
        for command in self.get_fix_commands():
            results.add(self.make_result(command, files))
        return results


class JSChecker(BaseChecker):
    """
    Javascript code checker
    """

    def get_check_commands(self):
        return (
            (self.exe('jscs'), '--config', self.cfg('jscs')),
            (self.exe('jshint'), '--config', self.cfg('jshint')),
        )

    def get_fix_commands(self):
        return (
            (self.exe('jscs'), '--fix', '--config', self.cfg('jscs')),
        )


class PHPChecker(BaseChecker):
    """
    PHP code checker
    """

    def get_check_commands(self):
        return (
            (self.exe('phpcs'), '--standard=' + self.cfg('phpcs'),
             '--encoding=' + parser.get('phpcs', 'encoding'),
             '--runtime-set', 'ignore_warnings_on_exit', 'true',
             ),
        )

    def get_fix_commands(self):
        return (
            (self.exe('phpcbf'), '--standard=' + self.cfg('phpcs'),
             '--encoding=' + parser.get('phpcs', 'encoding'),
             '--runtime-set', 'ignore_warnings_on_exit', 'true',
             ),
        )


class PythonChecker(BaseChecker):
    """
    Python code checker
    """

    def get_check_commands(self):
        return (
            (self.exe('flake8'), '--config=' + self.cfg('flake8')),
        )

    def get_fix_commands(self):
        return (
            (self.exe('autopep8'), '--in-place', '--aggressive'),
            (self.exe('autoflake'), '--in-place', '--remove-unused-variables'),
        )


class LessChecker(BaseChecker):
    """
    Less and CSS checker
    """

    def get_check_commands(self):
        return (
            (self.exe('csscomb'), '--lint', '--verbose',
             '--config', self.cfg('csscomb')),
        )

    def get_fix_commands(self):
        return (
            (self.exe('csscomb'), '--verbose',
             '--config', self.cfg('csscomb')),
        )


class HTMLChecker(BaseChecker):
    """
    HTML code checker
    """

    def get_check_commands(self):
        return (
            (self.exe('htmlcs'), 'hint',
             '--config', self.cfg('htmlcs')),
        )

    def get_fix_commands(self):
        return (
            (self.exe('htmlcs'), 'format', '--in-place',
             '--config', self.cfg('htmlcs')),
        )
