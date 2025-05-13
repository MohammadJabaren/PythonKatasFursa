import unittest
from katas.nginx_log_parser import parse_log

class TestNginxLogParser(unittest.TestCase):

    def test_invalid_log_format(self):
        invalid_log_entry = 'Invalid'
        with self.assertRaises(ValueError):
            parse_log(invalid_log_entry)

    def test_missing_log_field(self):
        log_entry = (
            '122.176.223.47 - - [05/Feb/2024:08:29:40 +0000] '
            '"GET /web-enabled/Enhanced-portal/bifurcated-forecast.js HTTP/1.1" 200 1684 '
            '"-" "-"'
        )
        expected_output = {
            "client_ip": "122.176.223.47",
            "date": "05/Feb/2024:08:29:40 +0000",
            "http_method": "GET",
            "path": "/web-enabled/Enhanced-portal/bifurcated-forecast.js",
            "http_version": "1.1",
            "status": "200",
            "response_bytes": "1684",
            "user_agent": "-"
        }
        result = parse_log(log_entry)
        self.assertEqual(result, expected_output)

    def test_post_request_with_different_user_agent(self):
        log_entry = (
            '203.0.113.5 - - [12/Mar/2024:14:15:22 +0000] '
            '"POST /api/v1/user/login HTTP/2.0" 401 512 '
            '"-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
            '(KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"'
        )
        expected_output = {
            "client_ip": "203.0.113.5",
            "date": "12/Mar/2024:14:15:22 +0000",
            "http_method": "POST",
            "path": "/api/v1/user/login",
            "http_version": "2.0",
            "status": "401",
            "response_bytes": "512",
            "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
        }
        result = parse_log(log_entry)
        self.assertEqual(result, expected_output)