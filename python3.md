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

## datetime

```py
import datetime

dt = datetime.datetime.now()
print(dt)

print(type(dt))

print(dt.year)
print(dt.month)
print(dt.day)
print(dt.weekday)
print(dt.hour)
print(dt.minute)
print(dt.second)
print(dt.microsecond)
```

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

```py
from datetime import datetime
from datetime import timedelta

dt = datetime(2019, 8, 2)
dt += timedelta(weeks=1, days=2, hours=3, minutes=4, seconds=5, milliseconds=6, microseconds=7)
print(dt)
```

> 2019-08-11 03:04:05.006007

```py
from datetime import datetime
from datetime import timedelta

td = datetime(2019, 12, 24) - datetime(2019, 8, 2, 9, 0, 0)
print(td)
```

> 143 days, 15:00:00

### 日付のリスト

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
```

> 20190730121658

### strからdatetime、date

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

## 辞書

### 追加・置換・削除

```py
dct = { 1:'first', 2:'second', 3:'third'}

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

### 初期化(リスト・タプルから変換)

```py
dct = {}
dct = { 1:'first', 2:'second', 3:'third', }
print(dct)

lst = [[1, 'first'], [2, 'second'], [3, 'third']]
dct = dict(lst)
print(dct)
```

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

### リストを結合

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
```

> {'1': 'f', '2': 's', '3': 't', '4': 'f', '5': 'f', '6': 's'}
>
> {'4': 'f', '5': 'f', '6': 's'}

> {'1': 'f', '2': 's', '3': 't', '4': 'x', '5': 'f', '6': 's', '8': 'e', '9': 'n'}
>
> {'4': 'x', '8': 'e', '9': 'n'}

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

# I/O

## パス文字列の操作

```py
import os

joined = os.path.join('.', 'test' + '-' + 'join', 'test.txt')
print(joined)

basename = os.path.basename('./test-join/test.txt')
print(basename)

dirname = os.path.dirname('./test-join/test.txt')
print(dirname)

root, ext = os.path.splitext('./test-join/test.txt')
print(root, ext)
splitext = os.path.splitext('./test-join/test.txt')
print(splitext[0], splitext[1])

abspath = os.path.abspath('./test-join/test.txt')
print(abspath)
if os.path.isabs(abspath): # パス文字列が絶対パスか検査する
    print('ABSPATH')

```

> './test-join/test.txt'
>
> test.txt
>
> ./test-join
>
> ./test-join/test .txt
>
> '/mnt/c/Users/y/Documents/GitHub/Python-cheatsheet/test-join/test.txt'

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

## ファイル・フォルダをコピー

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
