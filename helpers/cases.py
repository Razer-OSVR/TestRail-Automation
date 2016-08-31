#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import helpers.auth

__author__ = "OSVR and contributors."
__copyright__ = "Copyright 2016, %s" % (__author__)
__credits__ = ["Marcelo Araujo"]
__license__ = "Apache 2.0"


class TestRail(object):

    def __init__(self):
        self.client = helpers.auth.trclient()

    def get_test_case(self, case):
        '''
        Returns an existing test case or None.
        '''
        try:
            test_case = self.client.send_get('get_case/%s' % (case))
            return test_case
        except Exception:
            return None

    def set_test_case_result(self, test_run, case, status, comment):
        '''
        Set the result of a test in a test case.
        '''
        add_result_for_case = 'add_result_for_case/' + str(test_run) + '/' + \
            str(case)
        test_case_result = self.client.send_post(
            add_result_for_case,
            {'status_id': status, 'comment': comment})

        return test_case_result

    def get_test_runs(self, project_id):
        '''
        Returns a list of test runs for a project.
        '''
        runs = self.client.send_get('get_runs/%s' % (project_id))

        return runs

    def get_test_run_id(self, run_name, project_id):
        '''
        Returns the ID of a specific test run.
        '''
        test_run_id = None
        for run in self.get_test_runs(project_id):
            if run['name'] == run_name:
                test_run_id = run['id']

        return test_run_id

    def get_project_id(self, project_name):
        '''
        Returns the project id.
        '''
        project_id = None
        projects = self.client.send_get('get_projects')
        for project_list in projects:
            if project_list['name'] == project_name:
                project_id = project_list['id']

        return project_id

    def get_project_sections(self, project_id):
        '''
        Returns a list of sections for a project.
        '''
        sections = self.client.send_get('get_sections/%s' % (project_id))

        return sections

    def get_project_section_id(self, project_name, project_id):
        '''
        Returns the id of a specific section of a project.
        '''
        section_id = None
        projects = self.get_project_sections(project_id)
        for project in projects:
            if project['name'] == project_name:
                section_id = project['id']

        return section_id

    def get_project_suite_id(self, section_name, project_id):
        '''
        Returns the id of an existing test suite.
        '''
        suite_id = None
        for sections in self.get_project_sections(project_id):
            if sections['name'] == section_name:
                suite_id = sections['suite_id']

        return suite_id

    def get_cases(self, section_id, suite_id, project_id):
        '''
        Returns a list of test cases for a section in a test suite.
        '''
        get_cases = 'get_cases/' + str(project_id) + '&suite_id=' + \
                    str(suite_id) + '&section_id=' + str(section_id)
        cases = self.client.send_get(get_cases)

        return cases

    def get_case_id(self, case_name, section_id, suite_id, project_id):
        '''
        Returns the id of an specific case.
        '''
        case_id = None
        for case in self.get_cases(section_id, suite_id, project_id):
            if case['title'] == case_name:
                case_id = case['id']

        return case_id
