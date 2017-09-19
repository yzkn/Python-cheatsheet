# ファイル操作

# touch
from pathlib import Path
Path('test.txt').touch()

# テキストファイル

# 読込み
file = open('test.txt', 'r')
string = file.read()
print(string)  # 1つの文字列として読込み

file = open('test.txt', 'r')
string = file.readline()
while string:
    print(string)
    string = file.readline()  # 1行ずつ読込み

file = open('test.txt', 'r')
string = file.readlines()  # リストへ格納

# 書込み
file = open('test.txt', 'w')
string = 'foobar hoge'
file.write(string)  # 1行ずつ書込み

file = open('test.txt', 'w')
lst = ['foobar', 'hoge']
file.writelines(lst)  # リストを書込み

# 追記
file = open('test.txt', 'a')
string = 'foobar hoge'
file.write(string)

file = open('test.txt', 'a')
lst = ['foobar', 'hoge']
file.writelines(lst)

# ファイルを閉じる
file.close()

# ファイルを閉じる(不要になったら自動的に解放)
with open('test.txt', 'r') as file:  # with句
    string = 'foobar hoge'
    file.write(string)

# CSV

# 読込み
import csv
with open('test.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in csvreader:
        print(', '.join(row))
csvfile.close()

# 書込み
import csv
with open('test.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['foo', 'bar', 'hoge'])
    spamwriter.writerow(['foo', 'bar', 'hoge'])
csvfile.close()
csvfile.close()

# 追記
import csv
with open('test.csv', 'a', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['foo', 'bar', 'hoge'])
    spamwriter.writerow(['foo', 'bar', 'hoge'])
csvfile.close()
csvfile.close()

# JSON

# 読込み(JSONファイル)
import json

f = open('test.json', 'r')
json_dict = json.load(f)
print('json_dict:{}'.format(type(json_dict)))

# 読込み(JSON文字列)
import json

json_str = '''
{
    "key1":"val1",
    "key2":"val2"
}
'''

json_dict = json.loads(json_str)
print('json_dict:{}'.format(type(json_dict)))

# 読込み(JSON文字列　順序を保つ)
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

# 要素の読込み
import json

f = open('test.json', 'r')
json_dict = json.load(f)

for x in json_dict:
    num = json_dict[x]['num']

    if(num >= 500):
        print('{0}:{1}'.format(x, json_dict[x]))

# 書込み
import json

# 書き出すオブジェクト
data = {
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

savepath = 'test.json'
with open(savepath, 'w') as outfile:
    json.dump(data, outfile)

# ARFFファイル

# 読込み
# import arff
data = arff.load(open('test.arff', 'rb'))

# 書込み
arff.dumps(data)

# ディレクトリ操作

# パスの生成
import os.path
path = os.path.join('C:\\', 'Python', 'scripts')

# カレントディレクトリ
import os
os.getcwd()
os.chdir(path)

# 存在チェック
import os
path = 'C:\\'

os.path.exists(path)  # ファイルとフォルダを区別しない

os.path.isfile(path)  # ファイルの存在チェック

os.path.isdir(path)  # フォルダの存在チェック

# フォルダ作成
import os
os.mkdir(path)

import os
os.makedirs(os.path.join(path, 'sub'))

# フォルダ名・ファイル名・拡張子の取得
import os
dirname = os.path.dirname(path)
basename = os.path.basename(path)
root, ext = os.path.splitext(path)

# 絶対パスか検査・絶対パスを取得
os.path.isabs('C:\\')
os.path.abspath(".\\")

# コピー
path_old = ''
path_new = ''

import shutil
shutil.copyfile(path_old, path_new)
shutil.copytree(path_old, path_new)

# リネーム・移動
path_old = ''
path_new = ''

import os
os.rename(path_old, path_new)

shutil.move(path_old, path_new)

# 削除
import os
os.remove(path)  # ファイルを削除

import os
os.rmdir(path)  # 空のディレクトリを削除

import shutil
shutil.rmtree(path)  # 再帰的に削除

# ファイル走査

# 直下のみ
files = os.listdir(path)
print(files)

from glob import glob
files = glob("*.txt")
print(files)

# 再帰
import os


def find_all_files(path):
    for root, dirs, files in os.walk(path):
        # yield root
        for file in files:
            if os.path.splitext(file)[1] == u'.dll':
                yield os.path.join(root, file)


for file in find_all_files(path):
    print(file)

# ファイルプロパティ
os.path.getatime(path)  # 最終アクセス日時
os.path.getmtime(path)  # 最終更新日時
os.path.getsize(path)  # ファイルサイズ


# Copyright (c) 2017 YA-androidapp(https://github.com/YA-androidapp) All rights reserved.
