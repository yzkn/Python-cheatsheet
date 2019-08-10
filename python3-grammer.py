
print('foo' "bar")

hoge = """abc
def
ghi"""  # ヒアドキュメント

piyo = 'abc \
def'

# # バイト列(byte), Unicode
# Python 2
len = len(u'あいうえお')       # 5
len = len('あいうえお')        # バイト列として扱われるため、15
# Python 3
len = len('あいうえお')        # uをつけなくてもUnicodeとして扱われるため、5
len = len(b'あいうえお')       # バイト列として扱われるため、15
print(r"あいう\nえお")  # エスケープシーケンスが無視される

# エスケープシーケンス
"\\"            # \
"\'"            # '
"\""            # "
"\a"            # ベル
"\b"            # バックスペース
"\f"            # フォームフィード
"\n"            # LF
"\r"            # CR
"\t"            # タブ
"\v"            # 垂直タブ
"\nnn"          # 8進表記文字(nは0～7)
"\xnn"          # 16進表記文字(nは0～f)
"\uxxxx"        # ユニコード文字xxxx (xxxxは10進数　例: u"\u3042"→'あ')
"\Uxxxxxxxx"    # ユニコード文字xxxxxxxx (xxxxxxxxは10進数　例: U"\U00003042"→'あ')
"\N{name}"      # Unicodeデータベース文字 (例: u"\N{HIRAGANA LETTER A}"→'あ')

# printf
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


# 文字列に対する演算
print(hoge.replace("def", "xyz"))
print(hoge.split("\n", ","))

# 文字列の切り出し
print(hoge[1:3])    # bc
print(hoge[:3])     # abc
print(hoge[8:])     # ghi
print(hoge[-2:])    # hi
print(hoge[0:7:2])  # acdf
# index #################
# 0   1   2   3   4   5 #
# | A | B | C | D | E | #
#         -3  -2  -1    #
#########################


# [ ]:リスト, ( ):タプル, { }:セット/辞書
# リストは変更可能
l = ['foo', 'bar', 123, 456]
l[1]
l[1:3]
l[2] = 321
l = l + ['piyo']    # リストの結合
l[0:2] = ['f', 'b']
len(l)              # リストの要素数、5
l = [[1, 2], [1, 2], [1, 2]]    # リストのリスト

# タプルは変更不可
t = 'foo', 'bar', 123, 456
t[2]
t = t, ('piyo', 789)   # タプルの入れ子

empty = ()  # 空のタプル
t = 'hoge',  # 1要素のタプルを宣言するときは後ろにカンマをつける
t = 'hoge'  # だとただの変数

# リストとタプルの相互変換
print(list([1, 2, 3]))  # タプルからリスト
print(tuple((1, 2, 3)))  # リストからタプル

# リストへの要素追加
l = ['foo', 'bar']
l.append('hoge')  # 末尾に追加
print(l)  # ['foo', 'bar', 'hoge']
l.insert(2, 'piyo')  # 添え字と要素の値を指定
print(l)  # ['foo', 'bar', 'piyo', 'hoge']

l.extend(l)  # リストへリストを追加
print(l)  # ['foo', 'bar', 'piyo', 'hoge', 'foo', 'bar', 'piyo', 'hoge']

# リスト要素の削除
l = ['foo', 'bar']
l.remove('foo')
print(l)  # [bar']
l.remove('foooo')
print(l)  # 存在しない値を指定するとエラーが発生

# ソート
l = ['foo', 'bar', 'piyo', 'hoge', 'foo', 'bar', 'piyo', 'hoge']
sortedlist = sorted(l)
print(l)
# ['foo', 'bar', 'piyo', 'hoge', 'foo', 'bar', 'piyo', 'hoge']

print(sortedlist)
# ['bar', 'bar', 'foo', 'foo', 'hoge', 'hoge', 'piyo', 'piyo']

l.sort(key=None, reverse=False)
print(l)  # ['bar', 'bar', 'foo', 'foo', 'hoge', 'hoge', 'piyo', 'piyo']

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


# 関数
# 定義
def func1():
    print("hello")


# 呼出
func1()

# 引数あり
# 定義


def func2(arg):
    print(arg)


# 呼出
func2("hello")

# 既定値を持つ引数あり
# 定義


def func3(arg="bye"):
    print(arg)


# 呼出
func3()
func3(arg="hi")

# 戻り値あり
# 定義


def func4(arg):
    return arg


# 呼出
print(func4("hello"))

# docstringあり
# 定義


def func5():
    """helloと表示する関数"""
    print("hello")


# 呼出
func5()
# ヘルプを表示
help(func5)

# タプルと辞書を受け取る
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

# 引数のアンパック
args = [1, 5]
list(range(*args))

list(range(1, 5))   # と同じ

# クラス


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


# モジュールの呼び出し：呼び出し先のモジュールはカレントディレクトリ→環境変数PYTHONPATHに指定されたディレクトリの順に検索される
# bar.py
def bar1(n):
    pass()


def bar2(n):
    pass()


# foo.py
import bar
bar.bar1(100)
bar1 = bar.bar2
bar2(100)

from bar import bar1, bar2
bar1(100)

# ディレクトリに複数のモジュールをまとめる場合は、ドット区切りで指定する
# この時各フォルダ内に__init__.py(空のファイルでも可)を配置する必要がある
import abcd.efgh.bar    # ./abcd/efgh/bar.pyを呼び出す場合


# Copyright (c) 2017 YA-androidapp(https://github.com/YA-androidapp) All rights reserved.
