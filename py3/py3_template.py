# -*- coding: utf-8 -*-

"""
    py3_template.py

    Module summary
    USAGE
    Python version
    Required library
    etc..
"""

import logging


# CONSTANT
THIS_IS_CONST = "THIS_IS_CONST"

# LOG Setting
LOG_FILE_PATH = 'my_python.log'
LOG_FORMATTER = '%(levelname)s : %(asctime)s : %(message)s'

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# handler1 Stream
handler1 = logging.StreamHandler().setFormatter(logging.Formatter(LOG_FORMATTER))
handler1.setFormatter(logging.Formatter(LOG_FORMATTER))

# handler2 File
handler2 = logging.FileHandler(filename=LOG_FILE_PATH)
handler2.setFormatter(logging.Formatter(LOG_FORMATTER))

logger.addHandler(handler1)
logger.addHandler(handler2)


def my_func(num_1):
    """ Function Summary line.

    Args:
        num_1(int): number

    Returns:
        bool: Description of return value
    """

    logger.info("info log.")
    print(num_1)
    logger.error("error log.")

    return True


class MyClass:

    MY_CLASS_VARIABLE = "ABC"

    def __init__(self):
        """Constructor
        """
        self._pv_v = "instance_variable"

    def process(self, my_str):
        """ Method Summary Line

        Args:
            my_str: string
        """
        logger.debug(my_str)
        logger.debug(self._pv_v)

    def _private_process(self):
        logger.debug("_private_process")
        logger.debug(self._pv_v)

    @staticmethod
    def static_method():
        print(MyClass.MY_CLASS_VARIABLE)


def main():
    """ entry point
    """
    logger.debug("main() start")
    my_func(1)
    logger.debug("main() end")


if __name__ == "__main__":
    main()
