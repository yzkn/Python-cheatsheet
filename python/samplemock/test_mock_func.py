# test_mock_func.py
# ~~~~~~~~~~~~~~

# test_mock_func.log11()
# ~~~~~~~~~~~~~~
def log1(message: str):
    print('msg: {}'.format(message))


def func1(message: str):
    log1(message)


def func2():
    log1('Started.')
    print('Something...')
    log1('Finished.')


def test_func1(mocker):
    log = mocker.patch('test_mock_func.log1')
    func1('Lorem ipsum dolor sit amet.')
    # 想定通りの文字列を受け取って、かつ1回だけ呼び出されたか
    log.assert_called_once_with('Lorem ipsum dolor sit amet.')


def test_func2(mocker):
    log = mocker.patch('test_mock_func.log1')
    func2()
    # 呼び出し履歴が想定通りか
    assert log.call_args_list == [
        mocker.call('Started.'),
        mocker.call('Finished.'),
    ]


# --------------------


def log2(message: str) -> bool:
    print('msg: {}'.format(message))
    return True


def func3(message: str):
    ok = log2(message)
    if ok:
        print('succeeded')
    else:
        print('failed')


def test_send(mocker, capsys):
    # 戻り値を偽装
    # log = mocker.patch('test_mock_func.log2')
    log = mocker.patch('test_mock_func.log2', return_value=False)
    func3('Fusce placerat placerat placerat.')
    log.assert_called_once_with('Fusce placerat placerat placerat.')
    out, _ = capsys.readouterr()
    # assert out == 'succeeded\n'
    assert out == 'failed\n'
