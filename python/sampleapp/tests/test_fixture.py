import os
import pytest


@pytest.fixture
def test_file():
    print('1. 前処理: 一時ファイルを作成開始')

    file_path = './test.txt'
    with open(file_path, 'w') as f:
        # yieldまでが前処理
        print('1. 前処理: 一時ファイルを作成終了')
        yield file_path

    print('3. 後処理: 一時ファイルを削除開始')
    os.remove(file_path)
    print('3. 後処理: 一時ファイルを削除終了')


# test_file()の戻り値が引数test_fileとして渡される
def test_file_exist(test_file):
    print(f'2. テスト実施: 開始 [{test_file}]')
    assert os.path.isfile(test_file)
    print('2. テスト実施: 終了')
