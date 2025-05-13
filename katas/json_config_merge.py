import json
from typing import Any


def json_configs_merge(*json_paths: str) -> dict[str, Any]:
    """
    Merge multiple JSON configuration files into a single dictionary.

    You are given an unknown number of file paths pointing to JSON configuration files.
    These files should be merged in the order they are given:
    - Keys in later files override those in earlier ones.
    - Nested dictionaries must also be merged recursively.

    Example:

        File: default.json
        {
          "user": {
            "name": "John",
            "age": 30
          },
          "settings": {
            "theme": "light",
            "language": "english"
          }
        }

        File: local.json
        {
          "user": {
            "age": 31,
            "email": "john@example.com"
          },
          "settings": {
            "language": "spanish",
            "timezone": "UTC+1"
          }
        }

        Result:
        {
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

    Args:
        *json_paths: Variable number of JSON file paths to merge.

    Returns:
        dict: The merged configuration dictionary.
    """
    result = {}
    for path_js in json_paths:
        f = open(path_js,"r")
        data = json.load(f)
        result = json_configs_merge_helper(result,data)
        f.close()

    return result

def json_configs_merge_helper(dict1 , dict2):
        for key, value in dict2.items():
            if key in dict1 and isinstance(dict1[key], dict) and isinstance(value, dict):
                json_configs_merge_helper(dict1[key], value)
            else:
                dict1[key] = value
        return dict1


if __name__ == '__main__':
    # Example usage; make sure the files exist for this to run.
    config = json_configs_merge('configs/default.json', 'configs/local.json')
    print(config)


