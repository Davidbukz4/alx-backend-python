#!/usr/bin/env python3
'''
Client Test
'''
import unittest
from client import GithubOrgClient
from parameterized import parameterized
from unittest.mock import patch


class TestGithubOrgClient(unittest.TestCase):
    ''' GithubOrgClient Test Class '''
    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock):
        ''' Test GithubOrgClient.org '''
        test_class = GithubOrgClient(org_name)
        test_class.org()
        mock.called_with_once(test_class.ORG_URL.format(org=org_name))
