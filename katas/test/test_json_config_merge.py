import unittest
from katas.json_config_merge import json_configs_merge
import os

class TestJsonConfigMerge(unittest.TestCase):

    def test_merge_configs(self):

        base_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory of the current script
        config_dir = os.path.join(base_dir, '../configs')  # Navigate to the configs folder

        file_paths = [
            os.path.join(config_dir, 'default.json'),
            os.path.join(config_dir, 'local.json')
        ]

        merged_config = json_configs_merge(*file_paths)

        expected_config = {
          "user": {
            "name": "John",
            "age": 31,
            "email": "john@example.com"
          },
          "settings": {
            "theme": "light",
            "language": "spanish",
            "timezone": "UTC+1"
          }
        }

        self.assertEqual(merged_config, expected_config)

    def test_another_merge_configs(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory of the current script
        config_dir = os.path.join(base_dir, '../configs')  # Navigate to the configs folder

        file_paths = [
            os.path.join(config_dir, 'production.json'),
            os.path.join(config_dir, 'us-east-1-production.json')
        ]
        merged_config = json_configs_merge(*file_paths)

        expected_config = {
            "app": {
            "debug": False
          },
          "database": {
            "host": "us-east-1.db.prod.internal",
            "username": "prod_user",
            "password": "prod_secret"
          },
          "logging": {
            "level": "ERROR"
          },
          "security": {
            "enable_https": True,
            "cors": ["https://us.myapp.com"]
          },
            "region": "us-east-1"
        }

        self.assertEqual(merged_config, expected_config)