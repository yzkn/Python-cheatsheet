import pytest


import sys
current_module = sys.modules[__name__]


def mock_main():
    raise Exception('MockException')

def main():
    return echo('Lorem ipsum dolor sit amet, consectetur adipiscing elit.')

def test_main(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setattr(current_module, 'main', mock_main)

    with pytest.raises(Exception) as e:
        main()
    assert e.value.args[0] == 'MockException'
