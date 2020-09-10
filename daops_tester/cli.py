# -*- coding: utf-8 -*-

"""Console script for daops_tester."""

__author__ = """YOUR NAME"""
__contact__ = "YOUR EMAIL"
__copyright__ = "Copyright 2018 United Kingdom Research and Innovation"
__license__ = "BSD - see LICENSE file in top-level package directory"
import argparse
import sys


def main():
    """Console script for daops_tester."""
    parser = argparse.ArgumentParser()
    parser.add_argument('_', nargs='*')
    args = parser.parse_args()

    print("Arguments: " + str(args._))
    print("Replace this message by putting your code into "
          "daops_tester.cli.main")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
