# import pytest
#
#
# import sys
# current_module = sys.modules[__name__]
#
#
# def mock_echo(message: str):
#     return 'mock_echo'
#
# def main():
#     return echo('Lorem ipsum dolor sit amet, consectetur adipiscing elit.')
#
# def test_main(monkeypatch: pytest.MonkeyPatch):
#     monkeypatch.setattr(current_module, 'main', mock_echo)


# --------------------


# import pytest
#
#
# import monkey
#
#
# def mock_echo(message: str):
#     return 'mock_echo'
#
#
# def mock_main():
#     return 'mock_main'
#
#
# def test_main(monkeypatch: pytest.MonkeyPatch):
#     # monkeypatch.setattr(monkey, 'echo', lambda *_: 'mock_echo')
#     monkeypatch.setattr(monkey, 'echo', mock_echo)
#     monkeypatch.setattr(monkey, 'main', mock_main)
#
#     assert monkey.echo('') == 'mock_echo'
#     assert monkey.main() == 'mock_main'


# --------------------


# プライベート関数の場合は import <module> ではなく `as <alias>` でエイリアスを付ける必要がある
# from monkey import __private_function as pf
import monkey as pf


import sys
current_module = sys.modules[__name__]


def test_private_function(monkeypatch):
    monkeypatch.setattr(current_module, 'pf', lambda: 'MOCKED')
    assert pf() == 'MOCKED'
