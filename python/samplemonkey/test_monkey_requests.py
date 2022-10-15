import requests


import monkey_requests


class MockResponse:
    @staticmethod
    def json():
        return {'MOCKED_KEY': 'MOCKED_VALUE'}


def test_get_json(monkeypatch):
    # モックしない場合のJSON
    HTTPBIN_URL = 'http://httpbin.org/json'
    result = monkey_requests.get_json(HTTPBIN_URL)
    assert result['slideshow']['title'] == 'Sample Slide Show'



def test_get_json_mocked(monkeypatch):
    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests, 'get', mock_get)

    HTTPBIN_URL = 'http://httpbin.org/json'
    result = monkey_requests.get_json(HTTPBIN_URL)
    assert result['MOCKED_KEY'] == 'MOCKED_VALUE'
