import pytest


import sys
current_module = sys.modules[__name__]


class MyClass:
    def instance_method1(self):
        return 'instance_method'


def main():
    myClass = MyClass()
    return myClass.instance_method1()


def test_main(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setattr(current_module.MyClass, 'instance_method1', lambda *args: 'MOCKED')
    assert main() == 'MOCKED'
