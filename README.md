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

| 演算子                                       | 意味                                           |
| -------------------------------------------- | ---------------------------------------------- |
| (1), [1], {1:1}, {1}                         | 式結合／タプル、リスト、辞書、集合             |
| l[1], l[1,2], f(arg), c.attribute            | 添え字指定、スライス、関数呼び出し、属性参照   |
| await                                        | Await 式                                       |
| \*\*                                         | べき乗                                         |
| +x, -x, ~x                                   | 数、負数、ビット単位 NOT                       |
| \*, /, //, %                                 | 乗算、除算、整除除算、剰余／文字列フォーマット |
| +, -                                         | 加算、減算                                     |
| <<, >>                                       | シフト演算                                     |
| &                                            | ビット単位 AND                                 |
| ^                                            | ビット単位 XOR                                 |
|                                              |                                                | ビット単位 OR |
| in, not in, is, is not, <, <=, >, >=, !=, == | 比較                                           |
| not x                                        | NOT                                            |
| and                                          | AND                                            |
| or                                           | OR                                             |
| if -- else                                   | 条件式(三項演算子)                             |
| lambda                                       | ラムダ式                                       |


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


### 変数のスコープ

| スコープ                         | 特徴                       | 備考                                                     |
| -------------------------------- | -------------------------- | -------------------------------------------------------- |
| ローカルスコープ                 | 関数内で定義               |                                                          |
| エンクロージングローカルスコープ | def や lambda で定義       |                                                          |
| グローバルスコープ               | モジュール内で定義         | 関数内でグローバル変数に書き込む場合は `global` 文を使用 |
| ビルトインスコープ               | 組み込み関数や組み込み変数 |                                                          |

名前が衝突しないか調べるには以下の関数を使用する

```py
'VAR_NAME' in globals()
'VAR_NAME' in locals()
```


# データ型


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


### 整数の乱数を取得する

```py
import random

random.randint(1, 3) # m以上n以下の整数を返す
```

> 1
>
> 3

```py
import random

start=10
stop=100
step=20

# range(start, stop, step)で生成したリストの要素からランダムに抽出
random.randrange(start, stop, step)
```

> 90
>
> 70


#### 乱数値を固定する

```py
import random

# 乱数シードを設定する
random.seed(123)

random.random()
random.random()
random.random()

# 再度同じ乱数シードを設定する
random.seed(123)

random.random()
random.random()
random.random()
```

> 0.052363598850944326
>
> 0.08718667752263232
>
> 0.4072417636703983

> 0.052363598850944326
>
> 0.08718667752263232
>
> 0.4072417636703983


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


### 小数値の乱数を取得する

```py
import random

random.random() # 0以上1未満の小数を返す
```

> 0.9526105265369583
>
> 0.20576122073048697

```py
import random

# m以上n以下の小数を返す
# ( a + (b-a) * random() の丸められ方によっては「n未満」 )
random.uniform(1, 3)
```

> 2.812125216111861
>
> 1.2485392016103378


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


### 日時の各項目を取得

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


##### 現在日時を取得し、特定の時刻に変更

```py
from datetime import datetime

dt = datetime.now()

# 日時の要素を置換
print(dt.replace(hour=2,minute=0,second=0,microsecond=0))
```

> 2020-01-27 02:00:00


###### 今年が閏年かどうか調べる

```py
from datetime import datetime
from datetime import timedelta

dt = datetime.now()
dt = dt.replace(month=3,day=1,hour=0,minute=0,second=0,microsecond=0)
dt += timedelta(days=-1)
print(dt)

if 29 == dt.day:
    print('閏年')
else:
    print('not 閏年')
```


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


###### ロケールを指定して月・曜日を示す文字列を取得する

```py
import datetime
import locale

dt = datetime.datetime(2020, 1, 23)
print(dt) # 2020-01-23 00:00:00

print(locale.getlocale(locale.LC_TIME))
print(dt.strftime('%A, %a, %B, %b'))

locale.setlocale(locale.LC_TIME, 'en_US.UTF-8')
print(dt.strftime('%A, %a, %B, %b'))

locale.setlocale(locale.LC_TIME, 'ja_JP.UTF-8')
print(dt.strftime('%A, %a, %B, %b'))
```

| locale          | `%A`       | `%a`  | `%B`      | `%b`  |
| --------------- | ---------- | ----- | --------- | ----- |
| `(None, None)`  | `Thursday` | `Thu` | `January` | `Jan` |
| `'en_US.UTF-8'` | `Thursday` | `Thu` | `January` | `Jan` |
| `'ja_JP.UTF-8'` | `木曜日`   | `木`  | `1月`     | `1`   |


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


### 祝日判定

[emasaka/jpholidayp](https://github.com/emasaka/jpholidayp)


## str(文字列)

```py
print('str\nstr')
print("str\nstr")
print(str(123))
print('cq' * 3) # 文字列の繰り返し
print('cq' + 'cq') # 文字列をつなげる(連結／結合)
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


### RAW 文字列

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


#### 書式指定子

| 項目 | \*  | fill                              | \*           | align | \*                 | sign     | \*        | `#`  | `0`    | width        | \*           | grouping_option | \*         | precision             | \*                                      | type   | \*                                   |
| ---- | --- | --------------------------------- | ------------ | ----- | ------------------ | -------- | --------- | ---- | ------ | ------------ | ------------ | --------------- | ---------- | --------------------- | --------------------------------------- | ------ | ------------------------------------ |
|      |     | パディングに使う文字<sup>\*</sup> | (任意の文字) | 方向  |                    | 符号     |           | n 進 | 0 埋め | フィールド幅 | (任意の数値) | 桁区切り        |            | 小数桁数(type=f のみ) |                                         | 表現型 |                                      |
|      |     |                                   |              | `<`   | 左詰め             | `+`      | `+／-`    |      |        |              |              | `,`             | 3 桁区切り | `.<桁数>`             |                                         | `b`    | 2 進数                               |
|      |     |                                   |              | `>`   | 右詰め             | `-`      | `-` のみ  |      |        |              |              |                 |            | `.1`                  | 小数点以下１桁（小数点 2 位を四捨五入） | `c`    | Unicode 文字                         |
|      |     |                                   |              | `=`   | 符号の後ろを埋める | 半角空白 | `空白／-` |      |        |              |              |                 |            |                       |                                         | `d`    | 10 進数                              |
|      |     |                                   |              | `^`   | 中央               |          |           |      |        |              |              |                 |            |                       |                                         | `e`    | 指数表記                             |
|      |     |                                   |              |       |                    |          |           |      |        |              |              |                 |            |                       |                                         | `E`    | 大文字の `E` を使う指数表記          |
|      |     |                                   |              |       |                    |          |           |      |        |              |              |                 |            |                       |                                         | `f`    | 固定小数点数表記                     |
|      |     |                                   |              |       |                    |          |           |      |        |              |              |                 |            |                       |                                         | `F`    | (`nan` => `NAN`、`inf` => `INF`)     |
|      |     |                                   |              |       |                    |          |           |      |        |              |              |                 |            |                       |                                         | `g`    | 桁に応じて固定小数点か指数表記で表示 |
|      |     |                                   |              |       |                    |          |           |      |        |              |              |                 |            |                       |                                         | `G`    | (指数表記の時に`E`を使う)            |
|      |     |                                   |              |       |                    |          |           |      |        |              |              |                 |            |                       |                                         | `n`    | 数値(数値分割文字が挿入される)       |
|      |     |                                   |              |       |                    |          |           |      |        |              |              |                 |            |                       |                                         | `o`    | 8 進数                               |
|      |     |                                   |              |       |                    |          |           |      |        |              |              |                 |            |                       |                                         | `s`    | 文字列                               |
|      |     |                                   |              |       |                    |          |           |      |        |              |              |                 |            |                       |                                         | `x`    | 16 進数                              |
|      |     |                                   |              |       |                    |          |           |      |        |              |              |                 |            |                       |                                         | `X`    | `A`以降の数字に大文字を使う 16 進数  |
|      |     |                                   |              |       |                    |          |           |      |        |              |              |                 |            |                       |                                         | `%`    | 数値を 100 倍して%表記               |

注)f 文字列や str.format()では、fill に `{` と `}`を使えない


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


#### 正規表現で区切り文字を指定して分割

```py
import re

hoge = 'abc\n  def\nghi \njkl\nmno\npqr\nstu\nvwx\nyz.'
parts = re.split('[,. \\s]+', hoge)
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
>
> 9:


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


#### 文字列をランダムソートする

```py
import random

hoge = 'abcdefghi'
''.join(random.sample(hoge, len(hoge)))
```

> 'cigahdebf'


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
[ ]:リスト, ( ):タプル, { }:セット／辞書
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
| `lst.clear()`       | `[] # 初期化(すべての要素を削除)`                              |


#### 初期値を指定して生成

```py
lst = ['foo', 'bar', 'hoge']
print(lst)
```

> ['foo', 'bar', 'hoge']


#### リストをコピーして生成

```py
oldlist = ['foo', 'bar', 'hoge']
newlist = list(oldlist)
print(newlist)
```

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


#### スライスを使用して、別のリスト(別のイテラブルオブジェクト)の要素を指定位置に追加(連結／結合)する

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


#### 別のリスト(別のイテラブルオブジェクト)の要素を末尾に追加(連結／結合)する

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


### リストの要素を参照

```py
lst = ['foo', 'bar', 'hoge']
print(lst[0])
print(lst[len(lst) - 1])
```

> foo
>
> hoge


####リストの要素の存在チェック

```py
lst = ['foo', 'bar', 'hoge']
print('bar' in lst)
```

> True


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
> 3 None
>
> 4 None

> 0 5
>
> 1 6
>
> 2 7
>
> 3 999
>
> 4 999


#### リストの要素を連結(結合)した文字列を取得

```py
lst = ['foo', 'bar', 'hoge']
''.join(lst)
','.join(lst) # 区切り文字を指定
```

> 'foobarhoge'
>
> 'foo,bar,hoge'


#### 順列と組み合わせ


##### 順列

1,2,3,4,5 の 5 つから 3 つ選ぶ

```py
import itertools

items = range(1, 6)
for i in items:
    print(i, end=' ')

print('')

combi = list(itertools.combinations(items, 3))
print(combi)
print(len(combi))
```

> 1 2 3 4 5
>
> [(1, 2, 3), (1, 2, 4), (1, 2, 5), (1, 3, 4), (1, 3, 5), (1, 4, 5), (2, 3, 4), (2, 3, 5), (2, 4, 5), (3, 4, 5)]
>
> 10


##### 組み合わせ

1,2,3,4,5 の 5 つを並べる

```py
import itertools

items = range(1, 6)
for i in items:
    print(i, end=' ')

print('')

perm = list(itertools.permutations(items))
print(perm)
print(len(perm))
```

> 1 2 3 4 5
>
> [(1, 2, 3, 4, 5), (1, 2, 3, 5, 4), (1, 2, 4, 3, 5), (1, 2, 4, 5, 3), (1, 2, 5, 3, 4), (1, 2, 5, 4, 3), (1, 3, 2, 4, 5), (1, 3, 2, 5, 4), (1, 3, 4, 2, 5), (1, 3, 4, 5, 2), (1, 3, 5, 2, 4), (1, 3, 5, 4, 2), (1, 4, 2, 3, 5), (1, 4, 2, 5, 3), (1, 4, 3, 2, 5), (1, 4, 3, 5, 2), (1, 4, 5, 2, 3), (1, 4, 5, 3, 2), (1, 5, 2, 3, 4), (1, 5, 2, 4, 3), (1, 5, 3, 2, 4), (1, 5, 3, 4, 2), (1, 5, 4, 2, 3), (1, 5, 4, 3, 2), (2, 1, 3, 4, 5), (2, 1, 3, 5, 4), (2, 1, 4, 3, 5), (2, 1, 4, 5, 3), (2, 1, 5, 3, 4), (2, 1, 5, 4, 3), (2, 3, 1, 4, 5), (2, 3, 1, 5, 4), (2, 3, 4, 1, 5), (2, 3, 4, 5, 1), (2, 3, 5, 1, 4), (2, 3, 5, 4, 1), (2, 4, 1, 3, 5), (2, 4, 1, 5, 3), (2, 4, 3, 1, 5), (2, 4, 3, 5, 1), (2, 4, 5, 1, 3), (2, 4, 5, 3, 1), (2, 5, 1, 3, 4), (2, 5, 1, 4, 3), (2, 5, 3, 1, 4), (2, 5, 3, 4, 1), (2, 5, 4, 1, 3), (2, 5, 4, 3, 1), (3, 1, 2, 4, 5), (3, 1, 2, 5, 4), (3, 1, 4, 2, 5), (3, 1, 4, 5, 2), (3, 1, 5, 2, 4), (3, 1, 5, 4, 2), (3, 2, 1, 4, 5), (3, 2, 1, 5, 4), (3, 2, 4, 1, 5), (3, 2, 4, 5, 1), (3, 2, 5, 1, 4), (3, 2, 5, 4, 1), (3, 4, 1, 2, 5), (3, 4, 1, 5, 2), (3, 4, 2, 1, 5), (3, 4, 2, 5, 1), (3, 4, 5, 1, 2), (3, 4, 5, 2, 1), (3, 5, 1, 2, 4), (3, 5, 1, 4, 2), (3, 5, 2, 1, 4), (3, 5, 2, 4, 1), (3, 5, 4, 1, 2), (3, 5, 4, 2, 1), (4, 1, 2, 3, 5), (4, 1, 2, 5, 3), (4, 1, 3, 2, 5), (4, 1, 3, 5, 2), (4, 1, 5, 2, 3), (4, 1, 5, 3, 2), (4, 2, 1, 3, 5), (4, 2, 1, 5, 3), (4, 2, 3, 1, 5), (4, 2, 3, 5, 1), (4, 2, 5, 1, 3), (4, 2, 5, 3, 1), (4, 3, 1, 2, 5), (4, 3, 1, 5, 2), (4, 3, 2, 1, 5), (4, 3, 2, 5, 1), (4, 3, 5, 1, 2), (4, 3, 5, 2, 1), (4, 5, 1, 2, 3), (4, 5, 1, 3, 2), (4, 5, 2, 1, 3), (4, 5, 2, 3, 1), (4, 5, 3, 1, 2), (4, 5, 3, 2, 1), (5, 1, 2, 3, 4), (5, 1, 2, 4, 3), (5, 1, 3, 2, 4), (5, 1, 3, 4, 2), (5, 1, 4, 2, 3), (5, 1, 4, 3, 2), (5, 2, 1, 3, 4), (5, 2, 1, 4, 3), (5, 2, 3, 1, 4), (5, 2, 3, 4, 1), (5, 2, 4, 1, 3), (5, 2, 4, 3, 1), (5, 3, 1, 2, 4), (5, 3, 1, 4, 2), (5, 3, 2, 1, 4), (5, 3, 2, 4, 1), (5, 3, 4, 1, 2), (5, 3, 4, 2, 1), (5, 4, 1, 2, 3), (5, 4, 1, 3, 2), (5, 4, 2, 1, 3), (5, 4, 2, 3, 1), (5, 4, 3, 1, 2), (5, 4, 3, 2, 1)]
>
> 120


##### 重複組み合わせ

1,2,3,4,5 から、１つずつ取り出して元に戻す操作を 3 回繰り返した場合

```py
import itertools

items = range(1, 6)
for i in items:
    print(i, end=' ')

print('')

perm = list(itertools.combinations_with_replacement(items, 3))
print(perm)
print(len(perm))
```

> 1 2 3 4 5
>
> [(1, 1, 1), (1, 1, 2), (1, 1, 3), (1, 1, 4), (1, 1, 5), (1, 2, 2), (1, 2, 3), (1, 2, 4), (1, 2, 5), (1, 3, 3), (1, 3, 4), (1, 3, 5), (1, 4, 4), (1, 4, 5), (1, 5, 5), (2, 2, 2), (2, 2, 3), (2, 2, 4), (2, 2, 5), (2, 3, 3), (2, 3, 4), (2, 3, 5), (2, 4, 4), (2, 4, 5), (2, 5, 5), (3, 3, 3), (3, 3, 4), (3, 3, 5), (3, 4, 4), (3, 4, 5), (3, 5, 5), (4, 4, 4), (4, 4,
>
> > 5), (4, 5, 5), (5, 5, 5)]
>
> 35


##### 直積

2 つのリストの全要素の組み合わせを求める

```py
import itertools

items = range(1, 6)
for i in items:
    print(i, end=' ')

print('')

# perm = list(itertools.product(items, items))
perm = list(itertools.product(items, repeat=2))
print(perm)
print(len(perm))
```

> 1 2 3 4 5
>
> [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5)]
>
> 25


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


#### リストの要素の型


##### リストのリスト


###### リスト同士の比較方法(既定)

```py
print([2] > [1]) # 最初の要素
print([1] > [2])
print([1, 2] > [1, 1]) # 一番最初の異なる要素
print([1, 1] > [1, 2])
```

> True
>
> False
>
> True
>
> False

```py
lst = [[2, 10, 100], [3, 20, 300], [1, 10, 200], [1, 30, 200], [2, 10, 200]]

# lst = sorted(lst)
lst.sort()

print(lst)
```

> [
>
>     [1, 10, 200],
>
>     [1, 30, 200],
>
>     [2, 10, 100],
>
>     [2, 10, 200],
>
>     [3, 20, 300]
>
> ]


###### 任意の要素を比較してソート

```py
lst = [[2, 10, 100], [3, 20, 300], [1, 10, 200], [1, 30, 200], [2, 10, 200]]

lst = sorted(lst, key=lambda x: x[2]) # 逆順ソートの場合は sorted(lst, key=lambda x: x[2], reverse=True)
# lst.sort(key=lambda x: x[2])

print(lst)
```

> [
>
>     [2, 10, 100],
>
>     [1, 10, 200],
>
>     [1, 30, 200],
>
>     [2, 10, 200],
>
>     [3, 20, 300]
>
> ]


###### 3次元リスト

```py
lst = [[[2, 10, 100], [3, 20, 300], [1, 20, 200]], [[1, 10, 200], [1, 30, 200], [2, 10, 200]]]

# lst = sorted(lst, key=lambda x: x[0][0])
lst.sort(key=lambda x: x[0][0])

print(lst)
```

> [
>
>     [
>
>         [1, 10, 200],
>
>         [1, 30, 200],
>
>         [2, 10, 200]
>
>     ],
>
>     [
>
>         [2, 10, 100],
>
>         [3, 20, 300],
>
>         [1, 20, 200]
>
>     ]
>
> ]


##### 辞書のリスト

```py
lst = [
    {'height': 170, 'weight': 65},
    {'height': 160, 'weight': 55},
    {'height': 180, 'weight': 75}
]

lst = sorted(lst, key=lambda x: x['height'])
# lst.sort(key=lambda x: x[2])

print(lst)
```

> [
>
>     {'height': 160, 'weight': 55},
>
>     {'height': 170, 'weight': 65},
>
>     {'height': 180, 'weight': 75}
>
> ]


##### タプルのリスト

```py
lst = [
    ('Ichiro', 185, 65),
    ('Jiro', 160, 55),
    ('Saburo', 180, 75)
]

# lst = sorted(lst, key=lambda x: x[2])

# lst.sort(key=lambda x: x[2])

from operator import itemgetter
lst = sorted(lst, key=itemgetter(2))

print(lst)
```

> [
>
>     ('Jiro', 160, 55),
>
>     ('Ichiro', 185, 65),
>
>      ('Saburo', 180, 75)
>
> ]


##### セットのリスト


### リストのランダム処理


#### リストから要素を 1 個ランダムに取り出す

```py
import random

lst = list(range(1,7))

random.choice(lst)
```

> 6
>
> 3
>
> 2


#### リストから要素を複数個ランダムに取り出す(重複あり)

```py
import random

lst = list(range(1,7))
n = 3

[random.choice(lst) for _ in range(n)]

random.choices(lst, k=n)
```

> [5, 2, 3]
>
> [1, 1, 5]


#### リストから要素を複数個ランダムに取り出す(重複なし)

```py
import random

lst = list(range(1,7))
n = 3

random.sample(lst, n)
```

> [1, 6, 4]


#### リストの要素をランダムソート(シャッフル)する

```py
import random

lst1 = list(range(1,7))

# もとのリスト自体をソート
random.shuffle(lst1)
print(lst1)

# シャッフルした新しいリストを返す
lst2 = random.sample(lst1, len(lst1))
print(lst2)
```

> [2, 4, 3, 1, 6, 5]
>
> [1, 6, 5, 2, 3, 4]


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

```py
l = ['Lorem', '', 'ipsum', None, 'dolor', 'sit', 'amet']
l = [s for s in l if s]
print(l)
```

>


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


## 辞書


### 辞書が空か検査

| 判定方法      |
| ------------- |
| `not dct`     |
| `len(dct)==0` |
| `dct == {}`   |

```py
dct = {}
if not dct:
  print('empty')

if len(dct)==0:
  print('empty')

if dct == {}:
  print('empty')
```


### 辞書を生成


#### 空の辞書を生成

```py
dct = {}

# 初期化(すべての要素を削除)
dct.clear()
```


#### 初期値を指定して生成

```py
dct = { 1:'first', 2:'second', 3:'third'}

# デバッグ表示
print(str(dct))
print('%s' % dct)
```

> {1: 'first', 2: 'second', 3: 'third'}
>
> {1: 'first', 2: 'second', 3: 'third'}

```py
dct = { 1:'first', 2:'two', 2:'second', 3:'third'}
# キーが同じ要素が追加されたら上書きされる(2:'two'ではなく2:'second'が残る)
```

> {1: 'first', 2: 'second', 3: 'third'}


#### 辞書をコピーして生成

```py
olddict = { 1:'first', 2:'second', 3:'third'}
newdict = dict(olddict)
print(newdict)
```

> {1: 'first', 2: 'second', 3: 'third'}


##### 辞書を代入した場合

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


#### リスト・タプルから生成


##### リストから生成

```py
l = list(range(100))
lst = [str(i) for i in l] # リスト
dct = {li: str(li) for li in l} # 辞書
print(dct)
```

> {0: '0', 1: '1', 2: '2', ＜中略＞ 99: '99'}


###### 連番とリストの要素から生成

```py
values = ['first', 'second', 'third']
['{0}: {1}'.format(i + 100, values[i]) for i in range(len(values))]
['{0}: {1}'.format(i + 100, v) for i, v in enumerate(values)]
```

> ['100: first', '101: second', '102: third']
>
> ['100: first', '101: second', '102: third']


##### リストのリストから生成

```py
lst = [[1, 'first'], [2, 'second'], [3, 'third']]
dct = dict(lst)
print(dct)
```

> {1: 'first', 2: 'second', 3: 'third'}


##### 2 つのリストから生成


###### 要素数の少ないリストに合わせる

```py
keys = [1, 2, 3]
values = ['first', 'second', 'third']
dct = dict(zip(keys, values))
print(dct)
```

> {1: 'first', 2: 'second', 3: 'third'}


###### 要素数の多いリストに合わせる

```py
from itertools import zip_longest
keys = [1, 2]
values = ['first', 'second', 'third']
dct = dict(zip_longest(keys, values, fillvalue=3))
print(dct)
```

> {1: 'first', 2: 'second', 3: 'third'}


###### 条件に合致する要素のみからなる辞書を生成(抽出)

```py
keys = [1, 2, 3, 4, 5, 10, 12]
values = ['v1', 'v2', 'v3', 'v4', 'v5', 'v10', 'v12']
dct1 = {k: v for k, v in zip(keys, values) if k % 5 == 0 and k <= 50}
print(dct1)

dct2 = {k: v if k % 5 == 0 and k <= 50 else -1 for k, v in zip(keys, values)}
print(dct2)
```

> {5: 'v5', 10: 'v10'}
>
> {1: -1, 2: -1, 3: -1, 4: -1, 5: 'v5', 10: 'v10', 12: -1}


##### リストのタプルから生成

```py
tpl = ([1, 'first'], [2, 'second'], [3, 'third'])
dct = dict(tpl)
```

> {1: 'first', 2: 'second', 3: 'third'}


##### タプルのリストから生成

```py
lst = [(1, 'first'), (2, 'second'), (3, 'third')]
dct = dict(lst)
```

> {1: 'first', 2: 'second', 3: 'third'}


##### 文字列のリストから生成

```py
lst = ['1f', '2s', '3t']
dct = dict(lst)
```

> {'1': 'f', '2': 's', '3': 't'}


##### 文字列のタプルから生成

```py
tpl = ('1f', '2s', '3t')
dct = dict(tpl)
```

> {'1': 'f', '2': 's', '3': 't'}


### 辞書に要素を追加


#### キーを指定して要素を追加

```py
dct = { 1:'first', 2:'second', 3:'third'}
print(len(dct))

# 追加
dct[len(dct) + 1] = 'fourth'

# 要素の置換
dct[2] = 'secondsecond'

print(dct)
```

> 3
>
> {1: 'first', 2: 'secondsecond', 3: 'third', 4: 'fourth'}


#### 辞書を連結(結合)

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


#### 既存のキーと重複する場合に上書きせずにカンマ区切りで追加

```py
from collections import defaultdict

def merge(*dicts):
    merged = defaultdict(list)
    # merged = defaultdict(set) # setにすると、既存のものとキーも値も重複した場合は追加されない
    for d in dicts:
        for k, v in d.items():
            # if v not in merged[k]: # listを使いつつ、既存のものとキーも値も重複した場合は追加しない
            merged[k].append(v) # list
            # merged[k].add(v) # set
    return merged

dct1 = {'red':'1', 'green':'2'}
dct2 = {'red':'3', 'green':'2', 'blue':'4'}
dct = merge(dct1, dct2)
print(dct)

dct_csv = {k: ','.join(v) for k, v in dct.items()}
print(dct_csv)
```

> \# list
>
> defaultdict(<class 'list'>, {'red': ['1', '3'], 'green': ['2', '2'], 'blue': ['4']})
>
> {'red': '3,1', 'green': '2,2', 'blue': '4'}

> \# set
>
> defaultdict(<class 'set'>, {'red': {'3', '1'}, 'green': {'2'}, 'blue': {'4'}})
>
> {'red': '3,1', 'green': '2', 'blue': '4'}



### 辞書の要素を参照

```py
dct = { 'key1':'first', 'key2':'second', 'key3':'third'}

dct['key1']
dct.key1 # 辞書には使用できない(オブジェクトの属性を参照する際に使用)
```

> 'first'
>
> AttributeError: 'dict' object has no attribute 'key1'


#### 存在しないキーを指定した場合

```py
dct = { 'key1':'first', 'key2':'second', 'key3':'third'}
```

| 関数                             | 値                   | 備考                                      |
| -------------------------------- | -------------------- | ----------------------------------------- |
| `dct['key999']`                  | `KeyError: 'key999'` | エラーが発生する                          |
| `dct.get('key999')`              | `None`               | 指定したキーが存在しなければ None を返す  |
| `dct.get('key999', 'not found')` | `not found`          | 指定したキーが存在しなければ引数 2 を返す |


#### 辞書の要素の存在チェック

```py
dct = { 1:'first', 2:'second', 3:'third', }
```

| 項目     | 関数                          | 値      |
| -------- | ----------------------------- | ------- |
| キー     | `1 in dct`                    | `True`  |
|          | `1 not in dct`                | `False` |
| 値       | `'first' in dct.values()`     | `True`  |
| キーと値 | `(1, 'first') in dct.items()` | `True`  |


#### 指定した値を持つキーを取得する

```py
targets = ['first', 'third']
keys = [k for k, v in dct.items() if v in targets]
print(keys)
```

> [1, 3]


### 辞書の要素を除去

```py
dct = { 'key1':'first', 'key2':'second', 'key3':'third'}

# キーを指定して要素を削除
del dct['key1']

print(dct)
```

> {'key2': 'second', 'key3': 'third'}


### 辞書の反復処理(キー・値・インデックスを取得)

```py
dct = { 1:'first', 2:'second', 3:'third'}
```

| 項目               | 関数                                                                                                    | 値                                                               |
| ------------------ | ------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| キー               | `dct.keys()`                                                                                            | `dict_keys([1, 2, 3])`                                           |
|                    | `list(dct.keys())`                                                                                      | `[1, 2, 3]`                                                      |
| 値                 | `dct.values()`                                                                                          | `dict_values(['first', 'second', 'third'])`                      |
|                    | `list(dct.values())`                                                                                    | `['first', 'second', 'third']`                                   |
| キーと値のタプル   | `dct.items()`                                                                                           | `dict_items([(1, 'first'), (2, 'second'), (3, 'third')])`        |
|                    | `list(dct.items())`                                                                                     | `[(1, 'first'), (2, 'second'), (3, 'third')]`                    |
| インデックスとキー | `for index, key in enumerate(dct):` <br>&nbsp;&nbsp;&nbsp;&nbsp;`print(f'{index}: {key}')`              | `0: 1` <br> `1: 2` <br> `2: 3`                                   |
| インデックスと値   | `for index, value in enumerate(dct.values()):` <br>&nbsp;&nbsp;&nbsp;&nbsp;`print(f'{index}: {value}')` | `0: first` <br> `1: second` <br> `2: third`                      |
| インデックスと要素 | `for index, item in enumerate(dct.items()):` <br>&nbsp;&nbsp;&nbsp;&nbsp;`print(f'{index}: {item}')`    | `0: (1, 'first')` <br> `1: (2, 'second')` <br> `2: (3, 'third')` |


#### 複数の辞書を同時に繰り返す

```py
dct1 = {
    'key1-1':'val1-1',
    'key1-2':'val1-2',
    'key1-3':'val1-3'
    }
dct2 = {
    'key2-1':'val2-1',
    'key2-2': 'val2-2',
    'key2-3': 'val2-3'
    }
for index, item in enumerate(zip(dct1, dct1.values(), dct1.items(), dct2, dct2.values(), dct2.items())):
    print(f'{index}: {item}')
```

> 0: ('key1-1', 'val1-1', ('key1-1', 'val1-1'), 'key2-1', 'val2-1', ('key2-1', 'val2-1'))
>
> 1: ('key1-2', 'val1-2', ('key1-2', 'val1-2'), 'key2-2', 'val2-2', ('key2-2', 'val2-2'))
>
> 2: ('key1-3', 'val1-3', ('key1-3', 'val1-3'), 'key2-3', 'val2-3', ('key2-3', 'val2-3'))


#### タプルの要素を連結した文字列を取得

```py
dct = { 1:'first', 2:'second', 3:'third'}
print(
    ','.join(['"{0}":"{1}"'.format(key, value) for (key, value) in dct.items()])
)
```

> "1":"first","2":"second","3":"third"


#### 辞書のキーと値を交換する

```py
dct1 = dict(('1f', '2s', '3t'))
print(dct1)
dct2 = {v: k for k, v in dct1.items()}
print(dct2)
```

> {'1': 'f', '2': 's', '3': 't'}
>
> {'f': '1', 's': '2', 't': '3'}


### 辞書をソート


#### 辞書のキーでソート

```py
dct1 = dict(('1b', '4a', '3c'))
print(dct1)
dct2 = dict(sorted(dct1.items(), key=lambda x: x[0], reverse=True))
print(dct2)
```

> {'1': 'b', '4': 'a', '3': 'c'}
>
> {'3': 'c', '1': 'b', '4': 'a'}


#### 辞書の値でソート

```py
dct1 = dict(('1b', '4a', '3c'))
print(dct1)
dct2 = dict(sorted(dct1.items(), key=lambda x: x[1], reverse=True))
print(dct2)
```

> {'1': 'b', '4': 'a', '3': 'c'}
>
> {'3': 'c', '1': 'b', '4': 'a'}


### 辞書の内包表記

```
形式: {キー: 値 for 変数 in イテラブルオブジェクト}
```

`キー:`を忘れるとセット(Set／集合)になる


#### 文字の出現頻度を調べる

```py
code = 'Lorem ipsum dolor sit amet, dico quidam percipitur mea no, labitur scaevola molestiae in vis, malis veniam tacimates mea cu.'
{letter: code.count(letter) for letter in code}

# 文字でソート
dict(sorted({letter: code.count(letter) for letter in code}.items(), key=lambda x: x[0]))

# 多い順にソート
dict(sorted({letter: code.count(letter) for letter in code}.items(), key=lambda x: x[1], reverse=True))
```

> {'L': 1, 'o': 7, 'r': 5, 'e': 10, 'm': 10, ' ': 19, 'i': 13, 'p': 3, 's': 7, 'u': 5, 'd': 3, 'l': 5, 't': 7, 'a': 12, ',': 3, 'c': 5, 'q': 1, 'n': 3, 'b': 1, 'v': 3, '.': 1}
>
> [(' ', 19), (',', 3), ('.', 1), ('L', 1), ('a', 12), ('b', 1), ('c', 5), ('d', 3), ('e', 10), ('i', 13), ('l', 5), ('m', 10), ('n', 3), ('o', 7), ('p', 3), ('q', 1), ('r', 5), ('s', 7), ('t', 7), ('u', 5), ('v', 3)]
>
> [(' ', 19), ('i', 13), ('a', 12), ('e', 10), ('m', 10), ('o', 7), ('s', 7), ('t', 7), ('r', 5), ('u', 5), ('l', 5), ('c', 5), ('p', 3), ('d', 3), (',', 3), ('n', 3), ('v', 3), ('L', 1), ('q', 1), ('b', 1), ('.', 1)]


#### 頭文字と単語のリストを辞書にまとめる

```py
import re

code = 'Lorem ipsum dolor sit amet, dico quidam percipitur mea no, labitur scaevola molestiae in vis, malis veniam tacimates mea cu.'
codes = re.split('[,. \s]+', code)
codes = [s for s in codes if len(s) > 0]
print(codes)

results = {}
for c in codes:
    results.setdefault(c[0], []).append(c)

print(results)
```

> {
>
>     'L': ['Lorem'],
>
>     'i': ['ipsum', 'in'],
>
>     'd': ['dolor', 'dico'],
>
>     's': ['sit', 'scaevola'],
>
>     'a': ['amet'],
>
>     'q': ['quidam'],
>
>     'p': ['percipitur'],
>
>     'm': ['mea', 'molestiae', 'malis', 'mea'],
>
>     'n': ['no'], 'l': ['labitur'],
>
>     'v': ['vis', 'veniam'],
>
>     't': ['tacimates'],
>
>     'c': ['cu']
>
> }


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


## タプル

リストとは異なり、タプルは読み取り専用


### タプルが空か検査

| 判定方法      |
| ------------- |
| `not tpl`     |
| `len(tpl)==0` |
| `tpl == ()`   |

```py
tpl = ()
if not tpl:
  print('empty')

if len(tpl)==0:
  print('empty')

if tpl == ():
  print('empty')
```


### タプルを生成


#### 空のタプルを生成

```py
tpl = ()
```


#### 初期値を指定して生成

```py
tpl = 'foo', 'bar', 123, 456
tpl = ('foo', 'bar', 123, 456)
print(str(tpl))
```

> ('foo', 'bar', 123, 456)

1 要素のタプルを宣言するときは後ろにカンマをつける(カンマをつけないとただの変数として代入される)

```py
tpl = 'hoge',

print('%s' % (tpl,)) # print('%s' % tpl)とするとTypeError: not all arguments converted during string formatting
```

> ('hoge',)


#### タプルをコピーして生成

```py
import copy

tpl1 = 'foo', ['bar'], 123, 456
tpl2 = copy.deepcopy(tpl1) # copy()と異なり、要素の参照しているデータもコピー
tpl2[1].append('hoge')
print(tpl1)
print(tpl2)
```

> ('foo', ['bar'], 123, 456)
>
> ('foo', ['bar', 'hoge'], 123, 456)


#### タプルに要素を追加した新しいタプルを生成

```py
tpl1 = ("123", "456")
tpl2 = ("78", "90")

tpl3 = tpl1 + tpl2
print(tpl3)
```

> ('123', '456', '78', '90')


#### リストから生成

```py
tpl = tuple(['foo', 'bar', 123, 456])
print(tpl)
```

> ('foo', 'bar', 123, 456)


### タプルの要素を参照


#### タプルの要素の存在チェック


### タプルの要素を削除


### タプルの反復処理(インデックスを取得)

```py
tpl = tuple(range(5, 10))
for (index, item) in enumerate(tpl):
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


#### 複数のタプルを同時に繰り返す

```py
tpl1 = tuple(range(5)) # タプルの要素数が同じ場合
tpl2 = tuple(range(5,10))

for (i1, i2) in zip(tpl1, tpl2):
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
tpl1 = tuple(range(5)) # タプルの要素数が異なる場合
tpl2 = tuple(range(5,8))

# 要素数の少ないタプルの要素数分だけ繰り返す
for (i1, i2) in zip(tpl1, tpl2):
    print(i1, i2)
```

> 0 5
>
> 1 6
>
> 2 7

```py
from itertools import zip_longest

tpl1 = tuple(range(5)) # タプルの要素数が異なる場合
tpl2 = tuple(range(5,8))

# 要素数の多いタプルの要素数分だけ繰り返す
for (i1, i2) in zip_longest(tpl1, tpl2):
    print(i1, i2)

# 要素数の多いタプルの要素数分だけ繰り返す(不足している要素にNoneではなく指定した値を使用)
for (i1, i2) in zip_longest(tpl1, tpl2, fillvalue=999):
    print(i1, i2)
```

> 0 5
>
> 1 6
>
> 2 7
>
> 3 None
>
> 4 None

> 0 5
>
> 1 6
>
> 2 7
>
> 3 999
>
> 4 999


#### 多重タプル

```py
tpl = 'foo', ['bar'], 123, 456
tpl = tpl, (('hoge', 'piyo'), 789)
print(tpl)
```

> (('foo', ['bar'], 123, 456), (('hoge', 'piyo'), 789))


##### 平坦化(flatten)


###### 2 重タプルを平坦化(flatten)

```py
tpl1 = ((3, 1, 4), (1, 5, 9), (2, 6, 5))
print(tpl1)

tpl2 = [ f for i in tpl1 for f in i ]
print(tuple(tpl2))
# or
tpl2 = ()
for rows in tpl1:
    tpl2 = tpl2 + rows

print(tpl2)
```


###### 多重タプルを平坦化(flatten)


#### タプルの要素を連結した文字列を取得

```py
lst = 'foo', 'bar', 'hoge'
''.join(lst)
','.join(lst) # 区切り文字を指定
```

> 'foobarhoge'
>
> 'foo,bar,hoge'


### シーケンス・アンパッキング

タプルから複数の変数に展開(一括代入)する

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

代入元の要素数と代入先の変数の数が異なる場合

```py
x, y, z = 'foo', 'bar', 123, 456 # ValueError

x, y, *z = 'foo', 'bar', 123, 456 # アスタリスクをつけるとリストに格納
print(x, y, z)

x, y, z, *w = 'foo', 'bar', 123, 456
print(x, y, z, w)

x, y, z, w, *v = 'foo', 'bar', 123, 456
print(x, y, z, w, v)
```

> ValueError: too many values to unpack (expected 3)

> 'foo', 'bar', [123, 456]

> foo bar 123 [456]

> foo bar 123 456 []

入れ子のタプルを展開

```py
x, (y, z) = 'foo', (123, 456)
print(x, y, z)
```

> foo 123 456

不要な要素を展開しない

```py
x, y, *_ = 'foo', 'bar', 123, 456
print(x, y)
```

> foo bar


### タプルをソート


### タプルのランダム処理


#### タプルから要素を 1 個ランダムに取り出す

```py
import random

tpl = tuple(range(1,7))

random.choice(tpl)
```

> 1
>
> 1
>
> 4


#### タプルから要素を複数個ランダムに取り出す(重複あり)

```py
import random

tpl = tuple(range(1,7))
n = 3

tuple([random.choice(tpl) for _ in range(n)])

tuple(random.choices(tpl, k=n))
```

> (5, 3, 3)
>
> (6, 1, 3)


#### タプルから要素を複数個ランダムに取り出す(重複なし)

```py
import random

tpl = tuple(range(1,7))
n = 3

tuple(random.sample(tpl, n))
```

> (1, 5, 4)


#### タプルの要素をランダムソート(シャッフル)する

```py
import random

tpl1 = tuple(range(1,7))

# もとのタプル自体をソート→TypeError
random.shuffle(tpl1)

# シャッフルした新しいタプルを返す
tpl2 = tuple(random.sample(tpl1, len(tpl1)))
print(tpl2)
```

> TypeError: 'tuple' object does not support item assignment
>
> (1, 3, 4, 6, 5, 2)


### タプルの内包表記

丸括弧 `()` の内包表記はタプルではなくジェネレータとなる

```py
l = list(range(10))
(i * 2 for i in l) # 誤

tuple(i * 2 for i in l) # 正
```

> \<generator object \<genexpr\> at 0x000001E1C99F7F90\> \# 誤
>
> (0, 2, 4, 6, 8, 10, 12, 14, 16, 18) \# 正


## セット

リストとは異なり、重複する要素があれば削除される


### セットが空か判定


### セットを生成


#### 空のセットを生成

```py
s1 = {}
```


#### 初期値を指定して生成

```py
s1 = {'ab', 'cd', 'ab', 'cd'}
print(s1)
```

> {'ab', 'cd'}


#### リストから生成

```py
ls2 = ['ab', 'cd', 'ef', 'cd']
s2 = set(ls2)
print(s2)
```

> {'cd', 'ab', 'ef'}


### 辞書に要素を追加

```py
s1 = {'ab', 'cd'}
s1.add('yz')
print(s1)
```

> {'ab', 'yz', 'cd'}


### セットの要素を参照


#### セットの要素の存在チェック

```py
s1 = {'ab', 'cd', 'ab', 'cd'}
print('ab' in s1)
```

> True


### セットの演算

```py
s1 = {'ab', 'cd'}
s1 = {'ef', 'ab', 'cd'}
```

| 関数      | 値                   |
| --------- | -------------------- |
| `s1`      | `{'ab', 'cd'}`       |
| `s2`      | `{'ef', 'ab', 'cd'}` |
| `s1 - s2` | `set()`              |
| `s1 | s2` | `{'ab', 'cd', 'ef'}` |
| `s1 & s2` | `{'ab', 'cd'}`       |
| `s1 ^ s2` | `{'ef'}`             |


# 制御構文


## 条件分岐


### if

switch 文や case 文はなく、すべて if 文を使う

```py
x = 1
if x < 0:
    print('N')
elif x == 0: # else if
    print('0')
else:
    print('P')
```

条件式が長い場合は、各文末に `\` を付けるか、全体を括弧で囲む

```py
x = 1
y = 1
z = -1

if x > 0 \
    and \
    ( \
    y > 0 \
    or \
    z > 0 \
    ):
        print('true')
else:
    print('false')

if ( x > 0
    and
    (
    y > 0
    or
    z > 0
    )
    ):
        print('true')
else:
    print('false')
```


### 条件演算子(三項演算子)

```py
con = 0

result = 'true' if con == 1 else 'false'

print(result)
```

> false


## 繰り返し

| 構文    | 備考                             |
| ------- | -------------------------------- |
| `for`   | コレクションの各要素に対して処理 |
| `while` | 条件式が `True` の間繰り返し処理 |


### for

```py
for i in [0, 1, 2, 3]:
    j = 99
    print(i, end=' ')

# ループ変数やループ内で定義された変数を、ループの外でも参照できる
print(i, j)
```

> 0 1 2 3
>
> 3 99


#### for 文の else 節

```py
for i in range(5):
    print(i, end=' ')
else:
    # ループを抜けたときに実行される
    print('else')
```

> 0 1 2 3 4 else


#### 途中でループから脱出(break)

```py

for i in range(5):
    if i > 3:
        break
    print(i, end=' ')
```

> 0 1 2 3


#### スキップする(continue)

```py
for i in range(5):
    if i == 3:
        continue
    print(i, end=' ')
```

> 0 1 2 4


#### ループ回数を与える場合

| 関数                       | 内容                                             |
| -------------------------- | ------------------------------------------------ |
| `range(stop)`              | ループ回数                                       |
| `range(start, stop)`       | 指定された開始位置／終了位置の範囲をループ       |
| `range(start, stop, step)` | 指定された開始位置／終了位置／増分の範囲をループ |

```py
for i in range(4):
    print(i, end=' ')

for i in range(5, 8):
    j = i + 1
    print(i, end=' ')

for i in range(5, 20, 5):
    print(i, end=' ')

for i in range(5, 21, 5):
    print(i, end=' ')
```

> 0 1 2 3
>
> 5 6 7
>
> 5 10 15
>
> 5 10 15 20


#### 文字列型を与える場合

```py
for c in '012':
    print(c, end=' ')
```

> 0 1 2


#### ファイルオブジェクトを場合

```py
for line in open('test-fileio/inpututf8.txt', encoding='utf8'):
    print(line)
```

```
あいうえお8XkfWDHyFdcB52MbTNNswDnFRAsZdEgRmmsaNktD
かきくけこxahfE6WkxNFpU-4KgnJ4jS2jZUyWf9spDbKRaFyC
...
tRR_6_JHDbL27G24P2NaMb-znLJs5iC3wQbPxnyyJc6HV9XYjQ
```


#### 複数リストの直積を取得

```py
import itertools
for x, y,z in itertools.product(range(3), range(3), range(3)):
  print('%d,%d,%d' % (x,y,z))
```

```
0,0,0
0,0,1
0,0,2
0,1,0
0,1,1
0,1,2
0,2,0
0,2,1
0,2,2
1,0,0
1,0,1
1,0,2
1,1,0
1,1,1
1,1,2
1,2,0
1,2,1
1,2,2
2,0,0
2,0,1
2,0,2
2,1,0
2,1,1
2,1,2
2,2,0
2,2,1
2,2,2
```


### while

```py
i = 0
while i < 10:
    i += 1
    if i == 3:
        continue
    print(i, end=' ')
else:
    print('-1')
```

> 1 2 4 5 6 7 8 9 10 -1


## 例外処理


## try

```py
import traceback

str = 'ABC'
try:
    # 範囲外の文字が指定し、IndexError例外を発生させる
    c = str[5]
except IOError as err:
    print('I/O error: {0}'.format(err))
except IndexError as err:
    print('IndexError: {0}'.format(err))
except (UnicodeEncodeError, UnicodeDecodeError, UnicodeTranslateError) as err:
    # 複数の例外をまとめて扱う
    print('UnicodeError: {0}'.format(err))
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


### 例外を発生させる

例外を投げてプログラム実行を終了させる

```py
raise exception
```


### assert(アサーション)

`__debug__` が `True` の時のみ動作するので、テスト用に使用できる。
コマンドラインオプションに-O をつけると、 `__debug__` が `False` になるので assert が動作しなくなる。

```py
sum = 1 + 2
assert sum == 3
assert sum == 4  # AssertionErrorが発生
assert sum == 4, '期待される値と異なります'  # AssertionErrorが発生
```

> \# assert sum == 3
>
> &nbsp;&nbsp;&nbsp;&nbsp;\# (何も出力されない)

> \# assert sum == 4
>
> AssertionError

> \# assert sum == 4, '期待される値と異なります'
>
> AssertionError: 期待される値と異なります


## 評価

| 関数 | 用途         |
| ---- | ------------ |
| eval | 式として評価 |
| exec | 文として評価 |


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
print(result)

result = eval('a + b', {'a': 3, 'b': 4})
print(result)

result = eval('a + b', {'a': 5, 'b': 6}, {'a': 7, 'b': 8})
print(result)
```

> 3
>
> 7
>
> 15

```py
# compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)
# 第1引数に文字列を与えている(コードの読み出し元のファイルがない)ので、慣習的に第2引数にファイル名ではなく空文字か「<string>」を指定
result = eval(compile('1 + 2', '<string>', 'eval'))
print(result)
```

| mode     | 意味                                 |
| -------- | ------------------------------------ |
| `eval`   | 単一の式としてコンパイルする         |
| `single` | 単一の文としてコンパイルする         |
| `exec`   | 単一のモジュールとしてコンパイルする |

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
    exec(f'var{i+1} = {s}')

print(var1)
print(var2)
print(var3)
```

> foo
>
> bar
>
> hoge


#### グローバル名前空間の参照・変更を制限

```py
exec('import os;os.system("echo foobar")', {}, {})

exec('import os;os.system("echo foobar")', {'__builtins__':None}, {})
```

> foobar
>
> ImportError: **import** not found


## del

オブジェクトを削除

```py
s = 'foo'
i = [1, 2, 3]
b = Bar()
del s, i, b
```


## exit

プログラム実行を終了させる

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


## pass

空の関数や空の型を定義する

```py
def empty_func():
    pass


class EmptyClass:
    pass
```


## with

with ブロックが終了するとオブジェクトの終了処理が自動的に呼ばれる

```py
with open(filepath, 'w') as f:
    pass
```


### 複数の with をまとめる

入力ファイルと出力ファイルを同時に開く場合など、複数の with ブロックによってネストが深くなってしまうのを防ぐために、「,」で区切って 1 つの with ブロックにまとめることができる

```py
with open(filepath1, 'r') as f1:
    with open(filepath2, 'w') as f2:
        pass

with open(filepath1, 'r') as f1, with open(filepath2, 'w') as f2:
    pass
```


# 関数


## 引数なし

```py
# 定義
def func1():
    print('hello')

# 呼出
func1()
```


## 引数あり

```py
# 定義
def func2(arg):
    print(arg)

# 呼出
func2('hello')
```


## 既定値を持つ引数あり

```py
# 定義
def func3(arg='bye'):
    print(arg)

# 呼出
func3()
func3(arg='hi')
```


## 戻り値あり

```py
# 定義
def func4(arg):
    return arg

# 呼出
print(func4('hello'))
```


## docstring あり

```py
# 定義
def func5():
    '''helloと表示する関数'''
    print('hello')

# 呼出
func5()

# ヘルプを表示
help(func5)
```


## 引数のアンパック


## リストやタプルを受け取る

```py
args = [1, 5]
list(range(*args))

list(range(1, 5))   # と同じ
```

可変長引数よりも後に通常の引数を定義することもできるが、キーワード引数を使って呼び出す必要がある

```py
def func_variable_argument(arg, *l, arg1, arg2):
    print(arg)
    for val in l:
        print(val)
    print(arg1)
    print(arg2)

func_variable_argument('a0', ['l1','l2','l3'], 'a1', 'a2')

func_variable_argument('a0', ['l1','l2','l3'], arg1='a1', arg2='a2')
```

> TypeError: func_variable_argument() missing 2 required keyword-only arguments: 'arg1' and 'arg2'

> a0
>
> ['l1', 'l2', 'l3']
>
> a1
>
> a2


## 辞書を受け取る

```py
my_dict = {'sep': '%', 'end': '!\r\n!\r\n', 'flush': False}
print('foo', 'bar', 'hoge', **my_dict)
```

> foo%bar%hoge!
>
> !

```py
# 定義
def func_ld(arg, *l, **d):
    for val in l:
        print(val)
    keys = sorted(d.keys())
    for val in keys:
        print(val)

def func_lt(arg, *t, **d):
    for val in t:
        print(val)
    keys = sorted(d.keys())
    for val in keys:
        print(val)

# 呼出
func_ld('foobar',
        'l1',
        'l2',
        dk1='dv1',
        dk2='dv2',
        dk3='dv3')

func_lt('foobar',
        't1',
        't2',
        dk1='dv1',
        dk2='dv2',
        dk3='dv3')
```


## 関数オブジェクト


### 関数を変数に代入

- def
  - 中身は複数の文。単独の文になる
- lambda
  - 中身は単一の式。式になる

```py
print(print)

def print2(x):
    print(x)

print(print2)

print3 = print2
print(print3)

print3('foobar')
```

> \<built-in function print\>
>
> \<function print2 at 0x00000206FF1A4558\>
>
> \<function print2 at 0x00000206FF1A4558\>
>
> foobar

```py
print4 = lambda x: print(x)
print(print4)

print4('foobar')
```

> \<function <lambda> at 0x00000206FF1A40D8\>
>
> foobar


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
> 第 1 引数: python3md-arg.py
>
> 第 2 引数: aaa
>
> 第 3 引数: bbb
>
> 第 4 引数: ccc


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


### 無限ループをキー入力で抜ける

```py
import fcntl
import termios
import sys
import os

def getkey():
    fno = sys.stdin.fileno()

    #stdinの端末属性を取得
    attr_old = termios.tcgetattr(fno)

    # エコーバック・行単位での編集(カノニカルモード)を無効化する
    attr = termios.tcgetattr(fno)

    # Ctrl + CでKeyboardInterruptとする場合
    # attr[3] = attr[3] & ~termios.ECHO & ~termios.ICANON
    # Ctrl + Cをキー入力として利用する場合
    attr[3] = attr[3] & ~termios.ECHO & ~termios.ICANON & ~termios.ISIG
    # ##

    termios.tcsetattr(fno, termios.TCSADRAIN, attr)

    # NONBLOCKモードを設定して、リアルタイムに取る
    fcntl_old = fcntl.fcntl(fno, fcntl.F_GETFL)
    fcntl.fcntl(fno, fcntl.F_SETFL, fcntl_old | os.O_NONBLOCK)

    chr = 0

    try:
        # キーを取得
        c = sys.stdin.read(1)
        if len(c):
            while len(c):
                chr = (chr << 8) + ord(c)
                c = sys.stdin.read(1)
    finally:
        # stdinを元に戻す
        fcntl.fcntl(fno, fcntl.F_SETFL, fcntl_old)
        termios.tcsetattr(fno, termios.TCSANOW, attr_old)

    return chr

if __name__ == '__main__':
    while 1:
        key = getkey()
        if key == 10:
            # Enter
            break
        elif key == 27:
            # Esc
            break
        elif key == 1792836:
            # ←
            break
        elif key == 1792833:
            # ↑
            break
        elif key == 1792834:
            # ↓
            break
        elif key == 1792835:
            # →
            break
        elif key:
            print(key)
```


## 標準出力

```py
print('Hello Python!')

# すぐにフラッシュする(Python3.3以降)
print('Hello Python!', flush=True)

# すぐにフラッシュする(Python3.2以前)
import sys
print('Hello Python!')
sys.stdout.flush()
```


### 末尾に改行文字をつけずに出力する

```py
print('Hello Python!', end='');print('Hello Python!', end='')
```

> Hello Python!Hello Python!


### pprint()でデータ出力の整然化

辞書・リストなどのオブジェクトを整形して出力する

```py
from pprint import pprint

dctlst = [{ 1:'first', 2:'second', 3:'third'},{ 11:'first', 12:'second', 13:'third'},{ 21:'first', 22:'second', 23:'third'}]
pprint(dctlst, stream=f)
```

> [{1: 'first', 2: 'second', 3: 'third'},
>
> {11: 'first', 12: 'second', 13: 'third'},
>
> {21: 'first', 22: 'second', 23: 'third'}]

```py
from pprint import pprint

dctlst = [{ 1:'first', 2:'second', 3:'third'},{ 11:'first', 12:'second', 13:'third'},{ 21:'first', 22:'second', 23:'third'}]

# 深さを指定
pprint(dctlst, depth=1)

# 横幅を指定
pprint(dctlst, width=20)
```

> [{...}, {...}, {...}]

> [{1: 'first',
>
> 2: 'second',
>
> 3: 'third'},
>
> {11: 'first',
>
> 12: 'second',
>
> 13: 'third'},
>
> {21: 'first',
>
> 22: 'second',
>
> 23: 'third'}]


### 標準出力の内容をファイルに書き出す


#### stdout

```py
import sys
temp_sysout = sys.stdout
f = open('./path/to/file.txt', 'w')
sys.stdout = f

print('to file')

sys.stdout = temp_sysout
f.close()

print('to console')
```

- file.txt

> to file

- Console

> to console


#### print()

```py
with open('./path/to/file.txt', 'w') as f:
    print('contents', file=f)
```


### プログレスバーを表示

```sh
$ pip install tqdm
```


#### イテラブルなオブジェクトを指定

```py
from tqdm import tqdm
import time

for i in tqdm(range(100)):
    time.sleep(0.1)

for i in tqdm([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]):
    time.sleep(0.1)

for i in tqdm('Lorem ipsum dolor sit amet, vidit causae eum at.'):
    time.sleep(0.1)
```


#### 全量と割合を指定

```py
from tqdm import tqdm
import time

total = 10000
per = 100

bar = tqdm(total = total)
for i in range(100):
    bar.update(per)
    time.sleep(0.1)
```


## 環境変数


### 環境変数の読み出し


#### 一覧の取得

```py
import os
print(os.environ)
```

> environ({
>
>     'ALLUSERSPROFILE': 'C:\\ProgramData',
>
>     'APPDATA': 'C:\\Users\\y\\AppData\\Roaming',
>
>     (中略)
>
>     'COLORTERM': 'truecolor'
>
> })

※整形済

```py
import os
for k in os.environ: # そのままforループで回す
    print(k)

for k in os.environ.keys(): # keys()メソッドをつけてforループで回す
    print(k)
```

> ALLUSERSPROFILE
>
> APPDATA
>
> (中略)
>
> COLORTERM

```py
import os
for v in os.environ.values():
    print(v)

for v in list(os.environ.values()): # list型で取得
    print(v)
```

> C:\ProgramData
>
> C:\Users\y\AppData\Roaming
>
> (中略)
>
> truecolor

```py
import os
for k, v in os.environ.items():
    print(k, v)

for k, v in list(os.environ.items()): # list型で取得
    print(k, v)
```

> ALLUSERSPROFILE C:\ProgramData
>
> APPDATA C:\Users\y\AppData\Roaming
>
> (中略)
>
> COLORTERM truecolor


#### 環境変数の存在チェック

```py
import os

# キーの存在チェック
print('ALLUSERSPROFILE' in os.environ)
print('ALLUSERSPROFILE' not in os.environ.keys())

# 値の存在チェック
print('C:\\ProgramData' in os.environ.values())

# キーと値を組み合わせてチェック
print(('ALLUSERSPROFILE', 'C:\\ProgramData') in os.environ.items())
```

> True
>
> False

> True

> True


#### キーを指定して値を取得

```py
import os

print(os.environ['ALLUSERSPROFILE'])
print(os.environ.get('ALLUSERSPROFILE'))
print(os.getenv('ALLUSERSPROFILE'))

print(os.environ['_ALLUSERSPROFILE']) # 指定されたキーが存在しない場合はエラー
print(os.environ.get('_ALLUSERSPROFILE')) # 指定されたキーが存在しない場合はNone
print(os.environ.get('_ALLUSERSPROFILE', 'NULL')) # 指定されたキーが存在しない場合は第2引数に指定された値
print(os.getenv('_ALLUSERSPROFILE', 'NULL')) # 指定されたキーが存在しない場合は第2引数に指定された値
```

> C:\ProgramData
>
> C:\ProgramData
>
> C:\ProgramData

> KeyError: '\_ALLUSERSPROFILE'
>
> None
>
> NULL
>
> NULL


### 環境変数の書き込み

以下の手順で環境変数を設定／上書きしても、システムの環境変数が変更されるわけではなく、実行中のスクリプトでのみ反映される

```py
import os

os.environ['SAMPLE'] = 'foobar'
print(os.environ['SAMPLE'])

os.environ['SAMPLE'] = 'hogepiyo' # 上書きされる
print(os.environ['SAMPLE'])

os.environ['SAMPLE'] = 123 # 文字列以外を代入しようとするとTypeError
print(os.environ['SAMPLE'])
```

> foobar
>
> hogepiyo
>
> TypeError: str expected, not int
>
> hogepiyo


### 環境変数の削除

```py
import os

os.environ['SAMPLE'] = 'foobar'
print(os.environ['SAMPLE'])

print(os.environ.pop('SAMPLE'))
print(os.environ['SAMPLE'])

print(os.environ.pop('SAMPLE', None))
```

> foobar

> foobar
>
> KeyError: 'SAMPLE'

> None

```py
import os

os.environ['SAMPLE'] = 'foobar'
print(os.environ['SAMPLE'])

del os.environ['SAMPLE']

del os.environ['SAMPLE']
```

> foobar

>

> KeyError: 'SAMPLE'


### .env ファイルに記述した設定値を環境変数に設定

- 1. `python-dotenv` モジュールをインストールする

```sh
$ pip install python-dotenv
```

- 2. `.env` ファイルを作成

```
PASSWORD=my_password
```

- 3. `settings.py` を呼び出す

- settings.py

```py
import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(join(dirname(__file__), '.env'))
PASSWORD = os.environ.get('PASSWORD')
```

- app.py

```py
import settings

PASSWORD = settings.PASSWORD
print(PASSWORD)
```


## ハッシュ


### 文字列からハッシュを取得

```py
import hashlib

dat = 'foobar'

print(hashlib.algorithms_guaranteed) # サポートしているアルゴリズムの一覧を取得

print(hashlib.md5(dat.encode()).hexdigest()) # MD5
print(hashlib.sha1(dat.encode()).hexdigest()) # SHA-1
print(hashlib.sha256(dat.encode()).hexdigest()) # SHA256
print(hashlib.sha512(dat.encode()).hexdigest()) # SHA512
```

> {'shake_128', 'sha384', 'blake2b', 'sha3_224', 'blake2s', 'sha224', 'sha256', 'sha512', 'sha3_256', 'sha3_384', 'shake_256', 'sha3_512', 'md5', 'sha1'}
>
> 3858f62230ac3c915f300c664312c63f
>
> 8843d7f92416211de9ebb963ff4ce28125932878
>
> c3ab8ff13720e8ad9047dd39466b3c8974e592c2fa383d4a3960714caef0c4f2
>
> 0a50261ebd1a390fed2bf326f2673c145582a6342d523204973d0219337f81616a8069b012587cf5635f6925f1b56c360230c19b273500ee013e030601bf2425


#### 巨大なデータのハッシュを取得

```py
import hashlib

dat = b'hoge'*0x100000

# 比較用
print(hashlib.md5(dat).hexdigest())

h = hashlib.new('md5')

# 処理単位
chunk_size = h.block_size * 4096

while dat:
    chunk = dat[:chunk_size]
    dat = dat[chunk_size:]
    # ハッシュオブジェクトを更新
    h.update(chunk)

print(h.hexdigest())
```

> 58e20228105b868ae22ac4e3f5074631
>
> 58e20228105b868ae22ac4e3f5074631


### ファイルのハッシュを取得

```py
import hashlib
import os

with open(os.path.join('test-fileio', 'inputsjis.txt'),'rb') as f:
    dat = f.read()
    print(hashlib.algorithms_guaranteed) # サポートしているアルゴリズムの一覧を取得
    print(hashlib.md5(dat).hexdigest()) # MD5
    print(hashlib.sha1(dat).hexdigest()) # SHA-1
    print(hashlib.sha256(dat).hexdigest()) # SHA256
    print(hashlib.sha512(dat).hexdigest()) # SHA512
```

> {'shake_128', 'sha384', 'blake2b', 'sha3_224', 'blake2s', 'sha224', 'sha256', 'sha512', 'sha3_256', 'sha3_384', 'shake_256', 'sha3_512', 'md5', 'sha1'}
>
> 8618e191816aeee9ad8e3444be9a26b5
>
> 7904da5abecff2cfa009df4262140d2f55e4d3da
>
> 9f4b600039cc7d66def7f25be7c6e1b998f3afc6c23eb52fb840b19480dd1ca2
>
> 3e5df2441e594ce512d81de7db1574e8c5f3187610ac0855d1d8f9111b983ced5af1277ee036c7e6817419553a3f7c910986fbd9d6d754b57cd82f2ee0d25fcc


#### 巨大なファイルのハッシュを取得

```py
import hashlib
import os

h = hashlib.new('md5')

# 処理単位
chunk_size = h.block_size * 4096

with open(os.path.join('test-fileio', 'inputsjis.txt'),'rb') as f:
    chunk = f.read(chunk_size)
    while chunk:
        # ハッシュオブジェクトを更新
        h.update(chunk)
        chunk = f.read(chunk_size)

print(h.hexdigest())
```

> 8618e191816aeee9ad8e3444be9a26b5


## pathlib でのファイル操作

```py
from pathlib import Path
```

| 項目                 | 関数            | 値                                                             |
| -------------------- | --------------- | -------------------------------------------------------------- |
| カレントディレクトリ | `Path().cwd()`  | `WindowsPath('C:/Users/y/Documents/GitHub/Python-cheatsheet')` |
| ホームディレクトリ   | `Path().home()` | `WindowsPath('C:/Users/y')`                                    |

```py
from pathlib import Path

pd = Path() # カレントディレクトリ

filepath = ('./test-pathlib/test.txt')
pf = Path(filepath) # ファイルのPathオブジェクト
```

| 項目                                                                                             | 関数                                                         | 値                                                                                                                                                                                                                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ファイル情報（フォルダ）                                                                         | `pd.stat()`                                                  | `os.stat_result(st_mode=16895, st_ino=1970324838202858, st_dev=2665268219, st_nlink=1, st_uid=0, st_gid=0, st_size=4096, st_atime=1580268901, st_mtime=1580268901, st_ctime=1564111044)`                                                                                                                                                                              |
| 　　　　　　（ファイル）                                                                         | `pf.stat()`                                                  | `os.stat_result(st_mode=33206, st_ino=21110623253331987, st_dev=2665268219, st_nlink=1, st_uid=0, st_gid=0, st_size=533, st_atime=1580268916, st_mtime=1565394485, st_ctime=1580268916)`                                                                                                                                                                              |
|                                                                                                  |                                                              |                                                                                                                                                                                                                                                                                                                                                                       |
| 　（パスがシンボリックリンクの場合、シンボリックリンク自身の情報を取得）                         | `pd.lstat()`                                                 | `os.stat_result(st_mode=16895, st_ino=1970324838202858, st_dev=2665268219, st_nlink=1, st_uid=0, st_gid=0, st_size=4096, st_atime=1580268901, st_mtime=1580268901, st_ctime=1564111044)`                                                                                                                                                                              |
| ファイルの所有者のユーザー名                                                                     | `pd.owner()`                                                 | `NotImplementedError: Path.owner() is unsupported on this system` (Windows)                                                                                                                                                                                                                                                                                           |
| ファイルの所有者のグループ名                                                                     | `pd.group()`                                                 | `NotImplementedError: Path.owner() is unsupported on this system` (Windows)                                                                                                                                                                                                                                                                                           |
|                                                                                                  |                                                              |                                                                                                                                                                                                                                                                                                                                                                       |
| 相対パス（フォルダ）                                                                             | `pd`                                                         | `WindowsPath('.')`                                                                                                                                                                                                                                                                                                                                                    |
| 　　　　（ファイル）                                                                             | `pf`                                                         | `WindowsPath('test-pathlib/test.txt')`                                                                                                                                                                                                                                                                                                                                |
|                                                                                                  |                                                              |                                                                                                                                                                                                                                                                                                                                                                       |
| 絶対パス（フォルダ）                                                                             | `pd.resolve()` <br> `p.absolute()`                           | `WindowsPath('C:/Users/y/Documents/GitHub/Python-cheatsheet')`                                                                                                                                                                                                                                                                                                        |
| 　　　　（ファイル）                                                                             | `pf.resolve()` <br>or<br> `p.absolute()`                     | `WindowsPath('C:/Users/y/Documents/GitHub/Python-cheatsheet/test-pathlib/test.txt')`                                                                                                                                                                                                                                                                                  |
|                                                                                                  |                                                              |                                                                                                                                                                                                                                                                                                                                                                       |
| スラッシュ区切りのパス                                                                           | `Path('c:\\windows').resolve().as_posix()`                   | `'C:/Windows'`                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                  |                                                              |                                                                                                                                                                                                                                                                                                                                                                       |
| file URI                                                                                         | `pf.resolve().as_uri()`                                      | `'file:///C:/Users/y/Documents/GitHub/Python-cheatsheet/test-pathlib/test.txt'`                                                                                                                                                                                                                                                                                       |
|                                                                                                  |                                                              |                                                                                                                                                                                                                                                                                                                                                                       |
| ドライブ文字                                                                                     | `pf.resolve().drive`                                         | `'C:'`                                                                                                                                                                                                                                                                                                                                                                |
| ルート                                                                                           | `pf.resolve().root`                                          | `\\`                                                                                                                                                                                                                                                                                                                                                                  |
| アンカー（ドライブ文字＋ルート）                                                                 | `pf.resolve().anchor`                                        | `C:\\`                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                  |                                                              |                                                                                                                                                                                                                                                                                                                                                                       |
| ファイル名（basename）                                                                           | `pf.resolve().name`                                          | `'test.txt'`                                                                                                                                                                                                                                                                                                                                                          |
| 拡張子                                                                                           | `pf.resolve().suffix`                                        | `'.txt'`                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                  | `Path('test.tar.gz').resolve().suffix`                       | `'.gz'`                                                                                                                                                                                                                                                                                                                                                               |
| 拡張子のリスト                                                                                   | `pf.resolve().suffixes`                                      | `['.txt']`                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                  | `Path('test.tar.gz').resolve().suffixes`                     | `['.tar', '.gz']`                                                                                                                                                                                                                                                                                                                                                     |
| ファイル名から拡張子を除いたもの                                                                 | `pf.resolve().stem`                                          | `'test'`                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                  |                                                              |                                                                                                                                                                                                                                                                                                                                                                       |
| パスが存在するかどうか（フォルダ）                                                               | `pd.exists()`                                                | `True`                                                                                                                                                                                                                                                                                                                                                                |
| 　　　　　　　　　　　（ファイル）                                                               | `pf.exists()`                                                | `True`                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                  |                                                              |                                                                                                                                                                                                                                                                                                                                                                       |
| パスがディレクトリ（またはディレクトリへのシンボリックリンク）（フォルダ）                       | `pd.is_dir()`                                                | `True`                                                                                                                                                                                                                                                                                                                                                                |
| 　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　（ファイル）                       | `pf.is_dir()`                                                | `False`                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                  |                                                              |                                                                                                                                                                                                                                                                                                                                                                       |
| パスが一般ファイル（または一般ファイルへのシンボリックリンク）（フォルダ）                       | `pd.is_file()`                                               | `False`                                                                                                                                                                                                                                                                                                                                                               |
| 　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　（ファイル）                       | `pf.is_file()`                                               | `True`                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                  |                                                              |                                                                                                                                                                                                                                                                                                                                                                       |
| パスがシンボリックリンク（フォルダ）                                                             | `pd.is_symlink()`                                            | `False`                                                                                                                                                                                                                                                                                                                                                               |
| 　　　　　　　　　　　　（ファイル）                                                             | `pf.is_symlink()`                                            | `False`                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                  |                                                              |                                                                                                                                                                                                                                                                                                                                                                       |
| パスが Unix ソケット（または Unix ソケットへのシンボリックリンク）（フォルダ）                   | `pd.is_socket()`                                             | `False`                                                                                                                                                                                                                                                                                                                                                               |
| 　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　（ファイル）                   | `pf.is_socket()`                                             | `False`                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                  |                                                              |                                                                                                                                                                                                                                                                                                                                                                       |
| パスが FIFO（または FIFO へのシンボリックリンク）（フォルダ）                                    | `pd.is_fifo()`                                               | `False`                                                                                                                                                                                                                                                                                                                                                               |
| 　　　　　　　　　　　　　　　　　　　　　　　　　（ファイル）                                   | `pf.is_fifo()`                                               | `False`                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                  |                                                              |                                                                                                                                                                                                                                                                                                                                                                       |
| パスが絶対パスかどうか（フォルダ）                                                               | `pd.is_absolute()`                                           | `False`                                                                                                                                                                                                                                                                                                                                                               |
| 　　　　　　　　　　　（ファイル）                                                               | `pf.is_absolute()`                                           | `False`                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                  |                                                              |                                                                                                                                                                                                                                                                                                                                                                       |
| パス文字列の連結（結合）                                                                         | `Path('test-pathlib').joinpath('sub')`                       | `WindowsPath('test-pathlib/sub')`                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                  | `Path('test-pathlib').joinpath('test.txt')`                  | `WindowsPath('test-pathlib/test.txt')`                                                                                                                                                                                                                                                                                                                                |
|                                                                                                  | `Path('c:').joinpath('/Program Files')`                      | `WindowsPath('c:/Program Files')`                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                  | `Path('c:/').joinpath('Program Files')`                      | `WindowsPath('c:/Program Files')`                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                  | `Path('c:').joinpath('Program Files')`                       | `WindowsPath('c:Program Files')`                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                  | `Path('c:\\').joinpath('Program Files').joinpath('Python')`  | `WindowsPath('c:/Program Files/Python')`                                                                                                                                                                                                                                                                                                                              |
|                                                                                                  |                                                              |                                                                                                                                                                                                                                                                                                                                                                       |
| `~` および `~user` を展開（存在しないパスも可）                                                  | `Path('~/non-existent').expanduser()`                        | `WindowsPath('C:/Users/y/work')`                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                  |                                                              |                                                                                                                                                                                                                                                                                                                                                                       |
| パス文字列のうちファイル名（basename）のみを置換 （フォルダ）                                    | `Path('c:/non-existent').with_name('replaced')`              | `WindowsPath('c:/replaced')`                                                                                                                                                                                                                                                                                                                                          |
| 　　　　　　　　　　　　　　　　　　　　　　　　　（ファイル）                                   | `pf.with_name('replaced.txt')`                               | `WindowsPath('test-pathlib/replaced.txt')`                                                                                                                                                                                                                                                                                                                            |
|                                                                                                  |                                                              |                                                                                                                                                                                                                                                                                                                                                                       |
| パス文字列のうち拡張子のみを置換                                                                 | `pf.with_suffix('.txt')`                                     | `WindowsPath('test-pathlib/test.txt')`                                                                                                                                                                                                                                                                                                                                |
|                                                                                                  |                                                              |                                                                                                                                                                                                                                                                                                                                                                       |
| 上位パスを辿る                                                                                   | `pf.resolve().parents`                                       | `<WindowsPath.parents>`                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                  | `[i for i in pf.resolve().parents]`                          | `[WindowsPath('C:/Users/y/Documents/GitHub/Python-cheatsheet/test-pathlib'), WindowsPath('C:/Users/y/Documents/GitHub/Python-cheatsheet'),` ... `WindowsPath('C:/Users'), WindowsPath('C:/')]`                                                                                                                                                                        |
| 上位パス                                                                                         | `pf.resolve().parent`                                        | `WindowsPath('C:/Users/y/Documents/GitHub/Python-cheatsheet/test-pathlib')`                                                                                                                                                                                                                                                                                           |
|                                                                                                  | `Path('/').parent`                                           | `WindowsPath('/')` 親ディレクトリが存在しない場合                                                                                                                                                                                                                                                                                                                     |
|                                                                                                  | `Path('.').parent`                                           | `WindowsPath('.')` 空のパス                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                  | `Path('.').resolve().parent`                                 | `WindowsPath('C:/Users/y/Documents/GitHub')`                                                                                                                                                                                                                                                                                                                          |
|                                                                                                  |                                                              |                                                                                                                                                                                                                                                                                                                                                                       |
| 2 つのパスが参照するファイル／フォルダが一致するか（ファイルが存在しないと `FileNotFoundError`） | `Path('C:/Users/y/').samefile(Path('~/').expanduser())`      | `True`                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                  |                                                              |                                                                                                                                                                                                                                                                                                                                                                       |
| 2 つのパス間の相対パス                                                                           | `Path('/var/www/html').relative_to('/var')`                  | `WindowsPath('www/html')`                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                  | `Path('/var/www/html').relative_to('/etc')`                  | `ValueError: '\\var\\www\\html' does not start with '\\etc'`                                                                                                                                                                                                                                                                                                          |
|                                                                                                  |                                                              |                                                                                                                                                                                                                                                                                                                                                                       |
| ディレクトリの内容を列挙                                                                         | `for child in pd.iterdir(): child`                           | `WindowsPath('.git')` <br> `WindowsPath('.gitattributes')` <br> ... <br> `WindowsPath('__pycache__')`                                                                                                                                                                                                                                                                 |
|                                                                                                  |                                                              |                                                                                                                                                                                                                                                                                                                                                                       |
| glob 形式のパターンにマッチするか                                                                | `pf.match('*.txt')`                                          | `True`                                                                                                                                                                                                                                                                                                                                                                |
| 　（pattern が相対表記であればパスは相対／絶対パスを取り、右から一致を調べる）                   | `Path('/a/b/c.py').match('b/*.py')`                          | `True`                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                  | `Path('/a/b/c.py').match('a/*.py')`                          | `False`                                                                                                                                                                                                                                                                                                                                                               |
| 　（pattern が絶対表記であればパスは絶対パスでなければならず、パス全体が一致するか調べる）       | `Path('/a.py').match('/*.py')`                               | `True`                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                  | `Path('a/b.py').match('/*.py')`                              | `False`                                                                                                                                                                                                                                                                                                                                                               |
| 　（大文字／小文字の区別）                                                                       | `Path('b.py').match('*.PY')`                                 | `True` (Windows の場合)                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                  |                                                              |                                                                                                                                                                                                                                                                                                                                                                       |
| glob 形式のパターンにマッチするファイル・フォルダの一覧                                          | `sorted(Path('./test-glob').glob('*'))`                      | `[WindowsPath('test-glob/test-glob-1'), WindowsPath('test-glob/test-glob-2'), WindowsPath('test-glob/test-glob-3.dat')]`                                                                                                                                                                                                                                              |
|                                                                                                  | `sorted(Path('./test-glob').glob('non-existent-dir/*.dat'))` | `[]`                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                  | `sorted(Path('./test-glob').glob('*/*.dat'))`                | `[WindowsPath('test-glob/test-glob-1/test-glob-1-2.dat'), WindowsPath('test-glob/test-glob-2/.test-glob-2-1.dat'), WindowsPath('test-glob/test-glob-2/test-glob-2-2.dat')]`                                                                                                                                                                                           |
| 　（再帰的に検索）                                                                               | `sorted(Path('./test-glob').glob('**/*.dat'))`               | `[WindowsPath('test-glob/test-glob-1/test-glob-1-1/test-glob-1-1-1.dat'), WindowsPath('test-glob/test-glob-1/test-glob-1-1/test-glob-1-1-2.dat'), WindowsPath('test-glob/test-glob-1/test-glob-1-2.dat'), WindowsPath('test-glob/test-glob-2/.test-glob-2-1.dat'), WindowsPath('test-glob/test-glob-2/test-glob-2-2.dat'), WindowsPath('test-glob/test-glob-3.dat')]` |
| 　（再帰的に検索；pattern の前に `"**/"` を追加した glob()）                                     | `sorted(Path('./test-glob').rglob('*.py'))`                  | `[WindowsPath('test-glob/test-glob-1/test-glob-1-1/test-glob-1-1-1.dat'), WindowsPath('test-glob/test-glob-1/test-glob-1-1/test-glob-1-1-2.dat'), WindowsPath('test-glob/test-glob-1/test-glob-1-2.dat'), WindowsPath('test-glob/test-glob-2/.test-glob-2-1.dat'), WindowsPath('test-glob/test-glob-2/test-glob-2-2.dat'), WindowsPath('test-glob/test-glob-3.dat')]` |
|                                                                                                  |                                                              |                                                                                                                                                                                                                                                                                                                                                                       |

| stat の項目 | 説明                             |
| ----------- | -------------------------------- |
| `st_mode`   | ファイルモード                   |
| `st_ino`    | inode 番号（Unix）               |
|             | the file index（Windows）        |
| `st_dev`    | デバイスの識別子                 |
| `st_nlink`  | ハードリンクの数                 |
| `st_uid`    | ファイル所有者のユーザ識別子     |
| `st_gid`    | ファイル所有者のグループ識別子   |
| `st_size`   | バイト単位でのファイルサイズ     |
| `st_atime`  | 秒で表した最終アクセス時刻       |
| `st_mtime`  | 秒で表した最終更新時刻           |
| `st_ctime`  | メタデータの最終更新時刻（Unix） |
|             | 秒で表した作成時刻（Windows）    |

```py
from pathlib import Path

pd = Path('./test-pathlib/')
pf = Path('./test-pathlib/test.txt')
```

| 項目                                                                                                       | 関数                                                                                                                                       | オプション                                                                                 | 値                                                                                             |
| ---------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------- |
| ファイルを作成                                                                                             | `Path('./test-pathlib/test').touch(mode=0o666, exist_ok=True)`                                                                             | 途中のパスが存在しない場合はエラーを出さずに何もしない                                     |                                                                                                |
|                                                                                                            |                                                                                                                                            | `mode` がある場合、プロセスの umask 値と組み合わせてファイルのモードとアクセスフラグを決定 |                                                                                                |
| フォルダを作成                                                                                             | `Path('./test-pathlib/').mkdir(mode=0o777, parents=False, exist_ok=False)`                                                                 | `mode` がある場合、プロセスの umask 値と組み合わせてファイルのモードとアクセスフラグを決定 |                                                                                                |
|                                                                                                            |                                                                                                                                            | `parents=False` （既定）：親ディレクトリがないと FileNotFoundError                         |                                                                                                |
|                                                                                                            |                                                                                                                                            | `parents=True`：途中階層のディレクトリがなければ作成                                       |                                                                                                |
|                                                                                                            |                                                                                                                                            | `exist_ok=False` （既定）：対象のディレクトリが既に存在すると FileExistsError              |                                                                                                |
|                                                                                                            |                                                                                                                                            | `exist_ok=True`：パス要素の末尾が既に存在するがディレクトリではないと FileExistsError      |                                                                                                |
|                                                                                                            |                                                                                                                                            |                                                                                            |                                                                                                |
| シンボリックリンクを作成（Windows でフォルダにリンクする場合は `target_is_directory=True` を指定）         | `Path('./test-pathlib/link').symlink_to('./test-pathlib/test.txt')`                                                                        |                                                                                            |                                                                                                |
| ハードリンクを作成                                                                                         | `Path('./test-pathlib/link').link_to('./test-pathlib/test.txt')`                                                                           |                                                                                            |                                                                                                |
|                                                                                                            |                                                                                                                                            |                                                                                            |                                                                                                |
| ファイル・フォルダを移動                                                                                   | `Path('./test-pathlib/test.txt').rename('./test-pathlib/renamed.txt')`                                                                     | `WindowsPath('test-pathlib/renamed.txt')`                                                  |                                                                                                |
| （Unix の場合は target が既存のファイルだと上書きされるが、Windows の場合は `FileExistsError` ）           | `Path('./test-pathlib/renamed.txt').rename(Path('./test-pathlib/test.txt')).exists()`                                                      | `True`                                                                                     |                                                                                                |
| ファイル・フォルダを移動                                                                                   | `Path('./test-pathlib/test.txt').replace('./test-pathlib/replaced.txt')`                                                                   | `WindowsPath('test-pathlib/renamed.txt')`                                                  |                                                                                                |
| （target が既存のファイル／フォルダだと無条件に上書き）                                                    | `Path('./test-pathlib/replaced.txt').replace(Path('./test-pathlib/test.txt')).exists()`                                                    | `True`                                                                                     |                                                                                                |
| （既存のフォルダにファイルを上書きしようとすると `PermissionError`）                                       | `Path('./test-pathlib/test.txt').is_dir() and Path('./test-pathlib/replaced.txt').replace(Path('./test-pathlib/test.txt')).exists()`       | `PermissionError`                                                                          |                                                                                                |
|                                                                                                            |                                                                                                                                            |                                                                                            |                                                                                                |
| モードを変更                                                                                               | `pf.chmod(0o444)` < br > `pf.stat().st_mode`                                                                                               |                                                                                            | `33060`                                                                                        |
|                                                                                                            | `pd.chmod(0o444)` < br > `pd.stat().st_mode`                                                                                               |                                                                                            | `16749`                                                                                        |
| 　（シンボリックリンク自身のモードを変更）                                                                 | `pd.lchmod(0o444)` < br > `pd.stat().st_mode`                                                                                              |                                                                                            | `16749`                                                                                        |
|                                                                                                            |                                                                                                                                            |                                                                                            |                                                                                                |
| ファイルを削除 （デフォルトの missing_ok=False だと、ファイルが既に存在しない場合は `FileNotFoundError` ） | `Path('./test-pathlib/exist.txt').unlink()`                                                                                                |                                                                                            |                                                                                                |
| 　特定のフォルダ内にあるファイルをすべて削除                                                               | `[p.unlink() for p in Path('./test-pathlib/exist/').iterdir() if p.is_file()]`                                                             |                                                                                            |                                                                                                |
| 空のフォルダを削除                                                                                         | `Path('./test-pathlib/exist').rmdir()`                                                                                                     |                                                                                            | 配下にファイル／フォルダが存在すると `OSError: ディレクトリが空ではありません。`               |
|                                                                                                            |                                                                                                                                            |                                                                                            |                                                                                                |
| ファイルを開いて 1 行読み込む                                                                              | `with pf.open(mode='r', buffering=-1, encoding='utf_8_sig', errors=None, newline=None) as f:` <br> &nbsp;&nbsp;&nbsp;&nbsp; `f.readline()` | BOM なしの UTF-8 ならば `encoding = 'UTF-8'`                                               | `'あいうえお8XkfWDHyFdcB52MbTNNswDnFRAsZdEgRmmsaNktD\n'`                                       |
| ファイルの内容をバイナリデータとして取得 （パスが存在しない場合は `FileNotFoundError`）                    | `pf.read_bytes()`                                                                                                                          |                                                                                            | `b'\xef\xbb\xbf\xe3\x81\x82\xe3\x81\x84\xe3\x81\x86\xe3\x81\x88\xe3\x81\x8a8Xk` ... `YjQ\r\n'` |
| ファイルの内容をテキストデータ（文字列型）として取得（パスが存在しない場合は `FileNotFoundError`）         | `pf.read_text(encoding='utf_8_sig')`                                                                                                       |                                                                                            | `'あいうえお8Xk` ... `YjQ\n'`                                                                  |
|                                                                                                            |                                                                                                                                            |                                                                                            |                                                                                                |
| ファイルにバイナリデータを書き込む（上書き；パスが存在しない場合は新規作成）                               | `Path('./test-pathlib/write.bin').write_bytes(b'Binary data')`                                                                             |                                                                                            | `11`                                                                                           |
| ファイルにテキストデータを書き込む（上書き；パスが存在しない場合は新規作成）                               | `Path('./test-pathlib/write.txt').write_text('Text data', encoding='UTF-8')`                                                               |                                                                                            | `9`                                                                                            |
|                                                                                                            | `Path('./test-pathlib/write.txt').write_text('Text data', encoding='utf_8_sig')`                                                           |                                                                                            | `9`                                                                                            |
|                                                                                                            | `Path('./test-pathlib/write.txt').write_text('Ｔｅｘｔ ｄａｔａ', encoding='Shift-JIS')`                                                   |                                                                                            | `9`                                                                                            |

| ファイルが開かれるモードの項目 | 説明                                                     | パスが存在しない場合 |
| ------------------------------ | -------------------------------------------------------- | -------------------- |
| `r`                            | 読み込み用に開く(デフォルト)                             | `FileNotFoundError`  |
| `w`                            | 書き込み用に開き、まずファイルを切り詰める               | 新規作成             |
| `x`                            | 排他的な生成に開き、ファイルが存在する場合は失敗する     |                      |
| `a`                            | 書き込み用に開き、ファイルが存在する場合は末尾に追記する |                      |
| `b`                            | バイナリモード                                           | -                    |
| `t`                            | テキストモード(デフォルト)                               | -                    |
| `+`                            | 更新用に開く（読み込み／書き込み）                       | -                    |


## ローカルファイル


### パス文字列の操作

| 取得内容                           | 関数(`import os`が必要)                                                                                        | 値                                                                       | パスにファイルが存在しない場合                                           |
| ---------------------------------- | -------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| パス区切り文字                     | `os.path.sep`                                                                                                  | `'/'`                                                                    |                                                                          |
| パス文字列を組み立て(結合)         | `os.path.join('.', 'test' + '-' + 'join', 'test.txt')`                                                         | `'./test-join/test.txt'`                                                 | `'./test-join/test.txt'`                                                 |
|                                    |                                                                                                                |                                                                          |                                                                          |
| ファイル名                         | `os.path.basename('./test-join/test.txt')`                                                                     | `'test.txt'`                                                             | `'test.txt'`                                                             |
| ディレクトリ名                     | `os.path.dirname('./test-join/test.txt')`                                                                      | `'./test-join'`                                                          | `'./test-join'`                                                          |
| ファイル名とディレクトリ名のタプル | `dname, bname = os.path.split('./test-join/test.txt')` <br> `print(dname, bname)`                              | `./test-join test.txt`                                                   | `./test-join test.txt`                                                   |
| パス～ファイル名と拡張子           | `root, ext = os.path.splitext('./test-join/test.txt')` <br> `print(root, ext)`                                 | `./test-join/test .txt`                                                  | `./test-join/test .txt`                                                  |
|                                    | `spltext = os.path.splitext('./test-join/test.txt')` <br> `print(spltext[0], spltext[1])`                      | `./test-join/test .txt`                                                  | `./test-join/test .txt`                                                  |
|                                    |                                                                                                                |                                                                          |                                                                          |
| 絶対パス                           | `os.path.abspath('./test-join/test.txt')`                                                                      | `'/mnt/c/Users/y/Documents/GitHub/Python-cheatsheet/test-join/test.txt'` | `'/mnt/c/Users/y/Documents/GitHub/Python-cheatsheet/test-join/test.txt'` |
| 2 つのパス間の相対パス             | `os.path.relpath(os.path.abspath('./test-join/test.txt'), '.')`                                                | `'test-join/test.txt'`                                                   | `'test-join/test.txt'`                                                   |
| 共通パス(階層単位)                 | `os.path.commonpath( [os.path.abspath('./test-join/test1.txt'), os.path.abspath('./test-join/test2.txt')] )`   | `'C:\Users\y\Documents\GitHub\Python-cheatsheet\test-join'`              | `'C:\Users\y\Documents\GitHub\Python-cheatsheet\test-join'`              |
| 共通パス(文字単位)                 | `os.path.commonprefix( [os.path.abspath('./test-join/test1.txt'), os.path.abspath('./test-join/test2.txt')] )` | `'C:\Users\y\Documents\GitHub\Python-cheatsheet\test-join\test'`         | `'C:\Users\y\Documents\GitHub\Python-cheatsheet\test-join\test'`         |
| ドライブレター                     | `os.path.splitdrive(os.path.abspath('./test-join/test.txt'))[0]`                                               | `'C:'`                                                                   |                                                                          |

| 検査内容                         | 関数                                                                            | 値      | パスにファイルが存在しない場合                                         |
| -------------------------------- | ------------------------------------------------------------------------------- | ------- | ---------------------------------------------------------------------- |
| パス文字列が絶対パスか           | `os.path.isabs(os.path.abspath('./test-join/test.txt'))`                        | `True`  | `True`                                                                 |
| パス文字列がシンボリックリンクか | `os.path.islink(os.path.abspath('./test-join/test.txt'))`                       | `False` | `False`                                                                |
| パス文字列がマウントポイントか   | `os.path.ismount(os.path.abspath('./test-join/test.txt'))`                      | `False` | `False`                                                                |
| パスが示すファイルが同一か       | `os.path.samefile('./test-join/test.txt', './test-join/../test-join/test.txt')` | `True`  | `FileNotFoundError: [WinError 2] 指定されたファイルが見つかりません。` |


#### 複数のパスが同一のファイルを示しているか検査

```py
paths = [
    os.path.abspath('./test-join/test1.txt'),
    os.path.abspath('./test-join/test/../test1.txt'),
]

print(os.path.samefile(paths[0], paths[1])) # ファイルパスが同じファイルを参照しているか

with open(paths[0], 'r') as f1, open(paths[1], 'r') as f2:
    print(os.path.sameopenfile(f1.fileno(), f2.fileno())) # ファイル記述子が同じファイルを参照しているか

stat1 = os.stat(paths[0])
stat2 = os.stat(paths[1])
print(os.path.samestat(stat1, stat2)) # os.fstat(), os.lstat()，os.stat() の返り値 (stat1, stat2) が同じファイルを参照しているか
```

> True
>
> True
>
> True


#### パス文字列を正規化する

不要な区切り文字、 `..` の除去　／　 Windows 環境での大文字小文字の置換、スラッシュとバックスラッシュの置換

```py
import os

dirpath = 'path/to/to/to/../../folder/'

# 不要な区切り文字、 `..` の除去
nrmpath = os.path.normpath(dirpath)
print(nrmpath)

# Windows環境での大文字小文字の置換、スラッシュとバックスラッシュの置換
nrmcase = os.path.normcase(path)
print(nrmcase)
```

> path\to\folder
>
> c:\users\y\path\to\file.txt


#### ホームディレクトリのパスを取得

```py
import os.path

filepath = os.path.join('~', 'path', 'to', 'file.txt')
path  = os.path.expanduser(filepath)
print(path)
```

> C:\Users\y\path\to\file.txt


#### 環境変数を取得

```py
import os.path

# for Linux
filepath = os.path.join('$HOME', 'path', 'to', 'file.txt')
path  = os.path.expandvars(filepath)
print(path)

# for Windows
filepath = os.path.join('%USERPROFILE%', 'path', 'to', 'file.txt')
path  = os.path.expandvars(filepath)
print(path)
```

> /home/y/path/to/file.txt

> C:\Users\y\path\to\file.txt


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


#### シンボリックリンクのパスを正規化

```py
import os

os.path.realpath(__file__)
```


#### Linux 上で Windows 形式のパスを操作

```py
import ntpath

print(ntpath.sep)
print(ntpath.sep is '\\')

bname = ntpath.basename('\\path\\to\\file')
print(bname)
```

> \
>
> True

> file


### カレントディレクトリ

[python3md-cwd.py](python3md-cwd.py)

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
```

| FILEPATH           | `os.path.exists(FILEPATH)` | `os.path.isdir(FILEPATH)` | `os.path.isfile(FILEPATH)` |
| ------------------ | -------------------------- | ------------------------- | -------------------------- |
| `'.'`              | `True`                     | `True`                    | `False`                    |
| `'./'`             | `True`                     | `True`                    | `False`                    |
| `'./README.md'`    | `True`                     | `False`                   | `True`                     |
| `'./NOTFOUND.txt'` | `False`                    | `False`                   | `False`                    |


### ファイル・フォルダの一覧を取得

| 文字          | 内容                          |
| ------------- | ----------------------------- |
| \*            | 長さ 0 文字以上の任意の文字列 |
| ?             | 任意の一文字                  |
| []            | 括弧の中の文字                |
| [*], [?], [[] | エスケープ                    |

```py
from glob import glob
import os

DIRPATH = os.path.join('.', 'test-glob') # './test-glob'
DIRPATH += '' if DIRPATH.endswith(os.path.sep) else os.path.sep # './test-glob/'
```

| 取得内容                             | 関数                                                                                                                                           | 値                                                                                            | 備考                                           |
| ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| 直下のファイル・フォルダ一覧を取得   | `glob(os.path.join(DIRPATH, '*'), recursive=False)`                                                                                            | `['.\\test-glob\\test-glob-1', '.\\test-glob\\test-glob-2', '.\\test-glob\\test-glob-3.dat']` |                                                |
|                                      | `glob(os.path.join(DIRPATH, '*'), recursive=True)`                                                                                             | `['.\\test-glob\\test-glob-1', '.\\test-glob\\test-glob-2', '.\\test-glob\\test-glob-3.dat']` | `**` を指定していないため `recursive` は無関係 |
| 直下のファイル一覧を取得             | `glob(os.path.join(DIRPATH, '*.*'), recursive=True)`                                                                                           | `['./test-glob/test-glob-3.dat']`                                                             |                                                |
|                                      | `[f for f in glob(os.path.join(DIRPATH, '*')) if os.path.isfile(f)]`                                                                           | `['./test-glob/test-glob-3.dat']`                                                             |                                                |
| 直下のフォルダ一覧を取得             | `[f for f in glob(os.path.join(DIRPATH, '*')) if os.path.isdir(f)]`                                                                            | `['.\\test-glob\\test-glob-1', '.\\test-glob\\test-glob-2']`                                  |                                                |
|                                      |                                                                                                                                                |                                                                                               |                                                |
| 再帰的にファイル・フォルダ一覧を取得 | `glob(os.path.join(DIRPATH, '**'), recursive=True)`                                                                                            | [1]                                                                                           | _recursive_ が `True` かつ、パスに `**`        |
| 再帰的にファイル一覧を取得           | `glob(os.path.join(DIRPATH, os.path.join('**', '*.*')), recursive=True)`                                                                       | [2]                                                                                           |                                                |
| 再帰的にフォルダ一覧を取得           | `[f for f in glob(os.path.join(DIRPATH, '**'), recursive=True) if os.path.isdir(f)]`                                                           | [3]                                                                                           |                                                |
|                                      | `glob(os.path.join(DIRPATH, '**' + os.path.sep), recursive=True)`                                                                              | [4]                                                                                           | パスの末尾が `os.path.sep` になる              |
|                                      |                                                                                                                                                |                                                                                               |                                                |
| ワイルドカードを利用                 | `glob(os.path.join(DIRPATH, os.path.join('**', '*-[0-1].???')), recursive=True)`                                                               | `['.\\test-glob\\test-glob-1\\test-glob-1-1\\test-glob-1-1-1.dat']`                           |                                                |
| 正規表現を利用                       | `import re` <br> `[p for p in glob(os.path.join(DIRPATH, os.path.join('**', '*.*')), recursive=True) if re.search('test-glob(-1){3}.dat', p)]` | `['.\\test-glob\\test-glob-1\\test-glob-1-1\\test-glob-1-1-1.dat']`                           |                                                |

[1]

> ['.\\test-glob\\', '.\\test-glob\\test-glob-1', '.\\test-glob\\test-glob-1\\test-glob-1-1', '.\\test-glob\\test-glob-1\\test-glob-1-1\\test-glob-1-1-1.dat', '.\\test-glob\\test-glob-1\\test-glob-1-1\\test-glob-1-1-2.dat', '.\\test-glob\\test-glob-1\\test-glob-1-2.dat', '.\\test-glob\\test-glob-2', '.\\test-glob\\test-glob-2\\test-glob-2-2.dat', '.\\test-glob\\test-glob-3.dat']

[2]

> ['.\\test-glob\\test-glob-3.dat', '.\\test-glob\\test-glob-1\\test-glob-1-2.dat', '.\\test-glob\\test-glob-1\\test-glob-1-1\\test-glob-1-1-1.dat', '.\\test-glob\\test-glob-1\\test-glob-1-1\\test-glob-1-1-2.dat', '.\\test-glob\\test-glob-2\\test-glob-2-2.dat']

[3]

> ['.\\test-glob\\', '.\\test-glob\\test-glob-1', '.\\test-glob\\test-glob-1\\test-glob-1-1', '.\\test-glob\\test-glob-2']

[4]

> ['.\\test-glob\\', '.\\test-glob\\test-glob-1\\', '.\\test-glob\\test-glob-1\\test-glob-1-1\\', '.\\test-glob\\test-glob-2\\']


#### Python3.4 以前で、再帰的にファイル・フォルダ一覧を取得

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

filepath = './README.md'

atime1 = datetime.fromtimestamp(os.path.getatime(filepath))
atime
print(atime1)

atime2 = datetime.fromtimestamp(os.path.getatime(filepath), timezone(timedelta(hours=9)))
atime2
print(atime2)
print(atime2.tzinfo)

mtime1 = datetime.fromtimestamp(os.path.getmtime(filepath))
mtime1
print(mtime1)

mtime2 = datetime.fromtimestamp(os.path.getmtime(filepath), timezone(timedelta(hours=9)))
mtime2
print(mtime2)
print(mtime2.tzinfo)

size = os.path.getsize(filepath)
size
print(human_readable(size))
```

| 項目             | 関数                          | 値                                                                                                               |
| ---------------- | ----------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| 最終アクセス日時 | `atime1`                      | `datetime.datetime(2020, 1, 24, 8, 38, 56, 106605)`                                                              |
|                  | `print(atime1)`               | `2020-01-24 08:38:56.106605`                                                                                     |
|                  | `atime2`                      | `datetime.datetime(2020, 1, 24, 8, 38, 56, 106605, tzinfo=datetime.timezone(datetime.timedelta(seconds=32400)))` |
|                  | `print(atime2)`               | `2020-01-24 08:38:56.106605+09:00`                                                                               |
|                  | `print(atime2.tzinfo)`        | `UTC+09:00`                                                                                                      |
| 最終更新日時     | `mtime1`                      | `datetime.datetime(2020, 1, 24, 8, 38, 56, 106605)`                                                              |
|                  | `print(mtime1)`               | `2020-01-24 08:38:56.106605`                                                                                     |
|                  | `mtime2`                      | `datetime.datetime(2020, 1, 24, 8, 38, 56, 106605, tzinfo=datetime.timezone(datetime.timedelta(seconds=32400))`  |
|                  | `print(mtime2)`               | `2020-01-24 08:38:56.106605+09:00`                                                                               |
|                  | `print(mtime2.tzinfo)`        | `UTC+09:00`                                                                                                      |
| ファイルサイズ   | `size`                        | `321480`                                                                                                         |
|                  | `print(human_readable(size))` | `313.9 KB`                                                                                                       |


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

```py
import os

DIRPATH = './test-folder/'

os.makedirs(DIRPATH)
```


#### 既存のフォルダがある場合にエラーとしない

```py
import os

DIRPATH = './test-folder/'

os.makedirs(DIRPATH, exist_ok=True)
```


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

# os.makedirs(DIRPATH, exist_ok=True)
os.makedirs(DIRPATH)
```


### ファイル・フォルダをコピー

| 項目                             | コピー対象                                   | `dst` が既存                         | 備考                                                                                                        |
| -------------------------------- | -------------------------------------------- | ------------------------------------ | ----------------------------------------------------------------------------------------------------------- |
| `shutil.copy(src, dst)`          | ファイル（パーミッションを含む）             | 上書き                               | メタデータはコピーされない                                                                                  |
|                                  |                                              |                                      | dst がディレクトリであればファイル名は src と同じものが指定されたディレクトリ内に作成（または上書き）される |
| `shutil.copy2(src, dst)`         | ファイル（パーミッション、メタデータを含む） | 上書き                               | メタデータは `copystat()` 関数でコピー                                                                      |
| `shutil.copyfile(src, dst)`      | ファイル                                     | 上書き                               | `dst` にはディレクトリは指定できない                                                                        |
| `shutil.copyfileobj(fsrc, fdst)` | ファイル形式のオブジェクト                   | 上書き                               |                                                                                                             |
| `shutil.copymode(src, dst)`      | パーミッション                               |                                      | ファイル内容や所有者、グループはコピーされない                                                              |
| `shutil.copystat(src, dst)`      |                                              |                                      |                                                                                                             |
| `shutil.copytree(src, dst)`      | src を起点としたディレクトリツリー           | `dirs_exist_ok=False` ならば `Error` | `dst` には既存のディレクトリは指定できない（存在しない親ディレクトリも含めて作成される）                    |
|                                  |                                              |                                      | パーミッションと時刻は `copystat()` 関数で、個々のファイルは `shutil.copy2()` でコピーされる                |

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
```

> ./test-copy2.txt


#### ディレクトリツリーをコピー(copytree)

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
> './test-dirtree/',
>
> './test-dirtree/dir1',
>
> './test-dirtree/dir1/file1.txt',
>
> './test-dirtree/dir2',
>
> './test-dirtree/dir2/file1.txt'
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


#### ファイル形式のオブジェクトをコピー(copyfileobj)

```py
import os
import shutil
import requests


def download(url):
    file_name = os.path.basename(url)
    res = requests.get(url, stream=True)
    if res.status_code == 200:
        with open(file_name, 'wb') as file:
            res.raw.decode_content = True
            shutil.copyfileobj(res.raw, file)


if __name__ == '__main__':
    url = 'https://example.net/logo.png'
    download(url)
```


### ファイル・フォルダをリネーム

| 項目                   | 内容                                             | `dst` が既存                                         | 備考                                                                             |
| ---------------------- | ------------------------------------------------ | ---------------------------------------------------- | -------------------------------------------------------------------------------- |
| `os.rename(src, dst)`  | ファイルまたはディレクトリ src を dst に名前変更 | ディレクトリの場合、 `OSError`                       |                                                                                  |
|                        |                                                  | ファイルの場合、置換(Unix)または `OSError` (Windows) |                                                                                  |
| `os.renames(old, new)` | 再帰的にディレクトリやファイル名を変更           |                                                      | 新たなパス名を持つファイルを配置するために必要な途中のディレクトリ構造をまず作成 |

#### os.rename

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
glob('./test-rename/**', recursive=True)

os.rename(srcpath, dstpath)
glob('./test-rename/**', recursive=True)

touch(srcpath)
glob('./test-rename/**', recursive=True)

os.rename(srcpath, dstpath) # dstpathのファイルが既に存在すると、上書きされる
glob('./test-rename/**', recursive=True)
```

> ['./test-rename/', './test-rename/file1.txt']
>
> ['./test-rename/', './test-rename/file2.txt']
>
> ['./test-rename/', './test-rename/file1.txt', './test-rename/file2.txt']
>
> ['./test-rename/', './test-rename/file2.txt'] \# dstpath のファイルが既に存在すると、上書きされる

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

#### shutil.move

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
[os.remove(f) for f in glob('./test-remove/*.txt')]

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


#### テキストファイル

##### モード

| mode | 読み込み | 書き込み | ファイルポインタ | 既存ファイルが存在する | 既存ファイルが存在しない |
| ---- | -------- | -------- | ---------------- | ---------------------- | ------------------------ |
| r    | ○        | ×        | 先頭             | ○                      | FileNotFoundError        |
| x    |          |          | 先頭             | FileExistsError        | 新規作成                 |
| w    | ×        | ○        | 先頭             | ○                      | 新規作成                 |
| a    | ×        | ○        | 終端             | ○                      | 新規作成                 |
| r+   | ○        | ○        | 先頭             | ○                      | FileNotFoundError        |
| w+   | ○        | ○        | 先頭             | ○                      | 新規作成                 |
| a+   | ○        | ○        | 終端             | ○                      | 新規作成                 |

r+ 読み書き両用。
ファイルがない場合はエラー。
w+ 読み書き両用。
ファイルがある場合は「w」と同じ処理。
a+ 追記・読み書き両用。
ファイルがない場合は新規作成。

##### 文字コードの推測

ファイルの文字エンコーディングが OS 標準のものと異なる場合はエラーとなるため、Web から入手したファイルなど文字コードが不明のファイルを読み込む際には、推測する必要がある

```py
import codecs
import os

def detect_encode(filepath):
    cs = [
        'utf-8',
        'utf_8_sig',
        'euc_jp',
        'cp932',
        #
        'euc_jis_2004',
        'euc_jisx0213',
        'iso2022_jp_1',
        'iso2022_jp_2',
        'iso2022_jp_3',
        'iso2022_jp_2004',
        'iso2022_jp_ext',
        'iso2022_jp',
        'shift_jis_2004',
        'shift_jis',
        'shift_jisx0213',
        'utf_7',
        'utf_16_be',
        'utf_16_le',
        'utf_16',
    ]

    for c in cs:
        try:
            with codecs.open(filepath, 'r', c, errors='strict') as f:
                print(f.read())
                return c
        except Exception as e:
            continue
    return None

c = detect_encode(os.path.join('test-fileio', 'inputsjis.txt'))
print(c)
```

> cp932

###### エラーハンドラ

| 値       | 意味                                                                                                                  |
| -------- | --------------------------------------------------------------------------------------------------------------------- |
| 'strict' | UnicodeError (または、そのサブクラス) を送出します。これがデフォルトの動作です。 strict_errors() で実装されています。 |
| 'ignore' | 不正な形式のデータを無視し、何も通知することなく処理を継続します。ignore_errors() で実装されています。                |

ユニコード文字列をエンコードするコーデックでのみ有効な値:

| 値                  | 意味                                                                                                                                                                                                                                  |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 'replace'           | 適当な置換マーカーで置換します。Python では、組み込み codec のデコード時には公式の U+FFFD 代替文字が、エンコード時には '?' が使用されます。 replace_errors() で実装されています。                                                     |
| 'xmlcharrefreplace' | 適切な XML 文字参照で置換します (エンコードのみ)。 xmlcharrefreplace_errors() で実装されています。                                                                                                                                    |
| 'backslashreplace'  | バックスラッシュつきのエスケープシーケンスで置換します。 backslashreplace_errors() で実装されています。                                                                                                                               |
| 'namereplace'       | \N{...} エスケープシーケンスで置換します (エンコードのみ)。 namereplace_errors() で実装されています。                                                                                                                                 |
| 'surrogateescape'   | デコード時には、バイト列を U+DC80 から U+DCFF の範囲の個々のサロゲートコードで置き換えます。データのエンコード時に 'surrogateescape' エラーハンドラが使用されると、このコードは同じバイト列に戻されます。 (詳しくは PEP 383 を参照。) |

`utf-8, utf-16, utf-32, utf-16-be, utf-16-le, utf-32-be, utf-32-le` でのみ有効な値:

| 値              | 意味                                                                                                                   |
| --------------- | ---------------------------------------------------------------------------------------------------------------------- |
| 'surrogatepass' | サロゲートコードのエンコードとデコードを許可します。通常、これらの codecc は、サロゲートの存在をエラーとして扱います。 |

###### cChardet モジュールを使用

chardet モジュールだと `windows-1252` と判定されがちなので [cChardet](https://github.com/PyYoshi/cChardet) モジュールを利用する

```py
import cchardet

def detect_enc(filepath):
    with open(filepath, mode='rb') as f:
        return cchardet.detect(f.read())

print(detect_enc('./test-fileio/inputsjis.txt'))
```

> {'encoding': 'SHIFT_JIS', 'confidence': 1.0}

##### 読み込み

###### 単一の文字列として読み込み(r: 読み取り)

mode が `'r'` の場合、指定したパスにファイルが存在しない場合はエラーとなる

```py
import os
with open('NOT.FOUND', 'r') as file:
    file.read()
```

> FileNotFoundError

```py
import os

filepath = './NOT.FOUND'
if os.path.exists(os.path.dirname(os.path.abspath(filepath))):
    if os.path.exists(os.path.abspath(filepath)):
        with open(filepath, 'r') as file:
            file.write('')
    else:
        print('File Not Found')
else:
    print('Directory Not Found')
```

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

####### UTF-8 BOM なし

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
?あいうえお8XkfWDHyFdcB52MbTNNswDnFRAsZdEgRmmsaNktD
かきくけこxahfE6WkxNFpU-4KgnJ4jS2jZUyWf9spDbKRaFyC
```

####### UTF-8 BOM あり

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

###### 1 行ずつ読み込み(r: 読み取り)

```py
import os
with open(os.path.join('test-fileio', 'inpututf8.txt'), 'r', encoding='utf_8') as file:
    string = file.readline()
    while string:
        print(string)
        string = file.readline()
```

###### リストへ格納(r: 読み取り)

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

##### 書き込み

- mode が `'a'` の場合、指定したパスにファイルが存在する場合は追記、存在しない場合は新規作成、親フォルダが存在しない場合はエラーとなる

```py
import os
with open('PATH/NOT/FOUND', 'a') as file:
    file.write('')
```

> FileNotFoundError

- mode が `'r+'` の場合、読み書きモードで開く(ファイルポインタが先頭)

- mode が `'w'` の場合、指定したパスにファイルが存在する場合は上書き、存在しない場合は新規作成、親フォルダが存在しない場合はエラーとなる

```py
import os
with open('PATH/NOT/FOUND', 'w') as file:
    file.write('')
```

> FileNotFoundError

- mode が `'ｘ'` の場合、指定したパスにファイルが既に存在する場合はエラーとなる

```py
import os
with open(os.path.join('test-fileio', 'outpututf8.txt'), 'x') as file:
    file.write('')
with open(os.path.join('test-fileio', 'outpututf8.txt'), 'x') as file:
    file.write('')
```

> FileExistsError

###### 単一の文字列として書き込み(x: 新規作成)

```py
import os
string = 'foobar\nhoge\n'
with open(os.path.join('test-fileio', 'outpututf8.txt'), 'x', encoding='utf_8') as file:
    file.write(string)
```

> 11

###### リストを書き込み(x: 新規作成)

```py
import os
lst = ['foobar', 'hoge']
with open(os.path.join('test-fileio', 'outpututf8.txt'), 'x', encoding='utf_8') as file:
    file.writelines(lst) # 要素間には空白文字等は挿入されない
```

###### 単一の文字列として書き込み(w: 新規作成／上書き)

```py
import os
string = 'foobar\nhoge\n'
with open(os.path.join('test-fileio', 'outpututf8.txt'), 'w', encoding='utf_8') as file:
    file.write(string)
```

> 11

###### 既存ファイルが存在するときに上書きするか確認する

```py
import os
string = 'foobar\nhoge\n'

if os.path.exists(os.path.join('test-fileio', 'outpututf8.txt')):
    while True:
        answer = input('Overwrite?: (y/n)').lower()
        if answer == 'y':
            with open(os.path.join('test-fileio', 'outpututf8.txt'), 'w') as file:
                file.write(string)
            break
        elif answer == 'n':
            break
else:
    print('File Not Found')
```

###### リストを書き込み(w: 新規作成／上書き)

```py
import os
lst = ['foobar', 'hoge']
with open(os.path.join('test-fileio', 'outpututf8.txt'), 'w', encoding='utf_8') as file:
    file.writelines(lst) # 要素間には空白文字等は挿入されない
```

###### 単一の文字列として書き込み(a: 追記)

```py
import os
string = 'foobar\nhoge\n'
with open(os.path.join('test-fileio', 'outpututf8.txt'), 'a', encoding='utf_8') as file:
    file.write(string)
```

###### リストを書き込み(a: 追記)

```py
import os
lst = ['foobar', 'hoge']
with open(os.path.join('test-fileio', 'outpututf8.txt'), 'a', encoding='utf_8') as file:
    file.writelines(lst) # 要素間には空白文字等は挿入されない
```


#### csv ファイル

##### 読み込み

Windows 環境の場合は、明示的に UTF-8 を指定しないと SJIS として読み書きされる

###### リストに格納(csv.reader)

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

> 1, 2, 3
> 4, 5, 6
> 7, 8, 9

###### 辞書に格納(csv.DictReader)

```py
import csv
import os

with open(os.path.join('test-fileio', 'inputsjis.csv'), encoding='shift_jis', newline='') as csvfile:
    f = csv.DictReader(csvfile, delimiter=',', quotechar='"')
    l = [row for row in f]
    print(l)

# 1行目がヘッダでない場合は、fieldnamesにヘッダ項目を指定する
with open(os.path.join('test-fileio', 'inputsjis.csv'), encoding='shift_jis', newline='') as csvfile:
    f = csv.DictReader(csvfile, fieldnames=['h1', 'h2', 'h3'])
    for row in f:
        print(row)

# 1列目がデータではない場合(IDなど)
fieldnames = ['h1', 'h2', 'h3']
with open(os.path.join('test-fileio', 'inpututf8.csv'), encoding='utf_8', newline='') as csvfile:
    f = csv.DictReader(csvfile, fieldnames=fieldnames)
    l = [row for row in f]

print([m.pop(fieldnames[0]) for m in l])
print(l)
```

> [{'1': '4', '2': '5', '3': '6'}, {'1': '7', '2': '8', '3': '9'}]

> \# 1 行目がヘッダでない場合は、fieldnames にヘッダ項目を指定する
>
> {'h1': '1', 'h2': '2', 'h3': '3'}
>
> {'h1': '4', 'h2': '5', 'h3': '6'}
>
> {'h1': '7', 'h2': '8', 'h3': '9'}

> \# 1 列目がデータではない場合(ID など)
>
> [{'h2': '2', 'h3': '3'}, {'h2': '5', 'h3': '6'}, {'h2': '8', 'h3': '9'}]

###### メモリ上の csv 文字列の読み込み

```py
import csv
from io import StringIO

csv_str = """
1-1,1-2,1-3
2-1,2-2,"2-3-1
2-3-2"
"""

# sio = StringIO(csv_str.strip())

# try:
#     # 区切り文字を判別
#     dialect = csv.Sniffer().sniff(sio.readline())
# except:
#     dialect = csv.excel

# sio.seek(0)

for row in csv.reader(StringIO(csv_str.strip())):
    print(row)

```

> ['1-1', '1-2', '1-3']
>
> ['2-1', '2-2', '2-3-1\n2-3-2']

##### 書き込み

###### 上書き(mode:w)

```py
import csv

# リストを1行ずつ書き込み
with open(os.path.join('test-fileio', 'outpututf8.csv'), 'w', encoding='utf_8', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    # delimiter='\t'とすればタブ区切り(tsv)
    # quoting=csv.QUOTE_ALLとすれば区切り文字などを含まない要素もquotecharで囲まれ、
    # quoting=csv.QUOTE_NONNUMERICとすれば数値以外が囲まれる
    spamwriter.writerow(['foo', 'bar', 'hoge'])
    spamwriter.writerow(['foo', 'bar', 'hoge'])

# 2次元配列を一括書き込み
with open(os.path.join('test-fileio', 'outpututf8.csv'), 'w', encoding='utf_8', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['foo', 'bar', 'hoge'])
    spamwriter.writerows([['foo', 'bar'],['hoge', 'piyo']]) # 2次元配列

# 辞書の値を書き込み
dct1 = {'h1': 1, 'h2': 2, 'h3': 3, 'h4': 4, 'h5': 5}

with open(os.path.join('test-fileio', 'outpututf8.csv'), 'w', encoding='utf_8', newline='') as csvfile:
    spamwriter = csv.DictWriter(csvfile, ['h1', 'h2', 'h3', 'h4', 'unknownkey', 'h5']) # ['h1', 'h2', 'h3', 'h5']のように、不足している場合はwriterowでValueError
    spamwriter.writeheader()
    spamwriter.writerow(dct1)

# 辞書の値を書き込み(fieldnamesに指定した以外のキーを無視)
with open(os.path.join('test-fileio', 'outpututf8.csv'), 'w', encoding='utf_8', newline='') as csvfile:
    spamwriter = csv.DictWriter(csvfile, ['h1', 'h2', 'h3', 'h5'], extrasaction='ignore')
    spamwriter.writeheader()
    spamwriter.writerow(dct1)

# 辞書の配列を書き込み
dct1 = {'h1': 1, 'h2': 2, 'h3': 3, 'h4': 4, 'h5': 5}
dct2 = {'h1': 11, 'h2': 12, 'h3': 13, 'h5': 15}
with open(os.path.join('test-fileio', 'outpututf8.csv'), 'w', encoding='utf_8', newline='') as csvfile:
    spamwriter = csv.DictWriter(csvfile, dct1.keys())
    spamwriter.writeheader()
    spamwriter.writerows([dct1,dct2])
```

> \# 1 行ずつ書き込み
>
> 14
>
> 14

> \# 2 次元配列を一括書き込み
>
> foo,bar,hoge
>
> foo,bar
>
> hoge,piyo

> \# 辞書の値を書き込み
>
> h1,h2,h3,h4,unknownkey,h5
>
> 1,2,3,4,,5

> \# 辞書の値を書き込み(fieldnames に指定した以外のキーを無視)
>
> h1,h2,h3,h5
>
> 1,2,3,5

> \# 辞書の配列を書き込み
>
> h1,h2,h3,h4,h5
>
> 1,2,3,4,5
>
> 11,12,13,,15

###### 追記(mode:a)

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


#### tsv ファイル

###### メモリ上の tsv 文字列の読み込み

```py
import csv
from io import StringIO

csv_str = """
1-1\t1-2\t1-3
2-1\t2-2\t"2-3-1
2-3-2"
"""

for row in csv.reader(StringIO(csv_str.strip()), csv.excel_tab):
    print(row)

```

> ['1-1', '1-2', '1-3']
>
> ['2-1', '2-2', '2-3-1\n2-3-2']


#### json ファイル


##### スクリプトを書かず、json.tool で解析する

```sh
$ python -m json.tool ./test-fileio/inpututf8.json
```


##### 読み込み

`json.load()` にはファイルオブジェクトを指定、 `json.loads()` 文字列またはバイト列を指定する


##### ファイルから読み込み

```py
import json
import os

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
    'key1':'val1',
    'key2':'val2'
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
    'key1':'val1',
    'key2':'val2'
}
'''

decoder = json.jsonDecoder(object_pairs_hook=collections.OrderedDict)
print(decoder.decode(json_str))
```

> OrderedDict([('key1', 'val1'), ('key2', 'val2')])


##### 要素の読み込み

```py
import json

json_str = '''
{
    'key1':'val1',
    'key2':{
        'key2-1':'val2-1',
        vkey2-2':'val2-2'
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


###### 要素の検索

```py
import json
import os

def search(arg, cond):
    res =[]
    if cond(arg):
        res.append(arg)
    if isinstance(arg, list):
        for item in arg:
            res += search(item, cond)
    elif isinstance(arg, dict):
        for value in arg.values():
            res += search(value, cond)
    return res

def is_valid_value(arg):
    if isinstance(arg, str):
        return 'val3-' in arg
    if isinstance(arg, dict):
        return arg.keys() == {'key5-1', 'key5-2'}

with open(os.path.join('test-fileio', 'inpututf8nest.json'), encoding='utf-8') as f:
    json_str = json.load(f)
    result = search(json_str, is_valid_value)
    print(result)
```

> ['val3-1', 'val3-2', {'key5-1': 'val5-1', 'key5-2': 'val5-2'}]


##### 要素の追加

```py
import json
import os

with open(os.path.join('test-fileio', 'inpututf8.json'), 'r', encoding='utf_8') as file:
    json_dict = json.load(file)
    json_dict['key3'] = 'added'
    print('{}'.format(json_dict))
```

> {'key1': 'val1', 'key2': 'val2', 'key3': 'added'}


##### 要素の置換

```py
import json
import os

with open(os.path.join('test-fileio', 'inpututf8.json'), 'r', encoding='utf_8') as file:
    json_dict = json.load(file)
    json_dict['key1'] = 'replaced'
    print('{}'.format(json_dict))
```

> {'key1': 'replaced', 'key2': 'val2'}


##### 要素の削除

```py
import json
import os

with open(os.path.join('test-fileio', 'inpututf8.json'), 'r', encoding='utf_8') as file:
    json_dict = json.load(file)
    json_dict.pop('key1')
    print('{}'.format(json_dict))
```

> 'val1'
>
> {'key2': 'val2'}


##### ファイルに書き込み

`json.dump()` でファイル出力、 `json.dumps()` で文字列出力する


##### ファイルに書き込み

`json.dump()` でファイル出力、 `json.dumps()` で文字列出力する

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


##### 文字列として出力

```py
import json
import os

with open(os.path.join('test-fileio', 'inpututf8.json'), 'r', encoding='utf_8') as file:
    json_dict = json.load(file)

    jsonstr = json.dumps(json_dict)
    # Unicodeエスケープせずに出力
    jsonstr = json.dumps(json_dict, ensure_ascii=False)
    # 区切り文字を変更して出力
    jsonstr = json.dumps(json_dict, separators=(';', '='))
    # インデント幅を変更して出力
    jsonstr = json.dumps(json_dict, indent=8)
    # キーでソートして出力
    jsonstr = json.dumps(json_dict, sort_keys=True)

    print(jsonstr)
```

> {"key1": "val1", "key2": "val2"}


##### datetime 型を出力する

```py
import json
from datetime import date, datetime

def json_serial(obj):
    if isinstance(obj, (datetime, date)):
        return obj.isoformat() # ISO形式の文字列に変換
    raise TypeError ("Type %s not serializable" % type(obj))

# datetime型を含むdict
item = { "run_at" : datetime.now() }

# default引数を指定して、JSON文字列を生成します
jsonstr = json.dumps(item, default=json_serial)
print(jsonstr)
```

> {"run_at": "2020-01-27T08:15:26.848402"}


#### XML ファイル

##### ファイルから一括読み込み

```py
import os
import xml.etree.ElementTree as ET

filepath = os.path.join('test-fileio', 'inpututf8.xml')
tree = ET.parse(filepath)

# root要素を取得
root = tree.getroot()
print(root.tag)
print(dir(root))

# 子要素を取得
for child in root:
    print(child.tag, child.attrib)
```

> breakfast_menu
>
> ['__class__', '__copy__', '__deepcopy__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'attrib', 'clear', 'extend', 'find', 'findall', 'findtext', 'get', 'getchildren', 'getiterator', 'insert', 'items', 'iter', 'iterfind', 'itertext', 'keys', 'makeelement', 'remove', 'set', 'tag', 'tail', 'text']

> food {'title': '001'}
>
> food {'title': '002'}
>
> food {'title': '003'}
>
> food {'title': '004'}
>
> food {'title': '005'}

##### ファイルから逐次的に読み込み

```py
import os
import xml.etree.ElementTree as ET

filepath = os.path.join('test-fileio', 'inpututf8.xml')
for event, elem in ET.iterparse(filepath):
    print(event, elem.tag)
    elem.clear()
```

##### 文字列から読み込み

```py
import os
import xml.etree.ElementTree as ET

# <?xml version="1.0" encoding="UTF-8"?>
xml_str = '''<?xml version="1.0" encoding="UTF-8"?>
<note>
  <to>Tove</to>
  <from>Jani</from>
  <heading>Reminder</heading>
  <body>Don't forget me this weekend!</body>
</note>
'''

# root要素を取得
root = ET.fromstring(xml_str)
print(root.tag)
print(root.text)

# 子要素を取得
for child in root:
    print(child.tag, child.attrib)

# 指定した名前の要素を取得
for name in root.iter('from'):
    print(name.text)

# 指定したインデックスの要素を取得
print(root[0].text)
print(root[1].text)
```

> note

> to {}
>
> from {}
>
> heading {}
>
> body {}

> Jani

> Tove
>
> Jani

##### 書き込み

```py
import os
import xml.etree.ElementTree as ET

inputfilepath = os.path.join('test-fileio', 'inpututf8.xml')
outputfilepath = os.path.join('test-fileio', 'outpututf8.xml')

tree = ET.parse(inputfilepath)

# root要素を取得
root = tree.getroot()
print(root.tag)
print(dir(root))

# 何らかの加工処理
for child in root:
  child.text = 'replaced'

# ファイルに書き込み
tree.write(outputfilepath, encoding='UTF-8')
```


#### ARFF ファイル

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


#### ini ファイル

- config.ini

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


#### Markdown ファイル

```sh
$ pip install Markdown
```

```py
import markdown

markdown_text_string = '''
# Title

Lorem ipsum dolor sit amet, vix no mutat dicunt, movet petentium iudicabit at vim.

- one
- two
- three

'''

# モジュールとして利用
html = markdown.markdown(markdown_text_string)

# 文字列ごとに新しいインスタンスを作成せずに複数の文字列を処理する場合
md = markdown.Markdown()
html1 = md.convert(markdown_text_string)
html2 = md.reset().convert(markdown_text_string)
```

> '<h1>Title</h1>\n<p>Lorem ipsum dolor sit amet, vix no mutat dicunt, movet petentium iudicabit at vim.</p>\n<ul>\n<li>one</li>\n<li>two</li>\n<li>three</li>\n</ul>'

##### ファイル入出力

```py
import codecs
import markdown

with codecs.open('./test-fileio/input.md', mode='r', encoding='utf-8') as fi:
    text = fi.read()
    html = markdown.markdown(text)
    print(html)

with codecs.open('./test-fileio/output.md.html', 'w', encoding='utf-8', errors='xmlcharrefreplace') as fo:
    fo.write(html)
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


#### zip ファイル

##### zip ファイル圧縮

###### shutil を使ってフォルダごと圧縮

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

> \# base_dir を指定しない
>
> '/mnt/c/Users/y/Documents/GitHub/Python-cheatsheet/test-archive/archive.zip'
>
> ['dir2/', 'file1.txt', 'dir2/file2.txt']

> \# base_dir を指定する
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



with zipfile.ZipFile(archive_path, 'w', compression=zipfile.zip_DEFLATED) as z:
    z.write(srcdpath1, arcname=srcdpath1)
    z.write(srcdpath2, arcname=srcdpath2)
    z.write(srcfpath1, arcname=srcfpath1)

with zipfile.ZipFile(archive_path) as zip_contents:
    print(zip_contents.namelist())

# 既存の圧縮ファイルがある場合は圧縮ファイル自体が上書きされる
with zipfile.ZipFile(archive_path, 'w', compression=zipfile.zip_DEFLATED) as z:
    z.write(srcdpath1, arcname=srcdpath1)
    z.write(srcdpath2, arcname=srcdpath2)
    z.write(srcfpath2, arcname=srcfpath2)

with zipfile.ZipFile(archive_path) as zip_contents:
    print(zip_contents.namelist())

# 既存の圧縮ファイルに、ファイルを追加する
with zipfile.ZipFile(archive_path, 'a', compression=zipfile.zip_DEFLATED) as z:
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
>
> > 'test-archive/dir1/',
> > 'test-archive/dir1/dir2/',
> > 'test-archive/dir1/dir2/file2.txt',
> > 'test-archive/dir1/',
> > 'test-archive/dir1/dir2/',
> > 'test-archive/dir1/file1.txt',
> > 'test-archive/dir1/dir2/file2.txt'
> > ]

##### zip ファイル解凍

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


## ネットワーク

### URL 文字列の操作

#### URL エンコーディング

```py
from urllib import parse

# エンコード
print(parse.quote('検索クエリ', encoding='utf-8'))

# デコード
print(parse.unquote('%E6%A4%9C%E7%B4%A2%E3%82%AF%E3%82%A8%E3%83%AA', encoding='utf-8'))
```

> %E6%A4%9C%E7%B4%A2%E3%82%AF%E3%82%A8%E3%83%AA
>
> 検索クエリ

##### 変換対象の文字の違いと利用する関数

```py
print(urllib.parse.quote('+ /'))
print(urllib.parse.quote_plus('+ /'))
print(urllib.parse.quote_plus('+ /', safe='+/'))
```

> %2B%20/
>
> %2B+%2F
>
> ++/

```py
print(urllib.parse.unquote('a+b'))
print(urllib.parse.unquote_plus('a+b'))
```

> a+b
>
> a b

##### URL の一部の要素に日本語が含まれている場合

```py
from urllib.parse import urlparse
import urllib.request

url = 'https://httpbin.org/get/?q=日本語'
p = urlparse(url)
url = '{}://{}{}{}{}{}{}{}{}'.format(
    p.scheme, p.netloc, p.path,
    ';' if p.params else '', p.params,
    '?' if p.query else '', urllib.parse.quote_plus(p.query, safe='=&'),
    '#' if p.fragment else '', p.fragment)
print(url)
response = urllib.request.urlopen(url)
```

#### URL 文字列のパース

```py
from urllib import parse

parts = parse.urlparse('https://example.net/user?id=12345&pw=678&q='+'%E6%A4%9C%E7%B4%A2%E3%82%AF%E3%82%A8%E3%83%AA')
print(parts)
print(parts.path)
print(parse.parse_qs(parts.query))

```

> ParseResult(scheme='https', netloc='example.net', path='/user', params='', query='id=12345&pw=678&q=%E6%A4%9C%E7%B4%A2%E3%82%AF%E3%82%A8%E3%83%AA', fragment='')
>
> /user
>
> {'id': ['12345'], 'pw': ['678'], 'q': ['検索クエリ']}

#### URL 文字列の組み立て

```py
from urllib import parse

new_query = parse.urlencode({'id': ['12345'], 'pw': ['678'], 'q': ['検索クエリ']}, True)
print(new_query)


parts = parse.urlparse('https://example.net/user?id=12345&pw=678&q='+'%E6%A4%9C%E7%B4%A2%E3%82%AF%E3%82%A8%E3%83%AA')
print(parts)
new_url = parse.ParseResult(parts.scheme, parts.netloc, parts.path, parts.params, new_query, parts.fragment).geturl()
print(new_url)
```

> id=12345&pw=678&q=%E6%A4%9C%E7%B4%A2%E3%82%AF%E3%82%A8%E3%83%AA
>
> ParseResult(scheme='https', netloc='example.net', path='/user', params='', query='id=12345&pw=678&q=%E6%A4%9C%E7%B4%A2%E3%82%AF%E3%82%A8%E3%83%AA', fragment='')
>
> https://example.net/user?id=12345&pw=678&q=%E6%A4%9C%E7%B4%A2%E3%82%AF%E3%82%A8%E3%83%AA

### リクエストを送信

`urllib` モジュールではなく `Requests` モジュールを利用する場合、以下のコマンドでインストールする

```sh
$ pip install requests
```

#### コンテンツを文字列として取得

```py
import urllib.request
url = 'http://httpbin.org'

try:
    with urllib.request.urlopen(url) as response:
        html = response.read()
        print(html)
except urllib.error.HTTPError as e:
    print(e.code)
    print(e.read())
```

```py
import urllib.request
url = 'http://httpbin.org'
req = urllib.request.Request(url) # , method='GET')

try:
    with urllib.request.urlopen(req) as response:
        html = response.read()
        print(html)
except urllib.error.HTTPError as e:
    print(e.code)
    print(e.read())
```

```py
import requests
url = 'http://httpbin.org'
response = requests.get(url)
print(response.text)
```

#### 文字コードを指定

##### 特定の文字コード(Shift-JIS)を指定

```py
import urllib.request
url = 'http://www.soumu.go.jp/'

try:
    with urllib.request.urlopen(url) as response:
        html = response.read().decode('shift_jis')
        print(html)
except urllib.error.HTTPError as e:
    print(e.code)
    print(e.read())
```

```py
import requests
url = 'http://www.soumu.go.jp/'
response = requests.get(url)
if response.status_code == 200:
    response.encoding = 'Shift_JIS'
    print(response.text)
```

##### コンテンツの内容から文字コードを推定する

###### chardet による推定

```py
import requests
url = 'http://www.soumu.go.jp/'
response = requests.get(url)
if response.status_code == 200:
    response.encoding = response.apparent_encoding
    print(response.text)
```

###### cChardet による推定(chardet よりも高速)

```sh
$ pip install cchardet
```

```py
import cchardet
import requests
url = 'http://www.soumu.go.jp/'
response = requests.get(url)
if response.status_code == 200:
    response.encoding = cchardet.detect(response.content)['encoding']
    print(response.text)
```

#### コンテンツをテンポラリファイルとして取得

```py
import urllib.request
url = 'http://httpbin.org/get'
local_filename, headers = urllib.request.urlretrieve(url)
with open(local_filename) as f:
    string = f.read()

print(local_filename)
```

> C:\\Users\\y\\AppData\\Local\\Temp\\tmptkscpwv4

#### バイナリファイルを保存

```py
import os
import urllib.request
url = 'http://httpbin.org/image'
with urllib.request.urlopen(url) as response:
    with open(os.path.basename(url), 'wb') as localfile:
        localfile.write(response.read())
```

> 8090

```py
import os
import requests
url = 'https://www.python.org/static/img/python-logo.png'

def download_img(url, file_name):
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(file_name, 'wb') as f:
            f.write(r.content)

download_img(url, os.path.basename(url))
```

##### 画像ファイルの保存

```sh
$ pip install Image requests StringIO
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

##### 大容量ファイルの保存

```py
import os
import requests
url = 'https://www.python.org/static/img/python-logo.png'
r = requests.get(url, stream=True)
if r.status_code == 200:
    with open(os.path.basename(url), 'wb') as file:
        for chunk in r.iter_content(chunk_size=1024):
            file.write(chunk)
```

#### GET

```py
import urllib.parse
import urllib.request

url = 'http://httpbin.org/get'

with urllib.request.urlopen(url) as response:
    html = response.read()
    print(html)

# クエリを送信
params = {}
params['name'] = 'Sato'
params['location'] = 'Tokyo'
params['age'] = '30'
query = urllib.parse.urlencode(params)
url = url + '?' + query

with urllib.request.urlopen(url) as response:
    html = response.read()
    print(html)
```

```py
import requests
url = 'http://httpbin.org/get'
r = requests.get(url)
print(r.text)

# クエリを送信
import requests
r = requests.get('http://httpbin.org/get', params={'key':'value'})
print(r.url) # http://httpbin.org/get?key=value
print(r.text)

# 応答
import requests
url = 'http://httpbin.org/get'
r = requests.get(url)

print(r.headers)

print(r.text)

print(r.status_code)  # レスポンスコード
print(r.status_code == requests.codes.ok)  # 200か判定

r.raise_for_status() # エラー時に例外を発生させる
# requests.exceptions.HTTPError

print(r.encoding)  # 文字エンコードの確認
r.encoding = 'Shift-JIS'  # 文字コードの設定(変更)
print(r.text)  # 変更後のエンコーディングが使用される

# リダイレクト
import requests
url = 'http://httpbin.org/get'
# r = requests.get(url, allow_redirects=True)
r = requests.get(url)
print(r.history) # リダイレクト結果を確認する

r = requests.get(url, allow_redirects=False) # リダイレクトさせない
print(r.text)

# タイムアウト
import requests
url = 'https://httpbin.org/deley/5'
r = requests.get(url, timeout=1)
print(r.text)

# JSON
import json
import requests
url = 'http://httpbin.org/json'
r = requests.get(url)
data = r.json()
print(json.dumps(data, indent=4))
```

#### POST

```py
import urllib.parse
import urllib.request

url = 'http://httpbin.org/post'

params = {'name': 'Sato', 'location': 'Tokyo',  'age': '30'}

req = urllib.request.Request(url, urllib.parse.urlencode(params).encode('ascii')) # , method='POST')
with urllib.request.urlopen(req) as response:
    html = response.read()
    print(html)
```

```py
import requests

params = {'name': 'Sato', 'location': 'Tokyo',  'age': '30'}
r = requests.post('http://httpbin.org/post', data=params)
print(r.url)  # 生成されたURL(POSTなのでクエリ文字列がないことを確認)

import json
print(json.loads(res.content.decode())['form']) # {'age': '30', 'location': 'Tokyo', 'name': 'Sato'}
```

##### フォーム送信(Multipart エンコード)

```py
import requests
url = 'http://httpbin.org/post'
files = {'file': open('test.png', 'rb')}
r = requests.post(url, files=files)

import requests
url = 'http://httpbin.org/post'
files = {'file': ('test.png', open('test.png', 'rb'))}
r = requests.post(url, files=files)

import requests
url = 'http://httpbin.org/post'
files = {'file': ('test.txt', 'foobar')}
r = requests.post(url, files=files)
```

#### PUT

```py
import requests
url = 'http://httpbin.org/put'
r = requests.put(url)
```

#### DELETE

```py
import requests
url = 'http://httpbin.org/delete'
r = requests.delete(url)
```

#### HEAD

```py
import requests
url = 'http://httpbin.org/get'
r = requests.head(url)
```

#### HTTP ヘッダ

```py
import urllib.parse
import urllib.request

url = 'http://httpbin.org/headers'

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/xxx.xx (KHTML, like Gecko) Chrome/xx.x.xxxx.xx Safari/xxx.xx'
headers = {'User-Agent': user_agent} # ユーザーエージェント

params = {'name': 'Sato', 'location': 'Tokyo',  'age': '30'}

# headers引数
req = urllib.request.Request(url, data=urllib.parse.urlencode(params).encode('ascii'), method='GET', headers=headers)
with urllib.request.urlopen(req) as response:
    html = response.read()
    print(html)

# add_header()
req = urllib.request.Request(url, data=query.encode('ascii'), method='GET')
req.add_header('Referer', 'http://httpbin.org/')
with urllib.request.urlopen(req) as response:
    html = response.read()
    print(html)
```

```py
import requests
url = 'http://httpbin.org/headers'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/xxx.xx (KHTML, like Gecko) Chrome/xx.x.xxxx.xx Safari/xxx.xx'
headers = {'User-Agent': user_agent, 'Referer': 'http://httpbin.org/'}

payload = {'key1': 'val1', 'key2': 'val2'}

r = requests.get(url, data=json.dumps(payload), headers=headers)
print(r.status_code)
print(r.content)
```

#### BASIC 認証

```py
import urllib.request
import getpass

url = 'http://httpbin.org/basic-auth/Username/Password'
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

#### 応答ヘッダ・リダイレクト先 URL

```py
import urllib.parse
import urllib.request

url = 'http://httpbin.org/'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/xxx.xx (KHTML, like Gecko) Chrome/xx.x.xxxx.xx Safari/xxx.xx'
headers = {'User-Agent': user_agent}

params = {'name': 'Sato', 'location': 'Tokyo',  'age': '30'}

req = urllib.request.Request(url, urllib.parse.urlencode(params).encode('ascii'), headers) # , method='POST')
with urllib.request.urlopen(req) as response:
    url = response.geturl()
    headers = response.info()
    print(headers)
    # charset=req.info().get_content_charset() # 応答ヘッダから文字コードを取得してデコードする例
    # content=req.read().decode(charset)
```

#### セッション

```py
import requests

session = requests.Session()
r1 = session.get('http://httpbin.org/cookies/set/key1/value1')
r2 = session.get('http://httpbin.org/cookies')
print(r2.text)
```

> {
>
> "cookies": {
>
>     "key1": "value1"
>
> }
>
> }

```py
import requests

session = requests.Session()

# 共通する項目を設定
session.auth = ('Username', 'Password')
session.headers.update({'x-key0': 'value0'})

r = session.get('http://httpbin.org/headers', headers={'x-key1': 'value1'})
print(r.text)

# 個別項目を設定
r = session.get('http://httpbin.org/headers', headers={'x-key2': 'value2'})
print(r.text)
```

```json
{
  "headers": {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Host": "httpbin.org",
    "User-Agent": "python-requests/2.22.0",
    "X-Key0": "value0",
    "X-Key1": "value1"
  }
}

{
  "headers": {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Host": "httpbin.org",
    "User-Agent": "python-requests/2.22.0",
    "X-Key0": "value0",
    "X-Key2": "value2"
  }
}
```

#### Cookie

```py
import requests

# 設定
url = 'http://httpbin.org/get'
cookies = dict(key1='val1')
r = requests.get(url, cookies=cookies)

# 取得
url = 'http://httpbin.org/cookies/set/key1/value1'
r = requests.get(url)
r.cookies['key1']  # Cookieが存在する場合は非None
```

#### 例外処理とレスポンスコード

```py
import urllib.request
url = 'http://httpbin.org'
req = urllib.request.Request(url)
try:
    with urllib.request.urlopen(req) as res:
        body = res.read()
except urllib.error.HTTPError as e:
    print(e.code)
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

```py
import requests
url = 'http://httpbin.org'
try:
    r = requests.get(url)
except requests.exceptions.RequestException as e:
    print('Error: {}'.format(e))
```


# クラス

```py
class MyClass:
    '''docstring of MyClass'''

    # クラス変数
    id = 1
    name = 'n1'
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

    # 正式な文字列表現(__str__が定義されていないときに呼び出される)
    def __repr__(self):
        return '{}[ID:{}]'.format(self.name, self.id)

    # 非公式な文字列表現(print、format、strなどの組み込み関数でオブジェクトを指定したときに呼び出される)
    def __str__(self):
        return 'MyClass: ' + self.__privateInstanceVariable

    def __unicode__(self):
        return '__unicode__'

    def getName(self):          # getter
        return self.__privateInstanceVariable

    def setName(self, name):    # setter
        self.__privateInstanceVariable = name

    # 通常メソッド
    def Calc(self):
        self.publicInstanceVariable2 = 3
        print('パブリックメソッド')

    def __MyCalc(self):
        print('プライベートメソッド')

    @classmethod
    def SelfName(cls):
        publicClassVariable2 = 30
        print('パブリックメソッド')

    @classmethod
    def __PrivateSelfName(cls):
        print('プライベートクラスメソッド')


# インスタンス変数
myClass1.publicInstanceVariable = 3

# インスタンス変数の追加
myClass1.publicInstanceVariable3 = 4

# プライベートインスタンス変数にアクセス
# インスタンス._クラス名__変数名
print(myClass1._MyClass__publicInstanceVariable)

# パプリッククラス変数へアクセス
# インスタンス名でもクラス名でも可
# 　インスタンス変数が存在しない場合は「インスタンス.変数名」はクラス変数を参照するが、
# 　値を代入するとインスタンス変数が追加されるため、それ以降はインスタンス変数が参照される)
print(Widget.classVal)
print(w.classVal)

# クラス変数の追加
MyClass.publicClassVariable3 = 40

# プライベートクラス変数にアクセス
# インスタンス._クラス名__変数名
print(myClass1._MyClass__privateInstanceVariable)


myClass1 = MyClass(1, 2)    # インスタンス化
myClass1.getName()          # メソッド実行
mg = myClass1.getName       # 別名
mg()                        # メソッド実行
```

## オブジェクトの文字列表現

```py
class MyClass:

    id = 1
    name = 'n1'

    # 正式な文字列表現(__str__が定義されていないときに呼び出される)
    def __repr__(self):
        return 'repr: {}[ID:{}]'.format(self.name, self.id)

    # 非公式な文字列表現(print、format、strなどの組み込み関数でオブジェクトを指定したときに呼び出される)
    def __str__(self):
        return 'str: {}[ID:{}]'.format(self.name, self.id)

    def __unicode__(self):
        return 'unicode: {}[ID:{}]'.format(self.name, self.id)


myClass1 = MyClass()
print("myClass1: " + myClass1)
print("myClass1: " + str(myClass1))
```

> TypeError: can only concatenate str (not "MyClass") to str
>
> myClass1: str: n1[ID:1]

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

## クラスの継承

```py
class MySubClass(MyClass):
    def Calc(self):  # オーバーロード
        print('sub  a')
```

### 多重継承

```py
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

- test-import/main.py

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

- test-import/main2.py

```py
from subdir import *
main.hello()
subfile.hello()
```

- test-import/subfile.py

```py
def hello():
    print('test-import/subdir.py hello()')
```

- test-import/subdir/main.py

```py
def hello():
    print('test-import/subdir/main.py hello()')
```

- test-import/subdir/subfile.py

```py
def hello():
    print('test-import/subdir/subfile.py hello()')
```

- test-import/subdir/**init**.py

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
export PYTHONPATH='/path/to/module:$PYTHONPATH'`
```

site-packages フォルダの中に、`*.pth`ファイル(ファイル名は任意)を作成し、各行にパスを追加

- example.ptn

```py
# foo package configuration

path/to/module
```


# pydoc

- python3md-pydoc.py

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


# ロギング

logging ライブラリを利用する

```py
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(filename)s %(lineno)d %(funcName)s %(message)s')
logger = logging.getLogger(__name__)

logger.debug('message')
logger.info('message')
logger.warning('message')
logger.error('message')
logger.critical('message')
```

## ファイル出力

```py
import logging
import os

LOG_DIR = 'logfile'
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(filename=os.path.join(LOG_DIR, 'logger.log'), level=logging.INFO, format='%(asctime)s %(levelname)s %(filename)s %(lineno)d %(funcName)s %(message)s')
logger = logging.getLogger(__name__)

logger.info('message')
```

## Python のバージョンを取得

```py
import platform
version_number = int(platform.python_version_tuple()[0])
```

> 3

## 実行時間の計測

```py
from functools import wraps
import time
def measure(func) :
    @wraps(func)
    def wrapper(*args, **kargs) :
        start = time.time()
        result = func(*args,**kargs)
        process_time =  time.time() - start
        print(f"関数{func.__name__}の実行時間: {process_time}秒")
        return result
    return wrapper

@measure
def target_function() :
    print('計測対象の処理')

target_function()
```

> 計測対象の処理
>
> 関数 target_function の実行時間: 0.0005533695220947266 秒


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
> File "<stdin>", line 1, in <module>
>
> ZeroDivisionError: division by zero


<hr>

Copyright (c) 2019 YA-androidapp(https://github.com/YA-androidapp) All rights reserved.


