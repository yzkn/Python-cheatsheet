# データ型

```py
type(True)
```

> <class 'bool'>

```py
# 1
type(1)
type(int('1'))
type(float('1'))

# 1.23
type(1.23)
type(int('1.23'))
type(float('1.23'))

# 1 + 1.23
type(1 + 1.23)

# 10進数以外
type(0b11) # 2進数
type(0o11) # 8進数
type(0x11) # 16進数
```

> \# 1
>
> <class 'int'>
>
> <class 'int'>
>
> <class 'float'>
>
> \# 1.23
>
> <class 'float'>
>
> ValueError: invalid literal for int() with base 10: '1.23'
>
> <class 'float'>
>
> \# 1 + 1.23
>
> <class 'float'>
>
> \# 10進数以外
>
> <class 'int'>
>
> <class 'int'>
>
> <class 'int'>

```py
type('str')
```

> <class 'str'>

```py
type({0:0, 1:1, 2:2})
type([0, 1, 2])
type({0, 1, 2})
type((0, 1, 2))
```

> <class 'dict'>
>
> <class 'list'>
>
> <class 'set'>
>
> <class 'tuple'>

## 型の判定

## isinstance()

```py
type('str') is str
type(1) is not str

def is_valid_type(v):
    return type(v) in (int, str)

print(is_valid_type(1))
print(is_valid_type('1'))
```

> True
>
> True
>
> True
>
> True

```py
print(isinstance(1, str))
print(isinstance('1', str))
print(isinstance(100, (int, str)))
```

> False
>
> True
>
> True

## type()とisinstance()の差異

継承を考慮

```py
print(type(False) is bool)
print(type(False) is int)

# boolはintのサブクラス ⇒ isinstanceは継承元の型にもTrueを返す
print(isinstance(False, bool))
print(isinstance(False, int))
```

> True
>
> False
>
> True
>
> True

# 演算子

## [演算子の優先順位](https://docs.python.org/ja/3/reference/expressions.html#operator-precedence)

|  演算子  |  意味  |
| --- | --- |
|  (1), [1], {1:1}, {1}  |  式結合/タプル、リスト、辞書、集合  |
|  l[1], l[1,2], f(arg), c.attribute  | 添え字指定、スライス、関数呼び出し、属性参照  |
|  await  |  Await式
|  **  |  べき乗  |
|  +x, -x, ~x  |  数、負数、ビット単位NOT  |
|  *, /, //, %  |  乗算、除算、整除除算、剰余/文字列フォーマット  |
|  +, -  |  加算、減算  |
|  <<, >>  |  シフト演算  |
|  &  |  ビット単位 AND  |
|  ^  |  ビット単位 XOR  |
|  |  |  ビット単位 OR  |
|  in, not in, is, is not, <, <=, >, >=, !=, ==  |  比較  |
|  not x  |  NOT  |
|  and  |  AND  |
|  or  |  OR  |
|  if -- else  |  条件式(三項演算子)  |
|  lambda  |  ラムダ式  |

## boolean

|  True  |  False  |
| ---- | ---- |
|  bool(1)<br>bool(2)<br>bool(-3)<br>bool(.1)<br>bool(1j)<br>bool('a')<br>bool([0])<br>bool((0,))<br>bool({0})  |  bool(0)<br><br><br>bool(0.)<br>bool(0j)<br>bool('')<br>bool([])<br>bool(())<br>bool({})  |

## str

```py
print('str\nstr')
print("str\nstr")
print(r'str\nstr')
print(R'str\nstr')
```

> str
>
> str

> str
>
> str

> str\nstr

> str\nstr

### format

```py
print('{}'.format(1))
```

> 1

#### datetimeからstr

```py
from datetime import datetime
now = datetime.now().strftime('%Y%m%d%H%M%S')
print(now)
```

> 20190730121658

#### strからdatetime、date

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
>
> 2019-07-30

##### [日付時刻のformat文字列に埋め込むディレクティブ](https://docs.python.org/ja/3/library/time.html#time.strftime)

|  ディレクティブ  |  意味  |  注釈  |
| ---- | ---- | ---- |
|  %a  |  ロケールにおける省略形の曜日名。  |    |
|  %A  |  ロケールにおける省略なしの曜日名。  |    |
|  %b  |  ロケールにおける省略形の月名。  |    |
|  %B  |  ロケールにおける省略なしの月名。  |    |
|  %c  |  ロケールにおける適切な日付および時刻表現。  |    |
|  %d  |  月の始めから何日目かを表す 10 進数 [01,31]。  |    |
|  %H  |  (24 時間計での) 時を表す 10 進数 [00,23]。  |    |
|  %I  |  (12 時間計での) 時を表す 10 進数 [01,12]。  |    |
|  %j  |  年の初めから何日目かを表す 10 進数 [001,366]。  |    |
|  %m  |  月を表す 10 進数 [01,12]。  |    |
|  %M  |  分を表す 10 進数 [00,59]。  |    |
|  %p  |  ロケールにおける AM または PM に対応する文字列。  |  (1)  |
|  %S  |  秒を表す 10 進数 [00,61]。  |  (2)  |
|  %U  |  年の初めから何週目か (日曜を週の始まりとします)を表す<br>10 進数 [00,53]。年が明けてから最初の日曜日までの全ての曜日は 0 週目に属すると見なされます。  |  (3)  |
|  %w  |  曜日を表す 10 進数 [0(日曜日),6]。  |    |
|  %W  |  年の初めから何週目か (日曜を週の始まりとします)を表す<br>10 進数 [00,53]。年が明けてから最初の月曜日までの全ての曜日は 0 週目に属すると見なされます。  |  (3)  |
|  %x  |  ロケールにおける適切な日付の表現。  |    |
|  %X  |  ロケールにおける適切な時刻の表現。  |    |
|  %y  |  上 2 桁なしの西暦年を表す 10 進数 [00,99]。  |    |
|  %Y  |  上 2 桁付きの西暦年を表す 10 進数。  |    |
|  %Z  |  タイムゾーンの名前 (タイムゾーンがない場合には空文字列)。  |    |
|  %%  |  文字 “%” 自体の表現。  |    |

1. strptime() 関数で使う場合、%p ディレクティブが出力結果の時刻フィールドに影響を及ぼすのは、時刻を解釈するために %I を使ったときのみです。
1. 値の幅は実際に 0 から 61 です; 60 は うるう秒\<leap seconds\> を表し、 61 は歴史的理由によりサポートされています。
1. strptime() 関数で使う場合、%U および %W を計算に使うのは曜日と年を指定したときだけです。

### 検索

#### 単純な検索

```py
# -----:    0000000000111111111122222222223333333333444444444455
# count:    0123456789012345678901234567890123456789012345678901
haystack = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
needle = 'e'
```

```py
print(needle in haystack)
```

> True

```py
print(haystack.count(needle))
```

> 2

```py
print(haystack.find(needle))
print(haystack.find(needle, 4))
print(haystack.find(needle, 5))
print(haystack.find(needle, 5,30))
print(haystack.index(needle, 5,30))
print(haystack.find(needle, 5,31))
```

> 4
>
> 4
>
> 30
>
> -1
>
> ValueError: substring not found
>
> 30

```py
print(haystack.rfind(needle))
print(haystack.rfind(needle, None, 30))
print(haystack.rfind(needle, None, 31))
print(haystack.rfind(needle, 5,30))
print(haystack.rindex(needle, 5,30))
print(haystack.rfind(needle, 4,30))
```


> 30
>
> 4
>
> 30
>
> -1
>
> ValueError: substring not found
>
> 4



#### 正規表現による検索

##### 文字列の先頭でマッチ

```py
import re

haystack = 'haystack'
needle = '([a-rt-z]+)'

# コンパイル有
pattern = re.compile(needle)
matched = pattern.match(haystack)
print(matched)

# コンパイル無
matched = re.match(pattern, haystack)
print(matched)

# 結果を取得
if matched:
    print(matched.group())
    print(matched.start())
    print(matched.end())
    print(matched.span())
```

> <_sre.SRE_Match object; span=(0, 3), match='hay'>
>
> <_sre.SRE_Match object; span=(0, 3), match='hay'>
>
> hay
>
> 0
>
> 3
>
> (0, 3)

##### 文字列の途中でマッチした最初の箇所

```py
import re

haystack = 'haystack'
needle = '([a-rt-z]+)'

# コンパイル有
pattern = re.compile(needle)
searched = pattern.search(haystack)
print(searched)

# コンパイル無
searched = re.search(pattern, haystack)
print(searched)

# 結果を取得
if searched:
    print(searched.group())
    print(searched.start())
    print(searched.end())
    print(searched.span())
```

> <_sre.SRE_Match object; span=(0, 3), match='hay'>
>
> <_sre.SRE_Match object; span=(0, 3), match='hay'>
>
> hay
>
> 0
>
> 3
>
> (0, 3)

##### 文字列の途中でマッチした全ての箇所のリスト

```py
import re

haystack = 'haystack'
needle = '([a-rt-z]+)'

# コンパイル有
pattern = re.compile(needle)
allfound = pattern.findall(haystack)
print(allfound)

# コンパイル無
allfound = re.findall(pattern, haystack)
print(allfound)

# 結果を取得
if allfound:
    print(allfound)
```

> ['hay', 'tack']
>
> ['hay', 'tack']
>
> ['hay', 'tack']

##### 文字列の途中でマッチした全ての箇所のイテレーター

```py
import re

haystack = 'haystack'
needle = '([a-rt-z]+)'

# コンパイル有
pattern = re.compile(needle)
allfound = pattern.finditer(haystack)
print(allfound)

# コンパイル無
allfound = re.finditer(pattern, haystack)
print(allfound)

# 結果を取得
for found in allfound:
    print(found.group())
    print(found.start())
    print(found.end())
    print(found.span())
```

> \<callable_iterator object at 0x7fd0e8dd4da0\>
>
> \<callable_iterator object at 0x7fd0e8cc8a20\>
>
> hay
>
> 0
>
> 3
>
> (0, 3)
>
> tack
>
> 4
>
> 8
>
> (4, 8)

#### フラグを利用

```py

```

>
>
>

### 置換

#### 単純な置換

```py
haystack = 'haystack'
needle = 'a'
replacement = 'replacement'

content = haystack.replace(needle, replacement)
content = haystack.replace(needle, replacement, 1)
```

> 'hreplacementystreplacementck'
> 'hreplacementystack'

##### 改行文字を除去

```py
haystack = 'haystack\nhaystack\r\nhaystack'
replacement = ''

replacement.join(haystack.splitlines())
```

> 'haystackhaystackhaystack'

#### 正規表現による置換

```py
import re

haystack = 'haystack'
needle = '([a-rt-z]+)'
replacement = 'replacement[\\1]'

content = re.sub(needle, replacement, haystack)
print(content)
content = re.sub(needle, replacement, haystack, 1)
print(content)
```

> replacement[hay]sreplacement[tack]
>
> replacement[hay]stack

```py
import re

haystack = 'haystack'
needle = '([A-RT-Z]+)'
replacement = r'replacement[\1]'

content = re.sub(needle, replacement, haystack, flags=re.IGNORECASE)
print(content)
```

> replacement[hay]sreplacement[tack]

```py
import re

haystack = 'foobar\nhoge\npiyo'
needle = '(^h)|(e$)'
replacement = '#'

content = re.sub(needle, replacement, haystack)
print(content)
content = re.sub(needle, replacement, haystack, flags=re.MULTILINE)
print(content)
```

> foobar
>
> hoge
>
> piyo

> foobar
>
> #og#
>
> piyo

```py
import re

haystack = 'foobar\nhoge\npiyo'
needle = 'r.h'
replacement = '#'

content = re.sub(needle, replacement, haystack)
print(content)
content = re.sub(needle, replacement, haystack, flags=re.DOTALL)
print(content)
```

> foobar
>
> hoge
>
> piyo

> fooba#oge
>
> piyo

##### ファイル名に使用できない文字を除去

```py
import re

haystack = 'foobar/hoge!piyo'
replacement = '-'

content = re.sub(r'[\\|/|:|?|.|"|<|>|\|]', replacement, haystack)
print(content)
```

> foobar-hoge!piyo

#### 一文字ごとの置換

```py
haystack = 'haystack'
print(haystack.translate(str.maketrans({'h': 'H', 'a': 'oo', 's': '', 'k': None})))
```

> Hooytooc

# I/O

## カレントディレクトリ

```py
import os


CURRENT_DIRECTORY = os.getcwd()
os.chdir(CURRENT_DIRECTORY)
```

### スクリプトファイルのパスを取得

```py
import os

print(os.getcwd())
print(__file__)

print(os.path.basename(__file__))
print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))
```

> /mnt/c/Users/y/Documents/GitHub/Python-cheatsheet
>
> python3-cwd.py
>
> python3-cwd.py
>
> /mnt/c/Users/y/Documents/GitHub/Python-cheatsheet/python3-cwd.py
>
> /mnt/c/Users/y/Documents/GitHub/Python-cheatsheet

## ファイル・フォルダの存在チェック

```
import os

FILEPATH = '.'
print(os.path.exists(FILEPATH) and os.path.isdir(FILEPATH))
print(os.path.exists(FILEPATH) and os.path.isfile(FILEPATH))

FILEPATH = './'
print(os.path.exists(FILEPATH) and os.path.isdir(FILEPATH))
print(os.path.exists(FILEPATH) and os.path.isfile(FILEPATH))

FILEPATH = './Python3.md'
print(os.path.exists(FILEPATH) and os.path.isdir(FILEPATH))
print(os.path.exists(FILEPATH) and os.path.isfile(FILEPATH))
```

> True
>
> False

> True
>
> False

> False
>
> True

## ファイル一覧

[python3md-cwd.py](python3md-cwd.py)

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
>
>   './test-glob/test-glob-1',
>
>   './test-glob/test-glob-2',
>
>   './test-glob/test-glob-3.dat'
>
> ]

```py
dirs = glob(os.path.join(DIRPATH, '**'), recursive=False)
```

> [
>
>   './test-glob/test-glob-1',
>
>   './test-glob/test-glob-2',
>
>   './test-glob/test-glob-3.dat'
>
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
>
>   './test-glob/test-glob-3.dat'
>
> ]

### 直下のフォルダ一覧を取得

```py
[f for f in glob(os.path.join(DIRPATH, '*')) if os.path.isdir(f)]
```

> [
>
>   './test-glob/test-glob-1',
>
>   './test-glob/test-glob-2'
>
> ]

### 再帰的にファイル・フォルダ一覧を取得 ⇒ _recursive_ が _True_ かつ、パスに _**_

```py
dirs = glob(os.path.join(DIRPATH, '**'), recursive=True)
```

> [
>
>   './test-glob/',
>
>   './test-glob/test-glob-1',
>
>   './test-glob/test-glob-1/test-glob-1-1',
>
>   './test-glob/test-glob-1/test-glob-1-1/test-glob-1-1-1.dat',
>
>   './test-glob/test-glob-1/test-glob-1-1/test-glob-1-1-2.dat',
>
>   './test-glob/test-glob-1/test-glob-1-2.dat',
>
>   './test-glob/test-glob-2',
>
>   './test-glob/test-glob-2/test-glob-2-2.dat',
>
>   './test-glob/test-glob-3.dat'
>
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
>
>   './test-glob',
>
>   './test-glob/test-glob-3.dat',
>
>   './test-glob/test-glob-1',
>
>   './test-glob/test-glob-1/test-glob-1-2.dat',
>
>   './test-glob/test-glob-1/test-glob-1-1',
>
>   './test-glob/test-glob-1/test-glob-1-1/test-glob-1-1-1.dat',
>
>   './test-glob/test-glob-1/test-glob-1-1/test-glob-1-1-2.dat',
>
>   './test-glob/test-glob-2',
>
>   './test-glob/test-glob-2/.test-glob-2-1.dat',
>
>   './test-glob/test-glob-2/test-glob-2-2.dat'
>
> ]

### 再帰的にフォルダ一覧を取得 ⇒ パスの末尾が _os.path.sep_

```py
[f for f in glob(os.path.join(DIRPATH, '**'), recursive=True) if os.path.isdir(f)]
```

> [
>
>   './test-glob/',
>
>   './test-glob/test-glob-1',
>
>   './test-glob/test-glob-1/test-glob-1-1',
>
>   './test-glob/test-glob-2'
>
> ]

```py
dirs = glob(os.path.join(DIRPATH, '**' + os.path.sep), recursive=True)
```

> [
>
>   './test-glob/',
>
>   './test-glob/test-glob-1/',
>
>   './test-glob/test-glob-1/test-glob-1-1/',
>
>   './test-glob/test-glob-2/'
>
> ]

### 再帰的にファイル一覧を取得

```py
dirs = glob(os.path.join(DIRPATH, os.path.join('**', '*.*')), recursive=True)
```

> [
>
>   './test-glob/test-glob-3.dat',
>
>   './test-glob/test-glob-1/test-glob-1-2.dat',
>
>   './test-glob/test-glob-1/test-glob-1-1/test-glob-1-1-1.dat',
>
>   './test-glob/test-glob-1/test-glob-1-1/test-glob-1-1-2.dat',
>
>   './test-glob/test-glob-2/test-glob-2-2.dat'
>
> ]

### ワイルドカードを利用

```py
dirs = glob(os.path.join(DIRPATH, os.path.join('**', '*-[0-1].???')), recursive=True)
```

> [
>
>   './test-glob/test-glob-1/test-glob-1-1/test-glob-1-1-1.dat'
>
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
