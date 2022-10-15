import monkey_dict


def test_connection(monkeypatch):
    monkeypatch.setitem(monkey_dict.dct, 'key1', 'mocked1')
    monkeypatch.setitem(monkey_dict.dct, 'key2', 'mocked2')

    expected = 'Key1=mocked1;Key2=mocked2;'
    result = monkey_dict.get_dct()

    assert result == expected
