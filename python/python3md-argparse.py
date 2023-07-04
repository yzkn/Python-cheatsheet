#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2022 YA-androidapp(https://github.com/yzkn) All rights reserved.


# --------------------


# import argparse
#
# parser = argparse.ArgumentParser()
# parser.parse_args()


# --------------------


# import argparse
#
# parser = argparse.ArgumentParser(description='スクリプトの概要')
# parser.add_argument('name', help='文字型引数の説明')
# parser.add_argument('height', help='整数引数の説明', type=int)
# parser.add_argument('width', help='小数引数の説明', type=float)
# parser.add_argument('--verbose', help='真偽値引数の説明', action='store_true')
#
# args = parser.parse_args()
#
# if args.verbose:
#     print('verbosity turned on')
#
# print(
#     args.name,    type(args.name),
#     args.height,  type(args.height),
#     args.width,   type(args.width),
#     args.verbose, type(args.verbose)
# )


# --------------------


import argparse

parser = argparse.ArgumentParser(description='スクリプトの概要')

# ハイフン付きだとオプション引数
group = parser.add_mutually_exclusive_group()
group.add_argument('-v', '--verbose', action='store_true') # action='store_false'だと引数が指定された場合にFalse
group.add_argument('-q', '--quiet', action='store_true')

parser.add_argument('--message', default='Lorem ipsum')

parser.add_argument('--ipaddr', type=(lambda x:list(map(int, x.split('.')))))

parser.add_argument('--level', choices=['low', 'middle', 'high'])

parser.add_argument('--items', nargs='*')

# 必須
parser.add_argument('--output', required=True)

# ハイフンなしだと必須引数
parser.add_argument('name', help='文字型引数の説明')
parser.add_argument('height', help='整数引数の説明', type=int)
parser.add_argument('width', help='小数引数の説明', type=float)

args = parser.parse_args()

if args.quiet:
    print(name)
elif args.verbose:
    print(
        args.name,    type(args.name),
        args.height,  type(args.height),
        args.width,   type(args.width),
        args.verbose, type(args.verbose),
        args.message, type(args.message),
        args.ipaddr,  type(args.ipaddr),
        args.level,   type(args.level),
        args.items,   type(args.items),
        args.output,  type(args.output)
    )
else:
    print(
        args.name,
        args.height,
        args.width,
        args.verbose,
        args.message,
        args.ipaddr,
        args.level,
        args.items,
        args.output
    )
