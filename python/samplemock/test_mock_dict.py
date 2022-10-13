# test_mock_dict.py
# ~~~~~~~~~~~~~~


dct = {"key1": 123, "key2": 234, "key3": 345}


# test_mock_dict.func1()
# ~~~~~~~~~~~~~~
def func1():
    print(dct)


import test_mock_dict
def test_func1(mocker):
    mocker.patch.dict(dct, {"key3": 321})
    test_mock_dict.func1() # {'key1': 123, 'key2': 234, 'key3': 321}

    mocker.patch.dict(dct, {"key4": 456}, clear=True)
    test_mock_dict.func1() # {'key4': 456}


# --------------------


# 環境変数の置き換え
import os

def func_envvar():
    return os.environ

def test_func_envvar(mocker):
    ret = func_envvar()
    print(ret)

    mocker.patch.dict('os.environ', {'NEW_KEY': 'NEW_VALUE'})
    ret = func_envvar()
    print(ret)

    assert ret["NEW_KEY"] == "NEW_VALUE"
