#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import argparse
import helpers.auth
import helpers.cases
from helpers.status import *

__author__ = "OSVR and contributors."
__copyright__ = "Copyright 2016, %s" % (__author__)
__credits__ = ["Marcelo Araujo"]
__license__ = "Apache 2.0"


def usage():
    return '''
  main.py [-h] [--project PROJECT] [--suite SUITE] [--run RUN]
               [--case CASE] [--status STATUS] [--comment COMMENT]

example:
  ./main.py --project "OSVR" --suite "TestRailAutomation" --run "Python_API" --case "Check Python Integration" --status "PASSED" --comment "It worked as expected."
    '''
def menu():
    help_status = "final test status [PASSED|BLOCKED|RETEST|FAIL]"
    parser = argparse.ArgumentParser(usage=usage())
    parser.add_argument("--project", help="project name", type=str)
    parser.add_argument("--suite", help="suite name", type=str)
    parser.add_argument("--run", help="test run name", type=str)
    parser.add_argument("--case", help="test case name", type=str)
    parser.add_argument("--status", help=help_status, type=str)
    parser.add_argument("--comment", help="comment for the test case", type=str)
    args = parser.parse_args()

    return args


if __name__ == '__main__':
    case = helpers.cases.TestRail()
    args = menu()    

    #  We check status first, if it doesn't match we don't call the API 
    #  and exit(1).
    status = status(args.status)

    comment = args.comment
    project_id = case.get_project_id(args.project)
    suite_id = case.get_project_suite_id(args.suite, project_id)
    section_id = case.get_project_section_id(args.suite, project_id)
    run_id = case.get_test_run_id(args.run, project_id)
    case_id = case.get_case_id(args.case, section_id, suite_id, project_id)

    #  Update the test case.
    case.set_test_case_result(run_id, case_id, status, comment)
