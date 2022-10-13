import datetime


def func1():
    return datetime.datetime.now()


# -----


import pytest


@pytest.mark.freeze_time(datetime.datetime(2022, 10, 11, 22, 33))
def test_func1(mocker):
    assert func1() == datetime.datetime(2022, 10, 11, 22, 33)


# -----


def test_func2(mocker):
    expect = datetime.datetime(2022, 10, 11, 22, 33, 44, 55)
    mocker.patch("datetime.datetime", **{
        "now.return_value": datetime.datetime(2022, 10, 11, 22, 33, 44, 55)
    })
    assert func1() == expect
