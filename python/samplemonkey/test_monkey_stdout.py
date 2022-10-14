import pytest


import sys
current_module = sys.modules[__name__]


class MyClass(object):
    def echo(self):
        print('Lorem ipsum dolor sit amet.')


def test_echo(monkeypatch, capsys):
    monkeypatch.setattr(MyClass, 'echo', lambda x: print('MOCKED'))
    myClass = MyClass()
    actual = myClass.echo()
    actual, _ = capsys.readouterr()
    assert actual == 'MOCKED\n'
