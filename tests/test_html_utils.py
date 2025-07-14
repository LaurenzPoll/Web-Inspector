from unittest.mock import Mock, patch

import pytest
from html_utils import fetch_html


def test_fetch_html_success():
    fake_response = Mock()
    fake_response.status_code = 200
    fake_response.text = "<html><body>Test</body></html>"
    fake_response.raise_for_status = Mock()

    with patch("html_utils.requests.get", return_value=fake_response) as mock_get:
        html = fetch_html("https://example.com")
        assert html == "<html><body>Test</body></html>"
        mock_get.assert_called_once_with("https://example.com")


def test_fetch_html_http_error():
    fake_response = Mock()
    fake_response.raise_for_status.side_effect = Exception("HTTP Error")

    with patch("html_utils.requests.get", return_value=fake_response):
        with pytest.raises(Exception):
            fetch_html("https://badurl.example")
