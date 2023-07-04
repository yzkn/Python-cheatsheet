#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2022 YA-androidapp(https://github.com/yzkn) All rights reserved.


from janome.tokenizer import Tokenizer

# テキストファイル読込み
f = open('foobar.txt')
# テキストファイルの全行を読込む
inputed_text = f.read()
# ファイルを閉じる
f.close()

# 形態素解析
t = Tokenizer()
tokens = t.tokenize(inputed_text)

# 結果出力のためのファイルオープン
f2 = open('result.txt', 'w')

for token in tokens:
    partOfSpeech = token.part_of_speech.split(',')[0]
    # 名詞、動詞、形容詞のみ表示する
    if partOfSpeech == u'名詞' or partOfSpeech == u'動詞' or partOfSpeech == u'形容詞':
        print( token.surface )
        f2.writelines( token.surface + "\n" )

# ファイルを閉じる
f2.close()





# Copyright (c) 2017 YA-androidapp(https://github.com/yzkn) All rights reserved.
