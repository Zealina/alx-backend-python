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

    @parameterized.expand([
        ({"repos_url": "https://hamilton.com"},)])
    def test_public_repos_url(self, nary: Dict):
        """Test the _public_repos_url"""
        with patch(
                "client.GithubOrgClient.org",
                new_callable=PropertyMock) as mocky:
            inst = GithubOrgClient("hamilton")
            mocky.return_value =nary["repos_url"]
            self.assertEqual(inst._public_repos_url, nary["repos_url"])
