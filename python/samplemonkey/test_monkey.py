import pytest

import monkey


def mock_echo(message: str):
    return 'mock_echo'


def mock_main():
    return 'mock_main'


def test_main(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setattr(monkey, 'echo', mock_echo)
    monkeypatch.setattr(monkey, 'main', mock_main)

    assert monkey.echo('') == 'mock_echo'
    assert monkey.main() == 'mock_main'
