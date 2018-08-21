"""
Check that instantiating a class with `abc.ABCM` as ancestor fails if it
defines abstract methods.
"""

# pylint: disable=too-few-public-methods, missing-docstring, abstract-class-not-used, no-init

__revision__ = 0

import abc

class BadClass(abc.ABC):
    @abc.abstractmethod
    def test(self):
        pass

def main():
    """ do nothing """
    BadClass() # [abstract-class-instantiated]
