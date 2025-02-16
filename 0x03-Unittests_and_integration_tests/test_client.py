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
        expected_result = {'name': input, 'repos_url':
                           f'https://api.github.com/orgs/{input}/repos'}
        mock_json.return_value = expected_result
        test = GithubOrgClient(input)
        result = test.org
        self.assertEqual(result, expected_result)
        mock_json.assert_called_once_with(
            GithubOrgClient.ORG_URL.format(org=input)
            )

    def test_public_repos_url(self):
        known_payload = {'name': 'google',
                         'repos_url': 'https://github.com/orgs/google'}

        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock:
            mock.return_value = known_payload
            test = GithubOrgClient('google')
            self.assertEqual(test._public_repos_url,
                             known_payload['repos_url'])

    @patch('client.get_json')
    def test_public_repos(self, mock_json):
        json_res = [{'name': 'google', 'id': 123433, 'gists_url':
                     'https://api.github.com/orgs/google/repos'},
                    {'name': 'kratos', 'id': 123433, 'gists_url':
                     'https://api.github.com/orgs/kratos/repos'}
                    ]
        mock_json.return_value = json_res
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock:
            pub_repos_payload = 'https://github.com/orgs/google'
            mock.return_value = pub_repos_payload
            test = GithubOrgClient('google')
            res = test.public_repos()

            repos = [repo['name'] for repo in json_res]
            self.assertEqual(res, repos)

            mock.assert_called_once()
            mock_json.assert_called_once()

    @parameterized.expand([
        ({'license': {'key': 'my_license'}}, 'my_license', True),
        ({'license': {'key': 'other_license'}}, 'my_license', False)
    ])
    def test_has_license(self, repo, license_key, expected_license):
        res = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(res, expected_license)