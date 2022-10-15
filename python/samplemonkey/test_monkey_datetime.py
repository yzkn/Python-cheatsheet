import datetime
from unittest.mock import MagicMock


def test_datetime(monkeypatch):
    datetime_mock = MagicMock(wraps=datetime.datetime)
    datetime_mock.now.return_value = datetime.datetime(2022, 10, 11, 22, 33)
    monkeypatch.setattr(datetime, 'datetime', datetime_mock)

    now = datetime.datetime.now()
    assert now == datetime.datetime(2022, 10, 11, 22, 33)
