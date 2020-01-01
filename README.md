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


