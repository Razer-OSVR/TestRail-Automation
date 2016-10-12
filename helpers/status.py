#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import sys

__author__ = "OSVR and contributors."
__copyright__ = "Copyright 2016, %s" % (__author__)
__credits__ = ["Marcelo Araujo"]
__license__ = "Apache 2.0"

PASSED = 1
BLOCKED = 2
UNTESTED = 3
RETEST = 4
FAIL = 5


def status(str_status):
    '''
    A simple transformation from string to int.
    Ex. It is easy type PASSED than remember 1.
    '''
    if str_status is not None:
        str_status = str_status.upper()
        if str_status == 'PASSED':
            return PASSED
        elif str_status == "BLOCKED":
            return BLOCKED
        elif str_status == "UNTESTED":
            return UNTESTED
        elif str_status == "RETEST":
            return RETEST
        elif str_status == "FAIL":
            return FAIL
        else:
            print("[Error] Status not recognized.")
            sys.exit(1)
    else:
        sys.exit(1)
