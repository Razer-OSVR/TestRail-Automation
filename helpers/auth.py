#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import os
import sys
import ConfigParser
from TestRail.testrail import *

__author__ = "OSVR and contributors."
__copyright__ = "Copyright 2016, %s" % (__author__)
__credits__ = ["Marcelo Araujo"]
__license__ = "Apache 2.0"

# Config File.
config_file = "defaults.cfg"

def readConfigFile():
    TR_URL = TR_USER = TR_PWD = None
    section = 'TestRail'

    abspath = sys.path[0]
    if os.name == 'posix':
        dirpath = abspath + '/'
    else:
        main = abspath.split('\\')[-1]
        dirpath = abspath[:-len(main)]

    config_file_path = dirpath + config_file
    config = ConfigParser.ConfigParser()
    config.readfp(open(config_file_path))

    TR_USER = config.get(section, 'USER')
    TR_PWD = config.get(section, 'PWD')
    TR_URL = config.get(section, 'URL')

    return TR_USER, TR_PWD, TR_URL

def trclient():
    '''
    Set the connection and return it to be
    used by other methods.
    '''

    TR_USER, TR_PWD, TR_URL = readConfigFile()

    client = APIClient(TR_URL)
    client.user = TR_USER
    client.password = TR_PWD

    return client
