import json
import os


def get_json_data(param):
    current_path = os.path.abspath(__file__)
    grandparent_path = os.path.dirname(os.path.dirname(current_path))
    json_path = os.path.join(grandparent_path, r'test_data\json_data.json')
    with open(json_path, 'r', encoding='utf8') as f:
        fread = f.read()
        test_data = json.loads(fread)
    return test_data[param]


if __name__ == '__main__':
    print(get_json_data('test_get_topics'))
