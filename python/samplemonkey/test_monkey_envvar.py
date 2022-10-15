import pytest


import monkey_envvar


def test_get_my_envvar(monkeypatch):
    monkeypatch.setenv("MY_ENVVAR", "MY_ENVVAR_VALUE")
    assert monkey_envvar.get_my_envvar() == "MY_ENVVAR_VALUE"


def test_get_my_envvar_exception(monkeypatch):
    monkeypatch.delenv("MY_ENVVAR", raising=False)
    with pytest.raises(OSError):
        _ = monkey_envvar.get_my_envvar()
