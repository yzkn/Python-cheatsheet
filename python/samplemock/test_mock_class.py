# test_mock_class.py
# ~~~~~~~~~~~~~~~


import datetime


def gettime():
    # 標準モジュール
    return datetime.datetime.now()


# test_mock_class.function1
# ~~~~~~~~~~~~~~~
def function1():
    return 0


class MyClass1:
    __class_variable1 = 30

    def __init__(self):
        self.__property1 = 20

    def instance_method1(self):
        return self.__property1

    @property
    def property1(self):
        return self.__property1

    @classmethod
    # def classmethod1(cls):
    def get_class_variable1(cls):
        return cls.__class_variable1

    @staticmethod
    def static_method1():
        return 40


# test_mock_class.main
# ~~~~~~~~~~~~~~~
def main():
    s = MyClass1()
    # インスタンスメソッド
    print(s.instance_method1())
    # プロパティ
    print(s.property1)
    # クラスメソッド
    print(MyClass1.get_class_variable1())
    # スタティックメソッド
    print(MyClass1.static_method1())


# --------------------


import datetime
import pytest
import test_mock_class


@pytest.mark.freeze_time(datetime.datetime(2022, 10, 11, 22, 33))
def test_gettime(mocker):
    print(gettime())
    assert gettime() == datetime.datetime(2022, 10, 11, 22, 33)


def test_function1_1(mocker):
    mocker.patch("test_mock_class.function1", return_value=123) # 戻り値を定数に変更
    print(test_mock_class.function1()) # 123


def test_function1_2(mocker):
    mocker.patch("test_mock_class.function1", side_effect=[123, 234, 345]) # 呼び出し回数に応じて戻り値を変更
    print(test_mock_class.function1()) # 123
    print(test_mock_class.function1()) # 234
    print(test_mock_class.function1()) # 345


def test_main(mocker):
    # インスタンスメソッド
    mocker.patch("test_mock_class.MyClass1.instance_method1", return_value=12)
    print(test_mock_class.MyClass1.instance_method1()) # 12

    # プロパティには new_callable=mocker.PropertyMock を指定
    mocker.patch("test_mock_class.MyClass1.property1", return_value=23, new_callable=mocker.PropertyMock)
    print(test_mock_class.MyClass1.property1) # 23

    # クラスメソッド
    mocker.patch("test_mock_class.MyClass1.get_class_variable1", return_value=34)
    print(test_mock_class.MyClass1.get_class_variable1()) # 34

    # スタティックメソッド
    mocker.patch("test_mock_class.MyClass1.static_method1", return_value=45)
    print(test_mock_class.MyClass1.static_method1()) # 45
