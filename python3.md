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

```py
dirs = glob(os.path.join(DIRPATH, '*'), recursive=True)
# または dirs = glob(os.path.join(DIRPATH, '*'), recursive=False) も同じ
```

> ['./test-glob/test-glob-1', './test-glob/test-glob-2', './test-glob/test-glob-3.dat']

```py
dirs = glob(os.path.join(DIRPATH, '**'), recursive=False)
```

> ['./test-glob/test-glob-1', './test-glob/test-glob-2', './test-glob/test-glob-3.dat']

```py
dirs = glob(os.path.join(DIRPATH, '**'), recursive=True)
```

> ['./test-glob/', './test-glob/test-glob-1', './test-glob/test-glob-1/test-glob-1-1', './test-glob/test-glob-1/test-glob-1-1/test-glob-1-1-1.dat', './test-glob/test-glob-1/test-glob-1-1/test-glob-1-1-2.dat', './test-glob/test-glob-1/test-glob-1-2.dat', './test-glob/test-glob-2', './test-glob/test-glob-2/test-glob-2-2.dat', './test-glob/test-glob-3.dat']

```py
dirs = glob(os.path.join(DIRPATH, '**' + os.path.sep), recursive=True)
```

> ['./test-glob/', './test-glob/test-glob-1/', './test-glob/test-glob-1/test-glob-1-1/', './test-glob/test-glob-2/']

```py
dirs = glob(os.path.join(DIRPATH, '*.*'), recursive=True)
```

> ['./test-glob/test-glob-3.dat']

```py
dirs = glob(os.path.join(DIRPATH, os.path.join('**', '*.*')), recursive=True)
```

> ['./test-glob/test-glob-3.dat', './test-glob/test-glob-1/test-glob-1-2.dat', './test-glob/test-glob-1/test-glob-1-1/test-glob-1-1-1.dat', './test-glob/test-glob-1/test-glob-1-1/test-glob-1-1-2.dat', './test-glob/test-glob-2/test-glob-2-2.dat']

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
