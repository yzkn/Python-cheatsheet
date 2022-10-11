import pytest


# assert文
def add(x, y):
    return x + y

def test_add1():
    res = add(1, 2)
    assert res == 3

def test_add2():
    res = add(1, 2)
    assert res == 3, '検証に失敗したときのメッセージ: {}'.format(res)

# テスト実施をスキップ
@pytest.mark.skip
def test_add3():
    res = add(1, 2)
    assert res == 3


# 例外発生
def div(x, y):
    return x / y

def test_target():
    with pytest.raises(ZeroDivisionError) as e:
        div(1, 0)
    # エラーメッセージの検証
    assert str(e.value) == "division by zero"


# 標準出力・標準エラー出力
import sys

def test_std_out_err(capfd):
    print('標準出力内容')
    sys.stderr.write('標準エラー出力内容')

    # 検証
    out, err = capfd.readouterr()
    assert out == '標準出力内容\n'
    assert err == '標準エラー出力内容'


# 複数のフィクスチャ
import pytest

# 引数に指定されなくても常に実行されるフィクスチャ
@pytest.fixture(autouse=True)
def fixture00():
    print('fixture00')

# 複数のフィクスチャ
# 使用するフィクスチャを引数でテストメソッドに渡す
@pytest.fixture
def fixture01():
    print('fixture01')

@pytest.fixture
def fixture02():
    print('fixture02')

def test_case01():
    print('test_case01')

def test_case02(fixture01):
    print('test_case02')

def test_case03(fixture01, fixture02):
    print('test_case03')