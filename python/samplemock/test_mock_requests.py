import requests


def get_json_data(url):
    resp = requests.get(url)
    if resp.status_code != 200:
        raise
    return resp.json()


def main():
    url = 'http://httpbin.org/json'
    json_data = get_json_data(url)
    print(json_data)

# if __name__ == '__main__':
#     main()


# ----------


from test_mock_requests import get_json_data

import unittest
from unittest import mock


def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    if args[0] == 'http://example.net/':
        return MockResponse({"result": "mock"}, 200)

    return MockResponse({}, 404)


class TestGetJSONData(unittest.TestCase):
    # 正常系
    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_get_json_data1(self, mock_get):
        print('test_get_json_data1')
        json_data = get_json_data('http://example.net/')
        self.assertEqual(json_data, {"result": "mock"})
        print(json_data)

    # 異常系
    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_get_json_data2(self, mock_get):
        print('test_get_json_data2')
        with self.assertRaises(RuntimeError):
            # json_data = get_json_data('http://example.net/')
            json_data = get_json_data('url_invalid')
            print(json_data)

if __name__ == '__main__':
    unittest.main()
