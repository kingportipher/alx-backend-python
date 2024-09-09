#!/usr/bin/env python3

import unittest
from unittest.mock import patch, Mock
from utils import get_json

class TestGetJson(unittest.TestCase):
    """Test case for get_json function"""

    @patch("utils.requests.get")
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload, mock_get):
        """Test that get_json returns the correct payload"""
        # Create a mock response object with a json() method
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        # Call the get_json function and assert the result
        result = get_json(test_url)
        self.assertEqual(result, test_payload)

        # Check that requests.get was called once with the correct URL
        mock_get.assert_called_once_with(test_url)

if __name__ == "__main__":
    unittest.main()
