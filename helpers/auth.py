#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from TestRail.testrail import *

__author__ = "OSVR and contributors."
__copyright__ = "Copyright 2016, %s" % (__author__)
__credits__ = ["Marcelo Araujo"]
__license__ = "Apache 2.0"

#  Globals
TR_USER = 'YOUR_USER_HERE'
TR_PWD = 'YOUR_PASSWORD_HERE'
TR_URL = 'YOUR_TESTRAIL_URL_HERE'


def trclient():
    '''
    Set the connection and return it to be
    used by other methods.
    '''
    client = APIClient(TR_URL)
    client.user = TR_USER
    client.password = TR_PWD

    return client
