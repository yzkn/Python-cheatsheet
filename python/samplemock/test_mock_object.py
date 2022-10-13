import pytest


global_var = -1


def test_func_main(mocker):
    mocker.patch("test_mock_object.global_var", new=12345)
    print(global_var)
