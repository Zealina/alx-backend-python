#!/usr/bin/env python3
"""client.py test module"""

import unittest
from unittest.mock import patch, MagicMock, PropertyMock
from parameterized import parameterized  # type: ignore
from typing import Dict
GithubOrgClient = __import__('client').GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Testcases for the client.py module"""
    @parameterized.expand([
        ("google",),
        ("abc",)
        ])
    @patch('client.get_json')
    def test_org(self, org_text: str, mock_get_json: MagicMock) -> None:
        """Test the org method to work as expected"""
        inst = GithubOrgClient(org_text)
        org_url = f"https://api.github.com/orgs/{org_text}"
        inst.org()
        mock_get_json.assert_called_once_with(org_url)

    def test_public_repos_url(self):
        """Test the _public_repos_url"""
        with patch(
                "client.GithubOrgClient.org",
                new_callable=PropertyMock) as mocky:
            nary = {"repos_url": "testing"}
            mocky.return_value = nary
            inst = GithubOrgClient("test")
            self.assertEqual(inst._public_repos_url, nary["repos_url"])
