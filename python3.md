# おまじない

## shebang

```py
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# #から行末まではコメント
# 1行目または2行目のコメントで、正規表現coding[=:]\s*([-\w.]+)にマッチする場合はエンコーディング宣言として扱われる
```

# 命名規則

| 項目 | 文字種 | 区切り文字 |
| --- | --- | --- |
| パッケージ | 英数小文字 | - |
| モジュール | 英数小文字 | アンダースコア |
| クラス, 例外, 型変数 | 英数大小文字 | 大文字 |
| メソッド, 関数,変数 | 英数小文字 | アンダースコア |
| 定数 | 英数大文字 | アンダースコア |

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

```py
# 三項演算子
t = 'True'
f = 'False'
c = t if 1 == 1 else f  # 'True'
```

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
1 < a < 5
```

```py
content = 'foobarhogepiyo'

# if "foo" in s and "bar" in s:
if all(map(content.__contains__, ('foo', 'bar'))):
    print("found")

# if "foo" in s or "hoge" in s:
if any(map(content.__contains__, ('foo', 'hoge'))):
    print("found")
```

# 変数

```py
name = 3

# 異なる方の値を代入
name = "Suzuki"

# 変数の削除
del name

print(name)
```

```py
# 多重代入
x = y = z = 0
```

> NameError: name 'name' is not defined

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

```py
True == 1  # True
False == 0  # True
True + False  # 1
```

## int

```py
i = 123          # 10整数
i = 0b11111111  # 2進数
i = 0o777  # 8進数
i = 0xffff       # 16進数
i = int("1")  # 文字列型からの変換


# long(Python3ではint型として扱う)
# l = 1234567890123456789012345678901234567890123456789012345678901234567890L # Python 2
l = 1234567890123456789012345678901234567890123456789012345678901234567890
```

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

## float

```py
f = 1.23
f = 1.2e3     # 1.2 * 10 ** 3
f = 1.2E-3    # 1.2 * 10 ** -3
```

## complex(虚数)

```py
c = 1j
c = 2.3J
```

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

| 種類 | 内容 |
| --- | --- |
| aware | TimeZone情報を持つdatetimeオブジェクト(tzinfo属性) |
| naive | TimeZone情報を持たないdatetimeオブジェクト |

```py
from datetime import datetime, timedelta, timezone

# 現在時刻
print(datetime.now())
# 2019-08-08 12:17:51.835080

print(datetime.utcnow())
# 2019-08-08 03:17:53.033335
```

##### 生成

```py
from datetime import datetime, timedelta, timezone

# 任意の時刻を設定
print(datetime(2019, 8, 7, 6, 54, 32, 1000))
# 2019-08-07 06:54:32.001000

print(type(datetime(2019, 8, 7, 6, 54, 32, 1000)))
# <class 'datetime.datetime'>

print(datetime(2019, 8, 7, 6, 54, 32, 1000).tzinfo)
# None

print(datetime(2019, 8, 7, 6, 54, 32, 1000, tzinfo=timezone.utc))
# 2019-08-07 06:54:32.001000+00:00

print(datetime(2019, 8, 7, 6, 54, 32, 1000, tzinfo=timezone.utc).tzinfo)
# UTC

print(datetime(2019, 8, 7, 6, 54, 32, 1000, tzinfo=timezone(timedelta(hours=9))))
# 2019-08-07 06:54:32.001000+09:00
```

##### タイムゾーンを変更(変更前と同じ時刻)

```py
print(datetime(2019, 8, 7, 6, 54, 32, 1000, tzinfo=timezone(timedelta(hours=9))).astimezone(timezone(timedelta(hours=8))))
# 2019-08-07 06:54:32.001000+09:00 → 2019-08-07 05:54:32.001000+08:00

# Python3.6以降の場合、naiveなdatetimeオブジェクトにもastimezone関数を実行できる(ローカルのタイムゾーンから変換される)
print(datetime(2019, 8, 7, 6, 54, 32, 1000).astimezone(timezone(timedelta(hours=8))))
# 2019-08-07 06:54:32.001000+09:00 → 2019-08-07 05:54:32.001000+08:00
```

##### タイムゾーンを置換(変更前と異なる時刻)

```py
print(datetime(2019, 8, 7, 6, 54, 32, 1000, tzinfo=timezone(timedelta(hours=9))).replace(tzinfo=timezone.utc))
# 2019-08-07 06:54:32.001000+09:00 → 2019-08-07 06:54:32.001000+00:00

# タイムゾーンの削除
print(datetime(2019, 8, 7, 6, 54, 32, 1000, tzinfo=timezone(timedelta(hours=9))).replace(tzinfo=None))
# 2019-08-07 06:54:32.001000+09:00 → 2019-08-07 06:54:32.001000

```

#### pytzを使用する場合

##### 現在日時から生成

```py
#  $ pip install pytz

from pytz import timezone
from datetime import datetime

# datetime.now()で取得した日時をJSTとする

print(datetime.now())
# 2019-08-07 12:45:18.487441

print(type(datetime.now()))
# <class 'datetime.datetime'>

print(timezone('UTC'))
# UTC
print(type(timezone('UTC')))
# <class 'pytz.UTC'>
print(type(timezone('Asia/Tokyo')))
# <class 'pytz.tzfile.Asia/Tokyo'>

print(datetime.now(timezone('UTC')))
# 2019-08-07 03:45:18.553981+00:00

print(datetime.now(tz=timezone('Europe/London')))
# 2019-08-07 04:45:18.553981+01:00

print(datetime.now(tz=timezone('Asia/Tokyo')))
# 2019-08-07 12:45:18.553981+09:00

print(datetime.now(timezone('UTC')).astimezone(timezone('Europe/London')))
# 2019-08-07 04:45:18.634371+01:00

print(datetime.now(timezone('UTC')).astimezone(timezone('Asia/Tokyo')))
# 2019-08-07 12:45:18.754351+09:00

#

print(timezone('Europe/London').localize(datetime.now()))
# 2019-08-07 12:45:20.011410+01:00

print(timezone('Asia/Tokyo').localize(datetime.now()))
# 2019-08-07 12:45:20.011410+09:00

#

print(timezone('UTC').localize(datetime.now()))
# 2019-08-07 12:45:18.760637+00:00

print(timezone('UTC').localize(datetime.now()).astimezone(timezone('Europe/London')))
# 2019-08-07 13:45:18.760637+09:00

print(timezone('UTC').localize(datetime.now()).astimezone(timezone('Asia/Tokyo')))
# 2019-08-07 21:45:18.760637+09:00
```

##### 任意の日時を生成

```py
from datetime import datetime
from pytz import timezone

date = datetime(2019, 8, 9, 10)

tz = timezone('Asia/Tokyo')
print(tz.localize(date))

tz = timezone('Europe/London')
print(tz.localize(date))

tz = timezone('UTC')
print(tz.localize(date))
```

> 2019-08-09 10:11:12+09:00
>
> 2019-08-09 10:11:12+01:00
>
> 2019-08-10 02:00:00+00:00

##### サマータイム終了時点を跨いだ日時の加算

```py
from datetime import datetime, timedelta
from pytz import timezone

tz = timezone('Europe/London')
dt = datetime(year=2019, month=10, day=27, hour=0, minute=58)
localized = tz.normalize(tz.normalize(tz.localize(dt)) + timedelta(minutes=1))
print(localized)

dt = datetime(year=2019, month=10, day=27, hour=0, minute=59)
localized = tz.normalize(tz.normalize(tz.localize(dt)) + timedelta(minutes=1))
print(localized)

dt = datetime(year=2019, month=10, day=27, hour=0, minute=59, second=59)
localized = tz.normalize(tz.normalize(tz.localize(dt)) + timedelta(seconds=1))
print(localized)

dt = datetime(year=2019, month=10, day=27, hour=1, minute=0, second=0)
localized = tz.normalize(tz.normalize(tz.localize(dt)) + timedelta(seconds=1))
print(localized)

dt = datetime(year=2019, month=10, day=27, hour=1, minute=0)
localized = tz.normalize(tz.normalize(tz.localize(dt)) + timedelta(minutes=1))
print(localized)
```

> 2019-10-27 00:59:00+01:00
>
> 2019-10-27 01:00:00+01:00
>
> 2019-10-27 01:00:00+01:00
>
> 2019-10-27 01:00:01+00:00
>
> 2019-10-27 01:01:00+00:00

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

#      '2019-07-30T12:16:58.001000+00:00'
tstr = '2019-07-30T12:16:58.001000Z'
tdatetime = datetime.fromisoformat(tstr.replace('Z', '+00:00')) # ISO形式 (Python3.7以降) 末尾にUTCを示すZがついているとエラーになるので置換する
print(tdatetime)

tstr = '2019-07-30T12:16:58.001000+09:00'
tdatetime = datetime.fromisoformat(tstr) # ISO形式 (Python3.7以降)
print(tdatetime)
```

> 2019-07-30 12:16:58
>
> 2019-07-30
>
> 2019-07-30 12:16:58.001000
>
> 2019-07-30 12:16:58.001000+00:00
>
> 2019-07-30 12:16:58.001000+09:00

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
print(r'str\nstr') # エスケープシーケンスが無視される
print(R'str\nstr') # エスケープシーケンスが無視される
print(str(123))
print('cq' * 3) # 文字列の繰り返し
print('cq' 'cq' 'cq') # 文字列を演算子なしでつなげる
```

> str
>
> str

> str
>
> str

> str\nstr

> str\nstr

> 123

> cqcqcq
>
> cqcqcq

### ヒアドキュメント

```py
hoge = """abc
def
ghi"""

print(hoge)
```

> abc
>
> def
>
> ghi

```py
piyo = 'abc \
def'

print(piyo)

fuga = ('abc'
    'def'
    'ghi')

print(fuga)
```

> abc def
>
> abcdefghi

### format

```py
print('{}'.format(1))
```

> 1

```py
print("%s" % "ABC")  # 文字列： ABC
print("%d" % 123)  # 整数　： 123
print("%f" % 1.23)  # 実数　： 1.23
print("%x" % 255)  # 16進数： ff
print("%o" % 255)  # 8進数： 377
print("%d%%" % 100)  # %自体： 100%

print("|%5s|" % 'ABC')  # => |  ABC| : 右寄せ
print("|%-5s|" % 'ABC')  # => |ABC  | : 左寄せ
print("|%5d|" % 123)  # => |  123| : 右寄せ
print("|%-5d|" % 123)  # => |123  | : 左寄せ
print("|%+5d|" % 123)  # => | +123| : ±符号付き
print("|%5.2f|" % 1.23)  # => | 1.23| : 整数部の桁数.小数部の桁数
print("|%05d|" % 123)  # => |00123| : 0埋め
```

### エスケープシーケンス

| 項目 | 内容 |
| --- | --- |
| "\\" | \ |
| "\'" | ' |
| "\"" | " |
| "\a" | ベル |
| "\b" | バックスペース |
| "\f" | フォームフィード |
| "\n" | LF |
| "\r" | CR |
| "\t" | タブ |
| "\v" | 垂直タブ |
| "\nnn" | 8進表記文字(nは0～7) |
| "\xnn" | 16進表記文字(nは0～f) |
| "\uxxxx" | ユニコード文字xxxx (xxxxは10進数　例: u"\u3042"→'あ') |
| "\Uxxxxxxxx" | ユニコード文字xxxxxxxx (xxxxxxxxは10進数　例: U"\U00003042"→'あ') |
| "\N{name}" | Unicodeデータベース文字 (例: u"\N{HIRAGANA LETTER A}"→'あ') |

### バイト列(byte), Unicode

#### Python 2

```py
print u'あいうえお'
print len(u'あいうえお')
print 'あいうえお'
print len('あいうえお')        # バイト列として扱われる
```

> あいうえお
>
> 5
>
> あいうえお
>
> 15

#### Python 3

```py
print('あいうえお')
print(len('あいうえお'))        # uをつけなくてもUnicodeとして扱われる
print(b'あいうえお')
print(len(b'あいうえお'))       # バイト列として扱われる
print(r"あいう\nえお")
print(len(r"あいう\nえお"))
```

> あいうえお
>
> 5
>
> SyntaxError: bytes can only contain ASCII literal characters.
>
> SyntaxError: bytes can only contain ASCII literal characters.
>
> あいう\nえお
>
> 7

### 区切り文字による分割

```py
hoge = 'abc\ndef\nghi\njkl\nmno\npqr\nstu\nvwx\nyz'
parts = hoge.split('\n')
for key, value in enumerate(parts):
    print('{0}:{1}'.format(key, value))
```

> 0:abc
>
> 1:def
>
> 2:ghi
>
> 3:jkl
>
> 4:mno
>
> 5:pqr
>
> 6:stu
>
> 7:vwx
>
> 8:yz

### 部分文字列

```py
hoge = 'abcdefghi'
print(hoge[1:3])    # bc
print(hoge[:3])     # abc
print(hoge[8:])     # i
print(hoge[-2:])    # hi
print(hoge[0:7:2])  # acdf

# index #################################
# 0   1   2   3   4   5   6   7   8   9 #
# | A | B | C | D | E | f | g | h | i | #
# -9  -8  -7  -6  -5  -4  -3  -2  -1  0 #
#########################################
```

#### 部分文字列を全パターン取得する

```py
hoge = 'abcdefghi'
l = len(hoge)

for s in range(l+1):
  for e in range(s+1, l+1):
    print(hoge[s:e])
```

```py
import itertools

hoge = 'abcdefghi'
l = len(hoge)

for s, e in itertools.combinations(range(l+1), 2):
  print(hoge[s:e])
```

```
a
ab
abc
abcd
abcde
abcdef
abcdefg
abcdefgh
abcdefghi
b
bc
bcd
bcde
bcdef
bcdefg
bcdefgh
bcdefghi
c
cd
cde
cdef
cdefg
cdefgh
cdefghi
d
de
def
defg
defgh
defghi
e
ef
efg
efgh
efghi
f
fg
fgh
fghi
g
gh
ghi
h
hi
i
```

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

```
[ ]:リスト, ( ):タプル, { }:セット/辞書
リストは変更可能
タプルは変更不可
```

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
# 空のリスト
lst = []
print(lst)
lst = [None] * 10
print(lst)
lst = [0] * 10
print(lst)


```

> []
>
> [None, None, None, None, None, None, None, None, None, None]
>
> [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

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
# append(末尾に追加)
lst = ['foo', 'hoge']
lst.append('piyo')
print(lst)

# insert(添え字と要素の値を指定)
lst.insert(1, 'bar')
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

lst.remove('foo')
print(lst)
lst.remove('foo')
print(lst)
lst.remove('foo')
print(lst)
lst.remove('foo')
print(lst)  # 存在しない値を指定するとエラーが発生
```

> \# append
>
> ['foo', 'hoge', 'piyo']
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
>
> ['bar', 'hoge', 'foo', 'bar', 'hoge', 'foo', 'bar', 'hoge']
>
> ['bar', 'hoge', 'bar', 'hoge', 'foo', 'bar', 'hoge']
>
> ['bar', 'hoge', 'bar', 'hoge', 'bar', 'hoge']
>
> ValueError: list.remove(x): x not in list
>
> ['bar', 'hoge', 'bar', 'hoge', 'bar', 'hoge']

### リストの要素を除去

```py
lst = ['foo', 'bar', 'hoge']

lst.pop() # 末尾から除去

lst.pop(0) # 先頭から除去
```

> 'hoge'
>
> ['foo', 'bar']
>
> 'foo'
>
> ['bar']

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

### リストをソート

```py
lst = ['foo', 'bar', 'piyo', 'hoge', 'foo', 'bar', 'piyo', 'hoge']
sortedlist = sorted(lst)
print(lst)
print(sortedlist)

lst.sort(key=None, reverse=False)
print(lst)
```

> ['foo', 'bar', 'piyo', 'hoge', 'foo', 'bar', 'piyo', 'hoge']
>
> ['bar', 'bar', 'foo', 'foo', 'hoge', 'hoge', 'piyo', 'piyo']

> ['bar', 'bar', 'foo', 'foo', 'hoge', 'hoge', 'piyo', 'piyo']

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

### 高階関数

#### map

第2引数の各要素に対して、第1引数のlambda式を適用した結果をイテレータとして返す

```py
# リストに対する演算(map)：map関数は、Python2ではリストを返すがPython3ではイテレータを返すため、list関数を挟む必要がある
numlist = [1, 3, 5, 2, 4]

def double(x): return x * 2

print(map(double, numlist))
print(map(lambda x: x * 2, numlist))
print(list(map(double, numlist))) # Python3でリストを得たい場合
print(list(map(lambda x: x * 2, numlist))) # Python3でリストを得たい場合
print([x * 2 for x in numlist]) # 同じことを内包表記で行う
```

> [2, 6, 10, 4, 8]

#### filter

リストに対してフィルタリングする

```py
def isodd(x): return x % 2 # 条件式(True/Falseを返す)のlambda式

print(list(filter(isodd, numlist)))
print(list(filter(lambda x: x % 2, numlist)))
print([x for x in numlist if x % 2]) # 同じことを内包表記で行う
```

> [1, 3, 5]

#### reduce

リストに対する畳みこみ

```py
from functools import reduce

def add(x, y): return x + y

print(reduce(add, numlist))
print(reduce(lambda x, y: x + y, numlist))
```

> 15

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

### 辞書の要素の存在チェック

```py
dct = { 1:'first', 2:'second', 3:'third', }
print(1 in dct) # キー
print(1 not in dct)

print('first' in dct) # 値
print('first' in dct.values())

print((1, 'first') in dct.items()) # キーと値
```

> True
>
> False
>
> False
>
> True
>
> True

### 指定した値を持つキーを取得する

```py
dct = { 1:'first', 2:'second', 3:'third', }
keys = [k for k, v in dct.items() if v == 'first' or v == 'second']
print(keys)
```

> [1, 2]

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

### タプルを生成

タプルは変更不可

```py
# 空のタプル
empty = ()

# 1要素のタプルを宣言するときは後ろにカンマをつける
t = 'hoge',
t = 'hoge'  # カンマをつけないとただの変数

t = 'foo', 'bar', 123, 456
t[2]

# リストからタプルを生成
print(tuple([1, 2, 3]))  # リストからタプル
print(list((1, 2, 3))  # タプルからリスト
```

> 123

> (1, 2, 3)
>
> [1, 2, 3]

### タプルの入れ子

```py
t = t, ('piyo', 789)
print(t)
```

> (('foo', 'bar', 123, 456), ('piyo', 789))

#### 多重タプルをフラット化

##### 2重タプル

```py
t = ((3, 1, 4), (1, 5, 9), (2, 6, 5))
print(t)

res = [ f for i in t for flattfen in i ]
print(tuple(res))
# or
res = ()
for rows in t:
    res = res + rows

print(res)
```

##### 多重タプル

```py

```

### シーケンス・アンパッキング

タプルから複数の変数に一括代入する

```py
t = 'foo', 'bar', 123, 456
x, y, z, w = t
```

```py
def fibonacci(n):
    x, y = 0, 1
    for i in range(n):
        print(x)
        x, y = y, x+y # tmp変数が不要になる

fibonacci(10)
```

## セット

### セットを生成

重複する要素があれば削除される

```py
s1 = {'ab', 'cd', 'ab', 'cd'}
print(s1)

ls2 = ['ab', 'cd', 'ef', 'cd']
s2 = set(ls2)
print(s2)
```

> {'ab', 'cd'}
>
> {'ef', 'ab', 'cd'}

### セットの要素の存在チェック

```py
s1 = {'ab', 'cd', 'ab', 'cd'}
print('ab' in s1)
```

> True

### セットの要素を追加する

```py
s1 = {'ab', 'cd'}
s1.add('yz')
print(s1)
```

> {'ab', 'yz', 'cd'}

### セットの演算

```py
s1 = {'ab', 'cd'}
s1 = {'ef', 'ab', 'cd'}

print(s1)
print(s2)
print(s1 - s2)
print(s1 | s2)
print(s1 & s2)
print(s1 ^ s2)
```

> {'ab', 'cd'}
>
> {'ef', 'ab', 'cd'}
>
> set()
>
> {'ab', 'cd', 'ef'}
>
> {'ab', 'cd'}
>
> {'ef'}

## 順序つき辞書(OrderedDict)

```py
from collections import OrderedDict
testOrderedDict = OrderedDict()
testOrderedDict['k1'] = 'v1'
testOrderedDict['k2'] = 'v2'
testOrderedDict['k3'] = 'v3'

for k, v in testOrderedDict:
    print(k, v)
```

> k 1
>
> k 2
>
> k 3

# 制御構文

## if

```py
if x < 0:
    print('N')
elif x == 0: # else if
    print('0')
else:
    print('P')
```

## for

```py
for i in range(3):
    j = i + 1
    print(" " + str(i) + " ,")

for i in range(5, 8):
    j = i + 1
    print(" " + str(i) + " ,")

# Pythonではループ変数やループ内で定義された変数を、ループの外でも参照できる
print(", " + str(i) + " " + str(j))
```

### for(リストを与える場合)

```py
l = ['foo', 'bar', 123, 456]
for x in l:
    print(str(x))
```

### for(タプルを与える場合)

```py
t = ('foo', 'bar', 123, 456)
for x in t:
    print(str(x))
```

### for(辞書を与える場合)

```py
d = {'key1': 'foo', 'key2': 'bar', 'key3': 123, 'key4': 456}
for k in d:
    print(str(k))

for k, v in d.items():
    print(str(k), str(v))

for k in d.keys():
    print(str(k), str(d[k]))

for v in d.values():
    print(str(v))

# for k, v in d.iteritems():  # Python2
#     print(str(k), str(v))   # Python3では、items()が関数を返すためiteritemsは廃止
```

### for(試行回数を与える場合)


```py
for i in range(4):
    print(i)    # 0 1 2 3
for i in range(5, 21, 5):
    print(i)    # 5 10 15 20
```

### for文のelse節

```py
for i in range(5):
    print(i)
else:
    # ループを抜けたときに実行される
    print('else')
```

> 0
>
> 1
>
> 2
>
> 3
>
> 4
>
> else

```py
for i in (0, 1, 2):
    print(i)
```

> 0
>
> 1
>
> 2

```py
for k in {'k1': 1, 'k2': 2, 'k3': 3}:
    print(k)
```

> k1
>
> k2
>
> k3

```py
for c in "012":
    print(c)
```

> 0
>
> 1
>
> 2

```py
for line in open("grammer.py", encoding='utf8'):
    print(line)
    # 1行ずつ標準出力
```

```py
# keyとvalueを一緒に取得する
for k, v in enumerate(['v1', 'v2', 'v3']):
    print(k, v)
```

> 0 v1
>
> 1 v2
>
> 2 v3

```py
# 途中でループから脱出
for i in range(5):
    if i > 3:
        break
    print(i)
```

> 0
>
> 1
>
> 2
>
> 3

### スキップする(continue)

```py
for i in range(5):
    if i == 3:
        continue
    print(i)
```

> 0
>
> 1
>
> 2
>
> 4

### itertools

```py
import itertools
for x, y,z in itertools.product(range(10), range(10), range(10)):
  print("%d,%d,%d" % (x,y,z))
```

```
0,0,0
0,0,1
0,0,2
0,0,3
0,0,4
0,0,5
0,0,6
0,0,7
0,0,8
0,0,9
0,1,0
0,1,1
0,1,2
0,1,3
0,1,4
0,1,5
0,1,6
0,1,7
0,1,8
0,1,9
0,2,0
0,2,1
0,2,2
0,2,3
0,2,4
0,2,5
0,2,6
0,2,7
0,2,8
0,2,9
0,3,0
0,3,1
0,3,2
0,3,3
0,3,4
0,3,5
0,3,6
0,3,7
0,3,8
0,3,9
0,4,0
0,4,1
0,4,2
0,4,3
0,4,4
0,4,5
0,4,6
0,4,7
0,4,8
0,4,9
0,5,0
0,5,1
0,5,2
0,5,3
0,5,4
0,5,5
0,5,6
0,5,7
0,5,8
0,5,9
0,6,0
0,6,1
0,6,2
0,6,3
0,6,4
0,6,5
0,6,6
0,6,7
0,6,8
0,6,9
0,7,0
0,7,1
0,7,2
0,7,3
0,7,4
0,7,5
0,7,6
0,7,7
0,7,8
0,7,9
0,8,0
0,8,1
0,8,2
0,8,3
0,8,4
0,8,5
0,8,6
0,8,7
0,8,8
0,8,9
0,9,0
0,9,1
0,9,2
0,9,3
0,9,4
0,9,5
0,9,6
0,9,7
0,9,8
0,9,9
1,0,0
1,0,1
1,0,2
1,0,3
1,0,4
1,0,5
1,0,6
1,0,7
1,0,8
1,0,9
1,1,0
1,1,1
1,1,2
1,1,3
1,1,4
1,1,5
1,1,6
1,1,7
1,1,8
1,1,9
1,2,0
1,2,1
1,2,2
1,2,3
1,2,4
1,2,5
1,2,6
1,2,7
1,2,8
1,2,9
1,3,0
1,3,1
1,3,2
1,3,3
1,3,4
1,3,5
1,3,6
1,3,7
1,3,8
1,3,9
1,4,0
1,4,1
1,4,2
1,4,3
1,4,4
1,4,5
1,4,6
1,4,7
1,4,8
1,4,9
1,5,0
1,5,1
1,5,2
1,5,3
1,5,4
1,5,5
1,5,6
1,5,7
1,5,8
1,5,9
1,6,0
1,6,1
1,6,2
1,6,3
1,6,4
1,6,5
1,6,6
1,6,7
1,6,8
1,6,9
1,7,0
1,7,1
1,7,2
1,7,3
1,7,4
1,7,5
1,7,6
1,7,7
1,7,8
1,7,9
1,8,0
1,8,1
1,8,2
1,8,3
1,8,4
1,8,5
1,8,6
1,8,7
1,8,8
1,8,9
1,9,0
1,9,1
1,9,2
1,9,3
1,9,4
1,9,5
1,9,6
1,9,7
1,9,8
1,9,9
2,0,0
2,0,1
2,0,2
2,0,3
2,0,4
2,0,5
2,0,6
2,0,7
2,0,8
2,0,9
2,1,0
2,1,1
2,1,2
2,1,3
2,1,4
2,1,5
2,1,6
2,1,7
2,1,8
2,1,9
2,2,0
2,2,1
2,2,2
2,2,3
2,2,4
2,2,5
2,2,6
2,2,7
2,2,8
2,2,9
2,3,0
2,3,1
2,3,2
2,3,3
2,3,4
2,3,5
2,3,6
2,3,7
2,3,8
2,3,9
2,4,0
2,4,1
2,4,2
2,4,3
2,4,4
2,4,5
2,4,6
2,4,7
2,4,8
2,4,9
2,5,0
2,5,1
2,5,2
2,5,3
2,5,4
2,5,5
2,5,6
2,5,7
2,5,8
2,5,9
2,6,0
2,6,1
2,6,2
2,6,3
2,6,4
2,6,5
2,6,6
2,6,7
2,6,8
2,6,9
2,7,0
2,7,1
2,7,2
2,7,3
2,7,4
2,7,5
2,7,6
2,7,7
2,7,8
2,7,9
2,8,0
2,8,1
2,8,2
2,8,3
2,8,4
2,8,5
2,8,6
2,8,7
2,8,8
2,8,9
2,9,0
2,9,1
2,9,2
2,9,3
2,9,4
2,9,5
2,9,6
2,9,7
2,9,8
2,9,9
3,0,0
3,0,1
3,0,2
3,0,3
3,0,4
3,0,5
3,0,6
3,0,7
3,0,8
3,0,9
3,1,0
3,1,1
3,1,2
3,1,3
3,1,4
3,1,5
3,1,6
3,1,7
3,1,8
3,1,9
3,2,0
3,2,1
3,2,2
3,2,3
3,2,4
3,2,5
3,2,6
3,2,7
3,2,8
3,2,9
3,3,0
3,3,1
3,3,2
3,3,3
3,3,4
3,3,5
3,3,6
3,3,7
3,3,8
3,3,9
3,4,0
3,4,1
3,4,2
3,4,3
3,4,4
3,4,5
3,4,6
3,4,7
3,4,8
3,4,9
3,5,0
3,5,1
3,5,2
3,5,3
3,5,4
3,5,5
3,5,6
3,5,7
3,5,8
3,5,9
3,6,0
3,6,1
3,6,2
3,6,3
3,6,4
3,6,5
3,6,6
3,6,7
3,6,8
3,6,9
3,7,0
3,7,1
3,7,2
3,7,3
3,7,4
3,7,5
3,7,6
3,7,7
3,7,8
3,7,9
3,8,0
3,8,1
3,8,2
3,8,3
3,8,4
3,8,5
3,8,6
3,8,7
3,8,8
3,8,9
3,9,0
3,9,1
3,9,2
3,9,3
3,9,4
3,9,5
3,9,6
3,9,7
3,9,8
3,9,9
4,0,0
4,0,1
4,0,2
4,0,3
4,0,4
4,0,5
4,0,6
4,0,7
4,0,8
4,0,9
4,1,0
4,1,1
4,1,2
4,1,3
4,1,4
4,1,5
4,1,6
4,1,7
4,1,8
4,1,9
4,2,0
4,2,1
4,2,2
4,2,3
4,2,4
4,2,5
4,2,6
4,2,7
4,2,8
4,2,9
4,3,0
4,3,1
4,3,2
4,3,3
4,3,4
4,3,5
4,3,6
4,3,7
4,3,8
4,3,9
4,4,0
4,4,1
4,4,2
4,4,3
4,4,4
4,4,5
4,4,6
4,4,7
4,4,8
4,4,9
4,5,0
4,5,1
4,5,2
4,5,3
4,5,4
4,5,5
4,5,6
4,5,7
4,5,8
4,5,9
4,6,0
4,6,1
4,6,2
4,6,3
4,6,4
4,6,5
4,6,6
4,6,7
4,6,8
4,6,9
4,7,0
4,7,1
4,7,2
4,7,3
4,7,4
4,7,5
4,7,6
4,7,7
4,7,8
4,7,9
4,8,0
4,8,1
4,8,2
4,8,3
4,8,4
4,8,5
4,8,6
4,8,7
4,8,8
4,8,9
4,9,0
4,9,1
4,9,2
4,9,3
4,9,4
4,9,5
4,9,6
4,9,7
4,9,8
4,9,9
5,0,0
5,0,1
5,0,2
5,0,3
5,0,4
5,0,5
5,0,6
5,0,7
5,0,8
5,0,9
5,1,0
5,1,1
5,1,2
5,1,3
5,1,4
5,1,5
5,1,6
5,1,7
5,1,8
5,1,9
5,2,0
5,2,1
5,2,2
5,2,3
5,2,4
5,2,5
5,2,6
5,2,7
5,2,8
5,2,9
5,3,0
5,3,1
5,3,2
5,3,3
5,3,4
5,3,5
5,3,6
5,3,7
5,3,8
5,3,9
5,4,0
5,4,1
5,4,2
5,4,3
5,4,4
5,4,5
5,4,6
5,4,7
5,4,8
5,4,9
5,5,0
5,5,1
5,5,2
5,5,3
5,5,4
5,5,5
5,5,6
5,5,7
5,5,8
5,5,9
5,6,0
5,6,1
5,6,2
5,6,3
5,6,4
5,6,5
5,6,6
5,6,7
5,6,8
5,6,9
5,7,0
5,7,1
5,7,2
5,7,3
5,7,4
5,7,5
5,7,6
5,7,7
5,7,8
5,7,9
5,8,0
5,8,1
5,8,2
5,8,3
5,8,4
5,8,5
5,8,6
5,8,7
5,8,8
5,8,9
5,9,0
5,9,1
5,9,2
5,9,3
5,9,4
5,9,5
5,9,6
5,9,7
5,9,8
5,9,9
6,0,0
6,0,1
6,0,2
6,0,3
6,0,4
6,0,5
6,0,6
6,0,7
6,0,8
6,0,9
6,1,0
6,1,1
6,1,2
6,1,3
6,1,4
6,1,5
6,1,6
6,1,7
6,1,8
6,1,9
6,2,0
6,2,1
6,2,2
6,2,3
6,2,4
6,2,5
6,2,6
6,2,7
6,2,8
6,2,9
6,3,0
6,3,1
6,3,2
6,3,3
6,3,4
6,3,5
6,3,6
6,3,7
6,3,8
6,3,9
6,4,0
6,4,1
6,4,2
6,4,3
6,4,4
6,4,5
6,4,6
6,4,7
6,4,8
6,4,9
6,5,0
6,5,1
6,5,2
6,5,3
6,5,4
6,5,5
6,5,6
6,5,7
6,5,8
6,5,9
6,6,0
6,6,1
6,6,2
6,6,3
6,6,4
6,6,5
6,6,6
6,6,7
6,6,8
6,6,9
6,7,0
6,7,1
6,7,2
6,7,3
6,7,4
6,7,5
6,7,6
6,7,7
6,7,8
6,7,9
6,8,0
6,8,1
6,8,2
6,8,3
6,8,4
6,8,5
6,8,6
6,8,7
6,8,8
6,8,9
6,9,0
6,9,1
6,9,2
6,9,3
6,9,4
6,9,5
6,9,6
6,9,7
6,9,8
6,9,9
7,0,0
7,0,1
7,0,2
7,0,3
7,0,4
7,0,5
7,0,6
7,0,7
7,0,8
7,0,9
7,1,0
7,1,1
7,1,2
7,1,3
7,1,4
7,1,5
7,1,6
7,1,7
7,1,8
7,1,9
7,2,0
7,2,1
7,2,2
7,2,3
7,2,4
7,2,5
7,2,6
7,2,7
7,2,8
7,2,9
7,3,0
7,3,1
7,3,2
7,3,3
7,3,4
7,3,5
7,3,6
7,3,7
7,3,8
7,3,9
7,4,0
7,4,1
7,4,2
7,4,3
7,4,4
7,4,5
7,4,6
7,4,7
7,4,8
7,4,9
7,5,0
7,5,1
7,5,2
7,5,3
7,5,4
7,5,5
7,5,6
7,5,7
7,5,8
7,5,9
7,6,0
7,6,1
7,6,2
7,6,3
7,6,4
7,6,5
7,6,6
7,6,7
7,6,8
7,6,9
7,7,0
7,7,1
7,7,2
7,7,3
7,7,4
7,7,5
7,7,6
7,7,7
7,7,8
7,7,9
7,8,0
7,8,1
7,8,2
7,8,3
7,8,4
7,8,5
7,8,6
7,8,7
7,8,8
7,8,9
7,9,0
7,9,1
7,9,2
7,9,3
7,9,4
7,9,5
7,9,6
7,9,7
7,9,8
7,9,9
8,0,0
8,0,1
8,0,2
8,0,3
8,0,4
8,0,5
8,0,6
8,0,7
8,0,8
8,0,9
8,1,0
8,1,1
8,1,2
8,1,3
8,1,4
8,1,5
8,1,6
8,1,7
8,1,8
8,1,9
8,2,0
8,2,1
8,2,2
8,2,3
8,2,4
8,2,5
8,2,6
8,2,7
8,2,8
8,2,9
8,3,0
8,3,1
8,3,2
8,3,3
8,3,4
8,3,5
8,3,6
8,3,7
8,3,8
8,3,9
8,4,0
8,4,1
8,4,2
8,4,3
8,4,4
8,4,5
8,4,6
8,4,7
8,4,8
8,4,9
8,5,0
8,5,1
8,5,2
8,5,3
8,5,4
8,5,5
8,5,6
8,5,7
8,5,8
8,5,9
8,6,0
8,6,1
8,6,2
8,6,3
8,6,4
8,6,5
8,6,6
8,6,7
8,6,8
8,6,9
8,7,0
8,7,1
8,7,2
8,7,3
8,7,4
8,7,5
8,7,6
8,7,7
8,7,8
8,7,9
8,8,0
8,8,1
8,8,2
8,8,3
8,8,4
8,8,5
8,8,6
8,8,7
8,8,8
8,8,9
8,9,0
8,9,1
8,9,2
8,9,3
8,9,4
8,9,5
8,9,6
8,9,7
8,9,8
8,9,9
9,0,0
9,0,1
9,0,2
9,0,3
9,0,4
9,0,5
9,0,6
9,0,7
9,0,8
9,0,9
9,1,0
9,1,1
9,1,2
9,1,3
9,1,4
9,1,5
9,1,6
9,1,7
9,1,8
9,1,9
9,2,0
9,2,1
9,2,2
9,2,3
9,2,4
9,2,5
9,2,6
9,2,7
9,2,8
9,2,9
9,3,0
9,3,1
9,3,2
9,3,3
9,3,4
9,3,5
9,3,6
9,3,7
9,3,8
9,3,9
9,4,0
9,4,1
9,4,2
9,4,3
9,4,4
9,4,5
9,4,6
9,4,7
9,4,8
9,4,9
9,5,0
9,5,1
9,5,2
9,5,3
9,5,4
9,5,5
9,5,6
9,5,7
9,5,8
9,5,9
9,6,0
9,6,1
9,6,2
9,6,3
9,6,4
9,6,5
9,6,6
9,6,7
9,6,8
9,6,9
9,7,0
9,7,1
9,7,2
9,7,3
9,7,4
9,7,5
9,7,6
9,7,7
9,7,8
9,7,9
9,8,0
9,8,1
9,8,2
9,8,3
9,8,4
9,8,5
9,8,6
9,8,7
9,8,8
9,8,9
9,9,0
9,9,1
9,9,2
9,9,3
9,9,4
9,9,5
9,9,6
9,9,7
9,9,8
9,9,9
```

## while

```py
i = 0
while i < 10:
    i += 1
    if i == 3:
        continue
    print(i)
else:
    print('-1')
```

> 1
>
> 2
>
> 4
>
> 5
>
> 6
>
> 7
>
> 8
>
> 9
>
> 10
>
> -1

## try(例外処理)

```py
import traceback

str = 'ABC'
try:
    # 範囲外の文字が指定し、IndexError例外を発生させる
    c = str[5]
except IOError as err:
    print("I/O error: {0}".format(err))
except IndexError as err:
    print("IndexError: {0}".format(err))
except (UnicodeEncodeError, UnicodeDecodeError, UnicodeTranslateError) as err:
    # 複数の例外をまとめて扱う
    print("UnicodeError: {0}".format(err))
except:
    # その他の例外
    print(sys.exc_info())   # 現在処理中の例外(type, value, traceback)

    traceback.print_exc()   # 例外情報とスタックトレース項目
    traceback.format_exc()
else:
    # 例外が発生しない場合
    print('Success')
finally:
    # 最終処理
    print('Finally')

# 例外を発生させる
raise IOError('IOError')
```

## 評価

### eval

```py
result = eval('1 + 2')
print(result)

eval('a = 1 + 2')
```

> 3
>
> SyntaxError: invalid syntax

```py
# 式、グローバル、ローカル
result = eval('a + b', {}, {'a': 1, 'b': 2})
result = eval('a + b', {'a': 1, 'b': 2})
print(result)
result = eval('a + b', {'a': 3, 'b': 4}, {'a': 1, 'b': 2})
print(result)
```

> 3
>
> 3

```py
result = eval(compile('1 + 2', '<string>', 'eval'))
print(result)
```

> 3

### exec

```py
exec('a = 1 + 2')
exec('print(a)')
```

> 3

```py
exec('print(a)', {}, {'a': 4})
```

> 4

```py
# 式、グローバル、ローカル
a = {}
exec('b = 3', {}, a)
print(a)
```

> {'b': 3}

```py
for i, s in enumerate(["'foo'","'bar'", "'hoge'"]):
    exec(f"var{i+1} = {s}")

print(var1)
print(var2)
print(var3)
```

> foo
>
> bar
>
> hoge

### グローバル名前空間の参照・変更を制限

```py
exec('import os;os.system("echo foobar")', {}, {})

exec('import os;os.system("echo foobar")', {'__builtins__':None}, {})
```

> foobar
>
> ImportError: __import__ not found

## assert(アサーション)

`__debug__` が `True` の時のみ動作するので、テスト用に使用できる。
コマンドラインオプションに-Oをつけると、 `__debug__` が `False` になるのでassertが動作しなくなる。

```py
sum = 1 + 2
assert sum == 3
assert sum == 4  # AssertionErrorが発生
assert sum == 4, '期待される値と異なります'  # AssertionErrorが発生
```

> \# assert sum == 3
>
>  &nbsp;&nbsp;&nbsp;&nbsp;\# (何も出力されない)

> \# assert sum == 4
>
> AssertionError

> \# assert sum == 4, '期待される値と異なります'
>
> AssertionError: 期待される値と異なります

## del

オブジェクトを削除

```py
s = 'foo'
i = [1, 2, 3]
b = Bar()
del s, i, b
```

## exit(プログラム実行を終了)

```py
import sys
sys.exit()  # SystemExit例外を出して終了

import sys
sys.exit('error!') # 引数をstderrに出力し、SystemExit例外を出して終了

import os
status = 1
os._exit(status) # 例外を出さずに終了

raise exception # 例外を投げて終了
```

>
>
>

## pass

空の関数や空の型を定義する

```py
def empty_func():
    pass


class EmptyClass:
    pass
```

## with

withブロックが終了するとオブジェクトの終了処理が自動的に呼ばれる

```py
with open(filepath, 'w') as f:
    pass
```

# 関数

## 引数なし

```py
# 定義
def func1():
    print("hello")

# 呼出
func1()
```

## 引数あり

```py
# 定義
def func2(arg):
    print(arg)

# 呼出
func2("hello")
```

## 既定値を持つ引数あり

```py
# 定義
def func3(arg="bye"):
    print(arg)

# 呼出
func3()
func3(arg="hi")
```

## 戻り値あり

```py
# 定義
def func4(arg):
    return arg

# 呼出
print(func4("hello"))
```

## docstringあり

```py
# 定義
def func5():
    """helloと表示する関数"""
    print("hello")

# 呼出
func5()
```

### ヘルプを表示

```py
help(func5)
```

## タプルと辞書を受け取る

```py
# 定義
def func_vl(arg, *t, **d):
    for val in t:
        print(val)
    keys = sorted(d.keys())
    for val in keys:
        print(val)

# 呼出
func_vl("foobar",
        "t1",
        "t2",
        dk1="dv1",
        dk2="dv2",
        dk3="dv3")
```

## 引数のアンパック

```py
args = [1, 5]
list(range(*args))

list(range(1, 5))   # と同じ
```

# I/O

## コマンドライン引数

```py
import sys

args = sys.argv
print(args)

for i, arg in enumerate(args):
    print('第{}引数: {}'.format(i, args[i]))
```

> ['python3md-arg.py', 'aaa', 'bbb', 'ccc']
>
> 第1引数: python3md-arg.py
>
> 第2引数: aaa
>
> 第3引数: bbb
>
> 第4引数: ccc

## 標準入力

```py
s = input('Enter your name:').strip() # stripで空白文字を除去
print(s)

# 数値の場合
if s.isnumeric():
    print(int(s))
```

```
aaaaa
```

> aaaaa

```py
s = input() # splitで空白文字ごとに分割
ss = s.split()
for item in ss:
    print(item)
```

```
aaa bbb ccc
```

> aaa
>
> bbb
>
> ccc

```py
s = input()
num = int(s) if s.isnumeric() else 1 # 引数の要求数
ss = [input() for i in range(num)]
print(ss)
```

```
aaa
bbb
ccc
```

> ['aaa', 'bbb', 'ccc']

## 標準出力

```py
print("Hello Python!")
```

## ローカルファイル

### パス文字列の操作

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

#### 親ディレクトリのパスを取得

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

#### Linux上でWindows形式のパスを操作

```py
import ntpath

bname = ntpath.basename('\\path\\to\\file')
print(bname)
```

> file

### カレントディレクトリ

```py
import os


CURRENT_DIRECTORY = os.getcwd()
os.chdir(CURRENT_DIRECTORY)
```

#### スクリプトファイルのパスを取得

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

### ファイル・フォルダを存在チェック

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

### ファイル・フォルダの一覧を取得

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

#### 直下のファイル・フォルダ一覧を取得

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

#### 直下のファイル一覧を取得

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

#### 直下のフォルダ一覧を取得

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

#### 再帰的にファイル・フォルダ一覧を取得 ⇒ _recursive_ が _True_ かつ、パスに _**_

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

#### Python3.4以前で、再帰的にファイル・フォルダ一覧を取得

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

#### 再帰的にフォルダ一覧を取得 ⇒ パスの末尾が _os.path.sep_

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

#### 再帰的にファイル一覧を取得

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

#### ワイルドカードを利用

```py
dirs = glob(os.path.join(DIRPATH, os.path.join('**', '*-[0-1].???')), recursive=True)
```

> [
>
>   './test-glob/test-glob-1/test-glob-1-1/test-glob-1-1-1.dat'
>
> ]

### ファイル情報を取得

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

### ファイルを作成

#### touch()

```py
from pathlib import Path
def touch(filepath):
    Path(filepath).touch()
```

```py
import os
def touch(filepath):
    if os.path.isfile(filepath):
        pass
    else:
        with open(filepath, 'w', encoding='UTF-8') as f:
            pass
```

#### 既存のファイルがある場合はバックアップを作成して再作成

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

### フォルダを作成

#### 既存のフォルダがある場合はバックアップを作成して再作成

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

### ファイルをコピー

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

### フォルダをコピー

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

### ファイルをリネーム

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

### フォルダをリネーム

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

### ファイルを移動

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

### フォルダを移動

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

### ファイルを削除

#### 特定のファイルを削除

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

#### ファイルを検索して削除

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

### フォルダを削除

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

### タイプ別のファイル読み書き

#### ZIPファイル

##### ZIPファイル圧縮

###### shutilを使ってフォルダごと圧縮

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

###### 個別にファイルを追加して圧縮ファイルを作成

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

##### ZIPファイル解凍

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

#### ログファイル(テキストファイル・追記)

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

#### 設定ファイル(configparser)

* config.ini

```ini
[settings]
user = foobar
pw = 12345
```

```py
import configparser
import os

# save
config = configparser.ConfigParser()
config['settings'] = {'user': 'foobar',
                     'pw': '12345'}
with open('config.ini', 'w') as configfile:
    config.write(configfile)

# read
inifile = configparser.ConfigParser()
inifile.read(os.path.join('.', 'config.ini'), 'UTF-8')

print(inifile.get('settings', 'user'))
print(inifile.get('settings', 'pw'))

print(config['settings']['user'])
print(config['settings']['pw'])
```

> ['./config.ini']
>
> foobar
>
> 12345
>
> foobar
>
> 12345

#### テキストファイル

##### 読み込み

###### 単一の文字列として読込み

####### SHIFT-JIS

```py
import os
with open(os.path.join('test-fileio', 'inputsjis.txt'), 'r', encoding='sjis') as file:
    string = file.read()
    print(string)
```

```py
import os
with open(os.path.join('test-fileio', 'inputsjis.txt'), 'r', encoding='shiftjis') as file:
    string = file.read()
    print(string)
```

```py
import os
with open(os.path.join('test-fileio', 'inputsjis.txt'), 'r', encoding='shift-jis') as file:
    string = file.read()
    print(string)
```

```py
import os
with open(os.path.join('test-fileio', 'inputsjis.txt'), 'r', encoding='shift_jis') as file:
    string = file.read()
    print(string)
```

####### UTF-8 BOMなし

```
あいうえお8XkfWDHyFdcB52MbTNNswDnFRAsZdEgRmmsaNktD
かきくけこxahfE6WkxNFpU-4KgnJ4jS2jZUyWf9spDbKRaFyC
```

```py
import os
with open(os.path.join('test-fileio', 'inpututf8.txt'), 'r', encoding='utf8') as file:
    string = file.read()
    print(string)
```

```py
import os
with open(os.path.join('test-fileio', 'inpututf8.txt'), 'r', encoding='utf-8') as file:
    string = file.read()
    print(string)
```

```py
import os
with open(os.path.join('test-fileio', 'inpututf8.txt'), 'r', encoding='utf_8') as file:
    string = file.read()
    print(string)
```

```
﻿あいうえお8XkfWDHyFdcB52MbTNNswDnFRAsZdEgRmmsaNktD
かきくけこxahfE6WkxNFpU-4KgnJ4jS2jZUyWf9spDbKRaFyC
```

####### UTF-8 BOMあり

```py
import os
with open(os.path.join('test-fileio', 'inpututf8.txt'), 'r', encoding='utf_8_sig') as file:
    string = file.read()
    print(string)
```

```
あいうえお8XkfWDHyFdcB52MbTNNswDnFRAsZdEgRmmsaNktD
かきくけこxahfE6WkxNFpU-4KgnJ4jS2jZUyWf9spDbKRaFyC
```

###### 1行ずつ読込み

```py
import os
with open(os.path.join('test-fileio', 'inpututf8.txt'), 'r', encoding='utf_8') as file:
    string = file.readline()
    while string:
        print(string)
        string = file.readline()
```

###### リストへ格納

```py
import os
with open(os.path.join('test-fileio', 'inpututf8.txt'), 'r', encoding='utf_8') as file:
    strings = file.readlines()
    print(strings)
```

```
[
    '\ufeffあいうえお8XkfWDHyFdcB52MbTNNswDnFRAsZdEgRmmsaNktD\n',
    'かきくけこxahfE6WkxNFpU-4KgnJ4jS2jZUyWf9spDbKRaFyC\n'
]
```

##### 書込み

###### 1行ずつ書込み(上書き)

```py
import os
string = 'foobar hoge'
with open(os.path.join('test-fileio', 'outpututf8.txt'), 'w', encoding='utf_8') as file:
    file.write(string)
```

> 11

###### リストを書込み(上書き)

```py
import os
lst = ['foobar', 'hoge']
with open(os.path.join('test-fileio', 'outpututf8.txt'), 'w', encoding='utf_8') as file:
    file.writelines(lst) # 要素間には空白文字等は挿入されない
```

###### 1行ずつ書込み(追記)

```py
import os
string = 'foobar hoge'
with open(os.path.join('test-fileio', 'outpututf8.txt'), 'a', encoding='utf_8') as file:
    file.write(string)
```

###### リストを書き込み(追記)

```py
import os
lst = ['foobar', 'hoge']
with open(os.path.join('test-fileio', 'outpututf8.txt'), 'a', encoding='utf_8') as file:
    file.writelines(lst)
```

#### CSVファイル

##### 読み込み

Windows環境の場合は、明示的にUTF-8を指定しないとSJISとして読み書きされる

```py
import csv
import os

with open(os.path.join('test-fileio', 'inputsjis.csv'), encoding='shift_jis', newline='') as csvfile:
    for row in csv.reader(csvfile, delimiter=',', quotechar='"'):
        print(', '.join(row))

with open(os.path.join('test-fileio', 'inpututf8.csv'), encoding='utf_8', newline='') as csvfile:
    for row in csv.reader(csvfile, delimiter=',', quotechar='"'):
        print(', '.join(row))
```

##### 書き込み

###### 上書き

```py
import csv
with open(os.path.join('test-fileio', 'outpututf8.csv'), 'w', encoding='utf_8', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['foo', 'bar', 'hoge'])
    spamwriter.writerow(['foo', 'bar', 'hoge'])
```

> 14
>
> 14

###### 追記

```py
import csv
with open(os.path.join('test-fileio', 'outpututf8.csv'), 'a', encoding='utf_8', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['foo', 'bar', 'hoge'])
    spamwriter.writerow(['foo', 'bar', 'hoge'])
```

> 14
>
> 14


#### JSONファイル

##### ファイルから読み込み

```py
import json

with open(os.path.join('test-fileio', 'inpututf8.json'), 'r', encoding='utf_8') as file:
    string = file.read()
    print(string)
    json_dict = json.load(file)
    print('json_dict:{}'.format(type(json_dict)))
```

> {
>
>     "key1":"val1",
>
>     "key2":"val2"
>
> }
>
> json_dict:\<class 'dict'\>

##### 文字列から読み込み

```py
import json

json_str = '''
{
    "key1":"val1",
    "key2":"val2"
}
'''

json_dict = json.loads(json_str)
print('json_dict:{}'.format(type(json_dict)))
```

> json_dict:\<class 'dict'\>

##### 文字列から読み込み(順序を保つ)

```py
import collections
import json

json_str = '''
{
    "key1":"val1",
    "key2":"val2"
}
'''

decoder = json.JSONDecoder(object_pairs_hook=collections.OrderedDict)
print(decoder.decode(json_str))
```

> OrderedDict([('key1', 'val1'), ('key2', 'val2')])

##### 要素の読み込み

```py
import json

json_str = '''
{
    "key1":"val1",
    "key2":{
        "key2-1":"val2-1",
        "key2-2":"val2-2"
    }
}
'''

json_dict = json.loads(json_str)
print('json_dict:{}'.format(type(json_dict)))

for x in json_dict:
    print('{0}:{1}'.format(x, json_dict[x]))

for x in json_dict:
    print(json_dict[x])
    for y in json_dict[x]:
        if isinstance(y, dict):
            print('{0}:{1}'.format(y, json_dict[y]))
```

> json_dict:<class 'dict'>
>
> key1:val1
>
> key2:{'key2-1': 'val2-1', 'key2-2': 'val2-2'}
>
> val1
>
> {'key2-1': 'val2-1', 'key2-2': 'val2-2'}

##### 書き込み

```py
import json
import os

# 書き出すオブジェクト
jsondata = {
    'title': 'foobar',
    'items': [
        {
            'title': '1',
            'description': 'hoge'
        },
        {
            'title': '2',
            'description': 'hogehoge'
        }
    ]
}

savepath = os.path.join('test-fileio', 'outpututf8.json')
with open(savepath, 'w', encoding='utf_8') as outfile:
    json.dump(jsondata, outfile)
```

#### ARFFファイル

##### 読み込み

```py
import arff
data = arff.load(open('test.arff', 'rb'))
```

##### 書き込み

```py

import arff
arff.dumps(data)
```

## ネットワーク

### urllib

#### コンテンツを文字列として取得

```py
import urllib.request
url = 'http://python.org/'
with urllib.request.urlopen(url) as response:
    html = response.read()

import urllib.request
url = 'http://python.org/'
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    html = response.read()
```

```
b'<!doctype html>\n<!--[if lt IE 7]>   <html class="no-js ie6 lt-ie7 lt-ie8 lt-ie9">   <![endif]-->\n<!--[if IE 7]>      <html class="no-js ie7 lt-ie8 lt-ie9">          <![endif]-->\n<!--[if IE 8]>      <html class="no-js ie8 lt-ie9">                 <![endif]-->\n<!--[if gt IE 8]><!--><html class="no-js" lang="en" dir="ltr">  <!--<![endif]-->\n\n<head>\n    <meta charset="utf-8">\n    <meta http-equiv="X-UA-Compatible" content="IE=edge">\n\n    <link rel="prefetch" href="//ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js">\n\n    <meta name="application-name" content="Python.org">\n    <meta name="msapplication-tooltip" content="The official home of the Python Programming Language">\n    <meta name="apple-mobile-web-app-title" content="Python.org">\n    <meta name="apple-mobile-web-app-capable" content="yes">\n    <meta name="apple-mobile-web-app-status-bar-style" content="black">\n\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <meta name="HandheldFriendly" content="True">\n    <meta name="format-detection" content="telephone=no">\n    <meta http-equiv="cleartype" content="on">\n    <meta http-equiv="imagetoolbar" content="false">\n\n    <script src="/static/js/libs/modernizr.js"></script>\n\n    <link href="/static/stylesheets/style.67f4b30f7483.css" rel="stylesheet" type="text/css" title="default" />\n    <link href="/static/stylesheets/mq.3ae8e02ece5b.css" rel="stylesheet" type="text/css" media="not print, braille, embossed, speech, tty" />\n    \n\n    <!--[if (lte IE 8)&(!IEMobile)]>\n    <link href="/static/stylesheets/no-mq.fcf414dc68a3.css" rel="stylesheet" type="text/css" media="screen" />\n    \n    \n    <![endif]-->\n\n    \n    <link rel="icon" type="image/x-icon" href="/static/favicon.ico">\n    <link rel="apple-touch-icon-precomposed" sizes="144x144" href="/static/apple-touch-icon-144x144-precomposed.png">\n    <link rel="apple-touch-icon-precomposed" sizes="114x114" href="/static/apple-touch-icon-114x114-precomposed.png">\n    <link rel="apple-touch-icon-precomposed" sizes="72x72" href="/static/apple-touch-icon-72x72-precomposed.png">\n    <link rel="apple-touch-icon-precomposed" href="/static/apple-touch-icon-precomposed.png">\n    <link rel="apple-touch-icon" href="/static/apple-touch-icon-precomposed.png">\n\n    \n    <meta name="msapplication-TileImage" content="/static/metro-icon-144x144-precomposed.png"><!-- white shape -->\n    <meta name="msapplication-TileColor" content="#3673a5"><!-- python blue -->\n    <meta name="msapplication-navbutton-color" content="#3673a5">\n\n    <title>Welcome to Python.org</title>\n\n    <meta name="description" content="The official home of the Python Programming Language">\n    <meta name="keywords" content="Python programming language object oriented web free open source software license documentation download community">\n\n    \n    <meta property="og:type" content="website">\n    <meta property="og:site_name" content="Python.org">\n    <meta property="og:title" content="Welcome to Python.org">\n    <meta property="og:description" content="The official home of the Python Programming Language">\n    \n    <meta property="og:image" content="https://www.python.org/static/opengraph-icon-200x200.png">\n    <meta property="og:image:secure_url" content="https://www.python.org/static/opengraph-icon-200x200.png">\n    \n    <meta property="og:url" content="https://www.python.org/">\n\n    <link rel="author" href="/static/humans.txt">\n\n    <link rel="alternate" type="application/rss+xml" title="Python Enhancement Proposals"\n          href="https://www.python.org/dev/peps/peps.rss/">\n    <link rel="alternate" type="application/rss+xml" title="Python Job Opportunities"\n          href="https://www.python.org/jobs/feed/rss/">\n    <link rel="alternate" type="application/rss+xml" title="Python Software Foundation News"\n          href="https://feeds.feedburner.com/PythonSoftwareFoundationNews">\n    <link rel="alternate" type="application/rss+xml" title="Python Insider"\n          href="https://feeds.feedburner.com/PythonInsider">\n\n    \n\n    \n    <script type="application/ld+json">\n     {\n       "@context": "https://schema.org",\n       "@type": "WebSite",\n       "url": "https://www.python.org/",\n       "potentialAction": {\n         "@type": "SearchAction",\n         "target": "https://www.python.org/search/?q={search_term_string}",\n         "query-input": "required name=search_term_string"\n       }\n     }\n    </script>\n\n    \n    <script type="text/javascript">\n    var _gaq = _gaq || [];\n    _gaq.push([\'_setAccount\', \'UA-39055973-1\']);\n    _gaq.push([\'_trackPageview\']);\n\n    (function() {\n        var ga = document.createElement(\'script\'); ga.type = \'text/javascript\'; ga.async = true;\n        ga.src = (\'https:\' == document.location.protocol ? \'https://ssl\' : \'http://www\') + \'.google-analytics.com/ga.js\';\n        var s = document.getElementsByTagName(\'script\')[0]; s.parentNode.insertBefore(ga, s);\n    })();\n    </script>\n    \n</head>\n\n<body class="python home" id="homepage">\n\n    <div id="touchnav-wrapper">\n\n        <div id="nojs" class="do-not-print">\n            <p><strong>Notice:</strong> While Javascript is not essential for this website, your interaction with the content will be limited. Please turn Javascript on for the full experience. </p>\n        </div>\n\n        <!--[if lte IE 8]>\n        <div id="oldie-warning" class="do-not-print">\n            <p>\n                <strong>Notice:</strong> Your browser is <em>ancient</em>. Please\n                <a href="http://browsehappy.com/">upgrade to a different browser</a> to experience a better web.\n            </p>\n        </div>\n        <![endif]-->\n\n        <!-- Sister Site Links -->\n        <div id="top" class="top-bar do-not-print">\n\n            <nav class="meta-navigation container" role="navigation">\n\n                \n                <div class="skip-link screen-reader-text">\n                    <a href="#content" title="Skip to content">Skip to content</a>\n                </div>\n\n                \n                <a id="close-python-network" class="jump-link" href="#python-network" aria-hidden="true">\n                    <span aria-hidden="true" class="icon-arrow-down"><span>&#9660;</span></span> Close\n                </a>\n\n                \n\n<ul class="menu" role="tree">\n    \n    <li class="python-meta current_item selectedcurrent_branch selected">\n        <a href="/" title="The Python Programming Language" class="current_item selectedcurrent_branch selected">Python</a>\n    </li>\n    \n    <li class="psf-meta ">\n        <a href="/psf-landing/" title="The Python Software Foundation" >PSF</a>\n    </li>\n    \n    <li class="docs-meta ">\n        <a href="https://docs.python.org" title="Python Documentation" >Docs</a>\n    </li>\n    \n    <li class="pypi-meta ">\n        <a href="https://pypi.python.org/" title="Python Package Index" >PyPI</a>\n    </li>\n    \n    <li class="jobs-meta ">\n        <a href="/jobs/" title="Python Job Board" >Jobs</a>\n    </li>\n    \n    <li class="shop-meta ">\n        <a href="/community/" title="Python Community" >Community</a>\n    </li>\n    \n</ul>\n\n\n                <a id="python-network" class="jump-link" href="#top" aria-hidden="true">\n                    <span aria-hidden="true" class="icon-arrow-up"><span>&#9650;</span></span> The Python Network\n                </a>\n\n            </nav>\n\n        </div>\n\n        <!-- Header elements -->\n        <header class="main-header" role="banner">\n            <div class="container">\n\n                <h1 class="site-headline">\n                    <a href="/"><img class="python-logo" src="/static/img/python-logo.png" alt="python&trade;"></a>\n                </h1>\n\n                <div class="options-bar-container do-not-print">\n                    <a href="/psf/donations/" class="donate-button">Donate</a>\n                    <div class="options-bar">\n                        \n                        <a id="site-map-link" class="jump-to-menu" href="#site-map"><span class="menu-icon">&equiv;</span> Menu</a><form class="search-the-site" action="/search/" method="get">\n                            <fieldset title="Search Python.org">\n\n                                <span aria-hidden="true" class="icon-search"></span>\n\n                                <label class="screen-reader-text" for="id-search-field">Search This Site</label>\n                                <input id="id-search-field" name="q" type="search" role="textbox" class="search-field" placeholder="Search" value="" tabindex="1">\n\n                                <button type="submit" name="submit" id="submit" class="search-button" title="Submit this Search" tabindex="3">\n                                    GO\n                                </button>\n\n                                \n                                <!--[if IE]><input type="text" style="display: none;" disabled="disabled" size="1" tabindex="4"><![endif]-->\n\n                            </fieldset>\n                        </form><span class="breaker"></span><div class="adjust-font-size" aria-hidden="true">\n                            <ul class="navigation menu" aria-label="Adjust Text Size on Page">\n                                <li class="tier-1 last" aria-haspopup="true">\n                                    <a href="#" class="action-trigger"><strong><small>A</small> A</strong></a>\n                                    <ul class="subnav menu">\n                                        <li class="tier-2 element-1" role="treeitem"><a class="text-shrink" title="Make Text Smaller" href="javascript:;">Smaller</a></li>\n                                        <li class="tier-2 element-2" role="treeitem"><a class="text-grow" title="Make Text Larger" href="javascript:;">Larger</a></li>\n                                        <li class="tier-2 element-3" role="treeitem"><a class="text-reset" title="Reset any font size changes I have made" href="javascript:;">Reset</a></li>\n                                    </ul>\n                                </li>\n                            </ul>\n                        </div><div class="winkwink-nudgenudge">\n                            <ul class="navigation menu" aria-label="Social Media Navigation">\n                                <li class="tier-1 last" aria-haspopup="true">\n                                    <a href="#" class="action-trigger">Socialize</a>\n                                    <ul class="subnav menu">\n                                        <li class="tier-2 element-1" role="treeitem"><a href="https://www.facebook.com/pythonlang?fref=ts"><span aria-hidden="true" class="icon-facebook"></span>Facebook</a></li>\n                                        <li class="tier-2 element-2" role="treeitem"><a href="https://twitter.com/ThePSF"><span aria-hidden="true" class="icon-twitter"></span>Twitter</a></li>\n                                        <li class="tier-2 element-3" role="treeitem"><a href="/community/irc/"><span aria-hidden="true" class="icon-freenode"></span>Chat on IRC</a></li>\n                                    </ul>\n                                </li>\n                            </ul>\n                        </div>\n                        <span data-html-include="/authenticated"></span>\n                    </div><!-- end options-bar -->\n                </div>\n\n                <nav id="mainnav" class="python-navigation main-navigation do-not-print" role="navigation">\n                    \n                        \n<ul class="navigation menu" role="menubar" aria-label="Main Navigation">\n  \n    \n    \n    <li id="about" class="tier-1 element-1  " aria-haspopup="true">\n        <a href="/about/" title="" class="">About</a>\n        \n            \n\n<ul class="subnav menu" role="menu" aria-hidden="true">\n    \n        <li class="tier-2 element-1" role="treeitem"><a href="/about/apps/" title="">Applications</a></li>\n    \n        <li class="tier-2 element-2" role="treeitem"><a href="/about/quotes/" title="">Quotes</a></li>\n    \n        <li class="tier-2 element-3" role="treeitem"><a href="/about/gettingstarted/" title="">Getting Started</a></li>\n    \n        <li class="tier-2 element-4" role="treeitem"><a href="/about/help/" title="">Help</a></li>\n    \n        <li class="tier-2 element-5" role="treeitem"><a href="http://brochure.getpython.info/" title="">Python Brochure</a></li>\n    \n</ul>\n\n        \n    </li>\n    \n    \n    \n    <li id="downloads" class="tier-1 element-2  " aria-haspopup="true">\n        <a href="/downloads/" title="" class="">Downloads</a>\n        \n            \n\n<ul class="subnav menu" role="menu" aria-hidden="true">\n    \n        <li class="tier-2 element-1" role="treeitem"><a href="/downloads/" title="">All releases</a></li>\n    \n        <li class="tier-2 element-2" role="treeitem"><a href="/downloads/source/" title="">Source code</a></li>\n    \n        <li class="tier-2 element-3" role="treeitem"><a href="/downloads/windows/" title="">Windows</a></li>\n    \n        <li class="tier-2 element-4" role="treeitem"><a href="/downloads/mac-osx/" title="">Mac OS X</a></li>\n    \n        <li class="tier-2 element-5" role="treeitem"><a href="/download/other/" title="">Other Platforms</a></li>\n    \n        <li class="tier-2 element-6" role="treeitem"><a href="https://docs.python.org/3/license.html" title="">License</a></li>\n    \n        <li class="tier-2 element-7" role="treeitem"><a href="/download/alternatives" title="">Alternative Implementations</a></li>\n    \n</ul>\n\n        \n    </li>\n    \n    \n    \n    <li id="documentation" class="tier-1 element-3  " aria-haspopup="true">\n        <a href="/doc/" title="" class="">Documentation</a>\n        \n            \n\n<ul class="subnav menu" role="menu" aria-hidden="true">\n    \n        <li class="tier-2 element-1" role="treeitem"><a href="/doc/" title="">Docs</a></li>\n    \n        <li class="tier-2 element-2" role="treeitem"><a href="/doc/av" title="">Audio/Visual Talks</a></li>\n    \n        <li class="tier-2 element-3" role="treeitem"><a href="https://wiki.python.org/moin/BeginnersGuide" title="">Beginner&#39;s Guide</a></li>\n    \n        <li class="tier-2 element-4" role="treeitem"><a href="https://devguide.python.org/" title="">Developer&#39;s Guide</a></li>\n    \n        <li class="tier-2 element-5" role="treeitem"><a href="https://docs.python.org/faq/" title="">FAQ</a></li>\n    \n        <li class="tier-2 element-6" role="treeitem"><a href="http://wiki.python.org/moin/Languages" title="">Non-English Docs</a></li>\n    \n        <li class="tier-2 element-7" role="treeitem"><a href="http://python.org/dev/peps/" title="">PEP Index</a></li>\n    \n        <li class="tier-2 element-8" role="treeitem"><a href="https://wiki.python.org/moin/PythonBooks" title="">Python Books</a></li>\n    \n        <li class="tier-2 element-9" role="treeitem"><a href="/doc/essays/" title="">Python Essays</a></li>\n    \n</ul>\n\n        \n    </li>\n    \n    \n    \n    <li id="community" class="tier-1 element-4  " aria-haspopup="true">\n        <a href="/community/" title="" class="">Community</a>\n        \n            \n\n<ul class="subnav menu" role="menu" aria-hidden="true">\n    \n        <li class="tier-2 element-1" role="treeitem"><a href="/community/survey" title="">Community Survey</a></li>\n    \n        <li class="tier-2 element-2" role="treeitem"><a href="/community/diversity/" title="">Diversity</a></li>\n    \n        <li class="tier-2 element-3" role="treeitem"><a href="/community/lists/" title="">Mailing Lists</a></li>\n    \n        <li class="tier-2 element-4" role="treeitem"><a href="/community/irc/" title="">IRC</a></li>\n    \n        <li class="tier-2 element-5" role="treeitem"><a href="/community/forums/" title="">Forums</a></li>\n    \n        <li class="tier-2 element-6" role="treeitem"><a href="/psf/annual-report/2019/" title="">PSF Annual Impact Report</a></li>\n    \n        <li class="tier-2 element-7" role="treeitem"><a href="/community/workshops/" title="">Python Conferences</a></li>\n    \n        <li class="tier-2 element-8" role="treeitem"><a href="/community/sigs/" title="">Special Interest Groups</a></li>\n    \n        <li class="tier-2 element-9" role="treeitem"><a href="/community/logos/" title="">Python Logo</a></li>\n    \n        <li class="tier-2 element-10" role="treeitem"><a href="https://wiki.python.org/moin/" title="">Python Wiki</a></li>\n    \n        <li class="tier-2 element-11" role="treeitem"><a href="/community/merchandise/" title="">Merchandise</a></li>\n    \n        <li class="tier-2 element-12" role="treeitem"><a href="/community/awards" title="">Community Awards</a></li>\n    \n        <li class="tier-2 element-13" role="treeitem"><a href="https://www.python.org/psf/codeofconduct/" title="">Code of Conduct</a></li>\n    \n</ul>\n\n        \n    </li>\n    \n    \n    \n    <li id="success-stories" class="tier-1 element-5  " aria-haspopup="true">\n        <a href="/success-stories/" title="success-stories" class="">Success Stories</a>\n        \n            \n\n<ul class="subnav menu" role="menu" aria-hidden="true">\n    \n        <li class="tier-2 element-1" role="treeitem"><a href="/success-stories/category/arts/" title="">Arts</a></li>\n    \n        <li class="tier-2 element-2" role="treeitem"><a href="/success-stories/category/business/" title="">Business</a></li>\n    \n        <li class="tier-2 element-3" role="treeitem"><a href="/success-stories/category/education/" title="">Education</a></li>\n    \n        <li class="tier-2 element-4" role="treeitem"><a href="/success-stories/category/engineering/" title="">Engineering</a></li>\n    \n        <li class="tier-2 element-5" role="treeitem"><a href="/success-stories/category/government/" title="">Government</a></li>\n    \n        <li class="tier-2 element-6" role="treeitem"><a href="/success-stories/category/scientific/" title="">Scientific</a></li>\n    \n        <li class="tier-2 element-7" role="treeitem"><a href="/success-stories/category/software-development/" title="">Software Development</a></li>\n    \n</ul>\n\n        \n    </li>\n    \n    \n    \n    <li id="news" class="tier-1 element-6  " aria-haspopup="true">\n        <a href="/blogs/" title="News from around the Python world" class="">News</a>\n        \n            \n\n<ul class="subnav menu" role="menu" aria-hidden="true">\n    \n        <li class="tier-2 element-1" role="treeitem"><a href="/blogs/" title="Python Insider Blog Posts">Python News</a></li>\n    \n        <li class="tier-2 element-2" role="treeitem"><a href="http://planetpython.org/" title="Planet Python">Community News</a></li>\n    \n        <li class="tier-2 element-3" role="treeitem"><a href="http://pyfound.blogspot.com/" title="PSF Blog">PSF News</a></li>\n    \n        <li class="tier-2 element-4" role="treeitem"><a href="http://pycon.blogspot.com/" title="PyCon Blog">PyCon News</a></li>\n    \n</ul>\n\n        \n    </li>\n    \n    \n    \n    <li id="events" class="tier-1 element-7  " aria-haspopup="true">\n        <a href="/events/" title="" class="">Events</a>\n        \n            \n\n<ul class="subnav menu" role="menu" aria-hidden="true">\n    \n        <li class="tier-2 element-1" role="treeitem"><a href="/events/python-events" title="">Python Events</a></li>\n    \n        <li class="tier-2 element-2" role="treeitem"><a href="/events/python-user-group/" title="">User Group Events</a></li>\n    \n        <li class="tier-2 element-3" role="treeitem"><a href="/events/python-events/past/" title="">Python Events Archive</a></li>\n    \n        <li class="tier-2 element-4" role="treeitem"><a href="/events/python-user-group/past/" title="">User Group Events Archive</a></li>\n    \n        <li class="tier-2 element-5" role="treeitem"><a href="https://wiki.python.org/moin/PythonEventsCalendar#Submitting_an_Event" title="">Submit an Event</a></li>\n    \n</ul>\n\n        \n    </li>\n    \n    \n    \n    \n  \n</ul>\n\n                    \n                </nav>\n\n                <div class="header-banner "> <!-- for optional "do-not-print" class -->\n                    \n        <div id="dive-into-python" class="flex-slideshow slideshow">\n\n            <ul class="launch-shell menu" id="launch-shell">\n                <li>\n                    <a class="button prompt" id="start-shell" data-shell-container="#dive-into-python" href="/shell/">&gt;_\n                        <span class="message">Launch Interactive Shell</span>\n                    </a>\n                </li>\n            </ul>\n\n            <ul class="slides menu">\n                \n                <li>\n                    <div class="slide-code"><pre><code><span class="comment"># Python 3: Fibonacci series up to n</span>\r\n>>> def fib(n):\r\n>>>     a, b = 0, 1\r\n>>>     while a &lt; n:\r\n>>>         print(a, end=\' \')\r\n>>>         a, b = b, a+b\r\n>>>     print()\r\n>>> fib(1000)\r\n<span class="output">0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987</span></code></pre></div>\n                    <div class="slide-copy"><h1>Functions Defined</h1>\r\n<p>The core of extensible programming is defining functions. Python allows mandatory and optional arguments, keyword arguments, and even arbitrary argument lists. <a href="//docs.python.org/3/tutorial/controlflow.html#defining-functions">More about defining functions in Python&nbsp;3</a></p></div>\n                </li>\n                \n                <li>\n                    <div class="slide-code"><pre><code><span class="comment"># Python 3: List comprehensions</span>\r\n>>> fruits = [\'Banana\', \'Apple\', \'Lime\']\r\n>>> loud_fruits = [fruit.upper() for fruit in fruits]\r\n>>> print(loud_fruits)\r\n<span class="output">[\'BANANA\', \'APPLE\', \'LIME\']</span>\r\n\r\n<span class="comment"># List and the enumerate function</span>\r\n>>> list(enumerate(fruits))\r\n<span class="output">[(0, \'Banana\'), (1, \'Apple\'), (2, \'Lime\')]</span></code></pre></div>\n                    <div class="slide-copy"><h1>Compound Data Types</h1>\r\n<p>Lists (known as arrays in other languages) are one of the compound data types that Python understands. Lists can be indexed, sliced and manipulated with other built-in functions. <a href="//docs.python.org/3/tutorial/introduction.html#lists">More about lists in Python&nbsp;3</a></p></div>\n                </li>\n                \n                <li>\n                    <div class="slide-code"><pre><code><span class="comment"># Python 3: Simple arithmetic</span>\r\n>>> 1 / 2\r\n<span class="output">0.5</span>\r\n>>> 2 ** 3\r\n<span class="output">8</span>\r\n>>> 17 / 3  <span class="comment"># classic division returns a float</span>\r\n<span class="output">5.666666666666667</span>\r\n>>> 17 // 3  <span class="comment"># floor division</span>\r\n<span class="output">5</span></code></pre></div>\n                    <div class="slide-copy"><h1>Intuitive Interpretation</h1>\r\n<p>Calculations are simple with Python, and expression syntax is straightforward: the operators <code>+</code>, <code>-</code>, <code>*</code> and <code>/</code> work as expected; parentheses <code>()</code> can be used for grouping. <a href="http://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator">More about simple math functions in Python&nbsp;3</a>.</p></div>\n                </li>\n                \n                <li>\n                    <div class="slide-code"><pre><code><span class="comment"># Python 3: Simple output (with Unicode)</span>\r\n>>> print("Hello, I\'m Python!")\r\n<span class="output">Hello, I\'m Python!</span>\r\n\r\n<span class="comment"># Input, assignment</span>\r\n>>> name = input(\'What is your name?\\n\')\r\n>>> print(\'Hi, %s.\' % name)\r\n<span class="output">What is your name?\r\nPython\r\nHi, Python.</span></code></pre></div>\n                    <div class="slide-copy"><h1>Quick &amp; Easy to Learn</h1>\r\n<p>Experienced programmers in any other language can pick up Python very quickly, and beginners find the clean syntax and indentation structure easy to learn. <a href="//docs.python.org/3/tutorial/">Whet your appetite</a> with our Python&nbsp;3 overview.</p>\r\n                   </div>\n                </li>\n                \n                <li>\n                    <div class="slide-code"><pre><code><span class="comment"># For loop on a list</span>\r\n>>> numbers = [2, 4, 6, 8]\r\n>>> product = 1\r\n>>> for number in numbers:\r\n...    product = product * number\r\n... \r\n>>> print(\'The product is:\', product)\r\n<span class="output">The product is: 384</span></code></pre></div>\n                    <div class="slide-copy"><h1>All the Flow You&rsquo;d Expect</h1>\r\n<p>Python knows the usual control flow statements that other languages speak &mdash; <code>if</code>, <code>for</code>, <code>while</code> and <code>range</code> &mdash; with some of its own twists, of course. <a href="//docs.python.org/3/tutorial/controlflow.html">More control flow tools in Python&nbsp;3</a></p></div>\n                </li>\n                \n            </ul>\n        </div>\n\n\n                </div>\n\n                \n        <div class="introduction">\n            <p>Python is a programming language that lets you work quickly <span class="breaker"></span>and integrate systems more effectively. <a class="readmore" href="/doc/">Learn More</a></p>\n        </div>\n\n\n             </div><!-- end .container -->\n        </header>\n\n        <div id="content" class="content-wrapper">\n            <!-- Main Content Column -->\n            <div class="container">\n\n                <section class="main-content " role="main">\n\n                    \n                    \n\n                    \n\n                    \n\n                \n\n                <div class="row">\n\n                    <div class="small-widget get-started-widget">\n                        <h2 class="widget-title"><span aria-hidden="true" class="icon-get-started"></span>Get Started</h2>\r\n<p>Whether you\'re new to programming or an experienced developer, it\'s easy to learn and use Python.</p>\r\n<p><a href="/about/gettingstarted/">Start with our Beginner&rsquo;s Guide</a></p>\n                    </div>\n\n                    <div class="small-widget download-widget">\n                        <h2 class="widget-title"><span aria-hidden="true" class="icon-download"></span>Download</h2>\n<p>Python source code and installers are available for download for all versions!</p>\n<p>Latest: <a href="/downloads/release/python-374/">Python 3.7.4</a></p>\n                    </div>\n\n                    <div class="small-widget documentation-widget">\n                        <h2 class="widget-title"><span aria-hidden="true" class="icon-documentation"></span>Docs</h2>\r\n<p>Documentation for Python\'s standard library, along with tutorials and guides, are available online.</p>\r\n<p><a href="https://docs.python.org">docs.python.org</a></p>\n                    </div>\n\n                    <div class="small-widget jobs-widget last">\n                        <h2 class="widget-title"><span aria-hidden="true" class="icon-jobs"></span>Jobs</h2>\r\n<p>Looking for work or have a Python related position that you\'re trying to hire for? Our <strong>relaunched community-run job board</strong> is the place to go.</p>\r\n<p><a href="//jobs.python.org">jobs.python.org</a></p>\n                    </div>\n\n                </div>\n\n                <div class="list-widgets row">\n\n                    <div class="medium-widget blog-widget">\n                        \n                        <div class="shrubbery">\n                        \n                            <h2 class="widget-title"><span aria-hidden="true" class="icon-news"></span>Latest News</h2>\n                            <p class="give-me-more"><a href="https://blog.python.org" title="More News">More</a></p>\n                            \n                            <ul class="menu">\n                                \n                                \n                                <li>\n<time datetime="2019-08-07T08:37:00.000002+00:00"><span class="say-no-more">2019-</span>08-07</time>\n <a href="http://feedproxy.google.com/~r/PythonInsider/~3/0XCbz6INDL8/python-380b3-is-now-available-for.html">Python 3.8.0b3 is now available for testing</a></li>\n                                \n                                <li>\n<time datetime="2019-07-31T16:06:00.000002+00:00"><span class="say-no-more">2019-</span>07-31</time>\n <a href="http://feedproxy.google.com/~r/PythonInsider/~3/MwuRB1u_KNQ/pypi-now-supports-uploading-via-api.html">PyPI now supports uploading via API token</a></li>\n                                \n                                <li>\n<time datetime="2019-07-31T16:02:00.000002+00:00"><span class="say-no-more">2019-</span>07-31</time>\n <a href="http://feedproxy.google.com/~r/PythonSoftwareFoundationNews/~3/PyfIYGrs4Vo/pypi-now-supports-uploading-via-api.html">PyPI now supports uploading via API token</a></li>\n                                \n                                <li>\n<time datetime="2019-07-18T15:15:21.000003+00:00"><span class="say-no-more">2019-</span>07-18</time>\n <a href="https://mailchi.mp/python/psf-2019-q2-newsletter">Python Software Foundation - Q2 Newsletter</a></li>\n                                \n                                <li>\n<time datetime="2019-07-11T15:04:00.000003+00:00"><span class="say-no-more">2019-</span>07-11</time>\n <a href="http://feedproxy.google.com/~r/PythonSoftwareFoundationNews/~3/9sGpXmeE1-c/2019-psf-fundraiser-thank-you-debrief.html">2019 PSF Fundraiser - Thank you &amp; debrief</a></li>\n                                \n                            </ul>\n                        </div><!-- end .shrubbery -->\n\n                    </div>\n\n                    <div class="medium-widget event-widget last">\n                        \n                        <div class="shrubbery">\n                        \n                            <h2 class="widget-title"><span aria-hidden="true" class="icon-calendar"></span>Upcoming Events</h2>\n                            <p class="give-me-more"><a href="/events/calendars/" title="More Events">More</a></p>\n                            \n                            <ul class="menu">\n                                \n                                \n                                \n                                <li>\n<time datetime="2019-08-15T00:00:00+00:00"><span class="say-no-more">2019-</span>08-15</time>\n <a href="/events/python-events/854/">PyBay</a></li>\n                                \n                                \n                                \n                                <li>\n<time datetime="2019-08-15T00:00:00+00:00"><span class="say-no-more">2019-</span>08-15</time>\n <a href="/events/python-events/847/">PyCon Korea 2019</a></li>\n                                \n                                \n                                \n                                <li>\n<time datetime="2019-08-23T00:00:00+00:00"><span class="say-no-more">2019-</span>08-23</time>\n <a href="/events/python-events/846/">IndyPy Web Conf 2019</a></li>\n                                \n                                \n                                \n                                <li>\n<time datetime="2019-08-23T00:00:00+00:00"><span class="say-no-more">2019-</span>08-23</time>\n <a href="/events/python-events/855/">Kiwi PyCon X</a></li>\n                                \n                                \n                                \n                                <li>\n<time datetime="2019-08-29T00:00:00+00:00"><span class="say-no-more">2019-</span>08-29</time>\n <a href="/events/python-user-group/835/">PyCon Latam 2019</a></li>\n                                \n                                \n                            </ul>\n                        </div>\n\n                    </div>\n\n                </div>\n\n                <div class="row">\n\n                    <div class="medium-widget success-stories-widget">\n                        \n\n\n\n                        <div class="shrubbery">\n                            \n\n                            <h2 class="widget-title"><span aria-hidden="true" class="icon-success-stories"></span>Success Stories</h2>\n                            <p class="give-me-more"><a href="/success-stories/" title="More Success Stories">More</a></p>\n\n                            \n                            <div class="success-story-item" id="success-story-836">\n\n                            <blockquote>\n                                <a href="/success-stories/python-seo-link-analyzer/">&quot;Python is all about automating repetitive tasks, leaving more time for your other SEO efforts.&quot;</a>\n                            </blockquote>\n\n                            <table cellpadding="0" cellspacing="0" border="0" width="100%" class="quote-from">\n                                <tbody>\n                                    <tr>\n                                        \n                                        <td><p><a href="/success-stories/python-seo-link-analyzer/">Using Python scripts to analyse SEO and broken links on your site</a> <em>by Marnix de Munck</em></p></td>\n                                    </tr>\n                                </tbody>\n                            </table>\n                            </div>\n                            \n\n                        </div><!-- end .shrubbery -->\n\n                    </div>\n\n                    <div class="medium-widget applications-widget last">\n                        <div class="shrubbery">\n                            <h2 class="widget-title"><span aria-hidden="true" class="icon-python"></span>Use Python for&hellip;</h2>\r\n<p class="give-me-more"><a href="/about/apps" title="More Applications">More</a></p>\r\n\r\n<ul class="menu">\r\n    <li><b>Web Development</b>:\r\n        <span class="tag-wrapper"><a class="tag" href="http://www.djangoproject.com/">Django</a>, <a class="tag" href="http://www.pylonsproject.org/">Pyramid</a>, <a class="tag" href="http://bottlepy.org">Bottle</a>, <a class="tag" href="http://tornadoweb.org">Tornado</a>, <a href="http://flask.pocoo.org/" class="tag">Flask</a>, <a class="tag" href="http://www.web2py.com/">web2py</a></span></li>\r\n    <li><b>GUI Development</b>:\r\n        <span class="tag-wrapper"><a class="tag" href="http://wiki.python.org/moin/TkInter">tkInter</a>, <a class="tag" href="https://wiki.gnome.org/Projects/PyGObject">PyGObject</a>, <a class="tag" href="http://www.riverbankcomputing.co.uk/software/pyqt/intro">PyQt</a>, <a class="tag" href="https://wiki.qt.io/PySide">PySide</a>, <a class="tag" href="https://kivy.org/">Kivy</a>, <a class="tag" href="http://www.wxpython.org/">wxPython</a></span></li>\r\n    <li><b>Scientific and Numeric</b>:\r\n        <span class="tag-wrapper">\r\n<a class="tag" href="http://www.scipy.org">SciPy</a>, <a class="tag" href="http://pandas.pydata.org/">Pandas</a>, <a href="http://ipython.org" class="tag">IPython</a></span></li>\r\n    <li><b>Software Development</b>:\r\n        <span class="tag-wrapper"><a class="tag" href="http://buildbot.net/">Buildbot</a>, <a class="tag" href="http://trac.edgewall.org/">Trac</a>, <a class="tag" href="http://roundup.sourceforge.net/">Roundup</a></span></li>\r\n    <li><b>System Administration</b>:\r\n        <span class="tag-wrapper"><a class="tag" href="http://www.ansible.com">Ansible</a>, <a class="tag" href="http://www.saltstack.com">Salt</a>, <a class="tag" href="https://www.openstack.org">OpenStack</a></span></li>\r\n</ul>\r\n\n                        </div><!-- end .shrubbery -->\n                    </div>\n\n                </div>\n\n                \n                <div class="pep-widget">\n\n                    <h2 class="widget-title">\n                        <span class="prompt">&gt;&gt;&gt;</span> <a href="/dev/peps/">Python Enhancement Proposals<span class="say-no-more"> (PEPs)</span></a>: The future of Python<span class="say-no-more"> is discussed here.</span>\n                        <a aria-hidden="true" class="rss-link" href="/dev/peps/peps.rss"><span class="icon-feed"></span> RSS</a>\n                    </h2>\n\n\n                    \n                    \n                </div>\n\n                                <div class="psf-widget">\n\n                    <div class="python-logo"></div>\n                    \n                    <h2 class="widget-title">\r\n    <span class="prompt">&gt;&gt;&gt;</span> <a href="/psf/">Python Software Foundation</a>\r\n</h2>\r\n<p>The mission of the Python Software Foundation is to promote, protect, and advance the Python programming language, and to support and facilitate the growth of a diverse and international community of Python programmers. <a class="readmore" href="/psf/">Learn more</a> </p>\r\n<p class="click-these">\r\n    <a class="button" href="/users/membership/">Become a Member</a>\r\n    <a class="button" href="/psf/donations/">Donate to the PSF</a>\r\n</p>\n                </div>\n\n\n\n\n                </section>\n\n                \n                \n\n                \n                \n\n\n            </div><!-- end .container -->\n        </div><!-- end #content .content-wrapper -->\n\n        <!-- Footer and social media list -->\n        <footer id="site-map" class="main-footer" role="contentinfo">\n            <div class="main-footer-links">\n                <div class="container">\n\n                    \n                    <a id="back-to-top-1" class="jump-link" href="#python-network"><span aria-hidden="true" class="icon-arrow-up"><span>&#9650;</span></span> Back to Top</a>\n\n                    \n\n<ul class="sitemap navigation menu do-not-print" role="tree" id="container">\n    \n    <li class="tier-1 element-1">\n        <a href="/about/" >About</a>\n        \n            \n\n<ul class="subnav menu">\n    \n        <li class="tier-2 element-1" role="treeitem"><a href="/about/apps/" title="">Applications</a></li>\n    \n        <li class="tier-2 element-2" role="treeitem"><a href="/about/quotes/" title="">Quotes</a></li>\n    \n        <li class="tier-2 element-3" role="treeitem"><a href="/about/gettingstarted/" title="">Getting Started</a></li>\n    \n        <li class="tier-2 element-4" role="treeitem"><a href="/about/help/" title="">Help</a></li>\n    \n        <li class="tier-2 element-5" role="treeitem"><a href="http://brochure.getpython.info/" title="">Python Brochure</a></li>\n    \n</ul>\n\n        \n    </li>\n    \n    <li class="tier-1 element-2">\n        <a href="/downloads/" >Downloads</a>\n        \n            \n\n<ul class="subnav menu">\n    \n        <li class="tier-2 element-1" role="treeitem"><a href="/downloads/" title="">All releases</a></li>\n    \n        <li class="tier-2 element-2" role="treeitem"><a href="/downloads/source/" title="">Source code</a></li>\n    \n        <li class="tier-2 element-3" role="treeitem"><a href="/downloads/windows/" title="">Windows</a></li>\n    \n        <li class="tier-2 element-4" role="treeitem"><a href="/downloads/mac-osx/" title="">Mac OS X</a></li>\n    \n        <li class="tier-2 element-5" role="treeitem"><a href="/download/other/" title="">Other Platforms</a></li>\n    \n        <li class="tier-2 element-6" role="treeitem"><a href="https://docs.python.org/3/license.html" title="">License</a></li>\n    \n        <li class="tier-2 element-7" role="treeitem"><a href="/download/alternatives" title="">Alternative Implementations</a></li>\n    \n</ul>\n\n        \n    </li>\n    \n    <li class="tier-1 element-3">\n        <a href="/doc/" >Documentation</a>\n        \n            \n\n<ul class="subnav menu">\n    \n        <li class="tier-2 element-1" role="treeitem"><a href="/doc/" title="">Docs</a></li>\n    \n        <li class="tier-2 element-2" role="treeitem"><a href="/doc/av" title="">Audio/Visual Talks</a></li>\n    \n        <li class="tier-2 element-3" role="treeitem"><a href="https://wiki.python.org/moin/BeginnersGuide" title="">Beginner&#39;s Guide</a></li>\n    \n        <li class="tier-2 element-4" role="treeitem"><a href="https://devguide.python.org/" title="">Developer&#39;s Guide</a></li>\n    \n        <li class="tier-2 element-5" role="treeitem"><a href="https://docs.python.org/faq/" title="">FAQ</a></li>\n    \n        <li class="tier-2 element-6" role="treeitem"><a href="http://wiki.python.org/moin/Languages" title="">Non-English Docs</a></li>\n    \n        <li class="tier-2 element-7" role="treeitem"><a href="http://python.org/dev/peps/" title="">PEP Index</a></li>\n    \n        <li class="tier-2 element-8" role="treeitem"><a href="https://wiki.python.org/moin/PythonBooks" title="">Python Books</a></li>\n    \n        <li class="tier-2 element-9" role="treeitem"><a href="/doc/essays/" title="">Python Essays</a></li>\n    \n</ul>\n\n        \n    </li>\n    \n    <li class="tier-1 element-4">\n        <a href="/community/" >Community</a>\n        \n            \n\n<ul class="subnav menu">\n    \n        <li class="tier-2 element-1" role="treeitem"><a href="/community/survey" title="">Community Survey</a></li>\n    \n        <li class="tier-2 element-2" role="treeitem"><a href="/community/diversity/" title="">Diversity</a></li>\n    \n        <li class="tier-2 element-3" role="treeitem"><a href="/community/lists/" title="">Mailing Lists</a></li>\n    \n        <li class="tier-2 element-4" role="treeitem"><a href="/community/irc/" title="">IRC</a></li>\n    \n        <li class="tier-2 element-5" role="treeitem"><a href="/community/forums/" title="">Forums</a></li>\n    \n        <li class="tier-2 element-6" role="treeitem"><a href="/psf/annual-report/2019/" title="">PSF Annual Impact Report</a></li>\n    \n        <li class="tier-2 element-7" role="treeitem"><a href="/community/workshops/" title="">Python Conferences</a></li>\n    \n        <li class="tier-2 element-8" role="treeitem"><a href="/community/sigs/" title="">Special Interest Groups</a></li>\n    \n        <li class="tier-2 element-9" role="treeitem"><a href="/community/logos/" title="">Python Logo</a></li>\n    \n        <li class="tier-2 element-10" role="treeitem"><a href="https://wiki.python.org/moin/" title="">Python Wiki</a></li>\n    \n        <li class="tier-2 element-11" role="treeitem"><a href="/community/merchandise/" title="">Merchandise</a></li>\n    \n        <li class="tier-2 element-12" role="treeitem"><a href="/community/awards" title="">Community Awards</a></li>\n    \n        <li class="tier-2 element-13" role="treeitem"><a href="https://www.python.org/psf/codeofconduct/" title="">Code of Conduct</a></li>\n    \n</ul>\n\n        \n    </li>\n    \n    <li class="tier-1 element-5">\n        <a href="/success-stories/" title="success-stories">Success Stories</a>\n        \n            \n\n<ul class="subnav menu">\n    \n        <li class="tier-2 element-1" role="treeitem"><a href="/success-stories/category/arts/" title="">Arts</a></li>\n    \n        <li class="tier-2 element-2" role="treeitem"><a href="/success-stories/category/business/" title="">Business</a></li>\n    \n        <li class="tier-2 element-3" role="treeitem"><a href="/success-stories/category/education/" title="">Education</a></li>\n    \n        <li class="tier-2 element-4" role="treeitem"><a href="/success-stories/category/engineering/" title="">Engineering</a></li>\n    \n        <li class="tier-2 element-5" role="treeitem"><a href="/success-stories/category/government/" title="">Government</a></li>\n    \n        <li class="tier-2 element-6" role="treeitem"><a href="/success-stories/category/scientific/" title="">Scientific</a></li>\n    \n        <li class="tier-2 element-7" role="treeitem"><a href="/success-stories/category/software-development/" title="">Software Development</a></li>\n    \n</ul>\n\n        \n    </li>\n    \n    <li class="tier-1 element-6">\n        <a href="/blogs/" title="News from around the Python world">News</a>\n        \n            \n\n<ul class="subnav menu">\n    \n        <li class="tier-2 element-1" role="treeitem"><a href="/blogs/" title="Python Insider Blog Posts">Python News</a></li>\n    \n        <li class="tier-2 element-2" role="treeitem"><a href="http://planetpython.org/" title="Planet Python">Community News</a></li>\n    \n        <li class="tier-2 element-3" role="treeitem"><a href="http://pyfound.blogspot.com/" title="PSF Blog">PSF News</a></li>\n    \n        <li class="tier-2 element-4" role="treeitem"><a href="http://pycon.blogspot.com/" title="PyCon Blog">PyCon News</a></li>\n    \n</ul>\n\n        \n    </li>\n    \n    <li class="tier-1 element-7">\n        <a href="/events/" >Events</a>\n        \n            \n\n<ul class="subnav menu">\n    \n        <li class="tier-2 element-1" role="treeitem"><a href="/events/python-events" title="">Python Events</a></li>\n    \n        <li class="tier-2 element-2" role="treeitem"><a href="/events/python-user-group/" title="">User Group Events</a></li>\n    \n        <li class="tier-2 element-3" role="treeitem"><a href="/events/python-events/past/" title="">Python Events Archive</a></li>\n    \n        <li class="tier-2 element-4" role="treeitem"><a href="/events/python-user-group/past/" title="">User Group Events Archive</a></li>\n    \n        <li class="tier-2 element-5" role="treeitem"><a href="https://wiki.python.org/moin/PythonEventsCalendar#Submitting_an_Event" title="">Submit an Event</a></li>\n    \n</ul>\n\n        \n    </li>\n    \n    <li class="tier-1 element-8">\n        <a href="/dev/" >Contributing</a>\n        \n            \n\n<ul class="subnav menu">\n    \n        <li class="tier-2 element-1" role="treeitem"><a href="https://devguide.python.org/" title="">Developer&#39;s Guide</a></li>\n    \n        <li class="tier-2 element-2" role="treeitem"><a href="https://bugs.python.org/" title="">Issue Tracker</a></li>\n    \n        <li class="tier-2 element-3" role="treeitem"><a href="https://mail.python.org/mailman/listinfo/python-dev" title="">python-dev list</a></li>\n    \n        <li class="tier-2 element-4" role="treeitem"><a href="/dev/core-mentorship/" title="">Core Mentorship</a></li>\n    \n        <li class="tier-2 element-5" role="treeitem"><a href="/news/security/" title="">Report a Security Issue</a></li>\n    \n</ul>\n\n        \n    </li>\n    \n</ul>\n\n\n                    <a id="back-to-top-2" class="jump-link" href="#python-network"><span aria-hidden="true" class="icon-arrow-up"><span>&#9650;</span></span> Back to Top</a>\n                    \n\n                </div><!-- end .container -->\n            </div> <!-- end .main-footer-links -->\n\n            <div class="site-base">\n                <div class="container">\n                    \n                    <ul class="footer-links navigation menu do-not-print" role="tree">\n                        <li class="tier-1 element-1"><a href="/about/help/">Help &amp; <span class="say-no-more">General</span> Contact</a></li>\n                        <li class="tier-1 element-2"><a href="/community/diversity/">Diversity <span class="say-no-more">Initiatives</span></a></li>\n                        <li class="tier-1 element-3"><a href="https://github.com/python/pythondotorg/issues">Submit Website Bug</a></li>\n                        <li class="tier-1 element-4">\n                            <a href="https://status.python.org/">Status <span class="python-status-indicator-default" id="python-status-indicator"></span></a>\n                        </li>\n                    </ul>\n\n                    <div class="copyright">\n                        <p><small>\n                            <span class="pre">Copyright &copy;2001-2019.</span>\n                            &nbsp;<span class="pre"><a href="/psf-landing/">Python Software Foundation</a></span>\n                            &nbsp;<span class="pre"><a href="/about/legal/">Legal Statements</a></span>\n                            &nbsp;<span class="pre"><a href="/privacy/">Privacy Policy</a></span>\n                            &nbsp;<span class="pre"><a href="/psf/sponsorship/sponsors/#heroku">Powered by Heroku</a></span>\n                        </small></p>\n                    </div>\n\n                </div><!-- end .container -->\n            </div><!-- end .site-base -->\n\n        </footer>\n\n    </div><!-- end #touchnav-wrapper -->\n\n    \n    <script src="//ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js"></script>\n    <script>window.jQuery || document.write(\'<script src="/static/js/libs/jquery-1.8.2.min.js"><\\/script>\')</script>\n\n    <script src="/static/js/libs/masonry.pkgd.min.js"></script>\n    <script src="/static/js/libs/html-includes.js"></script>\n\n    <script type="text/javascript" src="/static/js/main-min.fbfe252506ae.js" charset="utf-8"></script>\n    \n\n    <!--[if lte IE 7]>\n    <script type="text/javascript" src="/static/js/plugins/IE8-min.16868e6a5d2f.js" charset="utf-8"></script>\n    \n    \n    <![endif]-->\n\n    <!--[if lte IE 8]>\n    <script type="text/javascript" src="/static/js/plugins/getComputedStyle-min.c3860be1d290.js" charset="utf-8"></script>\n    \n    \n    <![endif]-->\n\n    \n\n    \n    \n\n</body>\n</html>\n'
```

#### 文字コードを指定

```py
import urllib.request
url = 'http://python.org/'
with urllib.request.urlopen(url) as response:
    html = response.read().decode('utf-8')
```

#### コンテンツをテンポラリファイルとして取得

```py
import urllib.request
url = 'http://python.org/'
local_filename, headers = urllib.request.urlretrieve(url)
html = open(local_filename)
```

#### バイナリファイルを保存

```py
import os
import urllib.request
url = 'http://python.org/'
with urllib.request.urlopen(url) as response:
    with open(os.path.basename(url), 'wb') as localfile:
        localfile.write(response.read())
```

#### GET

```py
import urllib.parse
import urllib.request

url = 'http://python.org/'

params = {}
params['name'] = 'Sato'
params['location'] = 'Tokyo'
params['age'] = '30'
query = urllib.parse.urlencode(params)
url = url + '?' + query

with urllib.request.urlopen(url) as response:
    html = response.read()
```

#### POST

```py
import urllib.parse
import urllib.request

url = 'http://python.org/'

params = {'name': 'Sato', 'location': 'Tokyo',  'age': '30'}
query = urllib.parse.urlencode(params)
query = query.encode('ascii')

req = urllib.request.Request(url, query)
with urllib.request.urlopen(req) as response:
    html = response.read()
```

#### HTTPヘッダ(headers引数)

```py
import urllib.parse
import urllib.request

url = 'http://python.org/'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/xxx.xx (KHTML, like Gecko) Chrome/xx.x.xxxx.xx Safari/xxx.xx'
headers = {'User-Agent': user_agent}

params = {'name': 'Sato', 'location': 'Tokyo',  'age': '30'}
query = urllib.parse.urlencode(params)
query = query.encode('ascii')

req = urllib.request.Request(url, query, headers)
with urllib.request.urlopen(req) as response:
    html = response.read()
```

#### HTTPヘッダ(add_header)

```py
import urllib.parse
import urllib.request

url = 'http://python.org/'

params = {'name': 'Sato', 'location': 'Tokyo',  'age': '30'}
query = urllib.parse.urlencode(params)
query = query.encode('ascii')

req = urllib.request.Request(url, query)
req.add_header('Referer', 'http://www.python.org/')
with urllib.request.urlopen(req) as response:
    html = response.read()
```

#### BASIC認証

```py
import urllib.request
import urllib.request
import getpass

url = 'http://python.org/'
auth_user = 'Username'
auth_passwd = 'Password'

passman = urllib.request.HTTPPasswordMgrWithDefaultRealm()
# If we knew the realm, we could use it instead of None.
passman.add_password(None, url, auth_user, auth_passwd)
# HTTPBasicAuthHandler or HTTPDigestAuthHandler
authhandler = urllib.request.HTTPBasicAuthHandler(passman)
opener = urllib.request.build_opener(authhandler)
urllib.request.install_opener(opener)

with urllib.request.urlopen(url) as response:
    html = response.read()
```

#### 応答ヘッダ・リダイレクト先URL

```py
import urllib.parse
import urllib.request

url = 'http://python.org/'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/xxx.xx (KHTML, like Gecko) Chrome/xx.x.xxxx.xx Safari/xxx.xx'
headers = {'User-Agent': user_agent}

params = {'name': 'Sato', 'location': 'Tokyo',  'age': '30'}
query = urllib.parse.urlencode(params)
query = query.encode('ascii')

req = urllib.request.Request(url, query, headers)
with urllib.request.urlopen(req) as response:
    url = response.geturl()
    headers = response.info()
    print(headers)
    # charset=req.info().get_content_charset() # 応答ヘッダから文字コードを取得してデコードする例
    # content=req.read().decode(charset)
```

#### Cookie

```py
import urllib
import urllib.request  # opener
import urllib.parse  # urlencode
import http
import http.cookiejar

opener = urllib.request.build_opener(
    urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))

u, p = 'id', 'pw'

url1 = 'http://python.org/?login'
url2 = 'http://python.org/?user=%s' % u

post = {
    'name': u,
    'password': p
}
data = urllib.parse.urlencode(post).encode('utf-8')

conn = opener.open(url1, data)
ofs = open('out1.html', 'w', encoding='utf-8')
ofs.write(conn.read().decode('utf-8'))
ofs.close()

conn = opener.open(url2)
ofs = open('out2.html', 'w', encoding='euc-jp')
ofs.write(conn.read().decode('euc-jp'))
ofs.close()
```

#### 例外処理とレスポンスコード

```py
import urllib.parse
import urllib.request
from urllib.error import URLError

url = 'http://python.org/'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/xxx.xx (KHTML, like Gecko) Chrome/xx.x.xxxx.xx Safari/xxx.xx'
headers = {'User-Agent': user_agent}

params = {'name': 'Sato', 'location': 'Tokyo',  'age': '30'}
query = urllib.parse.urlencode(params)
query = query.encode('ascii')

req = urllib.request.Request(url, query, headers)
try:
    with urllib.request.urlopen(req) as response:
        html = response.read()
except URLError as e:  # URLErrorはHTTPErrorも拾う
    print(e.code)
    print(e.read())

    if hasattr(e, 'reason'):
        print('Reason: ', e.reason)
    elif hasattr(e, 'code'):
        print('Error code: ', e.code)
else:
    pass  # リクエストに成功
```

### Requests

```sh
$ pip install requests
```

#### GET

```py
import requests
url = 'http://python.org/'
requests.get(url)
```

#### POST

```py
import requests
url = 'http://python.org/'
requests.post(url)
```

#### PUT

```py
import requests
url = 'http://python.org/'
requests.put(url)
```

#### DELETE

```py
import requests
url = 'http://python.org/'
requests.delete(url)
```

#### header の取得

```py
import requests
url = 'http://python.org/'
requests.head(url)
```

#### クエリ

##### GET

```py
import requests
url = 'http://python.org/'
payload = {'key1': 'val1', 'key2': 'val2'}
r = requests.get(url, params=payload)
print(r.url)  # 生成されたURL
```

##### POST

```py
import requests
url = 'http://python.org/'
payload = {'key1': 'val1', 'key2': 'val2'}
r = requests.post(url, data=payload)
print(r.url)  # 生成されたURL(POSTなのでクエリ文字列がないことを確認)
```

#### ヘッダの追加

```py
import requests
url = 'http://python.org/'
payload = {'key1': 'val1', 'key2': 'val2'}
headers = {'Referer', 'http://www.python.org/'}
r = requests.post(url, data=json.dumps(payload), headers=headers)
```

#### フォーム送信(Multipartエンコード)

```py
import requests
url = 'http://python.org/'
files = {'file': open('test.png', 'rb')}
r = requests.post(url, files=files)

import requests
url = 'http://python.org/'
files = {'file': ('test.png', open('test.png', 'rb'))}
r = requests.post(url, files=files)

import requests
url = 'http://python.org/'
files = {'file': ('test.txt', 'foobar')}
r = requests.post(url, files=files)
```

#### 応答

```py
import requests
url = 'http://python.org/'
r = requests.get(url)
r.headers
# r.headers['status']
# r.headers.get('status')
r.text

import requests
url = 'http://python.org/'
r = requests.get(url)
r.status_code  # レスポンスコード
r.status_code == requests.codes.ok  # 200か判定

import requests
url = 'http://python.org/'
r = requests.get(url)
r.encoding  # 文字エンコードの確認
r.encoding = 'Shift-JIS'  # 文字コードの設定(変更)
r.text  # 変更後のエンコーディングが使用される
```

#### Cookie

##### 取得

```py
import requests
url = 'http://python.org/'
r = requests.get(url)
r.cookies['key1']  # Cookieが存在する場合は非None
```

##### 設定

```py
import requests
url = 'http://python.org/'
cookies = dict(key1='val1')
r = requests.get(url, cookies=cookies)
```

#### リダイレクト禁止

```py
import requests
url = 'http://python.org/'
r = requests.get(url, allow_redirects=True)
```

#### タイムアウト

```py
import requests
url = 'http://python.org/'
r = requests.get(url, timeout=1)
```

#### 画像ファイルの保存

```sh
$ pip install Image
$ pip install requests
$ pip install StringIO
```

```py
import os
import requests
from PIL import Image
from io import BytesIO
url = 'https://www.python.org/static/img/python-logo.png'
r = requests.get(url)
i = Image.open(BytesIO(r.content))
i.save(os.path.basename(url))
```

#### 大容量ファイルの保存

```py
import os
import requests
url = 'https://www.python.org/static/img/python-logo.png'
res = requests.get(url, stream=True)
if res.status_code == 200:
    with open(os.path.basename(url), 'wb') as file:
        for chunk in res.iter_content(chunk_size=1024):
            file.write(chunk)
```

#### JSON

```py
import requests
url = 'http://python.org/path/to/json/'
r = requests.get()
r.json()
```

#### セッション

```py
import requests
url = 'http://python.org/path/to/json/'
session = requests.session()
auth_data = {'username': 'foo', 'password': 'bar'}
res = session.post(url, data=auth_data)
res = session.post(url, data={'key1': 'val1'})
```

#### 例外処理とレスポンスコード

```py
import requests
url = 'http://python.org/'
try:
    r = requests.get(url)
except requests.exceptions.RequestException as e:
    print("Error: {}".format(e))
```

# クラス

```py
class MyClass:
    """docstring of MyClass"""

    # クラス変数
    publicClassVariable = 10

    # プライベートクラス変数
    __privateClassVariable = 20

    # コンストラクタ
    def __init__(self, iv1, iv2):
        self.publicInstanceVariable = iv1       # インスタンス変数
        self.__privateInstanceVariable = iv2    # プライベートインスタンス変数

    # デストラクタ
    def __del__(self):
        del(self.publicInstanceVariable)
        del(self.__privateInstanceVariable)

    # 文字列化
    def __str__(self):
        return "MyClass: " + self.__privateInstanceVariable

    def getName(self):          # getter
        return self.__privateInstanceVariable

    def setName(self, name):    # setter
        self.__privateInstanceVariable = name

    # 通常メソッド
    def Calc(self):
        self.publicInstanceVariable2 = 3
        print("パブリックメソッド")

    def __MyCalc(self):
        print("プライベートメソッド")

    @classmethod
    def SelfName(cls):
        publicClassVariable2 = 30
        print("パブリックメソッド")

    @classmethod
    def __PrivateSelfName(cls):
        print("プライベートクラスメソッド")


# インスタンス変数
myClass1.publicInstanceVariable = 3

# インスタンス変数の追加
myClass1.publicInstanceVariable3 = 4

# プライベートインスタンス変数にアクセス
# インスタンス._クラス名__変数名
print myClass1._MyClass__publicInstanceVariable

# パプリッククラス変数へアクセス
# インスタンス名でもクラス名でも可
# 　インスタンス変数が存在しない場合は「インスタンス.変数名」はクラス変数を参照するが、
# 　値を代入するとインスタンス変数が追加されるため、それ以降はインスタンス変数が参照される)
print Widget.classVal
print w.classVal

# クラス変数の追加
MyClass.publicClassVariable3 = 40

# プライベートクラス変数にアクセス
# インスタンス._クラス名__変数名
print myClass1._MyClass__privateInstanceVariable


myClass1 = MyClass(1, 2)    # インスタンス化
myClass1.getName()          # メソッド実行
mg = myClass1.getName       # 別名
mg()                        # メソッド実行


# クラスの継承
class MySubClass(MyClass):
    def Calc(self):  # オーバーロード
        print('sub  a')

# 多重継承


class A(object):
    def __init__(self):
        print 'Initialize A.'

    def method(self):
        print 'Call A method.'


class B(object):
    def __init__(self):
        print 'Initialize B.'

    def method(self):
        print 'Call B method.'


class C(object):
    def __init__(self):
        print 'Initialize C.'

    def method(self):
        print 'Call C method.'


class Main(A, B, C):
    def __init__(self):
        print('Initialize Main.')
        super(Main, self).__init__()
        super(A, self).__init__()
        super(B, self).__init__()

    def method(self):
        print('Call Main method')
        super(Main, self).method()
        super(A, self).method()
        super(B, self).method()


m = Main()
m.method()

```

## オブジェクトの属性の参照と存在チェック

```py

class MyClass:
    publicClassVariable = 10
    __privateClassVariable = 20

    def __init__(self):
        self.val1 = 10
        self.val2 = 20

myClass = MyClass()

# 属性のリスト
print(dir(myClass))

# dict属性
print(vars(myClass))

# 属性値の参照
print(myClass.publicClassVariable)

# 属性の存在チェック
hasattr(myClass, 'publicClassVariable')
hasattr(myClass, '__privateClassVariable')
```

> ['_MyClass__privateClassVariable', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'publicClassVariable', 'val1', 'val2']
>
> {'val1': 10, 'val2': 20}
>
> 10
>
> True
>
> False

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

### 推奨される読み込み順序

1. 標準ライブラリ
2. サードパーティライブラリ
3. ローカルライブラリ（自作のライブラリ）

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

## シンタックスハイライト

```sh
pip install colored-traceback
pip install colorama    # Windows環境下の場合
```

```py
import colored_traceback.always
1/0
```

> Traceback (most recent call last):
>
>   File "<stdin>", line 1, in <module>
>
> ZeroDivisionError: division by zero

---

Copyright (c) 2019 YA-androidapp(https://github.com/YA-androidapp) All rights reserved.
