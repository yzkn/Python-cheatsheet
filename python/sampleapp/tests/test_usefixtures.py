import pytest


@pytest.fixture()
def sample_fixture():
    print("前処理")


@pytest.mark.usefixtures('sample_fixture')
class TestSample(object):
    def test_1(self):
        print("テスト1")

    def test_2(self):
        print("テスト2")

    def test_3(self):
        print("テスト3")
