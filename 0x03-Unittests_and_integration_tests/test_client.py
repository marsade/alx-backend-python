#!/usr/bin/env python3
'''Testing the client module'''
import unittest
from unittest.mock import patch, PropertyMock
from typing import Mapping, Sequence, Type
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    '''Test github org class'''
    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, input, mock_json):
        '''Test Org method'''
        expected_result = {"name": input, "repos_url":
                           f"https://api.github.com/orgs/{input}/repos"}
        mock_json.return_value = expected_result
        test = GithubOrgClient(input)
        result = test.org
        self.assertEqual(result, expected_result)
        mock_json.assert_called_once_with(
            GithubOrgClient.ORG_URL.format(org=input)
            )

    def test_public_repos_url(self):
        known_payload = {'name': 'google',
                         'repos_url': 'https://github.com/orgs'}

        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock:
            mock.return_value = known_payload
            test = GithubOrgClient('google')
            self.assertEqual(test._public_repos_url,
                             known_payload['repos_url'])
