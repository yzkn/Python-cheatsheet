# str

## format

```py
print('{}'.format(1))
```

> 1

### datetimeからstr

```py
from datetime import datetime
now = datetime.now().strftime('%Y%m%d%H%M%S')
print(now)
```

> 20190730121658

### strからdatetime、date

[format文字列に埋め込むディレクティブ](https://docs.python.org/ja/3/library/time.html#time.strftime)

```py
from datetime import date
from datetime import datetime
tstr = '2019-07-30 12:16:58'
tdatetime = datetime.strptime(tstr, '%Y-%m-%d %H:%M:%S')
tdate = date(tdatetime.year, tdatetime.month, tdatetime.day)
print(tdatetime)
print(tdate)
```

> 2019-07-30 12:16:58
> 2019-07-30

## 置換

# I/O

## ファイル一覧

```py
from glob import glob
import os


DIRPATH = os.getcwd() # '/mnt/c/Users/y/Documents/GitHub/Python-cheatsheet'
os.chdir(DIRPATH)

DIRPATH = '.'
DIRPATH = os.path.join(DIRPATH, 'test-glob') # './test-glob'
DIRPATH += '' if DIRPATH.endswith(os.path.sep) else os.path.sep # './test-glob/'
```

### 直下のファイル・フォルダ一覧を取得

```py
dirs = glob(os.path.join(DIRPATH, '*'), recursive=True)
# または dirs = glob(os.path.join(DIRPATH, '*'), recursive=False) も同じ
```

> [
>   './test-glob/test-glob-1',
>   './test-glob/test-glob-2',
>   './test-glob/test-glob-3.dat'
> ]

```py
dirs = glob(os.path.join(DIRPATH, '**'), recursive=False)
```

> [
>   './test-glob/test-glob-1',
>   './test-glob/test-glob-2',
>   './test-glob/test-glob-3.dat'
> ]

### 直下のファイル一覧を取得

```py
dirs = glob(os.path.join(DIRPATH, '*.*'), recursive=True)
```

> ['./test-glob/test-glob-3.dat']

```py
[f for f in glob(os.path.join(DIRPATH, '*')) if os.path.isfile(f)]
```

> [
>   './test-glob/test-glob-3.dat'
> ]

### 直下のフォルダ一覧を取得

```py
[f for f in glob(os.path.join(DIRPATH, '*')) if os.path.isdir(f)]
```

> [
>   './test-glob/test-glob-1',
>   './test-glob/test-glob-2'
> ]

### 再帰的にファイル・フォルダ一覧を取得 ⇒ _recursive_ が _True_ かつ、パスに _**_

```py
dirs = glob(os.path.join(DIRPATH, '**'), recursive=True)
```

> [
>   './test-glob/',
>   './test-glob/test-glob-1',
>   './test-glob/test-glob-1/test-glob-1-1',
>   './test-glob/test-glob-1/test-glob-1-1/test-glob-1-1-1.dat',
>   './test-glob/test-glob-1/test-glob-1-1/test-glob-1-1-2.dat',
>   './test-glob/test-glob-1/test-glob-1-2.dat',
>   './test-glob/test-glob-2',
>   './test-glob/test-glob-2/test-glob-2-2.dat',
>   './test-glob/test-glob-3.dat'
> ]

### Python3.4以前で、再帰的にファイル・フォルダ一覧を取得

```py
import os

files = []
def glb(directory):
    for root, dirs, files in os.walk(directory):
        yield root
        for file in files:
            yield os.path.join(root, file)

for file in glb(DIRPATH):
    files.append(file)

print(files)
```

> [
>   './test-glob',
>   './test-glob/test-glob-3.dat',
>   './test-glob/test-glob-1',
>   './test-glob/test-glob-1/test-glob-1-2.dat',
>   './test-glob/test-glob-1/test-glob-1-1',
>   './test-glob/test-glob-1/test-glob-1-1/test-glob-1-1-1.dat',
>   './test-glob/test-glob-1/test-glob-1-1/test-glob-1-1-2.dat',
>   './test-glob/test-glob-2',
>   './test-glob/test-glob-2/.test-glob-2-1.dat',
>   './test-glob/test-glob-2/test-glob-2-2.dat'
> ]

### 再帰的にフォルダ一覧を取得 ⇒ パスの末尾が _os.path.sep_

```py
[f for f in glob(os.path.join(DIRPATH, '**'), recursive=True) if os.path.isdir(f)]
```

> [
>   './test-glob/',
>   './test-glob/test-glob-1',
>   './test-glob/test-glob-1/test-glob-1-1',
>   './test-glob/test-glob-2'
> ]

```py
dirs = glob(os.path.join(DIRPATH, '**' + os.path.sep), recursive=True)
```

> [
>   './test-glob/',
>   './test-glob/test-glob-1/',
>   './test-glob/test-glob-1/test-glob-1-1/',
>   './test-glob/test-glob-2/'
> ]

### 再帰的にファイル一覧を取得

```py
dirs = glob(os.path.join(DIRPATH, os.path.join('**', '*.*')), recursive=True)
```

> [
>   './test-glob/test-glob-3.dat',
>   './test-glob/test-glob-1/test-glob-1-2.dat',
>   './test-glob/test-glob-1/test-glob-1-1/test-glob-1-1-1.dat',
>   './test-glob/test-glob-1/test-glob-1-1/test-glob-1-1-2.dat',
>   './test-glob/test-glob-2/test-glob-2-2.dat'
> ]

### ワイルドカードを利用

```py
dirs = glob(os.path.join(DIRPATH, os.path.join('**', '*-[0-1].???')), recursive=True)
```

> [
>   './test-glob/test-glob-1/test-glob-1-1/test-glob-1-1-1.dat'
> ]

## ログ

標準出力をログファイルに書き出す

```py
from datetime import datetime
import sys

startTimeStr = datetime.now().strftime('%Y%m%d%H%M%S')
LOGFILE = 'log_{}.txt'.format(startTimeStr)

if __name__ == '__main__':
    try:
        sys.stdout = open(LOGFILE, 'a', encoding='utf-8')
        main()
    except Exception as e:
        with open(LOGFILE, 'a', encoding='utf-8') as logfile:
            nowStr = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
            print('Exception: {} {}'.format(e, nowStr), file=logfile, flush=True)
    finally:
        sys.stdout.close()
        sys.stdout = sys.__stdout__
```

```py

```

```py

```

```py

```
