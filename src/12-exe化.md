# exe 化

```bat
$ pip install pyinstaller

$ cd test-pyinstaller
$ pyinstaller app.py
```

> ...
>
> 4935 INFO: Building COLLECT COLLECT-00.toc completed successfully.

```bat
$ cd dist\app
$ app.exe
```

exe ファイルのみ生成する場合は、 `--onefile` オプションを追加する

```bat
$ pyinstaller --onefile app.py
$ cd dist
$ app.exe
```
