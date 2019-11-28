# coding: utf-8
"""Checking result classes."""
from abc import ABCMeta, abstractmethod, abstractproperty
from builtins import object, str

from future.utils import with_metaclass


class BaseResult(with_metaclass(ABCMeta, object)):
    """Base checking result."""

    @abstractmethod
    def is_success(self):
        """Check result is success."""
        return False

    @abstractproperty
    def output(self):
        """
        Get result output.

        (stdout and stderr).
        """
        return ''

    def __bool__(self):
        """Conversion to boolean."""
        return self.is_success()


class Result(BaseResult):
    """Code checking result."""

    target = ''
    status = -1
    output = ''
    _is_success = False

    def __init__(self, target=None, status=None, output=''):
        """Init Result with attributes."""
        self.target = target
        self.status = int(status)
        self.output = str(output) if output is not None else ''
        self._is_success = True if self.status == 0 else False

    def is_success(self):
        """Check result is success."""
        return self._is_success


class ResultSet(BaseResult):
    """Set of code checking results."""

    def __init__(self):
        """Init ResultSet with attributes."""
        self.results = []

    def add(self, result):
        """Add checking result."""
        self.results.append(result)

    @property
    def output(self):
        """Get output of all checking results."""
        output = ''
        for result in self.results:
            output += result.output
            if not output.endswith('\n'):
                output += '\n'
        return output

    def is_success(self):
        """Check for all checking results are success."""
        if len(self.results) == 0:
            return False
        is_success = True
        for result in self.results:
            if not result.is_success():
                is_success = False
                break
        return is_success
