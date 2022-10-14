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
    class MockedClass:
        def instance_method1(self):
            return 'MOCKED'

    monkeypatch.setattr(current_module, 'MyClass', MockedClass)
    assert main() == 'MOCKED'
