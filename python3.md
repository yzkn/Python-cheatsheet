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

## 比較

```py
x = None

if x is None: # Null判定
    print('True')
```

> True

```py
x = 1234567890
y = 1234567890
z = 12345678901

print(x == x)
print(x == y)
print(x != z)

print(x is x)
print(x is y)
print(x is z)
```

> True
>
> True
>
> True

> True
>
> False
>
> False

`is` での比較で、オブジェクトが同一でなくてもTrueが返る場合もある

```py
x = '1234567890'
print(len(x) is 10)
```

> True

```py
x = '1234567890'
y = '1234567890'
z = '12345678901'

print(x == x)
print(x == y)
print(x != z)

print(len(x) == 10)
print(len(x) != 11)

print(x is x)
print(x is y)
print(x is z)

print(1 < len(x) < 20)
print(1 < len(x) and len(x) < 20)
```

> True
>
> True
>
> True

> True
>
> True

> True
>
> True
>
> False

> True
>
> True

```py
def isNullOrEmpty(s): # string.isNullOrEmpty()
    if s is None or s == '':
        return True
    else:
        return False

isNullOrEmpty(None)
isNullOrEmpty('')
isNullOrEmpty('a')
```

> True
>
> True
>
> False

## 複数条件

```py
content = 'foobarhogepiyo'

# if "foo" in s and "bar" in s:
if all(map(content.__contains__, ('foo', 'bar'))):
    print("found")

# if "foo" in s or "hoge" in s:
if any(map(content.__contains__, ('foo', 'hoge'))):
    print("found")
```

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

## boolean

|  True  |  False  |
| ---- | ---- |
|  bool(1)<br>bool(2)<br>bool(-3)<br>bool(.1)<br>bool(1j)<br>bool('a')<br>bool([0])<br>bool((0,))<br>bool({0})  |  bool(0)<br><br><br>bool(0.)<br>bool(0j)<br>bool('')<br>bool([])<br>bool(())<br>bool({})  |

## int

### 数値の切り上げ・切り捨て

```py
# round(7 / 3, 2) # だと、小数点以下2桁で2.33
round(7 / 3) # 四捨五入
7 // 3 # 切り捨て
int(7 / 3) # 切り捨て
-(-7 // 3) # 切り上げ

import math
math.floor(7 / 3) # 切り捨て
math.ceil(7 / 3) # 切り上げ
```

> 2
>
> 2
>
> 2
>
> 3

> 2
>
> 3

## datetime

### 日時の比較

```py
import datetime
d1 = datetime.datetime(2016, 12, 31, 23, 59, 59)
d2 = datetime.datetime(2016, 1, 1, 0, 0, 0)
td = d1 - d2
print(td)
print(td.days)
print(td.seconds)

print(d2 < d1)
print(d2 > d1)
print(d1 == d2)
```

> 365 days, 23:59:59
>
> 365
>
> 86399

> True
>
> False
>
> False

### 現在日時

```py
from datetime import datetime

dt = datetime.today()
print(dt)

dt = datetime.now()
print(dt)

print(type(dt))

print(dt.year)
print(dt.month)
print(dt.day)
print(dt.weekday())  # 0:月曜; 6:日曜
print(dt.isoweekday())  # 1:月曜; 7:日曜
print(dt.hour)
print(dt.minute)
print(dt.second)
print(dt.microsecond)
```

> 2019-08-02 08:34:17.354115 \# today()
>
> 2019-08-02 08:34:17.354115 \# now()
>
> \<class 'datetime.datetime'\>
>
> 2019
>
> 8
>
> 2
>
> 8
>
> 34
>
> 17
>
> 354115

### 日付の生成

```py
from datetime import datetime
# 年・月・日は必須
dt = datetime(2019, 8, 2)
print(dt)
dt = datetime(2019, 8, 2, 1, 2, 3)
print(dt)
dt = datetime(2019, 8, 2, 1, 1, 63)
print(dt)
```

> 2019-08-02 00:00:00
>
> 2019-08-02 01:02:03
>
> ValueError: second must be in 0..59

#### 一定期間後の日付を生成

```py
from datetime import datetime
from datetime import timedelta

dt = datetime(2019, 8, 2)

# 一定期間後の日付を生成する場合はtimedeltaを使用
dt += timedelta(weeks=1, days=2, hours=3, minutes=4, seconds=5, milliseconds=6, microseconds=7)
print(dt)
```

> 2019-08-11 03:04:05.006007

#### 日時の要素を置換

```py
from datetime import datetime
from datetime import timedelta

dt = datetime(2019, 8, 2)

# 日時の要素を置換
print(dt.replace(day=22))
```

> 2019-08-22 00:00:00

#### 日付のリスト

```py
from datetime import date
from datetime import timedelta

f = '%Y-%m-%d'
n = 5
d = date(2019, 8, 2)
td = timedelta(weeks=1)

l = [(d + i * td).strftime(f) for i in range(n)]
print(l)
```

> ['2019-08-02', '2019-08-09', '2019-08-16', '2019-08-23', '2019-08-30']

### 指定日までの残り期間を取得

```py
from datetime import datetime
from datetime import timedelta

td = datetime(2019, 12, 24) - datetime(2019, 8, 2, 9, 0, 0)
print(td)
```

> 143 days, 15:00:00

### タイムゾーンを考慮したdatetime

#### datetimeパッケージのtimezoneモジュールを使用する場合

UTCからの時間差を指定して最低限の処理をすればよい場合

```py
from datetime import datetime, timedelta, timezone


# 現在時刻
print(datetime.now())
# 2019-08-08 12:17:51.835080

print(datetime.utcnow())
# 2019-08-08 03:17:53.033335


# 任意の時刻を設定
print(datetime(2019, 8, 7, 6, 54, 32, 1000))
# 2019-08-07 06:54:32.001000

print(datetime(2019, 8, 7, 6, 54, 32, 1000).tzinfo)
# None

print(datetime(2019, 8, 7, 6, 54, 32, 1000, tzinfo=timezone.utc))
# 2019-08-07 06:54:32.001000+00:00

print(datetime(2019, 8, 7, 6, 54, 32, 1000, tzinfo=timezone.utc).tzinfo)
# UTC

print(datetime(2019, 8, 7, 6, 54, 32, 1000, tzinfo=timezone(timedelta(hours=9))))
# 2019-08-07 06:54:32.001000+09:00
```

#### pytzを使用する場合

```py
#  $ pip install pytz

from pytz import timezone
from datetime import datetime

# datetime.now()で取得した日時をJSTとする

print(datetime.now())
# 2019-08-07 12:45:18.487441

print(datetime.now(timezone('UTC')))
# 2019-08-07 03:45:18.553981+00:00

print(datetime.now(tz=timezone('Asia/Tokyo')))
# 2019-08-07 12:45:18.613778+09:00

print(datetime.now(timezone('UTC')).astimezone(timezone('Asia/Tokyo')))
# 2019-08-07 12:45:18.754351+09:00

print(datetime.now(timezone('UTC')).astimezone(timezone('Europe/London')))
# 2019-08-07 04:45:18.634371+01:00

print(timezone('Asia/Tokyo').localize(datetime.now()))
# 2019-08-07 12:45:20.011410+09:00

#

print(timezone('UTC').localize(datetime.now()))
# 2019-08-07 12:45:18.760637+00:00

print(timezone('UTC').localize(datetime.now()).astimezone(timezone('Asia/Tokyo')))
# 2019-08-07 21:47:29.529403+09:00
```

### datetimeからdate

```py
from datetime import datetime

dt = datetime(2019, 8, 2)
print(dt.date())
print(type(dt.date()))

print(dt.date().weekday())
```

> 2019-08-02
>
> \<class 'datetime.date'\>
>
> 4

### datetimeからstr

```py
from datetime import datetime
now = datetime.now().strftime('%Y%m%d%H%M%S')
print(now)

print(datetime.now().isoformat()) # ISO形式
```

> 20190730121658
>
> 2019-07-30T12:16:58.427664

### strからdatetime、date

```py
from datetime import date
from datetime import datetime
tstr = '2019-07-30 12:16:58'
tdatetime = datetime.strptime(tstr, '%Y-%m-%d %H:%M:%S')
tdate = date(tdatetime.year, tdatetime.month, tdatetime.day)
print(tdatetime)
print(tdate)

tstr = '2019-07-30T12:16:58.001000'
tdatetime = datetime.fromisoformat(tstr) # ISO形式 (Python3.7以降)
print(tdatetime)
```

> 2019-07-30 12:16:58
>
> 2019-07-30

#### タイムゾーンを考慮したstrからdatetime

```py
from datetime import datetime
tstr = '2019/08/08 12:23:34+0900'
tdatetime = datetime.strptime(tstr, '%Y/%m/%d %H:%M:%S%z')
print(tdatetime)
print(tdatetime.tzinfo)
```

> 2019-08-08 12:23:34+09:00
>
> UTC+09:00

##### タイムゾーンを考慮したISO形式のstrからdatetime

dateutil.parserを利用する

```sh
$ pip install python-dateutil
```

```py
from datetime import datetime, timedelta, timezone
from dateutil.parser import parse


tstr = '2019-08-07T03:04:05.432100Z'

JST = timezone(timedelta(hours=+9), 'JST')
print(parse(tstr))
tdatetime = parse(tstr).astimezone(JST)
print(tdatetime)

print(tdatetime.astimezone(timezone('UTC'))) # 再度UTCに戻す
```

> 2019-08-07 03:04:05.432100+00:00
>
> 2019-08-07 12:04:05.432100+09:00

```py
import datetime
from dateutil.parser import parse


JST = datetime.timezone(datetime.timedelta(hours=+9), 'JST')

print(parse('2019-08-07T03:04:05.432100+00:00').astimezone(JST))
print(parse('2019-08-07T03:04:05.432100+0000').astimezone(JST))
print(parse('2019-08-07T03:04:05.432100+00').astimezone(JST))
print(parse('2019-08-07T03:04:05.432100Z').astimezone(JST))
print(parse('20190807T030405+00:00').astimezone(JST))
print(parse('20190807T030405Z').astimezone(JST))

print(parse('2019-08-07T03:04:05.432100+09:00').astimezone(JST))
print(parse('2019-08-07T03:04:05.432100JST').astimezone(JST))
```

> 2019-08-07 12:04:05.432100+09:00
>
> 2019-08-07 12:04:05.432100+09:00
>
> 2019-08-07 12:04:05.432100+09:00
>
> 2019-08-07 12:04:05.432100+09:00
>
> 2019-08-07 12:04:05+09:00
>
> 2019-08-07 12:04:05+09:00

> 2019-08-07 03:04:05.432100+09:00
>
> 2019-08-07 03:04:05.432100+09:00

#### [日付時刻のformat文字列に埋め込むディレクティブ](https://docs.python.org/ja/3/library/time.html#time.strftime)

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
needle = '([abd-jl-z]+)([ck]+)'

# コンパイル有
pattern = re.compile(needle)
matched = pattern.match(haystack)
print(matched)

# コンパイル無
matched = re.match(needle, haystack)
print(matched)

# 結果を取得
if matched:
    if matched.group() != '': # パターンが空文字とマッチするのを防ぐ場合
        print(matched.group())
        print(matched.start())
        print(matched.end())
        print(matched.span())

        ###

        print(matched.groups())
        for g in matched.groups():
            print(g)

        ###

        print(matched.group(0))
        print(matched.group(1))
        print(matched.group(2))
        print(matched.group(0, 1))

        ###

        print(matched.start(0))
        print(matched.end(1))
        print(matched.span(2))
```

> <_sre.SRE_Match object; span=(0, 8), match='haystack'>
>
> <_sre.SRE_Match object; span=(0, 8), match='haystack'>
>
> haystack
>
> 0
>
> 8
>
> (0, 8)
>
> \#\#\#
>
> ('haysta', 'ck')
>
> haysta
>
> ck
>
> \#\#\#
>
> haystack
>
> haysta
>
> ck
>
> ('haystack', 'haysta')
>
> \#\#\#
>
> 0
>
> 6
>
> (6, 8)

###### グループ化

```py
import re

haystack = 'haystack'
needle = '(h)([abd-gijl-z]+)([ck]+)'

matched = re.match(needle, haystack)
print(matched.groups())

print(matched.group(0))
print(matched.group(1))
print(matched.group(2))
print(matched.group(3))
```

> ('h', 'aysta', 'ck')
>
> haystack
>
> h
>
> aysta
>
> ck

```py
import re

haystack = 'haystack'
needle = r'(?P<ONE>h)(?P<two>[abd-gijl-z]+)(?P<three>[ck]+)'

matched = re.match(needle, haystack)
print(matched.group('ONE'))
print(matched.group('two'))
print(matched.group('three'))
print(matched.group(0, 'three'))

###

print(matched.groupdict())
```

> h
>
> aysta
>
> ck
>
> ('haystack', 'ck')
>
> \#\#\#
>
> {'ONE': 'h', 'two': 'aysta', 'three3': 'ck'}

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
searched = re.search(needle, haystack)
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
allfound = re.findall(needle, haystack)
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
allfound = re.finditer(needle, haystack)
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

##### フラグを利用

[モジュールコンテンツ](https://docs.python.org/ja/3/library/re.html#contents-of-module-re)

|  フラグ  |  効果  |
| --- | --- |
|  re.ASCII<br>re.A  |  \w 、\W 、\b 、\B 、\d 、\D 、\s 、および \S に、完全な Unicode マッチングではなく ASCII 限定マッチングを行わせます  |
|  re.DOTALL<br>re.S  | '.' 特殊文字を、改行を含むあらゆる文字にマッチさせます
|  re.IGNORECASE<br>re.I  |  大文字・小文字を区別しないマッチングを行います
|  re.MULTILINE<br>re.M  |  パターン文字 '^' は文字列の先頭で、および各行の先頭 (各改行の直後) で、マッチします。そしてパターン文字 '$' は文字列の末尾で、および各行の末尾 (各改行の直前) で、マッチします
|  re.VERBOSE<br>re.X  | 正規表現を、パターンの論理的な節を視覚的に分割し、コメントを加えることで、見た目よく読みやすく書けるようにします

```py
haystack = 'a12345.67890b'
patternA = re.compile(r'''\d +  # the integral part
                   \.    # the decimal point
                   \d *  # some fractional digits''', re.X)
patternB = re.compile(r'\d+\.\d*')
allfoundA = patternA.findall(haystack)
allfoundB = patternB.findall(haystack)

# 結果を取得
if allfoundA:
    print(allfoundA)

if allfoundB:
    print(allfoundB)
```

> ['12345.67890']
>
> ['12345.67890']

#### 文字種のフィルタリング

##### 文字列全体が半角英数だけ含まれているか検査

```py
import re

def validate(content):
    p = re.compile('[a-zA-Z0-9]+')
    if p.fullmatch(content):
        print('valid')
    else:
        print('invalid')

validate('abcdefg')

validate('abcdefgあいう')
```

> valid
>
> invalid

##### 半角カナなどが含まれていないか検査

```py
import re

def validate(content):
    p = re.compile('[｡-ﾟ]+') # 句読点などが不要であれば[ｦ-ﾟ]
    if p.search(content):
        print('found')
    else:
        print('valid')

validate('abcdefgあいう')
validate('abcdefgｱｲｳ')
```

> valid
>
> found

##### 文字種別のパターン

|  文字種  |  パターン  |  例  |
| --- | --- | --- |
|  半角英字  |  `'[a-zA-Z]+'`  |    |
|  半角数字  |  `'[0-9]+'`  |    |
|  ASCII文字  |  `'[\u0000-\u007F]+'`  |  `ABCabc!"#$%&`  |
|  半角記号  |  `'[\u0020-\u002F\u003A-\u0040\u005B-\u0060\u007B-\u007E]+'`  |  `!"#$%&`  |
|  全角英字  |  `'[ａ-ｚＡ-Ｚ]+'`  |    |
|  全角数字  |  `'[０-９]+'`  |    |
|  ローマ数字  |  `'[\u2160-\u217F]+'`  |  `ⅠⅡⅢ`  |
|  漢数字  |  `'[〇一二三四五六七八九十百千万億兆]+'`  |    |
|  ひらがな  |  `'[\u3041-\u309F]+'`  |    |
|  全角カタカナ  |  `'[\u30A1-\u30FF]+'`  |    |
|  半角カタカナ  |  `'[\uFF66-\uFF9F]+'`  |    |
|  漢字 (CJK統合漢字)  |  `'[\u4E00-\u9FFF]+'`  |    |

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

## リスト

### リストが空か検査

```py
a = []
if not a:
  print('empty')

if len(a)==0:
  print('empty')

if a == []:
  print('empty')
```

### リストを生成

```py
# リストをコピー
oldlist = ['foo', 'bar', 'hoge']
newlist = list(oldlist)
print(newlist)

# タプルからリストを生成
tpllist = list(('foo', 'bar', 'hoge'))
print(tpllist)

# range()を使って連番の要素を持つリストを生成
rnglist = list(range(5))
print(rnglist)

# 文字列からリストを生成
strlist = list('abcdefg')
print(strlist)
```

> \# newlist
>
> ['foo', 'bar', 'hoge']
>
> \# tpllist
>
> ['foo', 'bar', 'hoge']
>
> \# rnglist
>
> [0, 1, 2, 3, 4]
>
> \# strlist
>
> ['a', 'b', 'c', 'd', 'e', 'f', 'g']

### リストに要素を追加

```py
# append
lst = ['foo', 'bar', 'hoge']
lst.append('piyo')
print(lst)

lst.append(['fu', 'ga']) # appendの引数にリストを指定すると、リスト自体が新たな要素になる
print(lst)

# スライス
lst = ['foo', 'bar', 'hoge']
print(lst[0:len(lst)-1])
print(lst[0:len(lst)])

lst[len(lst):len(lst)] = ['fu', 'ga']
print(lst)

# 別のリスト(別のイテラブルオブジェクト)の要素を追加(連結)する
lst1 = ['foo', 'bar', 'hoge']
lst2 = ['fu', 'ga']
lst1.extend(lst2)
print(lst1)

lst1 = ['foo', 'bar', 'hoge']
lst2 = ['fu', 'ga']
lst1 = lst1 + lst2
print(lst1)

# リストの要素を繰り返す
lst = ['foo', 'bar', 'hoge']
lst= lst * 3
print(lst)
```

> \# append
>
> ['foo', 'bar', 'hoge', 'piyo']
>
> ['foo', 'bar', 'hoge', 'piyo', ['fu', 'ga']]
>
> \# スライス
>
> ['foo', 'bar']
>
> ['foo', 'bar', 'hoge']
>
> ['foo', 'bar', 'hoge', 'fu', 'ga']
>
> \# 別のリスト(別のイテラブルオブジェクト)の要素を追加(連結)する
>
> ['foo', 'bar', 'hoge', 'fu', 'ga']
>
> ['foo', 'bar', 'hoge', 'fu', 'ga']
>
> \# リストの要素を繰り返す
>
> ['foo', 'bar', 'hoge', 'foo', 'bar', 'hoge', 'foo', 'bar', 'hoge']

### リストの反復処理

#### インデックスを取得

```py
l = list(range(5, 10))
for (index, item) in enumerate(l):
    print(index, item)
```

> 0 5
>
> 1 6
>
> 2 7
>
> 3 8
>
> 4 9

#### 複数のリストを同時に繰り返す

```py
l1 = list(range(5))
l2 = list(range(5,10))

for (i1, i2) in zip(l1, l2):
    print(i1, i2)
```

> 0 5
>
> 1 6
>
> 2 7
>
> 3 8
>
> 4 9

```py
l1 = list(range(5))
l2 = list(range(5,8))

# 要素数の少ないリストの要素数分だけ繰り返す
for (i1, i2) in zip(l1, l2):
    print(i1, i2)
```

> 0 5
>
> 1 6
>
> 2 7

#### 多次元リスト

```py
l = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for (a, b, c) in zip(*l):
    print(a, b, c)
```

> 1 4 7
>
> 2 5 8
>
> 3 6 9

### リストの重複する要素を除去

```py
# 順番を無視
l = ['foo', 'bar', 'hoge', 'foo', 'bar', 'hoge', 'foo', 'bar', 'hoge']
ls = list(set(l))
print(ls)

# 順番を保存
# Python 3.6以降
ld = list(dict.fromkeys(l))
print(ld)

# Python 3.5以前
ss = sorted(set(l), key=l.index)
print(ss)

# リストが入れ子の場合
def uniq(td):
    f = []
    return [i for i in td if i not in f and not f.append(i)]

l2d = [['foo'], ['bar'], ['hoge'], ['foo'], ['bar'], ['hoge'], ['foo'], ['bar'], ['hoge']]
uniql2d = uniq(l2d)
print(uniql2d)
```

> \# 順番を無視
>
> ['hoge', 'bar', 'foo']
>
> \# 順番を保存
>
> ['foo', 'bar', 'hoge']
>
> ['foo', 'bar', 'hoge']
>
> \# リストが入れ子の場合
>
> [['foo'], ['bar'], ['hoge']]

### リストの重複する要素を抽出

```py
# 順番を無視
l = ['foo', 'bar', 'hoge', 'foo', 'bar', 'hoge', 'foo', 'bar', 'hoge']
sc = [x for x in set(l) if l.count(x) > 1]
print(sc)

# 順番を保存
# Python 3.6以降
df = [x for x in dict.fromkeys(l) if l.count(x) > 1]
print(df)

# Python 3.5以前
sk = sorted([x for x in set(l) if l.count(x) > 1], key=l.index)
print(ss)
```

> \# 順番を無視
>
> ['hoge', 'bar', 'foo']
>
> \# 順番を保存
>
> ['foo', 'bar', 'hoge']
>
> ['foo', 'bar', 'hoge']

### リストの内包表現

```py
l = list(range(100))

# 形式: [式 for 変数 in イテラブルオブジェクト if 条件式]

# 要素全てに処理を行う
strlist = [str(i) for i in l]
print(strlist)

# 条件に合致する要素のみからなるリストを生成(抽出)
fivelist = [i for i in l if i % 5 == 0 and i <= 50]
print(fivelist)

fivelist = [i  if i % 5 == 0 and i <= 50 else -1 for i in l]
print(fivelist)


# リストが入れ子の場合
def dupl(td):
    f = []
    return [i for i in td if td.count(i) > 1 and not f.append(i) and f.count(i) == 1]


l2d = [['foo'], ['bar'], ['hoge'], ['foo'], ['bar'], ['hoge'], ['foo'], ['bar'], ['hoge']]
dupll2d = dupl(l2d)
print(dupll2d)

```

> \# 要素全てに処理を行う
>
> ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99']
>
> \# 条件に合致する要素のみからなるリストを生成(抽出)
>
> [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
>
> [0, -1, -1, -1, -1, 5, -1, -1, -1, -1, 10, -1, -1, -1, -1, 15, -1, -1, -1, -1, 20, -1, -1, -1, -1, 25, -1, -1, -1, -1, 30, -1, -1, -1, -1, 35, -1, -1, -1, -1, 40, -1, -1, -1, -1, 45, -1, -1, -1, -1, 50, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
>
> \# リストが入れ子の場合
>
> [['foo'], ['bar'], ['hoge']]

## 辞書

### 追加・置換・削除

```py
dct = { 1:'first', 2:'two', 2:'second', 3:'third'}
# キーが同じ要素が追加されたら上書きされる(2:'two'ではなく2:'second'が残る)

# 追加
dct[4] = 'fourth'

# 置換
dct[2] = 'secondsecond'

# 検索
if 1 in dct:
    print(dct[1])
    print(dct.get(1))

print(dct.get(999)) # 指定したキーが存在しなければNoneを返す
print(dct.get(999, 'not found')) # 指定したキーが存在しなければ引数2を返す

dct.keys()
list(dct.keys())
dct.values()
list(dct.values())
dct.items()
list(dct.items())

# 要素を削除
del dct[1]

print(dct)

# 初期化
dct.clear()
dct = {}
```

> first
>
> first

> None
>
> not found

> dict_keys([1, 2, 3, 4])
>
> [1, 2, 3, 4]
>
> dict_values(['first', 'secondsecond', 'third', 'fourth'])
>
> ['first', 'secondsecond', 'third', 'fourth']
>
> ict_items([(1, 'first'), (2, 'secondsecond'), (3, 'third'), (4, 'fourth')])
>
> [(1, 'first'), (2, 'secondsecond'), (3, 'third'), (4, 'fourth')]

> {2: 'secondsecond', 3: 'third', 4: 'fourth'}

### 辞書を生成(リスト・タプルから変換／初期化)

```py
dct = {}
dct = { 1:'first', 2:'second', 3:'third', }
print(dct)


# 辞書をコピー
olddict = { 1:'first', 2:'second', 3:'third'}
newdict = dict(olddict)
print(newdict)

# リストから生成
lst = [[1, 'first'], [2, 'second'], [3, 'third']]
dct = dict(lst)
print(dct)

# キーと値が別のリスト
keys = [1, 2, 3]
values = ['first', 'second', 'third']
dct = dict(zip(keys, values))
print(dct)
```

> {1: 'first', 2: 'second', 3: 'third'}
>
> {1: 'first', 2: 'second', 3: 'third'}
>
> {1: 'first', 2: 'second', 3: 'third'}
>
> {1: 'first', 2: 'second', 3: 'third'}

```py
lst = [(1, 'first'), (2, 'second'), (3, 'third')]
dct = dict(lst)

tpl = ([1, 'first'], [2, 'second'], [3, 'third'])
dct = dict(tpl)

lst = ['1f', '2s', '3t']
dct = dict(lst)

tpl = ('1f', '2s', '3t')
dct = dict(tpl)
```

### 辞書を結合

```py
dct1 = dict(('1f', '2s', '3t'))
dct2 = dict(('4f', '5f', '6s'))
dct3 = dict(('4x', '8e', '9n'))

dct1.update(dct2)

print(dct1)
print(dct2)

dct1.update(dct3)

print(dct1)
print(dct3)

print({**dct2, **dct3})
```

> {'1': 'f', '2': 's', '3': 't', '4': 'f', '5': 'f', '6': 's'}
>
> {'4': 'f', '5': 'f', '6': 's'}

> {'1': 'f', '2': 's', '3': 't', '4': 'x', '5': 'f', '6': 's', '8': 'e', '9': 'n'}
>
> {'4': 'x', '8': 'e', '9': 'n'}
>
> {'4': 'x', '5': 'f', '6': 's', '8': 'e', '9': 'n'}

### 辞書のコピー

```py
dct1 = dict(('1f', '2s', '3t'))

dct2 = dct1
dct1['1'] = 'z'
print(dct1)
print(dct2)

dct1 = dict(('1f', '2s', '3t'))
dct2 = dct1.copy()
dct1['1'] = 'z'
print(dct1)
print(dct2)
```

> {'1': 'z', '2': 's', '3': 't'}
>
> {'1': 'z', '2': 's', '3': 't'}

> {'1': 'z', '2': 's', '3': 't'}
>
> {'1': 'f', '2': 's', '3': 't'}

### 辞書のキーと値を交換

```py
dct1 = dict(('1f', '2s', '3t'))
dct2 = {v: k for k, v in dct1.items()}
print(dct2)
```

> {'f': '1', 's': '2', 't': '3'}

### 辞書の値でソート

```py
dct1 = dict(('1f', '4s', '3t'))
dct2 = sorted(dct1.items(), key=lambda x: x[1], reverse=True)
print(dct2)
```

> [('3', 't'), ('4', 's'), ('1', 'f')]

### 辞書の重複する要素を除去 #TODO

```py

```

>
>
>

### 辞書の内包表現

```py
l = list(range(100))
strlist = [str(i) for i in l]

# {キー: 値 for 変数 in イテラブルオブジェクト}

# リストから辞書を生成
strdict = {li: str(li) for li in l}
print(strdict)

# キーと値が別のリスト
keys = [1, 2, 3]
values = ['first', 'second', 'third']
dct = {k: v for k, v in zip(keys, values)}
print(dct)

# 条件に合致する要素のみからなる辞書を生成(抽出)
fivedict = {k: v for k, v in zip(l, strlist) if k % 5 == 0 and k <= 50}
print(fivedict)

fivedict = {k: v if k % 5 == 0 and k <= 50 else -1 for k, v in zip(l, strlist)}
print(fivedict)
```

> \# リストから辞書を生成
>
> {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10', 11: '11', 12: '12', 13: '13', 14: '14', 15: '15', 16: '16', 17: '17', 18: '18', 19: '19', 20: '20', 21: '21', 22: '22', 23: '23', 24: '24', 25: '25', 26: '26', 27: '27', 28: '28', 29: '29', 30: '30', 31: '31', 32: '32', 33: '33', 34: '34', 35: '35', 36: '36', 37: '37', 38: '38', 39: '39', 40: '40', 41: '41', 42: '42', 43: '43', 44: '44', 45: '45', 46: '46', 47: '47', 48: '48', 49: '49', 50: '50', 51: '51', 52: '52', 53: '53', 54: '54', 55: '55', 56: '56', 57: '57', 58: '58', 59: '59', 60: '60', 61: '61', 62: '62', 63: '63', 64: '64', 65: '65', 66: '66', 67: '67', 68: '68', 69: '69', 70: '70', 71: '71', 72: '72', 73: '73', 74: '74', 75: '75', 76: '76', 77: '77', 78: '78', 79: '79', 80: '80', 81: '81', 82: '82', 83: '83', 84: '84', 85: '85', 86: '86', 87: '87', 88: '88', 89: '89', 90: '90', 91: '91', 92: '92', 93: '93', 94: '94', 95: '95', 96: '96', 97: '97', 98: '98', 99: '99'}
>
> \# キーと値が別のリスト
>
> {1: 'first', 2: 'second', 3: 'third'}
>
> \# 条件に合致する要素のみからなる辞書を生成(抽出)
>
> {0: '0', 5: '5', 10: '10', 15: '15', 20: '20', 25: '25', 30: '30', 35: '35', 40: '40', 45: '45', 50: '50'}
>
> {0: '0', 1: -1, 2: -1, 3: -1, 4: -1, 5: '5', 6: -1, 7: -1, 8: -1, 9: -1, 10: '10', 11: -1, 12: -1, 13: -1, 14: -1, 15: '15', 16: -1, 17: -1, 18: -1, 19: -1, 20: '20', 21: -1, 22: -1, 23: -1, 24: -1, 25: '25', 26: -1, 27: -1, 28: -1, 29: -1, 30: '30', 31: -1, 32: -1, 33: -1, 34: -1, 35: '35', 36: -1, 37: -1, 38: -1, 39: -1, 40: '40', 41: -1, 42: -1, 43: -1, 44: -1, 45: '45', 46: -1, 47: -1, 48: -1, 49: -1, 50: '50', 51: -1, 52: -1, 53: -1, 54: -1, 55: -1, 56: -1, 57: -1, 58: -1, 59: -1, 60: -1, 61: -1, 62: -1, 63: -1, 64: -1, 65: -1, 66: -1, 67: -1, 68: -1, 69: -1, 70: -1, 71: -1, 72: -1, 73: -1, 74: -1, 75: -1, 76: -1, 77: -1, 78: -1, 79: -1, 80: -1, 81: -1, 82: -1, 83: -1, 84: -1, 85: -1, 86: -1, 87: -1, 88: -1, 89: -1, 90: -1, 91: -1, 92: -1, 93: -1, 94: -1, 95: -1, 96: -1, 97: -1, 98: -1, 99: -1}

## タプル

```py

```

>
>
>

## セット

```py

```

>
>
>

# I/O

## パス文字列の操作

```py
import os

# パス文字列を組み立てる
print(os.path.sep)

joined = os.path.join('.', 'test' + '-' + 'join', 'test.txt')
print(joined)

# ファイル名を取得する
basename = os.path.basename('./test-join/test.txt')
print(basename)

# ディレクトリ名を取得する
dirname = os.path.dirname('./test-join/test.txt')
print(dirname)

# 拡張子を取得する
root, ext = os.path.splitext('./test-join/test.txt')
print(root, ext)
splitext = os.path.splitext('./test-join/test.txt')
print(splitext[0], splitext[1])

# 絶対パスを取得する
abspath = os.path.abspath('./test-join/test.txt')
print(abspath)
if os.path.isabs(abspath): # パス文字列が絶対パスか検査する
    print('ABSPATH')

# 2つのパス間の相対パスを取得する
relpath = os.path.relpath(abspath, '.')
print(relpath)

```

> \# パス文字列を組み立てる
>
> /
>
> './test-join/test.txt'
>
> \# ファイル名を取得する
>
> test.txt
>
> \# ディレクトリ名を取得する
>
> ./test-join
>
> \# 拡張子を取得する
>
> ./test-join/test .txt
>
> \# 絶対パスを取得する
>
> '/mnt/c/Users/y/Documents/GitHub/Python-cheatsheet/test-join/test.txt'
>
> ABSPATH
>
> \# 2つのパス間の相対パスを取得する
>
> test-join/test.txt'

### 親ディレクトリのパスを取得

```py
import os

def get_parent(path='.', lev=0):
    return str((os.path.sep).join(os.path.abspath(path).split(os.path.sep)[0:-1-lev]))

get_parent('__file__')
get_parent('__file__', 1)
```

> '/mnt/c/Users/y/Documents/GitHub'
>
> '/mnt/c/Users/y/Documents/GitHub/Python-cheatsheet'

```py
from pathlib import Path

def get_parent(path='.', lev=0):
    return Path(path).resolve().parents[lev]

get_parent('__file__')
get_parent('__file__', 1)
```

> PosixPath('/mnt/c/Users/y/Documents/GitHub/Python-cheatsheet')
>
> PosixPath('/mnt/c/Users/y/Documents/GitHub')

### Linux上でWindows形式のパスを操作

```py
import ntpath

bname = ntpath.basename('\\path\\to\\file')
print(bname)
```

> file

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

## ファイル・フォルダを存在チェック

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

## ファイル・フォルダの一覧を取得

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

## ファイル情報を取得

```py
import math

def roundstr(size):
    return '{}'.format(round(size, 1))

def human_readable(bytesize):
    if bytesize < 1024:
        return str(bytesize) + ' B'
    elif bytesize < 1024 ** 2:
        return roundstr(bytesize / 1024.0) + ' KB'
    elif bytesize < 1024 ** 3:
        return roundstr(bytesize / (1024.0 ** 2)) + ' MB'
    elif bytesize < 1024 ** 4:
        return roundstr(bytesize / (1024.0 ** 3)) + ' GB'
    elif bytesize < 1024 ** 5:
        return roundstr(bytesize / (1024.0 ** 4)) + ' TB'
    else:
        return str(bytesize) + ' B'

```

```py
from datetime import datetime, timezone, timedelta
import os

filepath = './Python3.md'

# 最終アクセス日時
# datetime.fromtimestamp(os.path.getatime(filepath))
atime = datetime.fromtimestamp(os.path.getatime(filepath), timezone(timedelta(hours=9)))
print(atime)
print(atime.tzinfo)

# 最終更新日時
# datetime.fromtimestamp(os.path.getmtime(filepath))
mtime = datetime.fromtimestamp(os.path.getmtime(filepath), timezone(timedelta(hours=9)))
print(mtime)
print(mtime.tzinfo)

# ファイルサイズ
size = os.path.getsize(filepath)
print(human_readable(size))
```

> 2019-08-02 21:40:27.305819+09:00
>
> UTC+09:00
>
> 2019-08-02 21:43:47.294729+09:00
>
> UTC+09:00
>
> 27661

## ファイルを作成

### touch()

```py
from pathlib import Path
def touch(filepath):
    Path(filepath).touch()



import os
def touch(filepath):
    if os.path.isfile(filepath):
        pass
    else:
        with open(filepath, 'w', encoding='UTF-8') as f:
            pass
```

### 既存のファイルがある場合はバックアップを作成して再作成

```py
from pathlib import Path
import os
import shutil


def touch(filepath):
    Path(filepath).touch()


FILEPATH = './test-file'

bkup_dt = datetime.now().strftime('%Y%m%d%H%M%S')
NEW_FILEPATH = os.path.splitext(FILEPATH)[0] + bkup_dt + os.path.splitext(FILEPATH)[1]

if os.path.exists(FILEPATH):
    RESULT_FILEPATH = shutil.move(
        FILEPATH,
        NEW_FILEPATH
        )
    print(RESULT_FILEPATH)

touch(FILEPATH)
```

## フォルダを作成

### 既存のフォルダがある場合はバックアップを作成して再作成

```py
import os
import shutil

DIRPATH = './test-folder/'

NEW_DIRPATH = os.path.dirname(DIRPATH) # './test-folder' # 末尾のスラッシュなし
bkup_dt = datetime.now().strftime('%Y%m%d%H%M%S')
NEW_DIRPATH += bkup_dt

if os.path.exists(DIRPATH):
    RESULT_DIRPATH = shutil.move(
        DIRPATH,
        NEW_DIRPATH
        )
    print(RESULT_DIRPATH)

# os.makedirs(DIRPATH), exist_ok=True
os.makedirs(DIRPATH)
```

## ファイルをコピー

```py
from pathlib import Path
import os
import shutil

srcpath = './test-copy1.txt'
dstpath = './test-copy2.txt'

Path(srcpath).touch()

# ファイル→ファイル (同名のファイルが既に存在すれば上書き)
result_path = shutil.copyfile(srcpath, dstpath)
print(result_path)

# ファイル→ファイル (同名のファイルが既に存在すれば上書き)
result_path = shutil.copy(srcpath, dstpath)
print(result_path)

dst1 = os.path.join(os.path.dirname(dstpath), 'test-copy2')
result_path = shutil.copy(srcpath, dst1)
print(result_path)

# ファイル→フォルダ (同名のファイルが既に存在すればエラー)
#  コピー先として指定されたディレクトリが予め存在し、その中に同名の既存ファイルが存在しなければコピーされる
dst2 = os.path.join(os.path.dirname(dstpath), 'test-copy2/') # dst1との差異は、末尾の'/'のみ
os.makedirs(dst2, exist_ok=True) # 予めディレクトリを作成しておかないとIsADirectoryError

dst_file_path = os.path.join(os.path.dirname(dst2), os.path.basename(srcpath))
if os.path.exists(dst_file_path):
    os.remove(dst_file_path)

result_path = shutil.copy(srcpath, dst2)
print(result_path)

# ファイル→ファイル (ファイル情報を保持)
result_path = shutil.copy2(srcpath, dstpath)
print(result_path)

result_path = shutil.copy2(srcpath, dst2) # 予めディレクトリを作成しておかないとIsADirectoryError
print(result_path)
```

> \# ファイル→ファイル (同名のファイルが既に存在すれば上書き)
>
> ./test-copy2.txt

> \# ファイル→ファイル (同名のファイルが既に存在すれば上書き)
>
> ./test-copy2.txt
>
>　./test-copy2

> \# ファイル→フォルダ (同名のファイルが既に存在すればエラー)
>
> ./test-copy2/test-copy1.txt

> \# ファイル→ファイル (ファイル情報を保持)
>
> ./test-copy2.txt
>
> ./test-copy2/test-copy1.txt

## フォルダをコピー

```py
from glob import glob
from pathlib import Path
import os
import shutil


def touch(filepath):
    Path(filepath).touch()


srcpath = './test-dirtree/dir1'
srcfpath = './test-dirtree/dir1/file1.txt'
dstpath = './test-dirtree/dir2'

os.makedirs(srcpath, exist_ok=True)
touch(srcfpath)

result_path = shutil.copytree(srcpath, dstpath) # ディレクトリが既に存在するとFileExistsError
print(result_path)

glob('./test-dirtree/**', recursive=True)
```

> './test-dirtree/dir2'
>
> [
>
>   './test-dirtree/',
>
>   './test-dirtree/dir1',
>
>   './test-dirtree/dir1/file1.txt',
>
>   './test-dirtree/dir2',
>
>   './test-dirtree/dir2/file1.txt'
>
> ]

```py
from glob import glob
from pathlib import Path
import os
from distutils.dir_util import copy_tree


def touch(filepath):
    Path(filepath).touch()


srcpath = './test-dirtree/dir1'
srcfpath = './test-dirtree/dir1/file1.txt'
dstpath = './test-dirtree/dir2'

os.makedirs(srcpath, exist_ok=True)
touch(srcfpath)
os.makedirs(dstpath, exist_ok=True)

# distutils.dir_util
result_path = copy_tree(srcpath, dstpath) # ディレクトリが既に存在してもコピーされる
print(result_path)

glob('./test-dirtree/**', recursive=True)
```

> ['./test-dirtree/dir2/file1.txt']
>
> ['./test-dirtree/', './test-dirtree/dir1', './test-dirtree/dir1/file1.txt', './test-dirtree/dir2', './test-dirtree/dir2/file1.txt']

## ファイルをリネーム

```py
from glob import glob
from pathlib import Path
import os
import shutil


def touch(filepath):
    Path(filepath).touch()


dirpath = './test-rename/'
srcpath = './test-rename/file1.txt'
dstpath = './test-rename/file2.txt'

os.makedirs(dirpath, exist_ok=True)
touch(srcpath)

os.rename(srcpath, dstpath)
glob('./test-rename/**', recursive=True)

touch(srcpath)
glob('./test-rename/**', recursive=True)

os.rename(srcpath, dstpath) # dstpathのファイルが既に存在すると、上書きされる
glob('./test-rename/**', recursive=True)
```

> ['./test-rename/', './test-rename/file2.txt']
>
> ['./test-rename/', './test-rename/file1.txt', './test-rename/file2.txt']
>
> ['./test-rename/', './test-rename/file2.txt'] \# dstpathのファイルが既に存在すると、上書きされる

## フォルダをリネーム

```py
from glob import glob
from pathlib import Path
import os
import shutil


def touch(filepath):
    Path(filepath).touch()


srcpath = './test-rename/dir1'
srcfpath = './test-rename/dir1/file1.txt'
dstpath = './test-rename/dir2'
dstfpath = './test-rename/dir2/file1.txt'

# 移動元ディレクトリと配下のファイルが存在
shutil.rmtree(srcpath, ignore_errors=True)
shutil.rmtree(dstpath, ignore_errors=True)
os.makedirs(srcpath, exist_ok=True)
# os.makedirs(dstpath, exist_ok=True)
touch(srcfpath)
# touch(dstfpath)

os.rename(srcpath, dstpath)
glob('./test-rename/**', recursive=True)

# 移動元ディレクトリと配下のファイル、移動先ディレクトリが存在
shutil.rmtree(srcpath, ignore_errors=True)
shutil.rmtree(dstpath, ignore_errors=True)
os.makedirs(srcpath, exist_ok=True)
os.makedirs(dstpath, exist_ok=True)
touch(srcfpath)
# touch(dstfpath)

os.rename(srcpath, dstpath)
glob('./test-rename/**', recursive=True)

# 移動元ディレクトリと配下のファイル、移動先ディレクトリと配下の(同名)ファイルが存在
shutil.rmtree(srcpath, ignore_errors=True)
shutil.rmtree(dstpath, ignore_errors=True)
os.makedirs(srcpath, exist_ok=True)
os.makedirs(dstpath, exist_ok=True)
touch(srcfpath)
touch(dstfpath)

os.rename(srcpath, dstpath) # OSError: [Errno 39] Directory not empty: './test-rename/dir1' -> './test-rename/dir2'
```

> \# 移動元ディレクトリと配下のファイルが存在
>
> ['./test-rename/', './test-rename/dir2', './test-rename/dir2/file1.txt']

> \# 移動元ディレクトリと配下のファイル、移動先ディレクトリが存在
>
> ['./test-rename/', './test-rename/dir2', './test-rename/dir2/file1.txt']

> \# 移動元ディレクトリと配下のファイル、移動先ディレクトリと配下の(同名)ファイルが存在
>
> OSError: [Errno 39] Directory not empty: './test-rename/dir1' -> './test-rename/dir2'

## ファイルを移動

```py
from glob import glob
from pathlib import Path
import os
import shutil


def touch(filepath):
    Path(filepath).touch()


srcpath = './test-move/dir1'
srcfpath = './test-move/dir1/file1.txt'
dstpath = './test-move/dir2'
dstfpath = './test-move/dir2/file2.txt'

os.makedirs(srcpath, exist_ok=True)
touch(srcfpath)
os.makedirs(dstpath, exist_ok=True)

result_path = shutil.move(srcfpath, dstpath)
print(result_path)

touch(srcfpath)

result_path = shutil.move(srcfpath, dstfpath)
print(result_path)
```

> ./test-move/dir2/file1.txt
>
> ./test-move/dir2/file2.txt

## フォルダを移動

```py
from glob import glob
from pathlib import Path
import os
import shutil


def touch(filepath):
    Path(filepath).touch()


srcpath = './test-move/dir1'
srcfpath = './test-move/dir1/file1.txt'
dstpath = './test-move/dir2'
dstdpath = './test-move/dir2/dir1'
dstfpath = './test-move/dir2/file1.txt'
dstfpath2 = './test-move/dir2/dir1/file1.txt'


# 移動元ディレクトリと配下のファイルが存在
os.makedirs(srcpath, exist_ok=True)
touch(srcfpath)
shutil.rmtree(dstpath, ignore_errors=True)

result_path = shutil.move(srcpath, dstpath)
print(result_path)

glob('./test-move/**', recursive=True)

# 移動元ディレクトリと配下のファイル、移動先ディレクトリが存在
os.makedirs(srcpath, exist_ok=True)
touch(srcfpath)
os.remove(dstfpath)

result_path = shutil.move(srcpath, dstpath)
print(result_path)

glob('./test-move/**', recursive=True)

# 移動元ディレクトリと配下のファイル、移動先ディレクトリと配下の(同名)ファイルが存在
os.makedirs(srcpath, exist_ok=True)
touch(srcfpath)
shutil.rmtree(dstdpath, ignore_errors=True)
touch(dstfpath2)

result_path = shutil.move(srcpath, dstpath)

glob('./test-move/**', recursive=True) # shutil.Error: Destination path './test-move/dir2/dir1' already exists
```

> \# 移動元ディレクトリと配下のファイルが存在
>
> ./test-move/dir2
>
> ['./test-move/', './test-move/dir2', './test-move/dir2/file1.txt']

> \# 移動元ディレクトリと配下のファイル、移動先ディレクトリが存在
>
> ./test-move/dir2/dir1
>
> ['./test-move/', './test-move/dir2', './test-move/dir2/dir1', './test-move/dir2/dir1/file1.txt']

> \# 移動元ディレクトリと配下のファイル、移動先ディレクトリと配下の(同名)ファイルが存在
>
> shutil.Error: Destination path './test-move/dir2/dir1' already exists

## ファイルを削除

### 特定のファイルを削除

```py
from pathlib import Path
import os


def touch(filepath):
    Path(filepath).touch()


path = './test-remove.txt'
touch(path)

# ファイルを削除
os.remove(path)

if not os.path.exists(path):
    print('removed')
```

> removed

### ファイルを検索して削除

```py
from glob import glob
from pathlib import Path
import os


def touch(filepath):
    Path(filepath).touch()


path = './test-remove'
fpath = './test-remove/test1.txt'
os.makedirs(path, exist_ok=True)
touch(fpath)

# ファイルを検索して削除
[os.remove(f) for f in glob("./test-remove/*.txt")]

os.rmdir(path)
```

## フォルダを削除

```py
from pathlib import Path
import os
import shutil


def touch(filepath):
    Path(filepath).touch()


path = './test-remove'
fpath = './test-remove/test1.txt'

os.makedirs(path, exist_ok=True)

os.remove(path) # IsADirectoryError

# 空フォルダを削除
os.rmdir(path)

os.makedirs(path, exist_ok=True)
touch(fpath)

# 中身ごとフォルダを削除
# shutil.rmtree(path, ignore_errors=True)
shutil.rmtree(path)

if not os.path.exists(path):
    print('removed')
```

> removed

## ファイル圧縮

### shutilを使ってフォルダごと圧縮

```py
from glob import glob
from pathlib import Path
import os
import shutil
import zipfile


def touch(filepath):
    Path(filepath).touch()


archive_path = './test-archive/archive' # 拡張子なし : './test-archive/archive.zip'が作成される

srcdpath1 = './test-archive/dir1'
srcdpath2 = './test-archive/dir1/dir2'
srcfpath1 = './test-archive/dir1/file1.txt'
srcfpath2 = './test-archive/dir1/dir2/file2.txt'

os.makedirs(srcdpath1, exist_ok=True)
os.makedirs(srcdpath2, exist_ok=True)
touch(srcfpath1)
touch(srcfpath2)

# base_dirを指定しない
shutil.make_archive(archive_path, 'zip', root_dir=srcdpath1, base_dir=None)

with zipfile.ZipFile(archive_path + '.zip') as zip_contents:
    print(zip_contents.namelist())

# base_dirを指定する
rlpath = os.path.relpath(srcdpath2, srcdpath1) # dir2
shutil.make_archive(archive_path, 'zip', root_dir=srcdpath1, base_dir=rlpath) # 既存の圧縮ファイルがある場合は圧縮ファイル自体が上書きされる

with zipfile.ZipFile(archive_path + '.zip') as zip_contents:
    print(zip_contents.namelist())

```

> \# base_dirを指定しない
>
> '/mnt/c/Users/y/Documents/GitHub/Python-cheatsheet/test-archive/archive.zip'
>
> ['dir2/', 'file1.txt', 'dir2/file2.txt']

> \# base_dirを指定する
>
> '/mnt/c/Users/y/Documents/GitHub/Python-cheatsheet/test-archive/archive.zip'
>
> ['dir2/', 'dir2/file2.txt']

### 個別にファイルを追加して圧縮ファイルを作成

```py
from glob import glob
from pathlib import Path
import os
import zipfile


def touch(filepath):
    Path(filepath).touch()


archive_path = './test-archive/archive.zip'

srcdpath1 = './test-archive/dir1'
srcdpath2 = './test-archive/dir1/dir2'
srcfpath1 = './test-archive/dir1/file1.txt'
srcfpath2 = './test-archive/dir1/dir2/file2.txt'

os.makedirs(srcdpath1, exist_ok=True)
os.makedirs(srcdpath2, exist_ok=True)
touch(srcfpath1)
touch(srcfpath2)



with zipfile.ZipFile(archive_path, 'w', compression=zipfile.ZIP_DEFLATED) as z:
    z.write(srcdpath1, arcname=srcdpath1)
    z.write(srcdpath2, arcname=srcdpath2)
    z.write(srcfpath1, arcname=srcfpath1)

with zipfile.ZipFile(archive_path) as zip_contents:
    print(zip_contents.namelist())

# 既存の圧縮ファイルがある場合は圧縮ファイル自体が上書きされる
with zipfile.ZipFile(archive_path, 'w', compression=zipfile.ZIP_DEFLATED) as z:
    z.write(srcdpath1, arcname=srcdpath1)
    z.write(srcdpath2, arcname=srcdpath2)
    z.write(srcfpath2, arcname=srcfpath2)

with zipfile.ZipFile(archive_path) as zip_contents:
    print(zip_contents.namelist())

# 既存の圧縮ファイルに、ファイルを追加する
with zipfile.ZipFile(archive_path, 'a', compression=zipfile.ZIP_DEFLATED) as z:
    z.write(srcdpath1, arcname=srcdpath1)
    z.write(srcdpath2, arcname=srcdpath2)
    z.write(srcfpath1, arcname=srcfpath1)
    z.write(srcfpath2, arcname=srcfpath2)

with zipfile.ZipFile(archive_path) as zip_contents:
    print(zip_contents.namelist())
```

> ['test-archive/dir1/', 'test-archive/dir1/dir2/', 'test-archive/dir1/file1.txt']
>
> \# 既存の圧縮ファイルがある場合は圧縮ファイル自体が上書きされる
>
> ['test-archive/dir1/', 'test-archive/dir1/dir2/', 'test-archive/dir1/dir2/file2.txt']
>
> \# 既存の圧縮ファイルに、ファイルを追加する
>
> UserWarning: Duplicate name: 'test-archive/dir1/'
>
> UserWarning: Duplicate name: 'test-archive/dir1/dir2/'
>
> UserWarning: Duplicate name: 'test-archive/dir1/dir2/file2.txt'
>
> [
>   'test-archive/dir1/',
>   'test-archive/dir1/dir2/',
>   'test-archive/dir1/dir2/file2.txt',
>   'test-archive/dir1/',
>   'test-archive/dir1/dir2/',
>   'test-archive/dir1/file1.txt',
>   'test-archive/dir1/dir2/file2.txt'
> ]

## ファイル解凍

```py
import zipfile


archive_path = './test-archive/archive.zip'
extract_path = '.'


# 内容を確認
with zipfile.ZipFile(archive_path) as zip_contents:
    print(zip_contents.namelist())


with zipfile.ZipFile(archive_path) as zip_contents:
    zip_contents.extractall(extract_path)

# 特定のファイルのみ解凍
with zipfile.ZipFile(archive_path) as zip_contents:
    result_path = zip_contents.extract('test-archive/dir1/file1.txt', extract_path)
    print(result_path)


# パスワードつきzipファイルを解凍
pw = 'Password'
with zipfile.ZipFile(archive_path) as zip_contents:
    zip_contents.extractall(extract_path, pwd=pw)

with zipfile.ZipFile(archive_path) as zip_contents:
    result_path = zip_contents.extract('test-archive/dir1/file1.txt', extract_path, pwd=pw)
    print(result_path)
```

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

# モジュール

## モジュールの読み込み

```py
# import <モジュール名>
import os

print(type(os))

print(os)

print(type(os.path.join))

print(type(os.sep))
```

> \<class 'module'\>
>
> \<module 'os' from '/home/y/.pyenv/versions/3.6.8/lib/python3.6/os.py'\>
>
> \<class 'function'\>
>
> <class 'str'>

```py
from glob import glob, iglob
```

## 外部スクリプトの読み込み

* test-import/main.py

```py
# subfile.py
import subfile
subfile.hello()


# subdir/main.py
import subdir.main
subdir.main.hello()

# or

from subdir import main
main.hello()


# subdir/subfile.py
import subdir.subfile
subdir.subfile.hello()
```

* test-import/main2.py

```py
from subdir import *
main.hello()
subfile.hello()
```

* test-import/subfile.py

```py
def hello():
    print('test-import/subdir.py hello()')
```

* test-import/subdir/main.py

```py
def hello():
    print('test-import/subdir/main.py hello()')
```

* test-import/subdir/subfile.py

```py
def hello():
    print('test-import/subdir/subfile.py hello()')
```

* test-import/subdir/__init__.py

```py
from glob import glob
from importlib import import_module
import os
import re
import sys

def main():
    myself = sys.modules[__name__]
    mod_paths = glob(os.path.join(os.path.dirname(os.path.abspath(__file__)), '*.py'))
    for py_file in mod_paths:
        mod_name = os.path.splitext(os.path.basename(py_file))[0]
        if re.search('.*__init__.*',mod_name) is None:
            mod = import_module(__name__+ '.' + mod_name)
            for m in mod.__dict__.keys():
                if not m in ['__builtins__', '__doc__', '__file__', '__name__', '__package__']:
                    myself.__dict__[m] = mod.__dict__[m]
main()
```

```sh
$ python test-import/main.py
```

> test-import/subdir.py hello()
>
> test-import/subdir/main.py hello()
>
> test-import/subdir/main.py hello()
>
> test-import/subdir/subfile.py hello()

```sh
$ python test-import/main2.py
```

> test-import/subdir/main.py hello()
>
> test-import/subdir/subfile.py hello()

## 一時的にモジュール検索パスを追加

```py
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
```

## 恒久的にモジュール検索パスを追加

```sh
export PYTHONPATH="/path/to/module:$PYTHONPATH"`
```

site-packagesフォルダの中に、`*.pth`ファイル(ファイル名は任意)を作成し、各行にパスを追加

* example.ptn

```py
# foo package configuration

path/to/module
```

# pydoc

* python3md-pydoc.py

```py
#!/usr/bin/python
# coding: UTF-8

'''
ファイルの説明
'''
__author__ = 'YA-androidapp<ya.androidapp@gmail.com>'
# __status__ = 'production'
__status__ = 'dev'
__version__ = '0.0.1'
__date__    = '01 Aug. 2019'
class Util():
    '''
    クラスの説明
    '''
    def init():
        '''
        メソッドの説明
        '''
        pass

def main():
    print('main')

if __name__ == '__main__':
    main()
```

```sh
# コンソールに出力
$ pydoc python3md-pydoc

# HTMLファイルを生成
$ pydoc python3md-pydoc
```

# エラーメッセージ

##
