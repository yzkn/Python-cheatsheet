# おまじない

## shebang

```py
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# #から行末まではコメント
# 1行目または2行目のコメントで、正規表現coding[=:]\s*([-\w.]+)にマッチする場合はエンコーディング宣言として扱われる
```

# 文法

## 命名規則

| 項目                 | 文字種       | 区切り文字     |
| -------------------- | ------------ | -------------- |
| パッケージ           | 英数小文字   | -              |
| モジュール           | 英数小文字   | アンダースコア |
| クラス, 例外, 型変数 | 英数大小文字 | 大文字         |
| メソッド, 関数,変数  | 英数小文字   | アンダースコア |
| 定数                 | 英数大文字   | アンダースコア |

## 予約語

キーワードの一覧を確認する

```py
import keyword

print(len(keyword.kwlist))
print(keyword.kwlist)
```

> 35
>
> ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

ある文字列がキーワードか判定する

```py
import keyword

target = keyword.kwlist[0]
print(keyword.iskeyword(target))
```

> True

## 演算子

### 演算子の優先順位

https://docs.python.org/ja/3/reference/expressions.html#operator-precedence

| 演算子                                       | 意味                                          |
| -------------------------------------------- | --------------------------------------------- |
| (1), [1], {1:1}, {1}                         | 式結合/タプル、リスト、辞書、集合             |
| l[1], l[1,2], f(arg), c.attribute            | 添え字指定、スライス、関数呼び出し、属性参照  |
| await                                        | Await 式                                      |
| \*\*                                         | べき乗                                        |
| +x, -x, ~x                                   | 数、負数、ビット単位 NOT                      |
| \*, /, //, %                                 | 乗算、除算、整除除算、剰余/文字列フォーマット |
| +, -                                         | 加算、減算                                    |
| <<, >>                                       | シフト演算                                    |
| &                                            | ビット単位 AND                                |
| ^                                            | ビット単位 XOR                                |
|                                              |                                               | ビット単位 OR |
| in, not in, is, is not, <, <=, >, >=, !=, == | 比較                                          |
| not x                                        | NOT                                           |
| and                                          | AND                                           |
| or                                           | OR                                            |
| if -- else                                   | 条件式(三項演算子)                            |
| lambda                                       | ラムダ式                                      |

### 条件式(三項演算子)

```py
t = 'True'
f = 'False'
c = t if 1 == 1 else f
```

> 'True'

### 比較演算子

#### Null 判定

##### None との比較

```py
x = None

if x is None: # Nullチェック
    print('True')
```

> True

##### isNullOrEmpty

C#の String.IsNullOrEmpty メソッドと同様の処理を行う

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

#### 同一(is)と同値(==)

- 整数同士の比較

| 演算子 | `x = 1234567890` と `x` | `x` と `y = 1234567890` | `x` と `z = 12345678901` |
| ------ | ----------------------- | ----------------------- | ------------------------ |
| `==`   | `True`                  | `True`                  | `True`                   |
| `is`   | `True`                  | `False`                 | `False`                  |

- 文字列同士の比較

| 演算子 | `x = '1234567890'` と `x` | `x` と `y = '1234567890'` | `x` と `z = '12345678901'` |
| ------ | ------------------------- | ------------------------- | -------------------------- |
| `==`   | `True`                    | `True`                    | `True`                     |
| `is`   | `True`                    | `True`                    | `False`                    |

同一(`is`)比較で、オブジェクトが同一でなくても True が返る場合もある

```py
x = '1234567890'
print(len(x) is 10) # 同一
print(len(x) == 10) # 同値
```

> True
>
> True

#### 複数条件

複数の比較を連続して書くことが可能

```py
a = 2
1 < a and a < 5
1 < a < 5
```

> True
>
> True

```py
content = 'foobarhogepiyo'

# if 'foo' in s and 'bar' in s:
if all(map(content.__contains__, ('foo', 'bar'))):
    print('found')

# if 'foo' in s or 'hoge' in s:
if any(map(content.__contains__, ('foo', 'hoge'))):
    print('found')
```

> found
>
> found

## 変数

```py
# 変数に値を代入
name = 'Suzuki'
print(name)

# 異なる型の値を代入
name = 3
print(name)

# 変数の削除
del name

print(name)
```

> Suzuki
>
> 3
>
> NameError: name 'name' is not defined

### 多重代入

```py
x = y = z = 2
print(x, y, z)
```

## データ型の判定

type()と isinstance()がある。継承を考慮する必要があるかで使い分ける。
以下の例では、bool は int のサブクラスなので、isinstance で判定すると継承元の型にも True を返す

| 関数                      | 結果    |
| ------------------------- | ------- |
| `type(False) is bool`     | `True`  |
| `type(False) is int`      | `False` |
| `isinstance(False, bool)` | `True`  |
| `isinstance(False, int)`  | `True`  |

### type

| 関数                    | 結果              |
| ----------------------- | ----------------- |
| `type(True)`            | `<class 'bool'>`  |
| ----------------------- | ----------------- |
| `type(1)`               | `<class 'int'>`   |
| `type(1.23)`            | `<class 'float'>` |
| `type(int('1'))`        | `<class 'int'>`   |
| `type(float('1'))`      | `<class 'float'>` |
| `type(float('1.23'))`   | `<class 'float'>` |
| `type(0b11)` 2 進数     | `<class 'int'>`   |
| `type(0o11)` 8 進数     | `<class 'int'>`   |
| `type(0x11)` 16 進数    | `<class 'int'>`   |
| ----------------------- | ----------------- |
| `type('str')`           | `<class 'str'>`   |
| ----------------------- | ----------------- |
| `type({0:0, 1:1, 2:2})` | `<class 'dict'>`  |
| ----------------------- | ----------------- |
| `type([0, 1, 2])`       | `<class 'list'>`  |
| ----------------------- | ----------------- |
| `type({0, 1, 2})`       | `<class 'set'>`   |
| ----------------------- | ----------------- |
| `type((0, 1, 2))`       | `<class 'tuple'>` |

```py
def is_valid_isinstance(v):
    return type(v) in (int, str)

print(is_valid_isinstance(1))
print(is_valid_isinstance('1'))
print(is_valid_isinstance(1.23))
```

> True
>
> True
>
> False

### isinstance

| 関数                                | 結果    |
| ----------------------------------- | ------- |
| `isinstance(True, bool)`            | `True`  |
| ----------------------------------- | ------- |
| `isinstance(1, int)`                | `True`  |
| `isinstance(1.23, int)`             | `False` |
| `isinstance(1, float)`              | `False` |
| `isinstance(1.23, float)`           | `True`  |
| `isinstance(int('1'), int)`         | `True`  |
| `isinstance(float('1'), float)`     | `True`  |
| `isinstance(0b11, int)` 2 進数      | `True`  |
| `isinstance(0o11, int)` 8 進数      | `True`  |
| `isinstance(0x11, int)` 16 進数     | `True`  |
| ----------------------------------- | ------- |
| `isinstance('str', str)`            | `True`  |
| ----------------------------------- | ------- |
| `isinstance({0:0, 1:1, 2:2}, dict)` | `True`  |
| ----------------------------------- | ------- |
| `isinstance([0, 1, 2], list)`       | `True`  |
| ----------------------------------- | ------- |
| `isinstance({0, 1, 2}, set)`        | `True`  |
| ----------------------------------- | ------- |
| `isinstance((0, 1, 2), tuple)`      | `True`  |

# データ型

## boolean

- False を返すオブジェクト
- - 偽であると定義されている定数: None と False
- - 数値型におけるゼロ: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)
- - 空のシーケンスまたはコレクション: '', (), [], {}, set(), range(0)

```py
print(True == bool(0.))

from fractions import Fraction
print(True == Fraction(0, 1))
```

> False
>
> False

| `True`                | `False`    |
| --------------------- | ---------- |
| `bool(1)`, `bool(-3)` | `bool(0)`  |
| `bool(.1)`            | `bool(0.)` |
| `bool(1j)`            | `bool(0j)` |
| `bool('a')`           | `bool('')` |
| `bool([0])`           | `bool([])` |
| `bool((0,))`          | `bool(())` |
| `bool({0})`           | `bool({})` |

```py
print(True == 1)
print(False == 0)
print(True + False)
```

> True
>
> True
>
> 1

## int

Python3 では long 型はなくなり、int 型として扱う

```py
# l = 1234567890123456789012345678901234567890123456789012345678901234567890L # Python 2
l = 1234567890123456789012345678901234567890123456789012345678901234567890
```

可読性のために、アンダースコアで桁を区切ることができる

```py
i = 1_000_000_000 # アンダースコアは無視され、int型として扱われる
print(i)
print('{:,}'.format(i)) # 3桁ごとにセミコロンを入れる
```

> 1000000000
>
> 1,000,000,000

### 整数文字列か判定

文字列に対して数値チェック(整数)を行う

| `s`            | `s.isnumeric()`の結果 | 備考                                                                |
| -------------- | --------------------- | ------------------------------------------------------------------- |
| `'1'`          | `True`                |                                                                     |
| `'１２３'`     | `True`                | 全角数字文字列                                                      |
| `'一五一十'`   | `True`                | 全角漢数字文字列(`零 一 二 三 四 五 六 七 八 九 十 百 千 万 億 兆`) |
| `'-1.23'`      | `False`               | `-`や小数点が含まれていると `False`                                 |
| `'－１２．３'` | `False`               | `－`や小数点が含まれていると `False`                                |
| `'10,000'`     | `False`               | 桁区切りのカンマが含まれていると `False`                            |

### int 型と文字列型

#### int 型のフォーマット

フォーマットに利用する関数には以下の種類がある

- 組み込み関数`format()`
- `str.format()`
- - f 文字列

| 種別           | 書き方                                    | 結果       |
| -------------- | ----------------------------------------- | ---------- |
| `format()`     | `format(255, '06o')`                      | `'000377'` |
| `str.format()` | `'{:06o}'.format(255)`                    | `'000377'` |
| f 文字列       | `f'right : {255:06o}'`                    | `'000377'` |
|                | `strval=255`<br>`f'right : {strval:06o}'` | `'000377'` |

詳細は[書式指定子](#書式指定子)の項を参照

#### 文字列型からのキャスト

| `s`          | `int(s)`の結果                                       | 備考                                                                                   |
| ------------ | ---------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `'1'`        | `1`                                                  |                                                                                        |
| `'1.23'`     | `ValueError: invalid literal for int() with base 10` |                                                                                        |
| `'１２３'`   | `123`                                                |                                                                                        |
| `'一五一十'` | `ValueError: invalid literal for int() with base 10` | 漢数字だけしか含まれていないため `isnumeric`では `True` が返るが、キャストには失敗する |

```py
s = '10,000'
s = s.replace(',', '') # 桁区切りのカンマが含まれていると isnumeric() は False を返し、キャストにも失敗する
if s.isnumeric():
    print('数値文字列')
    i = int(s)  # 文字列型からのキャスト
    print('{}'.format(i))
```

### n 進数

10 進数以外の数も、内部的には 10 進数として扱われる

| n 進数  | `i`          | 関数                        | 結果         | 備考                 |
| ------- | ------------ | --------------------------- | ------------ | -------------------- |
| 10 進数 | `123`        | `print(i)`                  | `123`        |                      |
| ------- | ------------ | --------------------------- | ------------ | -------------------- |
| 2 進数  | `0b11111111` | `print(i)`                  | `255`        | 10 進数で表示される  |
|         |              | `print(bin(i))`             | `0b11111111` | 2 進数の文字列       |
|         |              | `print(format(i, 'b'))`     | `11111111`   |                      |
|         |              | `print(format(i, '#b'))`    | `0b11111111` |                      |
|         |              | `print(format(i, '0>10b'))` | `0011111111` | 2 進数をゼロ埋め表示 |
| ------- | ------------ | --------------------------- | ------------ | -------------------- |
| 8 進数  | `0o777`      | `print(i)`                  | `511`        | 10 進数で表示される  |
|         |              | `print(oct(i))`             | `0o777`      | 8 進数の文字列       |
|         |              | `print(format(i, 'o'))`     | `777`        |                      |
|         |              | `print(format(i, '#o'))`    | `0o777`      |                      |
| ------- | ------------ | --------------------------- | ------------ | -------------------- |
| 16 進数 | `0xffff`     | `print(i)`                  | `65535`      | 10 進数で表示される  |
|         |              | `print(hex(i))`             | `0xffff`     | 16 進数の文字列      |
|         |              | `print(format(i, 'x'))`     | `ffff`       |                      |
|         |              | `print(format(i, '#x'))`    | `0xffff`     |                      |

#### n 進数のキャスト

接頭辞(0b, 0o, 0x)がついていれば、基数に 0 を指定しても変換される

| n 進数  | 関数                   | 結果    |
| ------- | ---------------------- | ------- |
| 2 進数  | `int('0b11111111', 2)` | `255`   |
|         | `int('0b11111111', 0)` | `255`   |
| 8 進数  | `int('0o777', 8)`      | `511`   |
|         | `int('0o777', 0)`      | `511`   |
| 16 進数 | `int('0xffff', 16)`    | `65535` |
|         | `int('0xffff', 0)`     | `65535` |

#### 2 進数の補数

```py
x = -36

print(
    '{:>10}\n{:>10}\n1の補数{:>10}\n2の補数{:>10}'.format(
        x,
        bin(x),
        bin((x & 0b11111111) - 1),
        bin(x & 0b11111111)
    )
)
```

```
       -36
 -0b100100
0b11011011
0b11011100
```

#### ビット演算

##### 左シフト

| 関数               | 結果          |
| ------------------ | ------------- |
| `bin(0b0101 << 0)` | &nbsp;`0b101` |
| `bin(0b0101 << 1)` | `0b1010`      |

##### 右シフト

| 関数               | 結果         |
| ------------------ | ------------ |
| `bin(0b0111 >> 0)` | `0b111`      |
| `bin(0b0111 >> 1)` | &nbsp;`0b11` |

##### AND 演算

| 関数                   | 結果       | 備考                                  |
| ---------------------- | ---------- | ------------------------------------- |
| `bin(bin(0b0 & 0b0))`  | `'0b0'`    |                                       |
| `bin(bin(0b0 & 0b1))`  | `'0b0'`    |                                       |
| `bin(bin(0b1 & 0b1))`  | `'0b1'`    |                                       |
| `bin(0b1100 & 0b1010)` | `'0b1000'` | 繰り上がりせず、各桁ごとに AND される |

##### OR 演算

| 関数                   | 結果       | 備考                                 |
| ---------------------- | ---------- | ------------------------------------ |
| `bin(bin(0b0 | 0b0))`  | `'0b0'`    |                                      |
| `bin(bin(0b0 | 0b1))`  | `'0b1'`    |                                      |
| `bin(bin(0b1 | 0b1))`  | `'0b1'`    |                                      |
| `bin(0b1100 | 0b1010)` | `'0b1110'` | 繰り上がりせず、各桁ごとに OR される |

##### XOR 演算

| 関数                   | 結果      | 備考                                  |
| ---------------------- | --------- | ------------------------------------- |
| `bin(bin(0b0 ^ 0b0))`  | `'0b0'`   |                                       |
| `bin(bin(0b0 ^ 0b1))`  | `'0b1'`   |                                       |
| `bin(bin(0b1 ^ 0b1))`  | `'0b0'`   |                                       |
| `bin(0b1100 ^ 0b1010)` | `'0b110'` | 繰り上がりせず、各桁ごとに XOR される |

### 漢数字のキャスト

#### 漢数字 1 文字のキャスト

```py
import unicodedata

print(unicodedata.numeric('五'))
```

> 5.0

#### 漢数字 2 文字以上のキャスト

##### アラビア数字に変換してからキャスト

```py
import re


re_num = re.compile(r'[十拾百千万億兆\d]+')
re_units = re.compile(r'[十拾百千]|\d+')
re_unitm = re.compile(r'[万億兆]|[^万億兆]+')

TRANSUNIT = {'十': 10, '拾': 10, '百': 100, '千': 1000}
TRANSMANS = {'万': 10000, '億': 100000000, '兆': 1000000000000}


def transformNum(kstring: str, sep=False):
    def _transvalue(sj: str, re_obj=re_units, transdic=TRANSUNIT):
        unit = 1
        result = 0
        for piece in reversed(re_obj.findall(sj)):
            if piece in transdic:
                if unit > 1:
                    result += unit
                unit = transdic[piece]
            else:
                val = int(piece) if piece.isdecimal() else _transvalue(piece)
                result += val * unit
                unit = 1
        if unit > 1:
            result += unit
        return result
    transuji = kstring.translate(str.maketrans('一二三四五六七八九〇壱弐参', '1234567890123'))
    for suji in sorted(set(re_num.findall(transuji)), key=lambda s: len(s),
                           reverse=True):
        if not suji.isdecimal():
            arabic = _transvalue(suji, re_unitm, TRANSMANS)
            arabic = '{:,}'.format(arabic) if sep else str(arabic)
            transuji = transuji.replace(suji, arabic)
        elif sep and len(suji) > 3:
            transuji = transuji.replace(suji, '{:,}'.format(int(suji)))
    return transuji


int(transformNum('１億２３４万５千六百七十八'))
```

> 102345678

##### kanjize パッケージを利用

```sh
$ pip install kanjize
```

```py
from kanjize import int2kanji, kanji2int

print(kanji2int('十二億三千四十五万六千七百八十九')) # 漢数字→int
print(int2kanji(1230456789)) # int→漢数字
```

> 1230456789
>
> 十二億三千四十五万六千七百八十九

### 四捨五入・数値の切り上げ・切り捨て

| 処理                      | 関数                | 結果              |
| ------------------------- | ------------------- | ----------------- |
| 四捨五入(偶数への丸め)    | `round(7 / 3)`      | `2`               |
|                           | `round(1 / 2)`      | `0` (`1`ではない) |
| 切り捨て                  | `7 // 3`            | `2`               |
|                           | `int(7 / 3)`        | `2`               |
| 切り上げ                  | `-(-7 // 3)`        | `3`               |
| 切り捨て(math モジュール) | `math.floor(7 / 3)` | `2`               |
| 切り上げ(math モジュール) | `math.ceil(7 / 3)`  | `3`               |

```py
import math
math.floor(7 / 3) # 切り捨て
math.ceil(7 / 3) # 切り上げ
```

> 2
>
> 3

偶数への丸めではなく四捨五入を行いたい時は、decimal モジュールを使用する

```py
from decimal import Decimal, ROUND_HALF_UP, ROUND_DOWN

f = 1234.567

# 四捨五入
print(Decimal(str(f)).quantize(Decimal('0'), rounding=ROUND_HALF_UP))

# int型に戻す
int_value = int(Decimal(str(f)).quantize(Decimal('0'), rounding=ROUND_HALF_UP))

# 切り捨て
print(Decimal(str(f)).quantize(Decimal('0'), rounding=ROUND_DOWN))

# 切り上げ
print(Decimal(str(f)).quantize(Decimal('0'), rounding=ROUND_UP))
```

> \# 四捨五入
>
> 1235

> \# 切り捨て
>
> 1234

> \# 切り上げ
>
> 1235

## float

| 定義                         | 結果     |
| ---------------------------- | -------- |
| `1.23`                       | `1.23`   |
| `1.2e3` (1.2 \* 10 \*\* 3)   | `1200.0` |
| `1.2E-3` (1.2 \* 10 \*\* -3) | `0.0012` |

### 整数文字列か判定

文字列に対して数値チェック(小数)を行う

```py
def is_float(s):
  try:
    float(s)
  except:
    return False
  return True


s = '1.23e-4'
if is_float(s):
    f = float(s)  # 文字列型からのキャスト
    print('{}'.format(f))
```

> 0.000123

### float 型と文字列型

#### float 型のフォーマット

フォーマットに利用する関数には以下の種類がある

- 組み込み関数`format()`
- `str.format()`
- - f 文字列

| 種別           | 書き方                                        | 結果      |
| -------------- | --------------------------------------------- | --------- |
| `format()`     | `format(1.2345, '0.3f')`                      | `'1.234'` |
| `str.format()` | `'{:0.3f}'.format(1.2345)`                    | `'1.234'` |
| f 文字列       | `f'right : {1.2345:0.3f}'`                    | `'1.234'` |
|                | `strval=1.2345`<br>`f'right : {strval:0.3f}'` | `'1.234'` |

詳細は[書式指定子](#書式指定子)の項を参照

#### 文字列型からのキャスト

| `s`         | `float(s)`の結果 |
| ----------- | ---------------- |
| `'1.23'`    | `1.23`           |
| `'.23'`     | `0.23`           |
| `'1.23e-4'` | `0.000123`       |

### 数値の指定桁数での四捨五入・切り上げ・切り捨て

| 処理                      | 関数                | 結果                     |
| ------------------------- | ------------------- | ------------------------ |
| 四捨五入(偶数への丸め)    | `round(7 / 3, 2)`   | `2.33`                   |
|                           | `round(1 / 4, 1)`   | `0.2` ( `0.25` ではない) |
| 切り捨て                  | `7 // 3`            | `2`                      |
|                           | `int(7 / 3)`        | `2`                      |
| 切り上げ                  | `-(-7 // 3)`        | `3`                      |
| 切り捨て(math モジュール) | `math.floor(7 / 3)` | `2`                      |
| 切り上げ(math モジュール) | `math.ceil(7 / 3)`  | `3`                      |

偶数への丸めではなく四捨五入を行いたい時は、decimal モジュールを使用する

```py
from decimal import Decimal, ROUND_HALF_UP, ROUND_DOWN

f = 1234.567

# 四捨五入
print(Decimal(str(f)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP))
print(Decimal(str(f)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))

# float型に戻す
float_value = float(Decimal(str(f)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP))

# 切り捨て
print(Decimal(str(f)).quantize(Decimal('0.1'), rounding=ROUND_DOWN))

# 切り上げ
print(Decimal(str(f)).quantize(Decimal('0.1'), rounding=ROUND_UP))
```

> \# 四捨五入
>
> 1234.6
>
> 1234.57

> \# 切り捨て
>
> 1234.5

> \# 切り上げ
>
> 1235.6

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

| 項目         | 値                   |
| ------------ | -------------------- |
| `td`         | `365 days, 23:59:59` |
| `td.days`    | `365`                |
| `td.seconds` | `86399`              |
| `d1 > d2`    | `True`               |
| `d1 < d2`    | `False`              |
| `d1 == d2`   | `False`              |

### 現在日時

```py
from datetime import datetime

dt = datetime.today()
print(dt)

dt = datetime.now()
print(dt)
```

> 2019-08-02 08:34:17.354115
>
> 2019-08-02 08:34:17.354115

| 項目              | 値                             | 備考           |
| ----------------- | ------------------------------ | -------------- |
| `type(dt)`        | `<class 'datetime.datetime'\>` |                |
| `dt.year`         | `2019`                         |                |
| `dt.month`        | `8`                            |                |
| `dt.day`          | `2`                            |                |
| `dt.weekday()`    | `4`                            | 0:月曜; 6:日曜 |
| `dt.isoweekday()` | `5`                            | 1:月曜; 7:日曜 |
| `dt.hour`         | `8`                            |                |
| `dt.minute`       | `34`                           |                |
| `dt.second`       | `17`                           |                |
| `dt.microsecond`  | `354115`                       |                |

### 祝日判定

[emasaka/jpholidayp](https://github.com/emasaka/jpholidayp)

### 日付の生成

```py
from datetime import datetime
# 年・月・日は必須
dt = datetime(2019, 8, 2)
dt = datetime(2019, 8, 2, 1, 2, 3)
```

| 関数                             | 結果                                  |
| -------------------------------- | ------------------------------------- |
| `datetime(2019, 8, 2)`           | `2019-08-02 00:00:00`                 |
| `datetime(2019, 8, 2, 1, 2, 3)`  | `2019-08-02 01:02:03`                 |
| `datetime(2019, 8, 2, 1, 1, 63)` | `ValueError: second must be in 0..59` |

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

### タイムゾーンを考慮した datetime

#### datetime パッケージの timezone モジュールを使用する場合

UTC からの時間差を指定して最低限の処理をすればよい場合

| 種類  | 内容                                                   |
| ----- | ------------------------------------------------------ |
| aware | TimeZone 情報を持つ datetime オブジェクト(tzinfo 属性) |
| naive | TimeZone 情報を持たない datetime オブジェクト          |

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

#### pytz を使用する場合

##### 現在日時から生成

```sh
$ pip install pytz
```

```py
from pytz import timezone
from datetime import datetime
```

- 型

| 項目                           | 値                                 |
| ------------------------------ | ---------------------------------- |
| `type(datetime.now())`         | `<class 'datetime.datetime'>`      |
| `type(timezone('UTC'))`        | `<class 'pytz.UTC'>`               |
| `type(timezone('Asia/Tokyo'))` | `<class 'pytz.tzfile.Asia/Tokyo'>` |

| 項目                                                                                    | 値                                 |
| --------------------------------------------------------------------------------------- | ---------------------------------- |
| `print(datetime.now())`                                                                 | `2019-08-07 12:45:18.487441`       |
|                                                                                         |                                    |
| `print(datetime.now(timezone('UTC')))`                                                  | `2019-08-07 03:45:18.553981+00:00` |
| `print(datetime.now(tz=timezone('Europe/London')))`                                     | `2019-08-07 04:45:18.553981+01:00` |
| `print(datetime.now(tz=timezone('Asia/Tokyo')))`                                        | `2019-08-07 12:45:18.553981+09:00` |
|                                                                                         |                                    |
| `print(datetime.now(timezone('UTC')).astimezone(timezone('Europe/London')))`            | `2019-08-07 04:45:18.634371+01:00` |
| `print(datetime.now(timezone('UTC')).astimezone(timezone('Asia/Tokyo')))`               | `2019-08-07 12:45:18.754351+09:00` |
|                                                                                         |                                    |
| `print(timezone('Europe/London').localize(datetime.now()))`                             | `2019-08-07 12:45:20.011410+01:00` |
| `print(timezone('Asia/Tokyo').localize(datetime.now()))`                                | `2019-08-07 12:45:20.011410+09:00` |
|                                                                                         |                                    |
| `print(timezone('UTC').localize(datetime.now()))`                                       | `2019-08-07 12:45:18.760637+00:00` |
|                                                                                         |                                    |
| `print(timezone('UTC').localize(datetime.now()).astimezone(timezone('Europe/London')))` | `2019-08-07 13:45:18.760637+09:00` |
| `print(timezone('UTC').localize(datetime.now()).astimezone(timezone('Asia/Tokyo')))`    | `2019-08-07 21:45:18.760637+09:00` |

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

### datetime 型のキャスト

#### datetime 型と date 型・time 型

##### datetime 型 から date 型・time 型

```py
from datetime import datetime

dt = datetime(2019, 8, 2)

# date型
print(dt.date())
print(type(dt.date()))

# time型
print(dt.time())
print(type(dt.time()))

print(dt.date().weekday())
```

> 2019-08-02
>
> \<class 'datetime.date'\>
>
> 00:00:00
>
> \<class 'datetime.time'>
>
> 4

##### date 型・time 型 から datetime 型

```py
import datetime

# 今日の日付(date)
date = datetime.date.today()

# time
# 範囲外の数値を指定するとエラー
# ValueError: second must be in 0..59
time = datetime.time(hour=12, minute=34, second=56)

dt = datetime.datetime.combine(date, time)
print(dt)
```

> 2019-08-02 12:34:56

#### datetime 型と文字列型

##### datetime 型 から 文字列型

```py
from datetime import datetime
now = datetime.now().strftime('%Y%m%d%H%M%S') # YYYYmmddHHMMSS
print(now)

print(datetime.now().isoformat()) # ISO形式
```

> 20190730121658
>
> 2019-07-30T12:16:58.427664

##### 文字列型 から datetime 型、date 型

```py
from datetime import date
from datetime import datetime
tstr = '2019-07-30 12:16:58'
tdatetime = datetime.strptime(tstr, '%Y-%m-%d %H:%M:%S') # YYYY-mm-dd HH:MM:SS
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

##### タイムゾーンを考慮した 文字列型 から datetime 型

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

##### タイムゾーンを考慮した ISO 形式の 文字列型 から datetime 型

dateutil.parser を利用する

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

##### 日付時刻の format 文字列に埋め込むディレクティブ

https://docs.python.org/ja/3/library/time.html#time.strftime

| ディレクティブ | 意味                                                                                                                                                  | 注釈 |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ---- |
| %a             | ロケールにおける省略形の曜日名。                                                                                                                      |      |
| %A             | ロケールにおける省略なしの曜日名。                                                                                                                    |      |
| %b             | ロケールにおける省略形の月名。                                                                                                                        |      |
| %B             | ロケールにおける省略なしの月名。                                                                                                                      |      |
| %c             | ロケールにおける適切な日付および時刻表現。                                                                                                            |      |
| %d             | 月の始めから何日目かを表す 10 進数 [01,31]。                                                                                                          |      |
| %H             | (24 時間計での) 時を表す 10 進数 [00,23]。                                                                                                            |      |
| %I             | (12 時間計での) 時を表す 10 進数 [01,12]。                                                                                                            |      |
| %j             | 年の初めから何日目かを表す 10 進数 [001,366]。                                                                                                        |      |
| %m             | 月を表す 10 進数 [01,12]。                                                                                                                            |      |
| %M             | 分を表す 10 進数 [00,59]。                                                                                                                            |      |
| %p             | ロケールにおける AM または PM に対応する文字列。                                                                                                      | (1)  |
| %S             | 秒を表す 10 進数 [00,61]。                                                                                                                            | (2)  |
| %U             | 年の初めから何週目か (日曜を週の始まりとします)を表す<br>10 進数 [00,53]。年が明けてから最初の日曜日までの全ての曜日は 0 週目に属すると見なされます。 | (3)  |
| %w             | 曜日を表す 10 進数 [0(日曜日),6]。                                                                                                                    |      |
| %W             | 年の初めから何週目か (日曜を週の始まりとします)を表す<br>10 進数 [00,53]。年が明けてから最初の月曜日までの全ての曜日は 0 週目に属すると見なされます。 | (3)  |
| %x             | ロケールにおける適切な日付の表現。                                                                                                                    |      |
| %X             | ロケールにおける適切な時刻の表現。                                                                                                                    |      |
| %y             | 上 2 桁なしの西暦年を表す 10 進数 [00,99]。                                                                                                           |      |
| %Y             | 上 2 桁付きの西暦年を表す 10 進数。                                                                                                                   |      |
| %Z             | タイムゾーンの名前 (タイムゾーンがない場合には空文字列)。                                                                                             |      |
| %%             | 文字 “%” 自体の表現。                                                                                                                                 |      |

1. strptime() 関数で使う場合、%p ディレクティブが出力結果の時刻フィールドに影響を及ぼすのは、時刻を解釈するために %I を使ったときのみです。
1. 値の幅は実際に 0 から 61 です; 60 は うるう秒\<leap seconds\> を表し、 61 は歴史的理由によりサポートされています。
1. strptime() 関数で使う場合、%U および %W を計算に使うのは曜日と年を指定したときだけです。

## str(文字列)

```py
print('str\nstr')
print("str\nstr")
print(str(123))
print('cq' * 3) # 文字列の繰り返し
print('cq' + 'cq') # 文字列をつなげる(連結/結合)
print('cq' 'cq' 'cq') # 文字列を演算子なしでつなげる
```

> str
>
> str

> str
>
> str

> 123

> cqcqcq
>
> cqcqcq

---

### エスケープシーケンス

| 項目         | 内容                                                                  |
| ------------ | --------------------------------------------------------------------- |
| '\\'         | \                                                                     |
| '\''         | '                                                                     |
| "\""         | "                                                                     |
| '\a'         | ベル                                                                  |
| '\b'         | バックスペース                                                        |
| '\f'         | フォームフィード                                                      |
| '\n'         | LF                                                                    |
| '\r'         | CR                                                                    |
| '\t'         | タブ                                                                  |
| '\v'         | 垂直タブ                                                              |
| '\nnn'       | 8 進表記文字(n は 0 ～ 7)                                             |
| '\xnn'       | 16 進表記文字(n は 0 ～ f)                                            |
| '\uxxxx'     | ユニコード文字 xxxx (xxxx は 10 進数　例: u'\u3042'→'あ')             |
| '\Uxxxxxxxx' | ユニコード文字 xxxxxxxx (xxxxxxxx は 10 進数　例: U'\U00003042'→'あ') |
| '\N{name}'   | Unicode データベース文字 (例: u'\N{HIRAGANA LETTER A}'→'あ')          |

## RAW 文字列

```py
print(r'str\nstr') # エスケープシーケンスが無視される
print(R'str\nstr') # エスケープシーケンスが無視される
```

> str\nstr
>
> str\nstr

### ヒアドキュメント

```py
hoge = '''abc
def
ghi'''

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

### 文字列のフォーマット

フォーマットに利用する関数には以下の種類がある

- 組み込み関数`format()`
- `str.format()`
- - f 文字列

| 種別           | 書き方                                    | 結果       |
| -------------- | ----------------------------------------- | ---------- |
| `format()`     | `format(255, '06o')`                      | `'000377'` |
| `str.format()` | `'{:06o}'.format(255)`                    | `'000377'` |
| f 文字列       | `f'right : {255:06o}'`                    | `'000377'` |
|                | `strval=255`<br>`f'right : {strval:06o}'` | `'000377'` |

詳細は[書式指定子](#書式指定子)の項を参照

#### ゼロ埋め

| 関数                            | 値           |                  |
| ------------------------------- | ------------ | ---------------- |
| `print('12345'.zfill(8))`       | `00012345`   |                  |
| `print('1234567890'.zfill(8))`  | `1234567890` |                  |
| `print('+1234'.zfill(8))`       | `+0001234`   | +の後ろに 0 埋め |
| `print('-1234'.zfill(8))`       | `-0001234`   | -の後ろに 0 埋め |
| `print('-a1234'.zfill(8))`      | `-00a1234`   |                  |
| `print('xyz'.zfill(8))`         | `00000xyz`   |                  |
| `print(str(12345).zfill(8))`    | `00012345`   |                  |
|                                 |              |                  |
| `print('1234'.rjust(8, '0'))`   | `00001234`   |                  |
| `print('1234'.ljust(8, '0'))`   | `12340000`   |                  |
| `print('1234'.center(8, '0'))`  | `00123400`   |                  |
| `print('-1234'.rjust(8, '0'))`  | `000-1234`   |                  |
| `print('-1234'.ljust(8, '0'))`  | `-1234000`   |                  |
| `print('-1234'.center(8, '0'))` | `0-123400`   |                  |

# 書式指定子

| 項目 | \*  | fill                  | \*           | align | \*                 | sign     | \*       | `#`  | `0`    | width        | \*           | grouping_option | \*         | precision   | \*                                      | type   | \*                                   |
| ---- | --- | --------------------- | ------------ | ----- | ------------------ | -------- | -------- | ---- | ------ | ------------ | ------------ | --------------- | ---------- | ----------- | --------------------------------------- | ------ | ------------------------------------ |
|      |     | パディングに          | (任意の文字) | 方向  |                    | 符号     |          | n 進 | 0 埋め | フィールド幅 | (任意の数値) | 桁区切り        |            | 小数桁数    |                                         | 表現型 |                                      |
|      |     | 使う文字<sup>\*</sup> |              |       |                    |          |          |      |        |              |              |                 |            | type=f のみ |                                         |        |                                      |
| ---- | --- | --------------------  | ------------ | ----- | ------------------ | -------- | -------- | ---- | ------ | ------------ | ------------ | --------------- | ---------- | ----------- | --------------------------------------- | ------ | ------------------------------------ |
|      |     |                       |              | `<`   | 左詰め             | `+`      | `+/-`    |      |        |              |              | `,`             | 3 桁区切り | `.<桁数>`   |                                         | `b`    | 2 進数                               |
|      |     |                       |              | `>`   | 右詰め             | `-`      | `-` のみ |      |        |              |              |                 |            | `.1`        | 小数点以下１桁（小数点 2 位を四捨五入） | `c`    | Unicode 文字                         |
|      |     |                       |              | `=`   | 符号の後ろを埋める | 半角空白 | `空白/-` |      |        |              |              |                 |            |             |                                         | `d`    | 10 進数                              |
|      |     |                       |              | `^`   | 中央               |          |          |      |        |              |              |                 |            |             |                                         | `e`    | 指数表記                             |
|      |     |                       |              |       |                    |          |          |      |        |              |              |                 |            |             |                                         | `E`    | 大文字の `E` を使う指数表記          |
|      |     |                       |              |       |                    |          |          |      |        |              |              |                 |            |             |                                         | `f`    | 固定小数点数表記                     |
|      |     |                       |              |       |                    |          |          |      |        |              |              |                 |            |             |                                         | `F`    | (`nan` => `NAN`、`inf` => `INF`)     |
|      |     |                       |              |       |                    |          |          |      |        |              |              |                 |            |             |                                         | `g`    | 桁に応じて固定小数点か指数表記で表示 |
|      |     |                       |              |       |                    |          |          |      |        |              |              |                 |            |             |                                         | `G`    | (指数表記の時に`E`を使う)            |
|      |     |                       |              |       |                    |          |          |      |        |              |              |                 |            |             |                                         | `n`    | 数値(数値分割文字が挿入される)       |
|      |     |                       |              |       |                    |          |          |      |        |              |              |                 |            |             |                                         | `o`    | 8 進数                               |
|      |     |                       |              |       |                    |          |          |      |        |              |              |                 |            |             |                                         | `s`    | 文字列                               |
|      |     |                       |              |       |                    |          |          |      |        |              |              |                 |            |             |                                         | `x`    | 16 進数                              |
|      |     |                       |              |       |                    |          |          |      |        |              |              |                 |            |             |                                         | `X`    | `A`以降の数字に大文字を使う 16 進数  |
|      |     |                       |              |       |                    |          |          |      |        |              |              |                 |            |             |                                         | `%`    | 数値を 100 倍して%表記               |

注)

- f 文字列や str.format()では、fill に `{` と `}`を使えない

#### format 関数

#### str.format 関数

| 関数                            | 値           |                                     |
| ------------------------------- | ------------ | ----------------------------------- |
| `print('{}'.format(1))`         | `1`          |                                     |
| `print('{{}}'.format(1))`       | `{}`         | {}自体を記述したい場合は 2 つ重ねる |
| `print('{:+}'.format(1))`       | `+1`         | 正の数でも符号を表示                |
| `print('{:0=10}'.format(100))`  | `0000000100` | ゼロ埋め                            |
| `print('{:010}'.format(100))`   | `0000000100` |                                     |
| `print('{:0=10}'.format(-100))` | `-000000100` |                                     |
| `print('{:010}'.format(-100))`  | `-000000100` |                                     |
| `print('{:w<10}'.format(1))`    | `1wwwwwwwww` | 左寄せ                              |
| `print('{:0<10}'.format(1))`    | `1000000000` |                                     |
| `print('{:w>10}'.format(1))`    | `wwwwwwwww1` | 右寄せ                              |
| `print('{:0>10}'.format(1))`    | `0000000001` |                                     |
| `print('{:w^10}'.format(1))`    | `wwww1wwwww` | センタリング(中央寄せ)              |
| `print('{:0^10}'.format(1))`    | `0000100000` |                                     |

- 入れ子

```py
val = 15
digits = 6

'{:0>{width}b}'.format(val, width=digits)
'{0:0>{1}b}'.format(val, digits)
'{:0>{}{}}'.format(val, digits, 'b')
'{:{}{}{}}'.format(val, '0>',digits, 'b')
```

##### 整列

| 関数                                                         | 値      |                        |
| ------------------------------------------------------------ | ------- | ---------------------- |
| `print('{} {} {}'.format(1, 2, 3))`                          | `1 2 3` | 複数の値を埋め込む     |
| `print('{2} {0} {1}'.format(1, 2, 3))`                       | `3 1 2` | 埋め込み順序を指定する |
| `print('{one} {three} {two}'.format(one=1, two=2, three=3))` | `1 3 2` | 埋め込み順序を指定する |

##### 小数点以下の桁数

```py
print('{:.0f}'.format(1.5))
print('{:.0f}'.format(2.5)) # 偶数への丸め(JIS Z 8401)なので、3ではなく2となる(round関数と同様)
```

> 2
>
> 2

##### 桁区切り文字

```py
print('{:,}'.format(1234567))
```

> 1,234,567

##### 指数表記

```py
print('{:.3e}'.format(1.234567))
```

> 1.235e+00

##### 2 進数、8 進数、16 進数

| 関数                         | 値           |                     |
| ---------------------------- | ------------ | ------------------- |
| `print('{:d}'.format(255))`  | `255`        | 10 進数             |
|                              |              |                     |
| `print('{:b}'.format(255))`  | `11111111`   | 2 進数              |
| `print('{:o}'.format(255))`  | `377`        | 8 進数              |
| `print('{:x}'.format(255))`  | `ff`         | 16 進数             |
| `print('{:#b}'.format(255))` | `0b11111111` | 2 進数(接頭辞付き)  |
| `print('{:#o}'.format(255))` | `0o377`      | 8 進数(接頭辞付き)  |
| `print('{:#x}'.format(255))` | `0xff`       | 16 進数(接頭辞付き) |

##### リストの値を代入

```py
lst = ['first', 'second', 'third']
mes = '{}: {}{}'.format(*lst)
print(mes)

mes = '{0[0]}: {0[1]}{0[2]}'.format(lst)
print(mes)
```

> first: secondthird
>
> first: secondthird

```py
# 複数のリストから値を埋め込む
lst1 = ['first', 'second', 'third']
lst2 = ['one', 'two', 'three']
mes = '{0[0]}: {0[1]}{0[2]}\t{1[0]}: {1[1]}{1[2]}'.format(lst1, lst2)
print(mes)
```

> first: secondthird one: twothree

##### タプルの値を代入

```py
tpl = ('first', 'second', 'third')
mes = '{}: {}{}'.format(*tpl)
print(mes)

mes = '{0[0]}: {0[1]}{0[2]}'.format(tpl)
print(mes)
```

> first: secondthird
>
> first: secondthird

##### 辞書の値を代入

```py
dct = { 'aaa':'first', 'bbb':'second', 'ccc':'third'}
mes = '{aaa}: {bbb}{ccc}'.format(**dct)
print(mes)
```

> first: secondthird

##### クラスの属性値を代入

```py
class MyClass:
    id = 1
    name = 'n1'

myClass = MyClass()
print('{0.id} {0.name}'.format(myClass)) # クラスの属性を指定する
```

> 1 n1 \# クラスの属性を指定する

#### f 文字列

```py
one = 'first'
two = 2
three = '3rd'
mes = f'{one}: {two}{three}'
print(mes)
```

> first: 23rd

##### リストの値を代入

```py
lst = ['first', 'second', 'third']
mes = f'{lst[0]}: {lst[1]}{lst[2]}'
print(mes)
```

> first: secondthird

##### タプルの値を代入

```py
tpl = ('first', 'second', 'third')
mes = f'{tpl[0]}: {tpl[1]}{tpl[2]}'
print(mes)
```

> first: secondthird

##### 辞書の値を代入

`f""` の中では `"` は使えず、 `f''`の中では `'` は使えない(バックスラッシュでエスケープできない)

```py
dct = { 'aaa':'first', 'bbb':'second', 'ccc':'third'}
mes = f"{dct['aaa']}: {dct['bbb']}{dct['ccc']}"
print(mes)
```

> first: secondthird

#### フォーマット演算子

- 種類

| 関数                  | 種類    | 値             |
| --------------------- | ------- | -------------- |
| `print('%c' % 'A')`   | 文字    | `A`            |
| `print('%s' % 'ABC')` | 文字列  | `ABC`          |
| `print('%r' % 'ABC')` |         | `ABC`          |
|                       |         |                |
| `print('%d' % 123)`   | 整数    | `123`          |
| `print('%i' % 123)`   |         | `123`          |
|                       |         |                |
| `print('%e' % 1.23)`  | 指数    | `1.230000e+00` |
| `print('%E' % 1.23)`  |         | `1.230000E+00` |
| `print('%f' % 1.23)`  | 実数    | `1.23`         |
| `print('%F' % 1.23)`  |         | `1.23`         |
|                       |         |                |
| `print('%o' % 255)`   | 8 進数  | `377`          |
| `print('%b' % 255)`   |         | `377`          |
|                       |         |                |
| `print('%x' % 255)`   | 16 進数 | `ff`           |
| `print('%X' % 255)`   |         | `FF`           |
|                       |         |                |
| `print('%d%%' % 100)` | %自体   | `100%`         |

- 配置

| 関数                      | 値        | 備考              |
| ------------------------- | --------- | ----------------- |
| `print('|%4s|' % 'ABC')`  | `| ABC|`  | 右寄せ            |
| `print('|%-4s|' % 'ABC')` | `|ABC |`  | 左寄せ            |
| `print('|%4d|' % 123)`    | `| 123|`  | 右寄せ            |
| `print('|%-4d|' % 123)`   | `|123 |`  | 左寄せ            |
| `print('|%+5d|' % 123)`   | `| +123|` | ± 符号付き        |
| `print('|%5.2f|' % 1.23)` | `| 1.23|` | 桁数.小数部の桁数 |
| `print('|%05d|' % 123)`   | `|00123|` | 0 埋め            |

### 文字種チェック

#### 数値チェック

```py
def is_int(intstr):
    try:
        int(intstr)
        return True
    except ValueError:
        return False
```

```py
def check_numstr(numstr):
    print(
        '{} {} {} {}'.format(
            numstr,
            numstr.isdigit(),
            numstr.isdecimal(),
            numstr.isnumeric()
        )
    )
```

| numstr | isdigit() | isdecimal() | isnumeric() |
| ------ | --------- | ----------- | ----------- |
| `1`    | True      | True        | True        |
| `01`   | True      | True        | True        |
| `１`   | True      | True        | True        |
| `①`    | True      |             | True        |
| `一`   |           |             | True        |
| `1`    |           |             |             |
| `0x11` |           |             |             |
| `1.1`  |           |             |             |

```py
import itertools

print('| chr | isdigit | isdecimal | isnumeric')
print('---------------------------------------')
for number in range(0, 12000):
    char = chr(number)
    if (char.isdigit() or char.isdecimal() or char.isnumeric()):
        print('| {0:>3} | {1:^7} | {2:^9} | {3:9} '.format(
            char,
            'True' if char.isdigit() else ' ',
            'True' if char.isdecimal() else ' ',
            'True' if char.isnumeric() else ' '
        )
    )

```

```
|   0 |  True   |   True    | True
|   1 |  True   |   True    | True
|   2 |  True   |   True    | True
|   3 |  True   |   True    | True
|   4 |  True   |   True    | True
|   5 |  True   |   True    | True
|   6 |  True   |   True    | True
|   7 |  True   |   True    | True
|   8 |  True   |   True    | True
|   9 |  True   |   True    | True
|   ² |  True   |           | True
|   ³ |  True   |           | True
|   ¹ |  True   |           | True
|   ¼ |         |           | True
|   ½ |         |           | True
|   ¾ |         |           | True
|   ٠ |  True   |   True    | True
|   ١ |  True   |   True    | True
|   ٢ |  True   |   True    | True
|   ٣ |  True   |   True    | True
|   ٤ |  True   |   True    | True
|   ٥ |  True   |   True    | True
|   ٦ |  True   |   True    | True
|   ٧ |  True   |   True    | True
|   ٨ |  True   |   True    | True
|   ٩ |  True   |   True    | True
|   ۰ |  True   |   True    | True
|   ۱ |  True   |   True    | True
|   ۲ |  True   |   True    | True
|   ۳ |  True   |   True    | True
|   ۴ |  True   |   True    | True
|   ۵ |  True   |   True    | True
|   ۶ |  True   |   True    | True
|   ۷ |  True   |   True    | True
|   ۸ |  True   |   True    | True
|   ۹ |  True   |   True    | True
|   ߀ |  True   |   True    | True
|   ߁ |  True   |   True    | True
|   ߂ |  True   |   True    | True
|   ߃ |  True   |   True    | True
|   ߄ |  True   |   True    | True
|   ߅ |  True   |   True    | True
|   ߆ |  True   |   True    | True
|   ߇ |  True   |   True    | True
|   ߈ |  True   |   True    | True
|   ߉ |  True   |   True    | True
|   ० |  True   |   True    | True
|   १ |  True   |   True    | True
|   २ |  True   |   True    | True
|   ३ |  True   |   True    | True
|   ४ |  True   |   True    | True
|   ५ |  True   |   True    | True
|   ६ |  True   |   True    | True
|   ७ |  True   |   True    | True
|   ८ |  True   |   True    | True
|   ९ |  True   |   True    | True
|   ০ |  True   |   True    | True
|   ১ |  True   |   True    | True
|   ২ |  True   |   True    | True
|   ৩ |  True   |   True    | True
|   ৪ |  True   |   True    | True
|   ৫ |  True   |   True    | True
|   ৬ |  True   |   True    | True
|   ৭ |  True   |   True    | True
|   ৮ |  True   |   True    | True
|   ৯ |  True   |   True    | True
|   ৴ |         |           | True
|   ৵ |         |           | True
|   ৶ |         |           | True
|   ৷ |         |           | True
|   ৸ |         |           | True
|   ৹ |         |           | True
|   ੦ |  True   |   True    | True
|   ੧ |  True   |   True    | True
|   ੨ |  True   |   True    | True
|   ੩ |  True   |   True    | True
|   ੪ |  True   |   True    | True
|   ੫ |  True   |   True    | True
|   ੬ |  True   |   True    | True
|   ੭ |  True   |   True    | True
|   ੮ |  True   |   True    | True
|   ੯ |  True   |   True    | True
|   ૦ |  True   |   True    | True
|   ૧ |  True   |   True    | True
|   ૨ |  True   |   True    | True
|   ૩ |  True   |   True    | True
|   ૪ |  True   |   True    | True
|   ૫ |  True   |   True    | True
|   ૬ |  True   |   True    | True
|   ૭ |  True   |   True    | True
|   ૮ |  True   |   True    | True
|   ૯ |  True   |   True    | True
|   ୦ |  True   |   True    | True
|   ୧ |  True   |   True    | True
|   ୨ |  True   |   True    | True
|   ୩ |  True   |   True    | True
|   ୪ |  True   |   True    | True
|   ୫ |  True   |   True    | True
|   ୬ |  True   |   True    | True
|   ୭ |  True   |   True    | True
|   ୮ |  True   |   True    | True
|   ୯ |  True   |   True    | True
|   ୲ |         |           | True
|   ୳ |         |           | True
|   ୴ |         |           | True
|   ୵ |         |           | True
|   ୶ |         |           | True
|   ୷ |         |           | True
|   ௦ |  True   |   True    | True
|   ௧ |  True   |   True    | True
|   ௨ |  True   |   True    | True
|   ௩ |  True   |   True    | True
|   ௪ |  True   |   True    | True
|   ௫ |  True   |   True    | True
|   ௬ |  True   |   True    | True
|   ௭ |  True   |   True    | True
|   ௮ |  True   |   True    | True
|   ௯ |  True   |   True    | True
|   ௰ |         |           | True
|   ௱ |         |           | True
|   ௲ |         |           | True
|   ౦ |  True   |   True    | True
|   ౧ |  True   |   True    | True
|   ౨ |  True   |   True    | True
|   ౩ |  True   |   True    | True
|   ౪ |  True   |   True    | True
|   ౫ |  True   |   True    | True
|   ౬ |  True   |   True    | True
|   ౭ |  True   |   True    | True
|   ౮ |  True   |   True    | True
|   ౯ |  True   |   True    | True
|   ౸ |         |           | True
|   ౹ |         |           | True
|   ౺ |         |           | True
|   ౻ |         |           | True
|   ౼ |         |           | True
|   ౽ |         |           | True
|   ౾ |         |           | True
|   ೦ |  True   |   True    | True
|   ೧ |  True   |   True    | True
|   ೨ |  True   |   True    | True
|   ೩ |  True   |   True    | True
|   ೪ |  True   |   True    | True
|   ೫ |  True   |   True    | True
|   ೬ |  True   |   True    | True
|   ೭ |  True   |   True    | True
|   ೮ |  True   |   True    | True
|   ೯ |  True   |   True    | True
|   ൘ |         |           | True
|   ൙ |         |           | True
|   ൚ |         |           | True
|   ൛ |         |           | True
|   ൜ |         |           | True
|   ൝ |         |           | True
|   ൞ |         |           | True
|   ൦ |  True   |   True    | True
|   ൧ |  True   |   True    | True
|   ൨ |  True   |   True    | True
|   ൩ |  True   |   True    | True
|   ൪ |  True   |   True    | True
|   ൫ |  True   |   True    | True
|   ൬ |  True   |   True    | True
|   ൭ |  True   |   True    | True
|   ൮ |  True   |   True    | True
|   ൯ |  True   |   True    | True
|   ൰ |         |           | True
|   ൱ |         |           | True
|   ൲ |         |           | True
|   ൳ |         |           | True
|   ൴ |         |           | True
|   ൵ |         |           | True
|   ൶ |         |           | True
|   ൷ |         |           | True
|   ൸ |         |           | True
|   ෦ |  True   |   True    | True
|   ෧ |  True   |   True    | True
|   ෨ |  True   |   True    | True
|   ෩ |  True   |   True    | True
|   ෪ |  True   |   True    | True
|   ෫ |  True   |   True    | True
|   ෬ |  True   |   True    | True
|   ෭ |  True   |   True    | True
|   ෮ |  True   |   True    | True
|   ෯ |  True   |   True    | True
|   ๐ |  True   |   True    | True
|   ๑ |  True   |   True    | True
|   ๒ |  True   |   True    | True
|   ๓ |  True   |   True    | True
|   ๔ |  True   |   True    | True
|   ๕ |  True   |   True    | True
|   ๖ |  True   |   True    | True
|   ๗ |  True   |   True    | True
|   ๘ |  True   |   True    | True
|   ๙ |  True   |   True    | True
|   ໐ |  True   |   True    | True
|   ໑ |  True   |   True    | True
|   ໒ |  True   |   True    | True
|   ໓ |  True   |   True    | True
|   ໔ |  True   |   True    | True
|   ໕ |  True   |   True    | True
|   ໖ |  True   |   True    | True
|   ໗ |  True   |   True    | True
|   ໘ |  True   |   True    | True
|   ໙ |  True   |   True    | True
|   ༠ |  True   |   True    | True
|   ༡ |  True   |   True    | True
|   ༢ |  True   |   True    | True
|   ༣ |  True   |   True    | True
|   ༤ |  True   |   True    | True
|   ༥ |  True   |   True    | True
|   ༦ |  True   |   True    | True
|   ༧ |  True   |   True    | True
|   ༨ |  True   |   True    | True
|   ༩ |  True   |   True    | True
|   ༪ |         |           | True
|   ༫ |         |           | True
|   ༬ |         |           | True
|   ༭ |         |           | True
|   ༮ |         |           | True
|   ༯ |         |           | True
|   ༰ |         |           | True
|   ༱ |         |           | True
|   ༲ |         |           | True
|   ༳ |         |           | True
|   ၀ |  True   |   True    | True
|   ၁ |  True   |   True    | True
|   ၂ |  True   |   True    | True
|   ၃ |  True   |   True    | True
|   ၄ |  True   |   True    | True
|   ၅ |  True   |   True    | True
|   ၆ |  True   |   True    | True
|   ၇ |  True   |   True    | True
|   ၈ |  True   |   True    | True
|   ၉ |  True   |   True    | True
|   ႐ |  True   |   True    | True
|   ႑ |  True   |   True    | True
|   ႒ |  True   |   True    | True
|   ႓ |  True   |   True    | True
|   ႔ |  True   |   True    | True
|   ႕ |  True   |   True    | True
|   ႖ |  True   |   True    | True
|   ႗ |  True   |   True    | True
|   ႘ |  True   |   True    | True
|   ႙ |  True   |   True    | True
|   ፩ |  True   |           | True
|   ፪ |  True   |           | True
|   ፫ |  True   |           | True
|   ፬ |  True   |           | True
|   ፭ |  True   |           | True
|   ፮ |  True   |           | True
|   ፯ |  True   |           | True
|   ፰ |  True   |           | True
|   ፱ |  True   |           | True
|   ፲ |         |           | True
|   ፳ |         |           | True
|   ፴ |         |           | True
|   ፵ |         |           | True
|   ፶ |         |           | True
|   ፷ |         |           | True
|   ፸ |         |           | True
|   ፹ |         |           | True
|   ፺ |         |           | True
|   ፻ |         |           | True
|   ፼ |         |           | True
|   ᛮ |         |           | True
|   ᛯ |         |           | True
|   ᛰ |         |           | True
|   ០ |  True   |   True    | True
|   ១ |  True   |   True    | True
|   ២ |  True   |   True    | True
|   ៣ |  True   |   True    | True
|   ៤ |  True   |   True    | True
|   ៥ |  True   |   True    | True
|   ៦ |  True   |   True    | True
|   ៧ |  True   |   True    | True
|   ៨ |  True   |   True    | True
|   ៩ |  True   |   True    | True
|   ៰ |         |           | True
|   ៱ |         |           | True
|   ៲ |         |           | True
|   ៳ |         |           | True
|   ៴ |         |           | True
|   ៵ |         |           | True
|   ៶ |         |           | True
|   ៷ |         |           | True
|   ៸ |         |           | True
|   ៹ |         |           | True
|   ᠐ |  True   |   True    | True
|   ᠑ |  True   |   True    | True
|   ᠒ |  True   |   True    | True
|   ᠓ |  True   |   True    | True
|   ᠔ |  True   |   True    | True
|   ᠕ |  True   |   True    | True
|   ᠖ |  True   |   True    | True
|   ᠗ |  True   |   True    | True
|   ᠘ |  True   |   True    | True
|   ᠙ |  True   |   True    | True
|   ᥆ |  True   |   True    | True
|   ᥇ |  True   |   True    | True
|   ᥈ |  True   |   True    | True
|   ᥉ |  True   |   True    | True
|   ᥊ |  True   |   True    | True
|   ᥋ |  True   |   True    | True
|   ᥌ |  True   |   True    | True
|   ᥍ |  True   |   True    | True
|   ᥎ |  True   |   True    | True
|   ᥏ |  True   |   True    | True
|   ᧐ |  True   |   True    | True
|   ᧑ |  True   |   True    | True
|   ᧒ |  True   |   True    | True
|   ᧓ |  True   |   True    | True
|   ᧔ |  True   |   True    | True
|   ᧕ |  True   |   True    | True
|   ᧖ |  True   |   True    | True
|   ᧗ |  True   |   True    | True
|   ᧘ |  True   |   True    | True
|   ᧙ |  True   |   True    | True
|   ᧚ |  True   |           | True
|   ᪀ |  True   |   True    | True
|   ᪁ |  True   |   True    | True
|   ᪂ |  True   |   True    | True
|   ᪃ |  True   |   True    | True
|   ᪄ |  True   |   True    | True
|   ᪅ |  True   |   True    | True
|   ᪆ |  True   |   True    | True
|   ᪇ |  True   |   True    | True
|   ᪈ |  True   |   True    | True
|   ᪉ |  True   |   True    | True
|   ᪐ |  True   |   True    | True
|   ᪑ |  True   |   True    | True
|   ᪒ |  True   |   True    | True
|   ᪓ |  True   |   True    | True
|   ᪔ |  True   |   True    | True
|   ᪕ |  True   |   True    | True
|   ᪖ |  True   |   True    | True
|   ᪗ |  True   |   True    | True
|   ᪘ |  True   |   True    | True
|   ᪙ |  True   |   True    | True
|   ᭐ |  True   |   True    | True
|   ᭑ |  True   |   True    | True
|   ᭒ |  True   |   True    | True
|   ᭓ |  True   |   True    | True
|   ᭔ |  True   |   True    | True
|   ᭕ |  True   |   True    | True
|   ᭖ |  True   |   True    | True
|   ᭗ |  True   |   True    | True
|   ᭘ |  True   |   True    | True
|   ᭙ |  True   |   True    | True
|   ᮰ |  True   |   True    | True
|   ᮱ |  True   |   True    | True
|   ᮲ |  True   |   True    | True
|   ᮳ |  True   |   True    | True
|   ᮴ |  True   |   True    | True
|   ᮵ |  True   |   True    | True
|   ᮶ |  True   |   True    | True
|   ᮷ |  True   |   True    | True
|   ᮸ |  True   |   True    | True
|   ᮹ |  True   |   True    | True
|   ᱀ |  True   |   True    | True
|   ᱁ |  True   |   True    | True
|   ᱂ |  True   |   True    | True
|   ᱃ |  True   |   True    | True
|   ᱄ |  True   |   True    | True
|   ᱅ |  True   |   True    | True
|   ᱆ |  True   |   True    | True
|   ᱇ |  True   |   True    | True
|   ᱈ |  True   |   True    | True
|   ᱉ |  True   |   True    | True
|   ᱐ |  True   |   True    | True
|   ᱑ |  True   |   True    | True
|   ᱒ |  True   |   True    | True
|   ᱓ |  True   |   True    | True
|   ᱔ |  True   |   True    | True
|   ᱕ |  True   |   True    | True
|   ᱖ |  True   |   True    | True
|   ᱗ |  True   |   True    | True
|   ᱘ |  True   |   True    | True
|   ᱙ |  True   |   True    | True
|   ⁰ |  True   |           | True
|   ⁴ |  True   |           | True
|   ⁵ |  True   |           | True
|   ⁶ |  True   |           | True
|   ⁷ |  True   |           | True
|   ⁸ |  True   |           | True
|   ⁹ |  True   |           | True
|   ₀ |  True   |           | True
|   ₁ |  True   |           | True
|   ₂ |  True   |           | True
|   ₃ |  True   |           | True
|   ₄ |  True   |           | True
|   ₅ |  True   |           | True
|   ₆ |  True   |           | True
|   ₇ |  True   |           | True
|   ₈ |  True   |           | True
|   ₉ |  True   |           | True
|   ⅐ |         |           | True
|   ⅑ |         |           | True
|   ⅒ |         |           | True
|   ⅓ |         |           | True
|   ⅔ |         |           | True
|   ⅕ |         |           | True
|   ⅖ |         |           | True
|   ⅗ |         |           | True
|   ⅘ |         |           | True
|   ⅙ |         |           | True
|   ⅚ |         |           | True
|   ⅛ |         |           | True
|   ⅜ |         |           | True
|   ⅝ |         |           | True
|   ⅞ |         |           | True
|   ⅟ |         |           | True
|   Ⅰ |         |           | True
|   Ⅱ |         |           | True
|   Ⅲ |         |           | True
|   Ⅳ |         |           | True
|   Ⅴ |         |           | True
|   Ⅵ |         |           | True
|   Ⅶ |         |           | True
|   Ⅷ |         |           | True
|   Ⅸ |         |           | True
|   Ⅹ |         |           | True
|   Ⅺ |         |           | True
|   Ⅻ |         |           | True
|   Ⅼ |         |           | True
|   Ⅽ |         |           | True
|   Ⅾ |         |           | True
|   Ⅿ |         |           | True
|   ⅰ |         |           | True
|   ⅱ |         |           | True
|   ⅲ |         |           | True
|   ⅳ |         |           | True
|   ⅴ |         |           | True
|   ⅵ |         |           | True
|   ⅶ |         |           | True
|   ⅷ |         |           | True
|   ⅸ |         |           | True
|   ⅹ |         |           | True
|   ⅺ |         |           | True
|   ⅻ |         |           | True
|   ⅼ |         |           | True
|   ⅽ |         |           | True
|   ⅾ |         |           | True
|   ⅿ |         |           | True
|   ↀ |         |           | True
|   ↁ |         |           | True
|   ↂ |         |           | True
|   ↅ |         |           | True
|   ↆ |         |           | True
|   ↇ |         |           | True
|   ↈ |         |           | True
|   ↉ |         |           | True
|   ① |  True   |           | True
|   ② |  True   |           | True
|   ③ |  True   |           | True
|   ④ |  True   |           | True
|   ⑤ |  True   |           | True
|   ⑥ |  True   |           | True
|   ⑦ |  True   |           | True
|   ⑧ |  True   |           | True
|   ⑨ |  True   |           | True
|   ⑩ |         |           | True
|   ⑪ |         |           | True
|   ⑫ |         |           | True
|   ⑬ |         |           | True
|   ⑭ |         |           | True
|   ⑮ |         |           | True
|   ⑯ |         |           | True
|   ⑰ |         |           | True
|   ⑱ |         |           | True
|   ⑲ |         |           | True
|   ⑳ |         |           | True
|   ⑴ |  True   |           | True
|   ⑵ |  True   |           | True
|   ⑶ |  True   |           | True
|   ⑷ |  True   |           | True
|   ⑸ |  True   |           | True
|   ⑹ |  True   |           | True
|   ⑺ |  True   |           | True
|   ⑻ |  True   |           | True
|   ⑼ |  True   |           | True
|   ⑽ |         |           | True
|   ⑾ |         |           | True
|   ⑿ |         |           | True
|   ⒀ |         |           | True
|   ⒁ |         |           | True
|   ⒂ |         |           | True
|   ⒃ |         |           | True
|   ⒄ |         |           | True
|   ⒅ |         |           | True
|   ⒆ |         |           | True
|   ⒇ |         |           | True
|   ⒈ |  True   |           | True
|   ⒉ |  True   |           | True
|   ⒊ |  True   |           | True
|   ⒋ |  True   |           | True
|   ⒌ |  True   |           | True
|   ⒍ |  True   |           | True
|   ⒎ |  True   |           | True
|   ⒏ |  True   |           | True
|   ⒐ |  True   |           | True
|   ⒑ |         |           | True
|   ⒒ |         |           | True
|   ⒓ |         |           | True
|   ⒔ |         |           | True
|   ⒕ |         |           | True
|   ⒖ |         |           | True
|   ⒗ |         |           | True
|   ⒘ |         |           | True
|   ⒙ |         |           | True
|   ⒚ |         |           | True
|   ⒛ |         |           | True
|   ⓪ |  True   |           | True
|   ⓫ |         |           | True
|   ⓬ |         |           | True
|   ⓭ |         |           | True
|   ⓮ |         |           | True
|   ⓯ |         |           | True
|   ⓰ |         |           | True
|   ⓱ |         |           | True
|   ⓲ |         |           | True
|   ⓳ |         |           | True
|   ⓴ |         |           | True
|   ⓵ |  True   |           | True
|   ⓶ |  True   |           | True
|   ⓷ |  True   |           | True
|   ⓸ |  True   |           | True
|   ⓹ |  True   |           | True
|   ⓺ |  True   |           | True
|   ⓻ |  True   |           | True
|   ⓼ |  True   |           | True
|   ⓽ |  True   |           | True
|   ⓾ |         |           | True
|   ⓿ |  True   |           | True
|   ❶ |  True   |           | True
|   ❷ |  True   |           | True
|   ❸ |  True   |           | True
|   ❹ |  True   |           | True
|   ❺ |  True   |           | True
|   ❻ |  True   |           | True
|   ❼ |  True   |           | True
|   ❽ |  True   |           | True
|   ❾ |  True   |           | True
|   ❿ |         |           | True
|   ➀ |  True   |           | True
|   ➁ |  True   |           | True
|   ➂ |  True   |           | True
|   ➃ |  True   |           | True
|   ➄ |  True   |           | True
|   ➅ |  True   |           | True
|   ➆ |  True   |           | True
|   ➇ |  True   |           | True
|   ➈ |  True   |           | True
|   ➉ |         |           | True
|   ➊ |  True   |           | True
|   ➋ |  True   |           | True
|   ➌ |  True   |           | True
|   ➍ |  True   |           | True
|   ➎ |  True   |           | True
|   ➏ |  True   |           | True
|   ➐ |  True   |           | True
|   ➑ |  True   |           | True
|   ➒ |  True   |           | True
|   ➓ |         |           | True
|   ⳽  |         |           | True

```

### バイト列(byte), Unicode

#### Python 3

```py
print('あいうえお')
print(len('あいうえお'))        # uをつけなくてもUnicodeとして扱われる
print(b'あいうえお')
print(len(b'あいうえお'))       # バイト列として扱われる
print(r'あいう\nえお')          # Raw文字列
print(len(r'あいう\nえお'))
```

> あいうえお
>
> 5
>
> SyntaxError: bytes can only contain ASCII literal characters.
>
> SyntaxError: bytes can only contain ASCII literal characters.
>
> あいう\n えお
>
> 7

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

#### 文字列とバイト列の変換

```py
'foobar'.encode() # b'foobar'
b'foobar'.decode() # 'foobar'

# 文字コードを明示
'foobar'.encode(encoding='utf-8') # b'foobar'
b'foobar'.decode(encoding='utf-8') # 'foobar'
bytes('abcd', encoding='utf-8')
str(b'abcd', encoding='utf-8')

# UnicodeDecodeErrorを無視する
b'\xff'.decode() # UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte

b'\xff'.decode('utf-8', 'replace') # '�'
b'\xff'.decode(encoding='utf-8', errors='replace') # '�'

bytes('abcd', encoding='utf-8', errors='replace') # b'abcd'
str(b'abcd', encoding='utf-8', errors='replace') # 'abcd'

```

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

#### split の引数を指定しないと、空白文字(タブ文字、改行文字を含む)で分割される

```py
hoge = 'a bc\nde f\nghi\njkl\nmno\npqr\nstu\nvwx\ny z'
parts = hoge.split('\n')
print(parts)
```

> ['a bc', 'de f', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'y z']

| 文字          |
| ------------- |
| スペース ``   |
| タブ `\t`     |
| 改行 `\n`     |
| 復帰 `\r`     |
| 改頁 `\f`     |
| 垂直タブ `\v` |

#### split で分割した後、各要素の先頭・末尾の空白文字を除去する

```py
hoge = 'abc, def,\tghi'
parts = [x.strip() for x in hoge.split(',')]
print(parts)
```

> ['abc', 'def', 'ghi']

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

#### 1 文字ずつ処理する

```py
for c in 'abc':
    print(c)
```

> a
>
> b
>
> c

##### インデックスを取得

```py
for i, c in enumerate('abc'):
    print("{0}: {1}".format(i, c))
```

> 0: a
>
> 1: b
>
> 2: c

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

### エンコード・デコード

#### Base64

```py
import base64

filepath = '/path/to/file'
filecontents = open(filepath, 'rb').read()

# エンコード
encoded = base64.b64encode( filecontents )
print(encoded)

# デコード
decoded = base64.b64decode( encoded )
if filecontents == decoded:
    print('success')
else:
    print('failure')
```

#### URL safe な Base64

```py
import base64

filepath = '/path/to/file'
filecontents = open(filepath, 'rb').read()

# エンコード
encoded = base64.urlsafe_b64encode( filecontents )
print(encoded)

# デコード
decoded = base64.urlsafe_b64decode( encoded )
if filecontents == decoded:
    print('success')
else:
    print('failure')
```

### 検索

#### 単純な検索

| メソッド | 特徴                                           |
| -------- | ---------------------------------------------- |
| find     | 文字列が見つからない場合に `-1` を返す         |
| index    | 文字列が見つからない場合に `ValueError` を返す |

```py
# -----:    0000000000111111111122222222223333333333444444444455
# count:    0123456789012345678901234567890123456789012345678901
haystack = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
needle = 'e'
```

| 機能                       | 関数                            | 値     |
| -------------------------- | ------------------------------- | ------ |
| 文字列が含まれているか判定 | `print(needle in haystack)`     | `True` |
| 出現回数                   | `print(haystack.count(needle))` | `2`    |

| 機能                                       | 関数                                      | 値                                |
| ------------------------------------------ | ----------------------------------------- | --------------------------------- |
| 左から検索した場合の出現箇所(インデックス) | `print(haystack.find(needle))`            | `4`                               |
| (検索開始位置を指定)                       | `print(haystack.find(needle, 4))`         | `4`                               |
|                                            | `print(haystack.find(needle, 5))`         | `30`                              |
| (検索開始位置・検索終了位置を指定)         | `print(haystack.find(needle, 5,30))`      | `-1`                              |
|                                            | `print(haystack.index(needle, 5,30))`     | `ValueError: substring not found` |
|                                            | `print(haystack.find(needle, 5,31))`      | `30`                              |
|                                            |                                           |                                   |
| 右から検索した場合の出現箇所(インデックス) | `print(haystack.rfind(needle))`           | `30`                              |
| (検索終了位置を指定)                       | `print(haystack.rfind(needle, None, 30))` | `4`                               |
|                                            | `print(haystack.rfind(needle, None, 31))` | `30`                              |
| (検索開始位置・検索終了位置を指定)         | `print(haystack.rfind(needle, 5,30))`     | `-1`                              |
| (検索開始位置・検索終了位置を指定)         | `print(haystack.rindex(needle, 5,30))`    | `ValueError: substring not found` |
| (検索開始位置・検索終了位置を指定)         | `print(haystack.rfind(needle, 4,30))`     | `4`                               |

##### 前方一致

```py
haystack = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
haystack.startswith('abc')
haystack.startswith('xyz')
```

> True
>
> False

##### 後方一致

```py
haystack = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
haystack.endswith('abc')
haystack.endswith('xyz')
```

> False
>
> True

#### 正規表現による検索

##### パターンのコンパイル

```py
import re
r = re.compile(r'(\w)')
```

###### パターンを文字列型変数からコンパイル

```py
s = r'C:\Users\y\Documents'     # Raw文字列
print(s)                        # C:\Users\y\Documents

s = 'C:\\Users\\y\\Documents'
print(s)                        # C:\Users\y\Documents

p = 'y\\'
print(re.search(repr(p)[1:-1], s)) # <re.Match object; span=(9, 11), match='y\\'>
```

- raw 文字列でも、引用符をバックスラッシュでエスケープできるが、バックスラッシュ自体も文字列に残る
- - raw 文字列の末尾に奇数個連続したバックスラッシュは置けない
- - `r"\""` は OK、 `r"\"` は NG

```py
print(re.search('y', s))        # <re.Match object; span=(9, 10), match='y'>
print(re.search(r'y\', s))      # SyntaxError: EOL while scanning string literal
print(re.search('y\', s))       # SyntaxError: EOL while scanning string literal
print(re.search(r'y\\', s))     # <re.Match object; span=(9, 11), match='y\\'>
print(re.search('y\\', s))      # re.error: bad escape (end of pattern) at position 1
print(re.search(r'y\\\', s))    # SyntaxError: EOL while scanning string literal
print(re.search('y\\\', s))     # SyntaxError: EOL while scanning string literal
```

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

| 関数                         | 値                                                        | 備考         |
| ---------------------------- | --------------------------------------------------------- | ------------ |
| `print(matched)`             | `<\_sre.SRE_Match object; span=(0, 8), match='haystack'>` | コンパイル有 |
| `print(matched)`             | `<\_sre.SRE_Match object; span=(0, 8), match='haystack'>` | コンパイル無 |
|                              |                                                           |              |
| `print(matched.group())`     | `haystack`                                                |              |
| `print(matched.start())`     | `0`                                                       |              |
| `print(matched.end())`       | `8`                                                       |              |
| `print(matched.span())`      | `(0, 8)`                                                  |              |
|                              |                                                           |              |
| `print(matched.groups())`    | `('haysta', 'ck')`                                        |              |
| `print(g)` (1 回目のループ)  | `haysta`                                                  |              |
| `print(g)` (2 回目のループ)  | `ck`                                                      |              |
|                              |                                                           |              |
| `print(matched.group(0))`    | `haystack`                                                |              |
| `print(matched.group(1))`    | `haysta`                                                  |              |
| `print(matched.group(2))`    | `ck`                                                      |              |
| `print(matched.group(0, 1))` | `('haystack', 'haysta')`                                  |              |
|                              |                                                           |              |
| `print(matched.start(0))`    | `0`                                                       |              |
| `print(matched.end(1))`      | `6`                                                       |              |
| `print(matched.span(2))`     | `(6, 8)`                                                  |              |

##### 文字列の途中でマッチ

###### マッチした最初の場所

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

| 関数                      | 値                                            | 備考         |
| ------------------------- | --------------------------------------------- | ------------ |
| `print(searched)`         | `<re.Match object; span=(0, 3), match='hay'>` | コンパイル有 |
| `print(searched)`         | `<re.Match object; span=(0, 3), match='hay'>` | コンパイル無 |
| `print(searched.group())` | `hay`                                         |              |
| `print(searched.start())` | `0`                                           |              |
| `print(searched.end())`   | `3`                                           |              |
| `print(searched.span())`  | `(0, 3)`                                      |              |

###### 文字列の途中でマッチした全ての箇所のリスト

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

| 関数              | 値                | 備考         |
| ----------------- | ----------------- | ------------ |
| `print(allfound)` | `['hay', 'tack']` | コンパイル有 |
| `print(allfound)` | `['hay', 'tack']` | コンパイル無 |
| `print(allfound)` | `['hay', 'tack']` | 結果を取得   |

###### 文字列の途中でマッチした全ての箇所のイテレーター

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

| 関数                                | 値                                              | 備考         |
| ----------------------------------- | ----------------------------------------------- | ------------ |
| `print(allfound)`                   | `<callable_iterator object at 0x7fd0e8dd4da0\>` | コンパイル有 |
| `print(allfound)`                   | `<callable_iterator object at 0x7fd0e8cc8a20\>` | コンパイル無 |
| `print(found.group())` (1 ループ目) | `hay`                                           |              |
| `print(found.start())` (1 ループ目) | `0`                                             |              |
| `print(found.end())` (1 ループ目)   | `3`                                             |              |
| `print(found.span())` (1 ループ目)  | `(0, 3)`                                        |              |
| `print(found.group())` (2 ループ目) | `tack`                                          |              |
| `print(found.start())` (2 ループ目) | `4`                                             |              |
| `print(found.end())` (2 ループ目)   | `8`                                             |              |
| `print(found.span())` (2 ループ目)  | `(4, 8)`                                        |              |

##### グループ化

###### グループ番号

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

| 関数                      | 値                     |
| ------------------------- | ---------------------- |
| `print(matched.groups())` | `('h', 'aysta', 'ck')` |
| `print(matched.group(0))` | `haystack`             |
| `print(matched.group(1))` | `h`                    |
| `print(matched.group(2))` | `aysta`                |
| `print(matched.group(3))` | `ck`                   |

###### シンボリックグループ名

```py
import re

haystack = 'haystack'
needle = r'(?P<ONE>h)(?P<two>[abd-gijl-z]+)(?P<three>[ck]+)'

matched = re.match(needle, haystack)
print(matched.group('ONE'))
print(matched.group('two'))
print(matched.group('three'))
print(matched.group(0, 'three'))

print(matched.groupdict())
```

| 関数                               | 値                                             |
| ---------------------------------- | ---------------------------------------------- |
| `print(matched.group('ONE'))`      | `h`                                            |
| `print(matched.group('two'))`      | `aysta`                                        |
| `print(matched.group('three'))`    | `ck`                                           |
| `print(matched.group(0, 'three'))` | `('haystack', 'ck')`                           |
|                                    |                                                |
| `print(matched.groupdict())`       | `{'ONE': 'h', 'two': 'aysta', 'three3': 'ck'}` |

##### フラグを利用

[モジュールコンテンツ](https://docs.python.org/ja/3/library/re.html#contents-of-module-re)

| フラグ                | 効果                                                                                                                                                                            |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| re.ASCII<br>re.A      | \w 、\W 、\b 、\B 、\d 、\D 、\s 、および \S に、完全な Unicode マッチングではなく ASCII 限定マッチングを行わせます                                                             |
| re.DOTALL<br>re.S     | '.' 特殊文字を、改行を含むあらゆる文字にマッチさせます                                                                                                                          |
| re.IGNORECASE<br>re.I | 大文字・小文字を区別しないマッチングを行います                                                                                                                                  |
| re.MULTILINE<br>re.M  | パターン文字 '^' は文字列の先頭で、および各行の先頭 (各改行の直後) で、マッチします。そしてパターン文字 '\$' は文字列の末尾で、および各行の末尾 (各改行の直前) で、マッチします |
| re.VERBOSE<br>re.X    | 正規表現を、パターンの論理的な節を視覚的に分割し、コメントを加えることで、見た目よく読みやすく書けるようにします                                                                |

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

| 関数               | 値                |
| ------------------ | ----------------- |
| `print(allfoundA)` | `['12345.67890']` |
| `print(allfoundB)` | `['12345.67890']` |

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

| 文字種              | パターン                                                    | 例             |
| ------------------- | ----------------------------------------------------------- | -------------- |
| 半角英字            | `'[a-zA-Z]+'`                                               |                |
| 半角数字            | `'[0-9]+'`                                                  |                |
| ASCII 文字          | `'[\u0000-\u007F]+'`                                        | `ABCabc!"#$%&` |
| 半角記号            | `'[\u0020-\u002F\u003A-\u0040\u005B-\u0060\u007B-\u007E]+'` | `!"#$%&`       |
| 全角英字            | `'[ａ-ｚＡ-Ｚ]+'`                                           |                |
| 全角数字            | `'[０-９]+'`                                                |                |
| ローマ数字          | `'[\u2160-\u217F]+'`                                        | `ⅠⅡⅢ`          |
| 漢数字              | `'[〇一二三四五六七八九十百千万億兆]+'`                     |                |
| ひらがな            | `'[\u3041-\u309F]+'`                                        |                |
| 全角カタカナ        | `'[\u30A1-\u30FF]+'`                                        |                |
| 半角カタカナ        | `'[\uFF66-\uFF9F]+'`                                        |                |
| 漢字 (CJK 統合漢字) | `'[\u4E00-\u9FFF]+'`                                        |
| ハングル            | `'[가-힣]+'`                                                |                |

#### 文字種のフィルタリング

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

##### 前後の空白文字を除去

```py
s = ' \txyz\t '
print('^' + s.strip() + '$')
print('^' + s.lstrip() + '$')
print('^' + s.rstrip() + '$')
```

> ^xyz\$
>
> ^xyz \$
>
> ^ xyz\$

```py
s = '### \txyz\t ###'
print('^' + s.strip('#') + '$') # 引数に指定された文字を先頭・末尾から除去する(空白文字は除去しない)
print('^' + s.lstrip('#') + '$')
print('^' + s.rstrip('#') + '$')
```

> ^ xyz \$
>
> ^ xyz ###\$
>
> ^### xyz \$

##### 大文字化・小文字化

```py
print('abcde'.upper())
print('ABCDE'.lower())
```

> ABCDE
>
> abcde

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

##### 数字のみ抽出

```py
# 正規表現操作のライブラリ
import re
content =  '123１２３一二三'
numstr = re.sub('\\D', '', content)
print(numstr)
```

> 123 １２３

##### ファイル名に使用できない文字を除去

```py
import re

haystack = 'foobar/hoge!piyo'
replacement = '-'

content = re.sub(r'[\\|/|:|?|.|"|<|>|\|]', replacement, haystack)
print(content)
```

> foobar-hoge!piyo

#### 1 文字ごとの置換

```py
haystack = 'haystack'
print(haystack.translate(str.maketrans({'h': 'H', 'a': 'oo', 's': '', 'k': None})))
```

> Hooytooc

### 絵文字

[emoji](https://pypi.org/project/emoji/)

```sh
$ pip install emoji --upgrade
```

```py
import emoji
print(emoji.emojize('Python is :thumbs_up:'))
```

> Python is 👍

### ランダムな文字列の生成

```py
import random

str_length = 10
universe = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

generated = "".join([random.choice(universe) for x in range(str_length)])
print(generated)
```

> XGIuCq68EQ

## リスト

```
[ ]:リスト, ( ):タプル, { }:セット/辞書
リストは変更可能
タプルは変更不可
```

### リストが空か検査

| 判定方法      |
| ------------- |
| `not lst`     |
| `len(lst)==0` |
| `lst == []`   |

```py
lst = []
if not lst:
  print('empty')

if len(lst)==0:
  print('empty')

if lst == []:
  print('empty')
```

### リストを生成

#### 空のリストを生成

| 関数                | 値                                                             |
| ------------------- | -------------------------------------------------------------- |
| `lst = []`          | `[]`                                                           |
| `lst = [None] * 10` | `[None, None, None, None, None, None, None, None, None, None]` |
| `lst = [0] * 10`    | `[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]`                               |

#### リストをコピーして生成

```py
oldlist = ['foo', 'bar', 'hoge']
newlist = list(oldlist)
print(newlist)
```

> \# newlist
>
> ['foo', 'bar', 'hoge']

#### タプルからリストを生成

```py
tpllist = list(('foo', 'bar', 'hoge'))
print(tpllist)
```

> \# tpllist
>
> ['foo', 'bar', 'hoge']

#### range()を使って連番の要素を持つリストを生成

```py
rnglist = list(range(5))
print(rnglist)
```

> \# rnglist
>
> [0, 1, 2, 3, 4]

#### 文字列からリストを生成

```py
strlist = list('abcdefg')
print(strlist)
```

> \# strlist
>
> ['a', 'b', 'c', 'd', 'e', 'f', 'g']

### リストに要素を追加

#### append(末尾に追加)

```py

lst = ['foo', 'hoge']
lst.append('piyo')
print(lst)

lst.append(['fu', 'ga']) # appendの引数にリストを指定すると、リスト自体が新たな要素になる
print(lst)
```

> ['foo', 'hoge', 'piyo']
>
> ['foo', 'hoge', 'piyo', ['fu', 'ga']]

#### insert(添え字と要素の値を指定)

```py
lst.insert(1, 'bar')
print(lst)
```

> ['foo', 'bar', 'hoge', 'piyo']

#### スライスを使用して、別のリスト(別のイテラブルオブジェクト)の要素を指定位置に追加(連結)する

```py
lst = ['foo', 'bar', 'hoge']
print(lst[0:len(lst)-1])
print(lst[0:len(lst)])

lst[len(lst):len(lst)] = ['fu', 'ga']
print(lst)
```

> ['foo', 'bar']
>
> ['foo', 'bar', 'hoge']
>
> ['foo', 'bar', 'hoge', 'fu', 'ga']

#### 別のリスト(別のイテラブルオブジェクト)の要素を末尾に追加(連結)する

```py
lst1 = ['foo', 'bar', 'hoge']
lst2 = ['fu', 'ga']
lst1.extend(lst2)
print(lst1)

lst1.extend('piyo') # 文字列を追加する場合、1文字ずつが要素となる
print(lst1)

lst1.extend(['piyo']) # 文字列を1要素として追加する場合
print(lst1)

lst1 = ['foo', 'bar', 'hoge']
lst2 = ['fu', 'ga']
lst1 = lst1 + lst2
print(lst1)

lst1 = lst1 + ['piyo'] # 文字列を1要素として追加する場合
print(lst1)
```

> ['foo', 'bar', 'hoge', 'fu', 'ga']
>
> ['foo', 'bar', 'hoge', 'fu', 'ga', 'p', 'i', 'y', 'o']
>
> ['foo', 'bar', 'hoge', 'fu', 'ga', 'p', 'i', 'y', 'o', 'piyo']
>
> ['foo', 'bar', 'hoge', 'fu', 'ga']
>
> ['foo', 'bar', 'hoge', 'fu', 'ga', 'piyo']

#### リストの要素を繰り返す

```py
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
lst.remove('bar') # 指定された値を持つ要素のうち、最初のものを除去

# 初期化(すべての要素を削除)
lst.clear()
```

> 'hoge'
>
> ['foo', 'bar']
>
> 'foo'
>
> ['bar']
>
> []
>
> []

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
l1 = list(range(5)) # リストの要素数が同じ場合
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
l1 = list(range(5)) # リストの要素数が異なる場合
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

```py
from itertools import zip_longest

l1 = list(range(5)) # リストの要素数が異なる場合
l2 = list(range(5,8))

# 要素数の多いリストの要素数分だけ繰り返す
for (i1, i2) in zip_longest(l1, l2):
    print(i1, i2)

# 要素数の多いリストの要素数分だけ繰り返す(不足している要素にNoneではなく指定した値を使用)
for (i1, i2) in zip_longest(l1, l2, fillvalue=999):
    print(i1, i2)
```

> 0 5
>
> 1 6
>
> 2 7
>
> 3 999
>
> 4 999

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

##### に平坦化(flatten)

##### 2 次元リストを 1 次元リストに平坦化(flatten)

```py
l = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 内包表記
result = [item for m in l for item in m]

# itertools
from itertools import chain
result = list(chain.from_iterable(l))
```

> [1, 2, 3, 4, 5, 6, 7, 8, 9]

##### 多次元リストを 1 次元リストに平坦化(flatten)

```py
import collections.abc

l = [
    [1, [2, 3]],
    [4, 5, [6]],
    [[7, 8], 9]
]

def flatten(l):
    i = 0
    while i < len(l):
        while isinstance(l[i], collections.Iterable):
            if not l[i]:
                l.pop(i)
                i -= 1
                break
            else:
                l[i:i + 1] = l[i]
        i += 1
    return l

result = flatten(l)
```

> [1, 2, 3, 4, 5, 6, 7, 8, 9]

#### リストの要素を連結した文字列を取得

```py
lst = ['foo', 'bar', 'hoge']
''.join(lst)
','.join(lst) # 区切り文字を指定
```

> 'foobarhoge'
>
> 'foo,bar,hoge'

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

#### ソート条件を変える

ラムダ式を指定すると、要素ごとに関数を実行した結果を基にソートされる

##### 文字数でソート

```py
print(len)

lst = ['foo', 'bar', 'piyo', 'hoge', 'foo', 'bar', 'piyo', 'hoge']
sortedlist = sorted(lst, key=len)
print(lst)
print(sortedlist)
```

> \<built-in function len\>
>
> ['foo', 'bar', 'piyo', 'hoge', 'foo', 'bar', 'piyo', 'hoge']
>
> ['foo', 'bar', 'foo', 'bar', 'piyo', 'hoge', 'piyo', 'hoge']

##### 末尾の文字のアルファベット順でソート

```py
lst = ['foo', 'bar', 'piyo', 'hoge', 'foo', 'bar', 'piyo', 'hoge']
sortedlist = sorted(lst, key=lambda x: x[-1:])
print(lst)
print(sortedlist)
```

> ['foo', 'bar', 'piyo', 'hoge', 'foo', 'bar', 'piyo', 'hoge']
>
> ['hoge', 'hoge', 'foo', 'piyo', 'foo', 'piyo', 'bar', 'bar']

#### ソート条件を変える

ラムダ式を指定すると、要素ごとに関数を実行した結果を基にソートされる

### リストの重複する要素

#### リストの重複する要素を除去

#### リストの重複する要素を除去

```py
# 順番を無視
l = ['foo', 'bar', 'hoge', 'foo', 'bar', 'hoge', 'foo', 'bar', 'hoge']
ls = list(set(l))
print(ls)
```

> ['hoge', 'bar', 'foo']

#### リストの重複する要素を除去

```py
# Python 3.6以降
ld = list(dict.fromkeys(l))
print(ld)

# Python 3.5以前
ss = sorted(set(l), key=l.index)
print(ss)
```

> ['foo', 'bar', 'hoge']
>
> ['foo', 'bar', 'hoge']

##### リストが入れ子の場合

```py
def uniq(td):
    f = []
    return [i for i in td if i not in f and not f.append(i)]

l2d = [['foo'], ['bar'], ['hoge'], ['foo'], ['bar'], ['hoge'], ['foo'], ['bar'], ['hoge']]
uniql2d = uniq(l2d)
print(uniql2d)
```

> [['foo'], ['bar'], ['hoge']]

#### リストの重複する要素を抽出

#### リストの重複する要素を抽出

```py
l = ['foo', 'bar', 'hoge', 'foo', 'bar', 'hoge', 'foo', 'bar', 'hoge']
sc = [x for x in set(l) if l.count(x) > 1]
print(sc)
```

> ['hoge', 'bar', 'foo']

#### リストの重複する要素を抽出

```py
# Python 3.6以降
df = [x for x in dict.fromkeys(l) if l.count(x) > 1]
print(df)

# Python 3.5以前
sk = sorted([x for x in set(l) if l.count(x) > 1], key=l.index)
print(ss)
```

> ['foo', 'bar', 'hoge']
>
> ['foo', 'bar', 'hoge']

### 高階関数

#### map(要素ごとに処理)

第 2 引数の各要素に対して、第 1 引数の lambda 式を適用した結果をイテレータとして返す

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

#### filter(要素のフィルタリング)

リストに対してフィルタリングする

```py
numlist = [1, 3, 5, 2, 4]

def isodd(x): return x % 2 # 条件式(True/Falseを返す)のlambda式

print(list(filter(isodd, numlist)))
print(list(filter(lambda x: x % 2, numlist)))
print([x for x in numlist if x % 2]) # 同じことを内包表記で行う
```

> [1, 3, 5]

#### reduce(畳み込み／集約)

リストに対する畳みこみ(集約)

```py
from functools import reduce

numlist = [1, 3, 5, 2, 4]

def add(x, y): return x + y

print(reduce(add, numlist))
print(reduce(lambda x, y: x + y, numlist))
```

> 15

### リストの内包表記

```
形式: [式 for 変数 in イテラブルオブジェクト if 条件式]
```

高階関数のうち、map と filter は内包表記でも同等の処理を行うことが可能

#### map(要素ごとに処理)

要素全てに処理を行う

```py
l = list(range(100))

# 要素全てに処理を行う
strlist = [str(i) for i in l]
print(strlist)
```

> ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99']

#### filter(要素のフィルタリング)

条件に合致する要素のみからなるリストを生成(抽出)

```py
l = list(range(100))

# 条件に合致する要素のみからなるリストを生成(抽出)
fivelist = [i for i in l if i % 5 == 0 and i <= 50]
print(fivelist)

fivelist = [i  if i % 5 == 0 and i <= 50 else -1 for i in l] # elseがある場合は三項演算子なので順序が変わる
print(fivelist)
```

> [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
>
> [0, -1, -1, -1, -1, 5, -1, -1, -1, -1, 10, -1, -1, -1, -1, 15, -1, -1, -1, -1, 20, -1, -1, -1, -1, 25, -1, -1, -1, -1, 30, -1, -1, -1, -1, 35, -1, -1, -1, -1, 40, -1, -1, -1, -1, 45, -1, -1, -1, -1, 50, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]

#### 多次元リスト

```py
[[i, j, i * j] for i in range(10) for j in range(10)]
```

> \# 多次元リスト
>
> [
>
> &nbsp;&nbsp;&nbsp;&nbsp;[0, 0, 0], [0, 1, 0], [0, 2, 0], [0, 3, 0], [0, 4, 0], [0, 5, 0], [0, 6, 0], [0, 7, 0], [0, 8, 0], [0, 9, 0],
>
> &nbsp;&nbsp;&nbsp;&nbsp;[1, 0, 0], [1, 1, 1], [1, 2, 2], [1, 3, 3], [1, 4, 4], [1, 5, 5], [1, 6, 6], [1, 7, 7], [1, 8, 8], [1, 9, 9],
>
> &nbsp;&nbsp;&nbsp;&nbsp;[2, 0, 0], [2, 1, 2], [2, 2, 4], [2, 3, 6], [2, 4, 8], [2, 5, 10], [2, 6, 12], [2, 7, 14], [2, 8, 16], [2, 9, 18],
>
> &nbsp;&nbsp;&nbsp;&nbsp;[3, 0, 0], [3, 1, 3], [3, 2, 6], [3, 3, 9], [3, 4, 12], [3, 5, 15], [3, 6, 18], [3, 7, 21], [3, 8, 24], [3, 9, 27],
>
> &nbsp;&nbsp;&nbsp;&nbsp;[4, 0, 0], [4, 1, 4], [4, 2, 8], [4, 3, 12], [4, 4, 16], [4, 5, 20], [4, 6, 24], [4, 7, 28], [4, 8, 32], [4, 9, 36],
>
> &nbsp;&nbsp;&nbsp;&nbsp;[5, 0, 0], [5, 1, 5], [5, 2, 10], [5, 3, 15], [5, 4, 20], [5, 5, 25], [5, 6, 30], [5, 7, 35], [5, 8, 40], [5, 9, 45],
>
> &nbsp;&nbsp;&nbsp;&nbsp;[6, 0, 0], [6, 1, 6], [6, 2, 12], [6, 3, 18], [6, 4, 24], [6, 5, 30], [6, 6, 36], [6, 7, 42], [6, 8, 48], [6, 9, 54],
>
> &nbsp;&nbsp;&nbsp;&nbsp;[7, 0, 0], [7, 1, 7], [7, 2, 14], [7, 3, 21], [7, 4, 28], [7, 5, 35], [7, 6, 42], [7, 7, 49], [7, 8, 56], [7, 9, 63],
>
> &nbsp;&nbsp;&nbsp;&nbsp;[8, 0, 0], [8, 1, 8], [8, 2, 16], [8, 3, 24], [8, 4, 32], [8, 5, 40], [8, 6, 48], [8, 7, 56], [8, 8, 64], [8, 9, 72],
>
> &nbsp;&nbsp;&nbsp;&nbsp;[9, 0, 0], [9, 1, 9], [9, 2, 18], [9, 3, 27], [9, 4, 36], [9, 5, 45], [9, 6, 54], [9, 7, 63], [9, 8, 72], [9, 9, 81]
>
> ]

#### リスト内包表記で FizzBuzz

```py
[
    'FizzBuzz' if not n % 15 else
    'Fizz'     if not n % 3  else
    'Buzz'     if not n % 5  else
    str(n)
    for n in range(1, 1 + 100)
]
```
