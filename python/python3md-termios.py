#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2022 YA-androidapp(https://github.com/yzkn) All rights reserved.


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