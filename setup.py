#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      roddi
#
# Created:     26.04.2016
# Copyright:   (c) roddi 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from distutils.core import setup
import py2exe


def main():
    setup(
        console=['main.py'],
        options={
                "py2exe": {
                        "includes": ["decimal"]
                }
        }
    )

if __name__ == '__main__':
    main()
