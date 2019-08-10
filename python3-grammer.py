
# 高階関数

# リストに対する演算(map)：map関数は、Python2ではリストを返すがPython3ではイテレータを返すため、list関数を挟む必要がある
numlist = [1, 3, 5, 2, 4]


def double(x): return x * 2


print(map(double, numlist))
print(map(lambda x: x * 2, numlist))
print(list(map(double, numlist)))             # Python3でリストを得たい場合
print(list(map(lambda x: x * 2, numlist)))    # Python3でリストを得たい場合
print([x * 2 for x in numlist])  # 内包表記

# リストに対するフィルタリング(filter)


def isodd(x): return x % 2


print(list(filter(isodd, numlist)))
print(list(filter(lambda x: x % 2, numlist)))
print([x for x in numlist if x % 2])  # 内包表記

# リストに対する畳みこみ(reduce)
from functools import reduce


def add(x, y): return x + y


print(reduce(add, numlist))
print(reduce(lambda x, y: x + y, numlist))

# 内包処理
print([x ** 2 for x in numlist])
print([x ** 2 for x in numlist if x == 3])
numlist2 = range(3)
print([x * y for x in numlist for y in numlist2])
print([[x, x ** 2] for x in numlist])
print([(x, x ** 2) for x in numlist])


# シーケンス・アンパッキング: タプルから複数の変数に一括代入
t = 'foo', 'bar', 123, 456
x, y, z, w = t

# セット
s1 = {'ab', 'cd', 'ab', 'cd'}

ls2 = ['ab', 'cd', 'ef', 'cd']
s2 = set(ls2)   # 重複が削除される
'ab' in s1      # True

print(s1)
print(s2)
print(s1 - s2)
print(s1 | s2)
print(s1 & s2)
print(s1 ^ s2)
print('ab' in s1)
s1.add('yz')
print(s1)

# 辞書
d1 = {'a': 'abcd', 'b': 'bcde'}
d1['c'] = 'cdef'  # {'a': 'abcd', 'c': 'cdef', 'b': 'bcde'}

d2 = dict([('a', 'abcd'), ('b', 'bcde'), ('c', 'cdef')])

# キーのリストを取得
d1.keys()
# dict_keys(['a', 'b', 'c'])

# 値のリストを取得
d1.values()
# dict_values(['abcd', 'bcde', 'cdef'])

# キーと値のタプルを取得
d1.items()
# dict_items([('a', 'abcd'), ('b', 'bcde'), ('c', 'cdef')])

# 要素の削除
del d1['b']

# 順序つき辞書(OrderedDict)
from collections import OrderedDict
testOrderedDict = OrderedDict()
testOrderedDict['k1'] = 'v1'
testOrderedDict['k2'] = 'v2'
testOrderedDict['k3'] = 'v3'

for k, v in testOrderedDict:
    print(k, v)


# 制御構文

# if
if x < 0:
    print('N')
elif x == 0:    # else if
    print('0')
else:
    print('P')

# for
for i in range(3):
    j = i + 1
    print(" " + str(i) + " ,")

for i in range(5, 8):
    j = i + 1
    print(" " + str(i) + " ,")

# Pythonではループ変数やループ内で定義された変数を、ループの外でも参照できる
print(", " + str(i) + " " + str(j))

# for(リストを与える場合)
l = ['foo', 'bar', 123, 456]
for x in l:
    print(str(x))

# for(タプルを与える場合)
t = ('foo', 'bar', 123, 456)
for x in t:
    print(str(x))

# for(辞書を与える場合)
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

# for(試行回数を与える場合)
for i in range(4):
    print(i)    # 0 1 2 3
for i in range(5, 21, 5):
    print(i)    # 5 10 15 20

# for文のelse節
for i in range(5):
    print(i)
else:
    # ループを抜けたときに実行される
    print('else')
# 0 1 2 3 4 else

for i in (0, 1, 2):
    print(i)
# 0, 1, 2
for k in {'k1': 1, 'k2': 2, 'k3': 3}:
    print(k)
# k2, k3, k1
for c in "012":
    print(c)
# 0, 1, 2
for line in open("grammer.py", encoding='utf8'):
    print(line)
# 1行ずつ標準出力

# keyとvalueを一緒に取得する
for k, v in enumerate(['v1', 'v2', 'v3']):
    print(k, v)
# 0 v1
# 1 v2
# 2 v3

# 途中でループから脱出
for i in range(5):
    if i > 3:
        break
    print(i)                  # 0, 1, 2, 3

# スキップする(continue)
for i in range(5):
    if i == 3:
        continue
    print(i)                  # 0, 1, 2, 4

# while
i = 0
while i < 10:
    print(str(i))
    i += 1
else:
    print('-1')

# 例外処理
str = 'ABC'
try:
    # 範囲外の文字が指定し、IndexError例外を発生させる
    c = str[5]
except IOError:
    print("I/O error: {0}".format(err))
except IndexError:
    print("IndexError: {0}".format(err))
except (UnicodeEncodeError, UnicodeDecodeError, UnicodeTranslateError):
    # 複数の例外をまとめて扱う
    print("UnicodeError: {0}".format(err))
except:
    # その他の例外
    print(sys.exc_info())   # 現在処理中の例外(type, value, traceback)

    import traceback
    traceback.print_exc()   # 例外情報とスタックトレース項目
else:
    # 例外が発生しない場合
    print('Success')
finally:
    # 最終処理
    print('Finally')

# 例外を発生させる
raise IOError('IOError')

# With構文
# withを用いた書き方1
with open("grammer.py", encoding='utf8') as f:
    print(f.read())

# withを用いた書き方2
f = open("grammer.py", encoding='utf8')
with f:
    print(f.read())

# アサーション文(assert) : __debug__ が True の時のみ動作する→テスト用
sum = 1 + 2
assert sum == 3
assert sum == 4  # AssertionErrorが発生

# パス文：空の関数や空の型を定義するときに使う


def empty_func():
    pass


class EmptyClass:
    pass


# オブジェクトを削除
e = EmptyClass()
del e

# 文字列を評価
exec("print('exec')")

