目次

<!-- TOC -->

- [おまじない](#おまじない)
  - [shebang](#shebang)
- [命名規則](#命名規則)
- [演算子](#演算子)
  - [演算子の優先順位](#演算子の優先順位)
  - [比較](#比較)
  - [複数条件](#複数条件)
- [変数](#変数)
- [データ型](#データ型)
  - [型の判定](#型の判定)
  - [isinstance()](#isinstance)
  - [type()と isinstance()の差異](#typeと-isinstanceの差異)
  - [boolean](#boolean)
  - [int](#int)
    - [文字列型からのキャスト](#文字列型からのキャスト)
      - [10 進数以外のキャスト](#10-進数以外のキャスト)
      - [漢数字のキャスト](#漢数字のキャスト)
        - [1 文字の漢数字のキャスト](#1-文字の漢数字のキャスト)
        - [2 文字以上の漢数字のキャスト(漢数字をアラビア数字に変換してから int 型にキャスト)](#2-文字以上の漢数字のキャスト漢数字をアラビア数字に変換してから-int-型にキャスト)
      - [kanjize パッケージを利用](#kanjize-パッケージを利用)
    - [数値の切り上げ・切り捨て](#数値の切り上げ・切り捨て)
    - [1 の補数、2 の補数](#1-の補数2-の補数)
    - [ビット演算](#ビット演算)
      - [左シフト(ゼロ埋め)](#左シフトゼロ埋め)
      - [右シフト(切り捨て)](#右シフト切り捨て)
      - [AND](#and)
      - [OR](#or)
      - [XOR](#xor)
  - [float](#float)
    - [文字列型からのキャスト](#文字列型からのキャスト-1)
      - [指数表記のキャスト](#指数表記のキャスト)
  - [complex(虚数)](#complex虚数)
  - [datetime](#datetime)
    - [日時の比較](#日時の比較)
    - [現在日時](#現在日時)
    - [祝日判定](#祝日判定)
    - [日付の生成](#日付の生成)
      - [一定期間後の日付を生成](#一定期間後の日付を生成)
      - [日時の要素を置換](#日時の要素を置換)
      - [日付のリスト](#日付のリスト)
    - [指定日までの残り期間を取得](#指定日までの残り期間を取得)
    - [タイムゾーンを考慮した datetime](#タイムゾーンを考慮した-datetime)
      - [datetime パッケージの timezone モジュールを使用する場合](#datetime-パッケージの-timezone-モジュールを使用する場合)
        - [生成](#生成)
        - [タイムゾーンを変更(変更前と同じ時刻)](#タイムゾーンを変更変更前と同じ時刻)
        - [タイムゾーンを置換(変更前と異なる時刻)](#タイムゾーンを置換変更前と異なる時刻)
      - [pytz を使用する場合](#pytz-を使用する場合)
        - [現在日時から生成](#現在日時から生成)
        - [任意の日時を生成](#任意の日時を生成)
        - [サマータイム終了時点を跨いだ日時の加算](#サマータイム終了時点を跨いだ日時の加算)
    - [datetime から date](#datetime-から-date)
    - [datetime から str](#datetime-から-str)
    - [str から datetime、date](#str-から-datetimedate)
      - [タイムゾーンを考慮した str から datetime](#タイムゾーンを考慮した-str-から-datetime)
        - [タイムゾーンを考慮した ISO 形式の str から datetime](#タイムゾーンを考慮した-iso-形式の-str-から-datetime)
      - [日付時刻の format 文字列に埋め込むディレクティブ](#日付時刻の-format-文字列に埋め込むディレクティブ)
  - [str(文字列)](#str文字列)
    - [ヒアドキュメント](#ヒアドキュメント)
    - [文字種チェック](#文字種チェック)
      - [数値](#数値)
    - [文字列のフォーマット](#文字列のフォーマット)
      - [ゼロ埋め](#ゼロ埋め)
      - [format](#format)
        - [整列](#整列)
        - [小数点以下の桁数](#小数点以下の桁数)
        - [桁区切り文字](#桁区切り文字)
        - [指数表記](#指数表記)
        - [2 進数、8 進数、16 進数](#2-進数8-進数16-進数)
        - [リストの値を代入](#リストの値を代入)
        - [タプルの値を代入](#タプルの値を代入)
        - [辞書の値を代入](#辞書の値を代入)
      - [f 文字列](#f-文字列)
        - [リストの値を代入](#リストの値を代入-1)
        - [タプルの値を代入](#タプルの値を代入-1)
        - [辞書の値を代入](#辞書の値を代入-1)
      - [フォーマット演算子](#フォーマット演算子)
    - [エスケープシーケンス](#エスケープシーケンス)
    - [バイト列(byte), Unicode](#バイト列byte-unicode)
      - [Python 2](#python-2)
      - [Python 3](#python-3)
      - [文字列とバイト列の変換](#文字列とバイト列の変換)
    - [区切り文字による分割](#区切り文字による分割)
      - [split の引数を指定しないと、空白文字(タブ文字、改行文字を含む)で分割される](#split-の引数を指定しないと空白文字タブ文字改行文字を含むで分割される)
      - [split で分割した後、各要素の先頭・末尾の空白文字を除去する](#split-で分割した後各要素の先頭・末尾の空白文字を除去する)
    - [部分文字列](#部分文字列)
      - [1 文字ずつ処理する](#1-文字ずつ処理する)
        - [インデックスを取得](#インデックスを取得)
      - [部分文字列を全パターン取得する](#部分文字列を全パターン取得する)
    - [エンコード・デコード](#エンコード・デコード)
      - [Base64](#base64)
      - [URL safe な Base64](#url-safe-な-base64)
    - [検索](#検索)
      - [単純な検索](#単純な検索)
        - [前方一致](#前方一致)
        - [後方一致](#後方一致)
      - [正規表現による検索](#正規表現による検索)
        - [パターンのコンパイル](#パターンのコンパイル)
        - [文字列の先頭でマッチ](#文字列の先頭でマッチ)
          - [グループ化](#グループ化)
        - [文字列の途中でマッチした最初の箇所](#文字列の途中でマッチした最初の箇所)
        - [文字列の途中でマッチした全ての箇所のリスト](#文字列の途中でマッチした全ての箇所のリスト)
        - [文字列の途中でマッチした全ての箇所のイテレーター](#文字列の途中でマッチした全ての箇所のイテレーター)
        - [フラグを利用](#フラグを利用)
      - [文字種のフィルタリング](#文字種のフィルタリング)
        - [文字列全体が半角英数だけ含まれているか検査](#文字列全体が半角英数だけ含まれているか検査)
        - [半角カナなどが含まれていないか検査](#半角カナなどが含まれていないか検査)
        - [文字種別のパターン](#文字種別のパターン)
    - [置換](#置換)
      - [単純な置換](#単純な置換)
        - [改行文字を除去](#改行文字を除去)
        - [前後の空白文字を除去](#前後の空白文字を除去)
        - [大文字化・小文字化](#大文字化・小文字化)
      - [正規表現による置換](#正規表現による置換)
        - [数字のみ抽出](#数字のみ抽出)
        - [ファイル名に使用できない文字を除去](#ファイル名に使用できない文字を除去)
      - [一文字ごとの置換](#一文字ごとの置換)
    - [絵文字](#絵文字)
  - [リスト](#リスト)
    - [リストが空か検査](#リストが空か検査)
    - [リストを生成](#リストを生成)
    - [リストに要素を追加](#リストに要素を追加)
    - [リストの要素を除去](#リストの要素を除去)
    - [リストの反復処理](#リストの反復処理)
      - [インデックスを取得](#インデックスを取得-1)
      - [複数のリストを同時に繰り返す](#複数のリストを同時に繰り返す)
      - [多次元リスト](#多次元リスト)
      - [リストの要素を連結した文字列を取得](#リストの要素を連結した文字列を取得)
    - [リストをソート](#リストをソート)
      - [ソート条件を変える](#ソート条件を変える)
    - [リストの重複する要素を除去](#リストの重複する要素を除去)
    - [リストの重複する要素を抽出](#リストの重複する要素を抽出)
    - [高階関数](#高階関数)
      - [map](#map)
      - [filter](#filter)
      - [reduce](#reduce)
    - [リストの内包表記](#リストの内包表記)
      - [リスト内包表記で FizzBuzz](#リスト内包表記で-fizzbuzz)
  - [辞書](#辞書)
    - [追加・置換・削除](#追加・置換・削除)
    - [辞書の要素を参照](#辞書の要素を参照)
    - [辞書を生成(リスト・タプルから変換／初期化)](#辞書を生成リスト・タプルから変換／初期化)
    - [辞書を結合](#辞書を結合)
    - [辞書のコピー](#辞書のコピー)
    - [辞書の反復処理](#辞書の反復処理)
      - [インデックスとキー](#インデックスとキー)
      - [インデックスと値](#インデックスと値)
      - [インデックスと要素](#インデックスと要素)
      - [複数の辞書を同時に繰り返す](#複数の辞書を同時に繰り返す)
    - [辞書の要素の存在チェック](#辞書の要素の存在チェック)
    - [指定した値を持つキーを取得する](#指定した値を持つキーを取得する)
    - [辞書のキーと値を交換](#辞書のキーと値を交換)
    - [辞書の値でソート](#辞書の値でソート)
    - [辞書の重複する要素を除去 #TODO](#辞書の重複する要素を除去-todo)
    - [辞書の内包表記](#辞書の内包表記)
  - [タプル](#タプル)
    - [タプルを生成](#タプルを生成)
    - [タプルの反復処理](#タプルの反復処理)
      - [インデックスを取得](#インデックスを取得-2)
    - [タプルの入れ子](#タプルの入れ子)
      - [多重タプルをフラット化(flatten)](#多重タプルをフラット化flatten)
        - [2 重タプル](#2-重タプル)
        - [多重タプル](#多重タプル)
    - [シーケンス・アンパッキング](#シーケンス・アンパッキング)
    - [タプルの内包表記](#タプルの内包表記)
  - [セット](#セット)
    - [セットを生成](#セットを生成)
    - [セットの要素の存在チェック](#セットの要素の存在チェック)
    - [セットの要素を追加する](#セットの要素を追加する)
    - [セットの演算](#セットの演算)
  - [順序つき辞書(OrderedDict)](#順序つき辞書ordereddict)
- [制御構文](#制御構文)
  - [if](#if)
  - [for](#for)
    - [for(リストを与える場合)](#forリストを与える場合)
    - [for(タプルを与える場合)](#forタプルを与える場合)
    - [for(辞書を与える場合)](#for辞書を与える場合)
    - [for(試行回数を与える場合)](#for試行回数を与える場合)
    - [for 文の else 節](#for-文の-else-節)
    - [スキップする(continue)](#スキップするcontinue)
    - [itertools](#itertools)
  - [while](#while)
  - [try(例外処理)](#try例外処理)
  - [評価](#評価)
    - [eval](#eval)
    - [exec](#exec)
    - [グローバル名前空間の参照・変更を制限](#グローバル名前空間の参照・変更を制限)
  - [assert(アサーション)](#assertアサーション)
  - [del](#del)
  - [exit(プログラム実行を終了)](#exitプログラム実行を終了)
  - [pass](#pass)
  - [with](#with)
    - [複数の with をまとめる](#複数の-with-をまとめる)
- [関数](#関数)
  - [引数なし](#引数なし)
  - [引数あり](#引数あり)
  - [既定値を持つ引数あり](#既定値を持つ引数あり)
  - [戻り値あり](#戻り値あり)
  - [docstring あり](#docstring-あり)
    - [ヘルプを表示](#ヘルプを表示)
  - [タプルと辞書を受け取る](#タプルと辞書を受け取る)
  - [引数のアンパック](#引数のアンパック)
  - [関数オブジェクト](#関数オブジェクト)
    - [関数を変数に代入](#関数を変数に代入)
- [I/O](#io)
  - [コマンドライン引数](#コマンドライン引数)
  - [標準入力](#標準入力)
    - [無限ループをキー入力で抜ける](#無限ループをキー入力で抜ける)
  - [標準出力](#標準出力)
    - [末尾に改行文字をつけずに出力する](#末尾に改行文字をつけずに出力する)
    - [pprint()でデータ出力の整然化](#pprintでデータ出力の整然化)
    - [標準出力の内容をファイルに書き出す](#標準出力の内容をファイルに書き出す)
      - [stdout](#stdout)
      - [print()](#print)
  - [環境変数](#環境変数)
    - [環境変数の読み書き](#環境変数の読み書き)
      - [環境変数の読み出し](#環境変数の読み出し)
        - [一覧の取得](#一覧の取得)
        - [環境変数の存在チェック](#環境変数の存在チェック)
        - [キーを指定して値を取得](#キーを指定して値を取得)
      - [環境変数の書き込み](#環境変数の書き込み)
      - [環境変数の削除](#環境変数の削除)
    - [.env ファイルに記述した設定値を環境変数に設定](#env-ファイルに記述した設定値を環境変数に設定)
  - [ハッシュ](#ハッシュ)
    - [文字列からハッシュを取得](#文字列からハッシュを取得)
      - [巨大なデータのハッシュを取得](#巨大なデータのハッシュを取得)
    - [ファイルのハッシュを取得](#ファイルのハッシュを取得)
      - [巨大なファイルのハッシュを取得](#巨大なファイルのハッシュを取得)
  - [ローカルファイル](#ローカルファイル)
    - [パス文字列の操作](#パス文字列の操作)
      - [複数のパスが同一のファイルを示しているか検査](#複数のパスが同一のファイルを示しているか検査)
      - [パス文字列を正規化する(不要な区切り文字、 `..` の除去　／　 Windows 環境での大文字小文字の置換、スラッシュとバックスラッシュの置換)](#パス文字列を正規化する不要な区切り文字--の除去　／　-windows-環境での大文字小文字の置換スラッシュとバックスラッシュの置換)
      - [ホームディレクトリのパスを取得](#ホームディレクトリのパスを取得)
      - [環境変数を取得](#環境変数を取得)
      - [親ディレクトリのパスを取得](#親ディレクトリのパスを取得)
      - [シンボリックリンクのパスを正規化](#シンボリックリンクのパスを正規化)
      - [Linux 上で Windows 形式のパスを操作](#linux-上で-windows-形式のパスを操作)
    - [カレントディレクトリ](#カレントディレクトリ)
      - [スクリプトファイルのパスを取得](#スクリプトファイルのパスを取得)
    - [ファイル・フォルダを存在チェック](#ファイル・フォルダを存在チェック)
    - [ファイル・フォルダの一覧を取得](#ファイル・フォルダの一覧を取得)
      - [直下のファイル・フォルダ一覧を取得](#直下のファイル・フォルダ一覧を取得)
      - [直下のファイル一覧を取得](#直下のファイル一覧を取得)
      - [直下のフォルダ一覧を取得](#直下のフォルダ一覧を取得)
      - [再帰的にファイル・フォルダ一覧を取得 ⇒ _recursive_ が _True_ かつ、パスに _\*\*_](#再帰的にファイル・フォルダ一覧を取得-⇒-_recursive_-が-_true_-かつパスに-__)
      - [Python3.4 以前で、再帰的にファイル・フォルダ一覧を取得](#python34-以前で再帰的にファイル・フォルダ一覧を取得)
      - [再帰的にフォルダ一覧を取得 ⇒ パスの末尾が _os.path.sep_](#再帰的にフォルダ一覧を取得-⇒-パスの末尾が-_ospathsep_)
      - [再帰的にファイル一覧を取得](#再帰的にファイル一覧を取得)
      - [ワイルドカードを利用](#ワイルドカードを利用)
      - [正規表現を利用](#正規表現を利用)
    - [ファイル情報を取得](#ファイル情報を取得)
    - [ファイルを作成](#ファイルを作成)
      - [touch()](#touch)
      - [既存のファイルがある場合はバックアップを作成して再作成](#既存のファイルがある場合はバックアップを作成して再作成)
    - [フォルダを作成](#フォルダを作成)
      - [既存のフォルダがある場合はバックアップを作成して再作成](#既存のフォルダがある場合はバックアップを作成して再作成)
    - [ファイルをコピー](#ファイルをコピー)
    - [フォルダをコピー](#フォルダをコピー)
    - [ファイルをリネーム](#ファイルをリネーム)
    - [フォルダをリネーム](#フォルダをリネーム)
    - [ファイルを移動](#ファイルを移動)
    - [フォルダを移動](#フォルダを移動)
    - [ファイルを削除](#ファイルを削除)
      - [特定のファイルを削除](#特定のファイルを削除)
      - [ファイルを検索して削除](#ファイルを検索して削除)
    - [フォルダを削除](#フォルダを削除)
    - [タイプ別のファイル読み書き](#タイプ別のファイル読み書き)
      - [ZIP ファイル](#zip-ファイル)
        - [ZIP ファイル圧縮](#zip-ファイル圧縮)
          - [shutil を使ってフォルダごと圧縮](#shutil-を使ってフォルダごと圧縮)
          - [個別にファイルを追加して圧縮ファイルを作成](#個別にファイルを追加して圧縮ファイルを作成)
        - [ZIP ファイル解凍](#zip-ファイル解凍)
      - [ログファイル(テキストファイル・追記)](#ログファイルテキストファイル・追記)
      - [設定ファイル(configparser)](#設定ファイルconfigparser)
      - [テキストファイル](#テキストファイル)
        - [モード](#モード)
        - [文字コードの推測](#文字コードの推測)
          - [エラーハンドラ](#エラーハンドラ)
          - [cChardet モジュールを使用](#cchardet-モジュールを使用)
        - [読み込み](#読み込み)
          - [単一の文字列として読み込み(r: 読み取り)](#単一の文字列として読み込みr-読み取り)
          - [# SHIFT-JIS](#-shift-jis)
          - [# UTF-8 BOM なし](#-utf-8-bom-なし)
          - [# UTF-8 BOM あり](#-utf-8-bom-あり)
          - [1 行ずつ読み込み(r: 読み取り)](#1-行ずつ読み込みr-読み取り)
          - [リストへ格納(r: 読み取り)](#リストへ格納r-読み取り)
        - [書き込み](#書き込み)
          - [単一の文字列として書き込み(x: 新規作成)](#単一の文字列として書き込みx-新規作成)
          - [リストを書き込み(x: 新規作成)](#リストを書き込みx-新規作成)
          - [単一の文字列として書き込み(w: 新規作成／上書き)](#単一の文字列として書き込みw-新規作成／上書き)
          - [既存ファイルが存在するときに上書きするか確認する](#既存ファイルが存在するときに上書きするか確認する)
          - [リストを書き込み(w: 新規作成／上書き)](#リストを書き込みw-新規作成／上書き)
          - [単一の文字列として書き込み(a: 追記)](#単一の文字列として書き込みa-追記)
          - [リストを書き込み(a: 追記)](#リストを書き込みa-追記)
      - [CSV ファイル](#csv-ファイル)
        - [読み込み](#読み込み-1)
          - [メモリ上の CSV 文字列の読み込み](#メモリ上の-csv-文字列の読み込み)
        - [書き込み](#書き込み-1)
          - [上書き](#上書き)
          - [追記](#追記)
      - [JSON ファイル](#json-ファイル)
        - [json.tool](#jsontool)
        - [ファイルから読み込み](#ファイルから読み込み)
          - [スクリプトを書かず、json.tool で解析する](#スクリプトを書かずjsontool-で解析する)
        - [文字列から読み込み](#文字列から読み込み)
        - [文字列から読み込み(順序を保つ)](#文字列から読み込み順序を保つ)
        - [要素の読み込み](#要素の読み込み)
          - [要素の検索](#要素の検索)
        - [書き込み](#書き込み-2)
      - [ini ファイル](#ini-ファイル)
        - [ファイルから読み込み](#ファイルから読み込み-1)
      - [TSV ファイル](#tsv-ファイル) - [メモリ上の TSV 文字列の読み込み](#メモリ上の-tsv-文字列の読み込み)
      - [XML ファイル](#xml-ファイル)
        - [ファイルから読み込み](#ファイルから読み込み-2)
        - [文字列から読み込み](#文字列から読み込み-1)
        - [書き込み](#書き込み-3)
      - [ARFF ファイル](#arff-ファイル)
        - [読み込み](#読み込み-2)
        - [書き込み](#書き込み-4)
  - [ネットワーク](#ネットワーク)
    - [URL 文字列の操作](#url-文字列の操作)
      - [URL エンコーディング](#url-エンコーディング)
        - [変換対象の文字の違いと利用する関数](#変換対象の文字の違いと利用する関数)
        - [URL の一部の要素に日本語が含まれている場合](#url-の一部の要素に日本語が含まれている場合)
      - [URL 文字列のパース](#url-文字列のパース)
      - [URL 文字列の組み立て](#url-文字列の組み立て)
    - [リクエストを送信](#リクエストを送信)
      - [コンテンツを文字列として取得](#コンテンツを文字列として取得)
      - [文字コードを指定](#文字コードを指定)
        - [特定の文字コード(Shift-JIS)を指定](#特定の文字コードshift-jisを指定)
        - [コンテンツの内容から文字コードを推定する](#コンテンツの内容から文字コードを推定する)
          - [chardet による推定](#chardet-による推定)
          - [cChardet による推定(chardet よりも高速)](#cchardet-による推定chardet-よりも高速)
      - [コンテンツをテンポラリファイルとして取得](#コンテンツをテンポラリファイルとして取得)
      - [バイナリファイルを保存](#バイナリファイルを保存)
        - [画像ファイルの保存](#画像ファイルの保存)
        - [大容量ファイルの保存](#大容量ファイルの保存)
      - [GET](#get)
      - [POST](#post)
        - [フォーム送信(Multipart エンコード)](#フォーム送信multipart-エンコード)
      - [PUT](#put)
      - [DELETE](#delete)
      - [HEAD](#head)
      - [HTTP ヘッダ](#http-ヘッダ)
      - [BASIC 認証](#basic-認証)
      - [応答ヘッダ・リダイレクト先 URL](#応答ヘッダ・リダイレクト先-url)
      - [セッション](#セッション)
      - [Cookie](#cookie)
      - [例外処理とレスポンスコード](#例外処理とレスポンスコード)
- [クラス](#クラス)
  - [オブジェクトの文字列表現](#オブジェクトの文字列表現)
  - [オブジェクトの属性の参照と存在チェック](#オブジェクトの属性の参照と存在チェック)
  - [クラスの継承](#クラスの継承)
    - [多重継承](#多重継承)
- [モジュール](#モジュール)
  - [モジュールの読み込み](#モジュールの読み込み)
    - [推奨される読み込み順序](#推奨される読み込み順序)
  - [外部スクリプトの読み込み](#外部スクリプトの読み込み)
  - [一時的にモジュール検索パスを追加](#一時的にモジュール検索パスを追加)
  - [恒久的にモジュール検索パスを追加](#恒久的にモジュール検索パスを追加)
- [pydoc](#pydoc)
- [ロギング](#ロギング)
  - [ファイル出力](#ファイル出力)
- [エラーメッセージ](#エラーメッセージ)
  - [シンタックスハイライト](#シンタックスハイライト)

<!-- /TOC -->

<a id="markdown-おまじない" name="おまじない"></a>

# おまじない

<a id="markdown-shebang" name="shebang"></a>

## shebang

```py
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# #から行末まではコメント
# 1行目または2行目のコメントで、正規表現coding[=:]\s*([-\w.]+)にマッチする場合はエンコーディング宣言として扱われる
```

<a id="markdown-命名規則" name="命名規則"></a>

# 命名規則

| 項目                 | 文字種       | 区切り文字     |
| -------------------- | ------------ | -------------- |
| パッケージ           | 英数小文字   | -              |
| モジュール           | 英数小文字   | アンダースコア |
| クラス, 例外, 型変数 | 英数大小文字 | 大文字         |
| メソッド, 関数,変数  | 英数小文字   | アンダースコア |
| 定数                 | 英数大文字   | アンダースコア |

<a id="markdown-演算子" name="演算子"></a>

# 演算子

<a id="markdown-演算子の優先順位" name="演算子の優先順位"></a>

## 演算子の優先順位

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

```py
# 三項演算子
t = 'True'
f = 'False'
c = t if 1 == 1 else f  # 'True'
```

<a id="markdown-比較" name="比較"></a>

## 比較

```py
x = None

if x is None: # Null判定
    print('True')
```

> True

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

`is` での比較で、オブジェクトが同一でなくても True が返る場合もある

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

<a id="markdown-複数条件" name="複数条件"></a>

## 複数条件

```py
1 < a < 5
```

```py
content = 'foobarhogepiyo'

# if 'foo' in s and 'bar' in s:
if all(map(content.__contains__, ('foo', 'bar'))):
    print('found')

# if 'foo' in s or 'hoge' in s:
if any(map(content.__contains__, ('foo', 'hoge'))):
    print('found')
```

<a id="markdown-変数" name="変数"></a>

# 変数

```py
name = 3

# 異なる方の値を代入
name = 'Suzuki'

# 変数の削除
del name

print(name)
```

```py
# 多重代入
x = y = z = 0
```

> NameError: name 'name' is not defined

<a id="markdown-データ型" name="データ型"></a>

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
> \# 10 進数以外
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

<a id="markdown-型の判定" name="型の判定"></a>

## 型の判定

<a id="markdown-isinstance" name="isinstance"></a>

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

<a id="markdown-typeと-isinstanceの差異" name="typeと-isinstanceの差異"></a>

## type()と isinstance()の差異

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

<a id="markdown-boolean" name="boolean"></a>

## boolean

| True                                                                                                        | False                                                                                   |
| ----------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| bool(1)<br>bool(2)<br>bool(-3)<br>bool(.1)<br>bool(1j)<br>bool('a')<br>bool([0])<br>bool((0,))<br>bool({0}) | bool(0)<br><br><br>bool(0.)<br>bool(0j)<br>bool('')<br>bool([])<br>bool(())<br>bool({}) |

```py
True == 1  # True
False == 0  # True
True + False  # 1
```

<a id="markdown-int" name="int"></a>

## int

```py
i = 123 # 10整数
print(i)

i = 0b11111111 # 2進数
print(i) # 10進数以外をprint関数に与えた場合でも、内部的にはint型なので10進数で表示される
print(bin(i)) # 2進表記の文字列に変換して表示する
print(format(i, 'b'))
print(format(i, '#b'))

i = 0o777 # 8進数
print(i)
print(oct(i)) # 8進表記の文字列に変換して表示する
print(format(i, 'o'))
print(format(i, '#o'))

i = 0xffff # 16進数
print(i)
print(hex(i)) # 16進表記の文字列に変換して表示する
print(format(i, 'x'))
print(format(i, '#x'))

# long(Python3ではint型として扱う)
# l = 1234567890123456789012345678901234567890123456789012345678901234567890L # Python 2
l = 1234567890123456789012345678901234567890123456789012345678901234567890
```

> 123

> 255 \# 10 進数以外を print 関数に与えると 10 進数で表示される
>
> 0b11111111
>
> 11111111
>
> 0b11111111

> 511
>
> 0o777
>
> 777
>
> 0o777

> 65535
>
> 0xffff
>
> ffff
>
> 0xffff

```py
i = 1_000_000_000 # アンダースコアは無視され、int型として扱われる
print(i)
print('{:,}'.format(i)) # 3桁ごとにセミコロンを入れる
```

> 1000000000
>
> 1,000,000,000

<a id="markdown-文字列型からのキャスト" name="文字列型からのキャスト"></a>

### 文字列型からのキャスト

```py
s = '1'
if s.isnumeric():
    i = int(s)  # 文字列型からのキャスト
    print('{}'.format(i))

s = '１２３' # 全角数字文字列からint型へのキャスト(－や．は全角だとエラーとなる)
if s.isnumeric():
    i = int(s)  # 文字列型からのキャスト
    print('{}'.format(i))

s = '10,000'
s = s.replace(',', '') # 桁区切りのカンマが含まれていると isnumeric() は False を返し、キャストにも失敗する
if s.isnumeric():
    i = int(s)  # 文字列型からのキャスト
    print('{}'.format(i))

s = '一五一十'
if s.isnumeric():
    print('isNumeric')
    i = int(s)  # 文字列型からのキャスト
```

> \# '1'
>
> 1
>
> \# '１２３'
>
> 123
>
> \# '10,000'
>
> 10000
>
> \# '一五一十'
>
> isNumeric \# 漢数字だけしか含まれていないため True が返る
>
> ValueError: invalid literal for int() with base 10: '一五一十' \# キャストには失敗する

- `isnumeric()` が `True` となる文字

```
零 一 二 三 四 五 六 七 八 九 十 百 千 万 億 兆
```

<a id="markdown-10-進数以外のキャスト" name="10-進数以外のキャスト"></a>

#### 10 進数以外のキャスト

```py
print(int('0b11111111', 2)) # 2進数
print(int('0o777', 8)) # 8進数
print(int('0xffff', 16)) # 16進数

# 接頭辞(0b, 0o, 0x)がついていれば、基数に0を指定しても変換される
print(int('0b11111111', 0)) # 2進数
print(int('0o777', 0)) # 8進数
print(int('0xffff', 0)) # 16進数
```

> 255
>
> 511
>
> 65535

> 255
>
> 511
>
> 65535

<a id="markdown-漢数字のキャスト" name="漢数字のキャスト"></a>

#### 漢数字のキャスト

<a id="markdown-1-文字の漢数字のキャスト" name="1-文字の漢数字のキャスト"></a>

##### 1 文字の漢数字のキャスト

```py
import unicodedata

print(unicodedata.numeric('五')) # 漢数字1文字ごとにキャスト
```

> 5.0

<a id="markdown-2-文字以上の漢数字のキャスト漢数字をアラビア数字に変換してから-int-型にキャスト" name="2-文字以上の漢数字のキャスト漢数字をアラビア数字に変換してから-int-型にキャスト"></a>

##### 2 文字以上の漢数字のキャスト(漢数字をアラビア数字に変換してから int 型にキャスト)

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

<a id="markdown-kanjize-パッケージを利用" name="kanjize-パッケージを利用"></a>

#### kanjize パッケージを利用

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

<a id="markdown-数値の切り上げ・切り捨て" name="数値の切り上げ・切り捨て"></a>

### 数値の切り上げ・切り捨て

```py
# round(7 / 3, 2) # だと、小数点以下2桁で2.33
round(7 / 3) # 四捨五入
7 // 3 # 切り捨て
int(7 / 3) # 切り捨て
-(-7 // 3) # 切り上げ

import math
math.floor(7 / 3) # 切り捨て
math.ceil(7 / 3) # 切り上げ
```

> 2
>
> 2
>
> 2
>
> 3

> 2
>
> 3

<a id="markdown-1-の補数2-の補数" name="1-の補数2-の補数"></a>

### 1 の補数、2 の補数

```py
x = -8

print(
    '{:>10}\n{:>10}\n{:>10}\n{:>10}'.format(
        x,
        bin(x),
        bin((x & 0b11111111) - 1),
        bin(x & 0b11111111)
    )
)
```

>         -8
>
> -0b1000
>
> 0b11110111
>
> 0b11111000

<a id="markdown-ビット演算" name="ビット演算"></a>

### ビット演算

<a id="markdown-左シフトゼロ埋め" name="左シフトゼロ埋め"></a>

#### 左シフト(ゼロ埋め)

```py
bin(0b0101 << 0)
bin(0b0101 << 1)
```

> '0b101'
>
> '0b1010'

<a id="markdown-右シフト切り捨て" name="右シフト切り捨て"></a>

#### 右シフト(切り捨て)

```py
bin(0b0111 >> 0)
bin(0b0111 >> 1)
```

> '0b111'
>
> '0b11'

<a id="markdown-and" name="and"></a>

#### AND

```py
bin(0b0 & 0b0)
bin(0b0 & 0b1)
bin(0b1 & 0b1)

bin(0b1100 & 0b1010) # 繰り上がりせず、各桁ごとにANDされる
```

> '0b0'
>
> '0b0'
>
> '0b1'
>
> '0b1000' \# 繰り上がりせず、各桁ごとに AND される

<a id="markdown-or" name="or"></a>

#### OR

```py
bin(0b0 | 0b0)
bin(0b0 | 0b1)
bin(0b1 | 0b1)

bin(0b1100 | 0b1010) # 繰り上がりせず、各桁ごとにORされる
```

> '0b0'
>
> '0b1'
>
> '0b1'
>
> '0b1110' \# 繰り上がりせず、各桁ごとに OR される

<a id="markdown-xor" name="xor"></a>

#### XOR

```py
bin(0b0 ^ 0b0)
bin(0b0 ^ 0b1)
bin(0b1 ^ 0b1)

bin(0b1100 ^ 0b1010) # 繰り上がりせず、各桁ごとにXORされる
```

> '0b0'
>
> '0b1'
>
> '0b0'
>
> '0b110' \# 繰り上がりせず、各桁ごとに OR される

<a id="markdown-float" name="float"></a>

## float

```py
f = 1.23
f = 1.2e3     # 1.2 * 10 ** 3
f = 1.2E-3    # 1.2 * 10 ** -3
```

<a id="markdown-文字列型からのキャスト-1" name="文字列型からのキャスト-1"></a>

### 文字列型からのキャスト

```py
s = '1.23'
if s.isnumeric():
    f = float(s)  # 文字列型からのキャスト
    print('{}'.format(f))

s = '.23'
if s.isnumeric():
    f = float(s)  # 文字列型からのキャスト
    print('{}'.format(f))
```

> \# '1'
>
> 1
>
> \# '10,000'

<a id="markdown-指数表記のキャスト" name="指数表記のキャスト"></a>

#### 指数表記のキャスト

```py
print(float('1.23e-4'))
```

> 0.000123

<a id="markdown-complex虚数" name="complex虚数"></a>

## complex(虚数)

```py
c = 1j
c = 2.3J
```

<a id="markdown-datetime" name="datetime"></a>

## datetime

<a id="markdown-日時の比較" name="日時の比較"></a>

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

> 365 days, 23:59:59
>
> 365
>
> 86399

> True
>
> False
>
> False

<a id="markdown-現在日時" name="現在日時"></a>

### 現在日時

```py
from datetime import datetime

dt = datetime.today()
print(dt)

dt = datetime.now()
print(dt)

print(type(dt))

print(dt.year)
print(dt.month)
print(dt.day)
print(dt.weekday())  # 0:月曜; 6:日曜
print(dt.isoweekday())  # 1:月曜; 7:日曜
print(dt.hour)
print(dt.minute)
print(dt.second)
print(dt.microsecond)
```

> 2019-08-02 08:34:17.354115 \# today()
>
> 2019-08-02 08:34:17.354115 \# now()
>
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

<a id="markdown-祝日判定" name="祝日判定"></a>

### 祝日判定

[emasaka/jpholidayp](https://github.com/emasaka/jpholidayp)

<a id="markdown-日付の生成" name="日付の生成"></a>

### 日付の生成

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

<a id="markdown-一定期間後の日付を生成" name="一定期間後の日付を生成"></a>

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

<a id="markdown-日時の要素を置換" name="日時の要素を置換"></a>

#### 日時の要素を置換

```py
from datetime import datetime
from datetime import timedelta

dt = datetime(2019, 8, 2)

# 日時の要素を置換
print(dt.replace(day=22))
```

> 2019-08-22 00:00:00

<a id="markdown-日付のリスト" name="日付のリスト"></a>

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

<a id="markdown-指定日までの残り期間を取得" name="指定日までの残り期間を取得"></a>

### 指定日までの残り期間を取得

```py
from datetime import datetime
from datetime import timedelta

td = datetime(2019, 12, 24) - datetime(2019, 8, 2, 9, 0, 0)
print(td)
```

> 143 days, 15:00:00

<a id="markdown-タイムゾーンを考慮した-datetime" name="タイムゾーンを考慮した-datetime"></a>

### タイムゾーンを考慮した datetime

<a id="markdown-datetime-パッケージの-timezone-モジュールを使用する場合" name="datetime-パッケージの-timezone-モジュールを使用する場合"></a>

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

<a id="markdown-生成" name="生成"></a>

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

<a id="markdown-タイムゾーンを変更変更前と同じ時刻" name="タイムゾーンを変更変更前と同じ時刻"></a>

##### タイムゾーンを変更(変更前と同じ時刻)

```py
print(datetime(2019, 8, 7, 6, 54, 32, 1000, tzinfo=timezone(timedelta(hours=9))).astimezone(timezone(timedelta(hours=8))))
# 2019-08-07 06:54:32.001000+09:00 → 2019-08-07 05:54:32.001000+08:00

# Python3.6以降の場合、naiveなdatetimeオブジェクトにもastimezone関数を実行できる(ローカルのタイムゾーンから変換される)
print(datetime(2019, 8, 7, 6, 54, 32, 1000).astimezone(timezone(timedelta(hours=8))))
# 2019-08-07 06:54:32.001000+09:00 → 2019-08-07 05:54:32.001000+08:00
```

<a id="markdown-タイムゾーンを置換変更前と異なる時刻" name="タイムゾーンを置換変更前と異なる時刻"></a>

##### タイムゾーンを置換(変更前と異なる時刻)

```py
print(datetime(2019, 8, 7, 6, 54, 32, 1000, tzinfo=timezone(timedelta(hours=9))).replace(tzinfo=timezone.utc))
# 2019-08-07 06:54:32.001000+09:00 → 2019-08-07 06:54:32.001000+00:00

# タイムゾーンの削除
print(datetime(2019, 8, 7, 6, 54, 32, 1000, tzinfo=timezone(timedelta(hours=9))).replace(tzinfo=None))
# 2019-08-07 06:54:32.001000+09:00 → 2019-08-07 06:54:32.001000

```

<a id="markdown-pytz-を使用する場合" name="pytz-を使用する場合"></a>

#### pytz を使用する場合

<a id="markdown-現在日時から生成" name="現在日時から生成"></a>

##### 現在日時から生成

```py
#  $ pip install pytz

from pytz import timezone
from datetime import datetime

# datetime.now()で取得した日時をJSTとする

print(datetime.now())
# 2019-08-07 12:45:18.487441

print(type(datetime.now()))
# <class 'datetime.datetime'>

print(timezone('UTC'))
# UTC
print(type(timezone('UTC')))
# <class 'pytz.UTC'>
print(type(timezone('Asia/Tokyo')))
# <class 'pytz.tzfile.Asia/Tokyo'>

print(datetime.now(timezone('UTC')))
# 2019-08-07 03:45:18.553981+00:00

print(datetime.now(tz=timezone('Europe/London')))
# 2019-08-07 04:45:18.553981+01:00

print(datetime.now(tz=timezone('Asia/Tokyo')))
# 2019-08-07 12:45:18.553981+09:00

print(datetime.now(timezone('UTC')).astimezone(timezone('Europe/London')))
# 2019-08-07 04:45:18.634371+01:00

print(datetime.now(timezone('UTC')).astimezone(timezone('Asia/Tokyo')))
# 2019-08-07 12:45:18.754351+09:00

#

print(timezone('Europe/London').localize(datetime.now()))
# 2019-08-07 12:45:20.011410+01:00

print(timezone('Asia/Tokyo').localize(datetime.now()))
# 2019-08-07 12:45:20.011410+09:00

#

print(timezone('UTC').localize(datetime.now()))
# 2019-08-07 12:45:18.760637+00:00

print(timezone('UTC').localize(datetime.now()).astimezone(timezone('Europe/London')))
# 2019-08-07 13:45:18.760637+09:00

print(timezone('UTC').localize(datetime.now()).astimezone(timezone('Asia/Tokyo')))
# 2019-08-07 21:45:18.760637+09:00
```

<a id="markdown-任意の日時を生成" name="任意の日時を生成"></a>

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

<a id="markdown-サマータイム終了時点を跨いだ日時の加算" name="サマータイム終了時点を跨いだ日時の加算"></a>

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

<a id="markdown-datetime-から-date" name="datetime-から-date"></a>

### datetime から date

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

<a id="markdown-datetime-から-str" name="datetime-から-str"></a>

### datetime から str

```py
from datetime import datetime
now = datetime.now().strftime('%Y%m%d%H%M%S')
print(now)

print(datetime.now().isoformat()) # ISO形式
```

> 20190730121658
>
> 2019-07-30T12:16:58.427664

<a id="markdown-str-から-datetimedate" name="str-から-datetimedate"></a>

### str から datetime、date

```py
from datetime import date
from datetime import datetime
tstr = '2019-07-30 12:16:58'
tdatetime = datetime.strptime(tstr, '%Y-%m-%d %H:%M:%S')
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

<a id="markdown-タイムゾーンを考慮した-str-から-datetime" name="タイムゾーンを考慮した-str-から-datetime"></a>

#### タイムゾーンを考慮した str から datetime

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

<a id="markdown-タイムゾーンを考慮した-iso-形式の-str-から-datetime" name="タイムゾーンを考慮した-iso-形式の-str-から-datetime"></a>

##### タイムゾーンを考慮した ISO 形式の str から datetime

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

<a id="markdown-日付時刻の-format-文字列に埋め込むディレクティブ" name="日付時刻の-format-文字列に埋め込むディレクティブ"></a>

#### 日付時刻の format 文字列に埋め込むディレクティブ

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

<a id="markdown-str文字列" name="str文字列"></a>

## str(文字列)

```py
print('str\nstr')
print("str\nstr")
print(r'str\nstr') # エスケープシーケンスが無視される
print(R'str\nstr') # エスケープシーケンスが無視される
print(str(123))
print('cq' * 3) # 文字列の繰り返し
print('cq' 'cq' 'cq') # 文字列を演算子なしでつなげる
```

> str
>
> str

> str
>
> str

> str\nstr

> str\nstr

> 123

> cqcqcq
>
> cqcqcq

<a id="markdown-ヒアドキュメント" name="ヒアドキュメント"></a>

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

<a id="markdown-文字種チェック" name="文字種チェック"></a>

### 文字種チェック

<a id="markdown-数値" name="数値"></a>

#### 数値

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

<a id="markdown-文字列のフォーマット" name="文字列のフォーマット"></a>

### 文字列のフォーマット

<a id="markdown-ゼロ埋め" name="ゼロ埋め"></a>

#### ゼロ埋め

```py
print('12345'.zfill(8))
print('1234567890'.zfill(8))
print('+1234'.zfill(8))
print('-1234'.zfill(8))
print('-a1234'.zfill(8)) # -の後ろに0埋め
print('xyz'.zfill(8))

print(str(12345).zfill(8))
```

> 00012345
>
> 1234567890
>
> +0001234
>
> -0001234
>
> -00a1234
>
> 00000xyz

> 00012345

```py
print('1234'.rjust(8, '0'))
print('1234'.ljust(8, '0'))
print('1234'.center(8, '0'))
print('-1234'.rjust(8, '0'))
print('-1234'.ljust(8, '0'))
print('-1234'.center(8, '0'))
```

> 00001234
>
> 12340000
>
> 00123400
>
> 000-1234
>
> -1234000
>
> 0-123400

<a id="markdown-format" name="format"></a>

#### format

<a id="markdown-整列" name="整列"></a>

##### 整列

```py
print('{}'.format(1))
print('{} {} {}'.format(1, 2, 3)) # 複数の値を埋め込む
print('{2} {0} {1}'.format(1, 2, 3)) # 埋め込み順序を指定する
print('{one} {three} {two}'.format(one=1, two=2, three=3)) # 埋め込み順序を指定する
print('{{}}'.format(1)) # {}自体を記述したい場合は2つ重ねる
```

> 1
>
> 1 2 3
>
> 3 1 2
>
> 1 3 2
>
> {}

```py
class MyClass:
    id = 1
    name = 'n1'

myClass = MyClass()
print('{0.id} {0.name}'.format(myClass)) # クラスの属性を指定する
```

> 1 n1 \# クラスの属性を指定する

```py
print('{:+}'.format(1)) # 正の数でも符号を表示

print('{:0=10}'.format(100)) # ゼロ埋め
print('{:010}'.format(100))
print('{:0=10}'.format(-100))
print('{:010}'.format(-100))

print('{:<10}'.format(1)) # 左寄せ

print('{:>10}'.format(1)) # 右寄せ
print('{:0>10}'.format(1))

print('{:^10}'.format(1)) # センタリング(中央寄せ)
print('{:0^10}'.format(1))
print('{:*^10}'.format(1))
```

> +1
>
> 0000000100
>
> 0000000100
>
> -000000100
>
> -000000100

> 1
>
>          1
>
> 0000000001
>
>     1
>
> 0000100000
>
> \***\*1\*\*\***

<a id="markdown-小数点以下の桁数" name="小数点以下の桁数"></a>

##### 小数点以下の桁数

```py
print('{:.0f}'.format(1.5))
print('{:.0f}'.format(2.5)) # 偶数への丸め(JIS Z 8401)なので、3ではなく2となる(round関数と同様)
```

> 2
>
> 2

<a id="markdown-桁区切り文字" name="桁区切り文字"></a>

##### 桁区切り文字

```py
print('{:,}'.format(1234567))
```

> 1,234,567

<a id="markdown-指数表記" name="指数表記"></a>

##### 指数表記

```py
print('{:.3e}'.format(1.234567))
```

> 1.235e+00

<a id="markdown-2-進数8-進数16-進数" name="2-進数8-進数16-進数"></a>

##### 2 進数、8 進数、16 進数

```py

print('{:d}'.format(255)) # 10進数
print('{:b}'.format(255)) # 2進数
print('{:o}'.format(255)) # 8進数
print('{:x}'.format(255)) # 16進数
print('{:#b}'.format(255)) # 接頭辞 + 2進数
print('{:#o}'.format(255)) # 接頭辞 + 8進数
print('{:#x}'.format(255)) # 接頭辞 + 16進数
```

> 255
>
> 11111111
>
> 377
>
> ff
>
> 0b11111111
>
> 0o377
>
> 0xff

<a id="markdown-リストの値を代入" name="リストの値を代入"></a>

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

<a id="markdown-タプルの値を代入" name="タプルの値を代入"></a>

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

<a id="markdown-辞書の値を代入" name="辞書の値を代入"></a>

##### 辞書の値を代入

```py
dct = { 'aaa':'first', 'bbb':'second', 'ccc':'third'}
mes = '{aaa}: {bbb}{ccc}'.format(**dct)
print(mes)
```

> first: secondthird

<a id="markdown-f-文字列" name="f-文字列"></a>

#### f 文字列

```py
one = 'first'
two = 2
three = '3rd'
mes = f'{one}: {two}{three}'
print(mes)
```

> first: 23rd

<a id="markdown-リストの値を代入-1" name="リストの値を代入-1"></a>

##### リストの値を代入

```py
lst = ['first', 'second', 'third']
mes = f'{lst[0]}: {lst[1]}{lst[2]}'
print(mes)
```

> first: secondthird

<a id="markdown-タプルの値を代入-1" name="タプルの値を代入-1"></a>

##### タプルの値を代入

```py
tpl = ('first', 'second', 'third')
mes = f'{tpl[0]}: {tpl[1]}{tpl[2]}'
print(mes)
```

> first: secondthird

<a id="markdown-辞書の値を代入-1" name="辞書の値を代入-1"></a>

##### 辞書の値を代入

`f""` の中では `"` は使えず、 `f''`の中では `'` は使えない(バックスラッシュでエスケープできない)

```py
dct = { 'aaa':'first', 'bbb':'second', 'ccc':'third'}
mes = f"{dct['aaa']}: {dct['bbb']}{dct['ccc']}"
print(mes)
```

> first: secondthird

<a id="markdown-フォーマット演算子" name="フォーマット演算子"></a>

#### フォーマット演算子

```py
print('%c' % 'A')  # 文字： A
print('%s' % 'ABC')  # 文字列： ABC
print('%r' % 'ABC')  # 文字列： ABC

print('%d' % 123)  # 整数： 123
print('%i' % 123)  # 整数： 123

print('%e' % 1.23)  # 指数： 1.230000e+00
print('%E' % 1.23)  # 指数： 1.230000E+00
print('%f' % 1.23)  # 実数： 1.23
print('%F' % 1.23)  # 実数： 1.23

print('%o' % 255)  # 8進数： 377
print('%b' % 255)  # 8進数： 377

print('%x' % 255)  # 16進数： ff
print('%X' % 255)  # 16進数： FF

print('%d%%' % 100)  # %自体： 100%
```

```py
print('|%5s|' % 'ABC')  # => |  ABC| : 右寄せ
print('|%-5s|' % 'ABC')  # => |ABC  | : 左寄せ
print('|%5d|' % 123)  # => |  123| : 右寄せ
print('|%-5d|' % 123)  # => |123  | : 左寄せ
print('|%+5d|' % 123)  # => | +123| : ±符号付き
print('|%5.2f|' % 1.23)  # => | 1.23| : 整数部の桁数.小数部の桁数
print('|%05d|' % 123)  # => |00123| : 0埋め
```

<a id="markdown-エスケープシーケンス" name="エスケープシーケンス"></a>

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

<a id="markdown-バイト列byte-unicode" name="バイト列byte-unicode"></a>

### バイト列(byte), Unicode

<a id="markdown-python-2" name="python-2"></a>

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

<a id="markdown-python-3" name="python-3"></a>

#### Python 3

```py
print('あいうえお')
print(len('あいうえお'))        # uをつけなくてもUnicodeとして扱われる
print(b'あいうえお')
print(len(b'あいうえお'))       # バイト列として扱われる
print(r'あいう\nえお')
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

<a id="markdown-文字列とバイト列の変換" name="文字列とバイト列の変換"></a>

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

<a id="markdown-区切り文字による分割" name="区切り文字による分割"></a>

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

<a id="markdown-split-の引数を指定しないと空白文字タブ文字改行文字を含むで分割される" name="split-の引数を指定しないと空白文字タブ文字改行文字を含むで分割される"></a>

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

<a id="markdown-split-で分割した後各要素の先頭・末尾の空白文字を除去する" name="split-で分割した後各要素の先頭・末尾の空白文字を除去する"></a>

#### split で分割した後、各要素の先頭・末尾の空白文字を除去する

```py
hoge = 'abc, def,\tghi'
parts = [x.strip() for x in hoge.split(',')]
print(parts)
```

> ['abc', 'def', 'ghi']

<a id="markdown-部分文字列" name="部分文字列"></a>

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

<a id="markdown-1-文字ずつ処理する" name="1-文字ずつ処理する"></a>

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

<a id="markdown-インデックスを取得" name="インデックスを取得"></a>

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

<a id="markdown-部分文字列を全パターン取得する" name="部分文字列を全パターン取得する"></a>

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

<a id="markdown-エンコード・デコード" name="エンコード・デコード"></a>

### エンコード・デコード

<a id="markdown-base64" name="base64"></a>

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

<a id="markdown-url-safe-な-base64" name="url-safe-な-base64"></a>

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

<a id="markdown-検索" name="検索"></a>

### 検索

<a id="markdown-単純な検索" name="単純な検索"></a>

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

<a id="markdown-前方一致" name="前方一致"></a>

##### 前方一致

```py
haystack = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
haystack.startswith('abc')
haystack.startswith('xyz')
```

> True
>
> False

<a id="markdown-後方一致" name="後方一致"></a>

##### 後方一致

```py
haystack = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
haystack.endswith('abc')
haystack.endswith('xyz')
```

> False
>
> True

<a id="markdown-正規表現による検索" name="正規表現による検索"></a>

#### 正規表現による検索

<a id="markdown-パターンのコンパイル" name="パターンのコンパイル"></a>

##### パターンのコンパイル

```py
import re
r = re.compile('(\w)')
```

<a id="markdown-文字列の先頭でマッチ" name="文字列の先頭でマッチ"></a>

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

> <\_sre.SRE_Match object; span=(0, 8), match='haystack'>
>
> <\_sre.SRE_Match object; span=(0, 8), match='haystack'>
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

<a id="markdown-グループ化" name="グループ化"></a>

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

<a id="markdown-文字列の途中でマッチした最初の箇所" name="文字列の途中でマッチした最初の箇所"></a>

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

> <\_sre.SRE_Match object; span=(0, 3), match='hay'>
>
> <\_sre.SRE_Match object; span=(0, 3), match='hay'>
>
> hay
>
> 0
>
> 3
>
> (0, 3)

<a id="markdown-文字列の途中でマッチした全ての箇所のリスト" name="文字列の途中でマッチした全ての箇所のリスト"></a>

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

<a id="markdown-文字列の途中でマッチした全ての箇所のイテレーター" name="文字列の途中でマッチした全ての箇所のイテレーター"></a>

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

<a id="markdown-フラグを利用" name="フラグを利用"></a>

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

> ['12345.67890']
>
> ['12345.67890']

<a id="markdown-文字種のフィルタリング" name="文字種のフィルタリング"></a>

#### 文字種のフィルタリング

<a id="markdown-文字列全体が半角英数だけ含まれているか検査" name="文字列全体が半角英数だけ含まれているか検査"></a>

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

<a id="markdown-半角カナなどが含まれていないか検査" name="半角カナなどが含まれていないか検査"></a>

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

<a id="markdown-文字種別のパターン" name="文字種別のパターン"></a>

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
| 漢字 (CJK 統合漢字) | `'[\u4E00-\u9FFF]+'`                                        |                |

<a id="markdown-置換" name="置換"></a>

### 置換

<a id="markdown-単純な置換" name="単純な置換"></a>

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

<a id="markdown-改行文字を除去" name="改行文字を除去"></a>

##### 改行文字を除去

```py
haystack = 'haystack\nhaystack\r\nhaystack'
replacement = ''

replacement.join(haystack.splitlines())
```

> 'haystackhaystackhaystack'

<a id="markdown-前後の空白文字を除去" name="前後の空白文字を除去"></a>

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

<a id="markdown-大文字化・小文字化" name="大文字化・小文字化"></a>

##### 大文字化・小文字化

```py
print('abcde'.upper())
print('ABCDE'.lower())
```

> ABCDE
>
> abcde

<a id="markdown-正規表現による置換" name="正規表現による置換"></a>

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

<a id="markdown-数字のみ抽出" name="数字のみ抽出"></a>

##### 数字のみ抽出

```py
# 正規表現操作のライブラリ
import re
content =  '123１２３一二三'
numstr = re.sub('\\D', '', content)
print(numstr)
```

> 123 １２３

<a id="markdown-ファイル名に使用できない文字を除去" name="ファイル名に使用できない文字を除去"></a>

##### ファイル名に使用できない文字を除去

```py
import re

haystack = 'foobar/hoge!piyo'
replacement = '-'

content = re.sub(r'[\\|/|:|?|.|"|<|>|\|]', replacement, haystack)
print(content)
```

> foobar-hoge!piyo

<a id="markdown-一文字ごとの置換" name="一文字ごとの置換"></a>

#### 一文字ごとの置換

```py
haystack = 'haystack'
print(haystack.translate(str.maketrans({'h': 'H', 'a': 'oo', 's': '', 'k': None})))
```

> Hooytooc

<a id="markdown-絵文字" name="絵文字"></a>

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

<a id="markdown-リスト" name="リスト"></a>

## リスト

```
[ ]:リスト, ( ):タプル, { }:セット/辞書
リストは変更可能
タプルは変更不可
```

<a id="markdown-リストが空か検査" name="リストが空か検査"></a>

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

<a id="markdown-リストを生成" name="リストを生成"></a>

### リストを生成

```py
# 空のリスト
lst = []
print(lst)
lst = [None] * 10
print(lst)
lst = [0] * 10
print(lst)


```

> []
>
> [None, None, None, None, None, None, None, None, None, None]
>
> [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

```py
# リストをコピー
oldlist = ['foo', 'bar', 'hoge']
newlist = list(oldlist)
print(newlist)

# タプルからリストを生成
tpllist = list(('foo', 'bar', 'hoge'))
print(tpllist)

# range()を使って連番の要素を持つリストを生成
rnglist = list(range(5))
print(rnglist)

# 文字列からリストを生成
strlist = list('abcdefg')
print(strlist)
```

> \# newlist
>
> ['foo', 'bar', 'hoge']
>
> \# tpllist
>
> ['foo', 'bar', 'hoge']
>
> \# rnglist
>
> [0, 1, 2, 3, 4]
>
> \# strlist
>
> ['a', 'b', 'c', 'd', 'e', 'f', 'g']

<a id="markdown-リストに要素を追加" name="リストに要素を追加"></a>

### リストに要素を追加

```py
# append(末尾に追加)
lst = ['foo', 'hoge']
lst.append('piyo')
print(lst)

# insert(添え字と要素の値を指定)
lst.insert(1, 'bar')
print(lst)

lst.append(['fu', 'ga']) # appendの引数にリストを指定すると、リスト自体が新たな要素になる
print(lst)

# スライスを使用して、別のリスト(別のイテラブルオブジェクト)の要素を指定位置に追加(連結)する
lst = ['foo', 'bar', 'hoge']
print(lst[0:len(lst)-1])
print(lst[0:len(lst)])

lst[len(lst):len(lst)] = ['fu', 'ga']
print(lst)

# 別のリスト(別のイテラブルオブジェクト)の要素を末尾に追加(連結)する
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

# リストの要素を繰り返す
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

> \# append
>
> ['foo', 'hoge', 'piyo']
>
> ['foo', 'bar', 'hoge', 'piyo']
>
> ['foo', 'bar', 'hoge', 'piyo', ['fu', 'ga']]
>
> \# スライス
>
> ['foo', 'bar']
>
> ['foo', 'bar', 'hoge']
>
> ['foo', 'bar', 'hoge', 'fu', 'ga']
>
> \# 別のリスト(別のイテラブルオブジェクト)の要素を追加(連結)する
>
> ['foo', 'bar', 'hoge', 'fu', 'ga']
>
> ['foo', 'bar', 'hoge', 'fu', 'ga', 'p', 'i', 'y', 'o']
>
> ['foo', 'bar', 'hoge', 'fu', 'ga', 'p', 'i', 'y', 'o', 'piyo']
>
> ['foo', 'bar', 'hoge', 'fu', 'ga']
>
> ['foo', 'bar', 'hoge', 'fu', 'ga', 'piyo']
>
> \# リストの要素を繰り返す
>
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

<a id="markdown-リストの要素を除去" name="リストの要素を除去"></a>

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

<a id="markdown-リストの反復処理" name="リストの反復処理"></a>

### リストの反復処理

<a id="markdown-インデックスを取得-1" name="インデックスを取得-1"></a>

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

<a id="markdown-複数のリストを同時に繰り返す" name="複数のリストを同時に繰り返す"></a>

#### 複数のリストを同時に繰り返す

```py
l1 = list(range(5))
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
l1 = list(range(5))
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

l1 = list(range(5))
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

<a id="markdown-多次元リスト" name="多次元リスト"></a>

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

<a id="markdown-リストの要素を連結した文字列を取得" name="リストの要素を連結した文字列を取得"></a>

#### リストの要素を連結した文字列を取得

```py
lst = ['foo', 'bar', 'hoge']
''.join(lst)
','.join(lst) # 区切り文字を指定
```

> 'foobarhoge'
>
> 'foo,bar,hoge'

<a id="markdown-リストをソート" name="リストをソート"></a>

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

<a id="markdown-ソート条件を変える" name="ソート条件を変える"></a>

#### ソート条件を変える

ラムダ式を指定すると、要素ごとに関数を実行した結果を基にソートされる

- 文字数でソート

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

- 末尾の文字のアルファベット順でソート

```py
lst = ['foo', 'bar', 'piyo', 'hoge', 'foo', 'bar', 'piyo', 'hoge']
sortedlist = sorted(lst, key=lambda x: x[-1:])
print(lst)
print(sortedlist)
```

> ['foo', 'bar', 'piyo', 'hoge', 'foo', 'bar', 'piyo', 'hoge']
>
> ['hoge', 'hoge', 'foo', 'piyo', 'foo', 'piyo', 'bar', 'bar']

<a id="markdown-リストの重複する要素を除去" name="リストの重複する要素を除去"></a>

### リストの重複する要素を除去

```py
# 順番を無視
l = ['foo', 'bar', 'hoge', 'foo', 'bar', 'hoge', 'foo', 'bar', 'hoge']
ls = list(set(l))
print(ls)

# 順番を保存
# Python 3.6以降
ld = list(dict.fromkeys(l))
print(ld)

# Python 3.5以前
ss = sorted(set(l), key=l.index)
print(ss)

# リストが入れ子の場合
def uniq(td):
    f = []
    return [i for i in td if i not in f and not f.append(i)]

l2d = [['foo'], ['bar'], ['hoge'], ['foo'], ['bar'], ['hoge'], ['foo'], ['bar'], ['hoge']]
uniql2d = uniq(l2d)
print(uniql2d)
```

> \# 順番を無視
>
> ['hoge', 'bar', 'foo']
>
> \# 順番を保存
>
> ['foo', 'bar', 'hoge']
>
> ['foo', 'bar', 'hoge']
>
> \# リストが入れ子の場合
>
> [['foo'], ['bar'], ['hoge']]

<a id="markdown-リストの重複する要素を抽出" name="リストの重複する要素を抽出"></a>

### リストの重複する要素を抽出

```py
# 順番を無視
l = ['foo', 'bar', 'hoge', 'foo', 'bar', 'hoge', 'foo', 'bar', 'hoge']
sc = [x for x in set(l) if l.count(x) > 1]
print(sc)

# 順番を保存
# Python 3.6以降
df = [x for x in dict.fromkeys(l) if l.count(x) > 1]
print(df)

# Python 3.5以前
sk = sorted([x for x in set(l) if l.count(x) > 1], key=l.index)
print(ss)
```

> \# 順番を無視
>
> ['hoge', 'bar', 'foo']
>
> \# 順番を保存
>
> ['foo', 'bar', 'hoge']
>
> ['foo', 'bar', 'hoge']

<a id="markdown-高階関数" name="高階関数"></a>

### 高階関数

<a id="markdown-map" name="map"></a>

#### map

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

<a id="markdown-filter" name="filter"></a>

#### filter

リストに対してフィルタリングする

```py
def isodd(x): return x % 2 # 条件式(True/Falseを返す)のlambda式

print(list(filter(isodd, numlist)))
print(list(filter(lambda x: x % 2, numlist)))
print([x for x in numlist if x % 2]) # 同じことを内包表記で行う
```

> [1, 3, 5]

<a id="markdown-reduce" name="reduce"></a>

#### reduce

リストに対する畳みこみ

```py
from functools import reduce

def add(x, y): return x + y

print(reduce(add, numlist))
print(reduce(lambda x, y: x + y, numlist))
```

> 15

<a id="markdown-リストの内包表記" name="リストの内包表記"></a>

### リストの内包表記

```py
l = list(range(100))

# 形式: [式 for 変数 in イテラブルオブジェクト if 条件式]

# 要素全てに処理を行う
strlist = [str(i) for i in l]
print(strlist)

# 条件に合致する要素のみからなるリストを生成(抽出)
fivelist = [i for i in l if i % 5 == 0 and i <= 50]
print(fivelist)

fivelist = [i  if i % 5 == 0 and i <= 50 else -1 for i in l] # elseがある場合は三項演算子なので順序が変わる
print(fivelist)

# 多次元リスト
[[i, j, i * j] for i in range(10) for j in range(10)]

# リストが入れ子の場合
def dupl(td):
    f = []
    return [i for i in td if td.count(i) > 1 and not f.append(i) and f.count(i) == 1]


l2d = [['foo'], ['bar'], ['hoge'], ['foo'], ['bar'], ['hoge'], ['foo'], ['bar'], ['hoge']]
dupll2d = dupl(l2d)
print(dupll2d)

```

> \# 要素全てに処理を行う
>
> ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99']
>
> \# 条件に合致する要素のみからなるリストを生成(抽出)
>
> [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
>
> [0, -1, -1, -1, -1, 5, -1, -1, -1, -1, 10, -1, -1, -1, -1, 15, -1, -1, -1, -1, 20, -1, -1, -1, -1, 25, -1, -1, -1, -1, 30, -1, -1, -1, -1, 35, -1, -1, -1, -1, 40, -1, -1, -1, -1, 45, -1, -1, -1, -1, 50, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
>
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
>
> \# リストが入れ子の場合
>
> [['foo'], ['bar'], ['hoge']]

<a id="markdown-リスト内包表記で-fizzbuzz" name="リスト内包表記で-fizzbuzz"></a>

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

<a id="markdown-辞書" name="辞書"></a>

## 辞書

<a id="markdown-追加・置換・削除" name="追加・置換・削除"></a>

### 追加・置換・削除

```py
dct = { 1:'first', 2:'two', 2:'second', 3:'third'}
# キーが同じ要素が追加されたら上書きされる(2:'two'ではなく2:'second'が残る)

# デバッグ表示
print(str(dct))
print('%s' % dct)

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

# 初期化(すべての要素を削除)
dct.clear()
dct = {}
```

> {1: 'first', 2: 'second', 3: 'third'}
>
> {1: 'first', 2: 'second', 3: 'third'}
>
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

<a id="markdown-辞書の要素を参照" name="辞書の要素を参照"></a>

### 辞書の要素を参照

```py
dct = { 'key1':'first', 'key2':'second', 'key3':'third'}

dct['key1']
dct.key1 # 辞書には使用できない(オブジェクトの属性を参照する際に使用)
```

> 'first'
>
> AttributeError: 'dict' object has no attribute 'key1'

<a id="markdown-辞書を生成リスト・タプルから変換／初期化" name="辞書を生成リスト・タプルから変換／初期化"></a>

### 辞書を生成(リスト・タプルから変換／初期化)

```py
dct = {}
dct = { 1:'first', 2:'second', 3:'third', }
print(dct)


# 辞書をコピー
olddict = { 1:'first', 2:'second', 3:'third'}
newdict = dict(olddict)
print(newdict)

# リストから生成
lst = [[1, 'first'], [2, 'second'], [3, 'third']]
dct = dict(lst)
print(dct)

# キーと値が別のリスト(要素数の少ないリストの要素数分だけ繰り返す)
keys = [1, 2, 3]
values = ['first', 'second', 'third']
dct = dict(zip(keys, values))
print(dct)

# キーと値が別のリスト(要素数の多いリストの要素数分だけ繰り返す)
from itertools import zip_longest
keys = [1, 2]
values = ['first', 'second', 'third']
dct = dict(zip_longest(keys, values, fillvalue=3))
print(dct)
```

> {1: 'first', 2: 'second', 3: 'third'}
>
> {1: 'first', 2: 'second', 3: 'third'}
>
> {1: 'first', 2: 'second', 3: 'third'}
>
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

<a id="markdown-辞書を結合" name="辞書を結合"></a>

### 辞書を結合

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

<a id="markdown-辞書のコピー" name="辞書のコピー"></a>

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

<a id="markdown-辞書の反復処理" name="辞書の反復処理"></a>

### 辞書の反復処理

<a id="markdown-インデックスとキー" name="インデックスとキー"></a>

#### インデックスとキー

```py
dct = { 'key1':'val1', 'key2':'val2', 'key3':'val3'}
for index, key in enumerate(dct):
    print(f'{index}: {key}')
```

> 0: key1
>
> 1: key2
>
> 2: key3

<a id="markdown-インデックスと値" name="インデックスと値"></a>

#### インデックスと値

```py
dct = { 'key1':'val1', 'key2':'val2', 'key3':'val3'}
for index, value in enumerate(dct.values()):
    print(f'{index}: {value}')
```

> 0: val1
>
> 1: val2
>
> 2: val3

<a id="markdown-インデックスと要素" name="インデックスと要素"></a>

#### インデックスと要素

```py
dct = { 'key1':'val1', 'key2':'val2', 'key3':'val3'}
for index, item in enumerate(dct.items()):
    print(f'{index}: {item}')
```

> 0: ('key1', 'val1')
>
> 1: ('key2', 'val2')
>
> 2: ('key3', 'val3')

<a id="markdown-複数の辞書を同時に繰り返す" name="複数の辞書を同時に繰り返す"></a>

#### 複数の辞書を同時に繰り返す

```py
dct1 = { 'key1-1':'val1-1', 'key1-2':'val1-2', 'key1-3':'val1-3'}
dct2 = { 'key2-1':'val2-1', 'key2-2':'val2-2', 'key2-3':'val2-3'}
for index, item in enumerate(zip(dct1, dct1.values(), dct1.items(), dct2, dct2.values(), dct2.items())):
    print(f'{index}: {item}')
```

> 0: ('key1-1', 'val1-1', ('key1-1', 'val1-1'), 'key2-1', 'val2-1', ('key2-1', 'val2-1'))
>
> 1: ('key1-2', 'val1-2', ('key1-2', 'val1-2'), 'key2-2', 'val2-2', ('key2-2', 'val2-2'))
>
> 2: ('key1-3', 'val1-3', ('key1-3', 'val1-3'), 'key2-3', 'val2-3', ('key2-3', 'val2-3'))

<a id="markdown-辞書の要素の存在チェック" name="辞書の要素の存在チェック"></a>

### 辞書の要素の存在チェック

```py
dct = { 1:'first', 2:'second', 3:'third', }
print(1 in dct) # キー
print(1 not in dct)

print('first' in dct) # 値
print('first' in dct.values())

print((1, 'first') in dct.items()) # キーと値
```

> True
>
> False
>
> False
>
> True
>
> True

<a id="markdown-指定した値を持つキーを取得する" name="指定した値を持つキーを取得する"></a>

### 指定した値を持つキーを取得する

```py
dct = { 1:'first', 2:'second', 3:'third', }
keys = [k for k, v in dct.items() if v == 'first' or v == 'second']
print(keys)
```

> [1, 2]

<a id="markdown-辞書のキーと値を交換" name="辞書のキーと値を交換"></a>

### 辞書のキーと値を交換

```py
dct1 = dict(('1f', '2s', '3t'))
dct2 = {v: k for k, v in dct1.items()}
print(dct2)
```

> {'f': '1', 's': '2', 't': '3'}

<a id="markdown-辞書の値でソート" name="辞書の値でソート"></a>

### 辞書の値でソート

```py
dct1 = dict(('1f', '4s', '3t'))
dct2 = sorted(dct1.items(), key=lambda x: x[1], reverse=True)
print(dct2)
```

> [('3', 't'), ('4', 's'), ('1', 'f')]

<a id="markdown-辞書の重複する要素を除去-todo" name="辞書の重複する要素を除去-todo"></a>

### 辞書の重複する要素を除去 #TODO

```py

```

>

<a id="markdown-辞書の内包表記" name="辞書の内包表記"></a>

### 辞書の内包表記

波括弧`{}`を使うと集合となる

```py
l = list(range(100))
strlist = [str(i) for i in l]

# {キー: 値 for 変数 in イテラブルオブジェクト}

# リストから辞書を生成
strdict = {li: str(li) for li in l}
print(strdict)

# 連番とリストの要素からなる辞書
values = ['first', 'second', 'third']
['{0}: {1}'.format(i + 100, values[i]) for i in range(len(values))]
['{0}: {1}'.format(i + 100, v) for i, v in enumerate(values)]

# キーと値が別のリスト
keys = [1, 2, 3]
values = ['first', 'second', 'third']
dct = {k: v for k, v in zip(keys, values)}
print(dct)

# 条件に合致する要素のみからなる辞書を生成(抽出)
fivedict = {k: v for k, v in zip(l, strlist) if k % 5 == 0 and k <= 50}
print(fivedict)

fivedict = {k: v if k % 5 == 0 and k <= 50 else -1 for k, v in zip(l, strlist)}
print(fivedict)

# 文字の出現頻度を数える
code = 'Lorem ipsum dolor sit amet, dico quidam percipitur mea no, labitur scaevola molestiae in vis, malis veniam tacimates mea cu.'
{letter: code.count(letter) for letter in code}

# 文字でソート
sorted({letter: code.count(letter) for letter in code}.items(), key=lambda x: x[0])

# 多い順にソート
sorted({letter: code.count(letter) for letter in code}.items(), key=lambda x: x[1], reverse=True)
```

> \# リストから辞書を生成
>
> {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10', 11: '11', 12: '12', 13: '13', 14: '14', 15: '15', 16: '16', 17: '17', 18: '18', 19: '19', 20: '20', 21: '21', 22: '22', 23: '23', 24: '24', 25: '25', 26: '26', 27: '27', 28: '28', 29: '29', 30: '30', 31: '31', 32: '32', 33: '33', 34: '34', 35: '35', 36: '36', 37: '37', 38: '38', 39: '39', 40: '40', 41: '41', 42: '42', 43: '43', 44: '44', 45: '45', 46: '46', 47: '47', 48: '48', 49: '49', 50: '50', 51: '51', 52: '52', 53: '53', 54: '54', 55: '55', 56: '56', 57: '57', 58: '58', 59: '59', 60: '60', 61: '61', 62: '62', 63: '63', 64: '64', 65: '65', 66: '66', 67: '67', 68: '68', 69: '69', 70: '70', 71: '71', 72: '72', 73: '73', 74: '74', 75: '75', 76: '76', 77: '77', 78: '78', 79: '79', 80: '80', 81: '81', 82: '82', 83: '83', 84: '84', 85: '85', 86: '86', 87: '87', 88: '88', 89: '89', 90: '90', 91: '91', 92: '92', 93: '93', 94: '94', 95: '95', 96: '96', 97: '97', 98: '98', 99: '99'}
>
> \# 連番とリストの要素からなる辞書
>
> ['100: first', '101: second', '102: third']
>
> ['100: first', '101: second', '102: third']
>
> \# キーと値が別のリスト
>
> {1: 'first', 2: 'second', 3: 'third'}
>
> \# 条件に合致する要素のみからなる辞書を生成(抽出)
>
> {0: '0', 5: '5', 10: '10', 15: '15', 20: '20', 25: '25', 30: '30', 35: '35', 40: '40', 45: '45', 50: '50'}
>
> {0: '0', 1: -1, 2: -1, 3: -1, 4: -1, 5: '5', 6: -1, 7: -1, 8: -1, 9: -1, 10: '10', 11: -1, 12: -1, 13: -1, 14: -1, 15: '15', 16: -1, 17: -1, 18: -1, 19: -1, 20: '20', 21: -1, 22: -1, 23: -1, 24: -1, 25: '25', 26: -1, 27: -1, 28: -1, 29: -1, 30: '30', 31: -1, 32: -1, 33: -1, 34: -1, 35: '35', 36: -1, 37: -1, 38: -1, 39: -1, 40: '40', 41: -1, 42: -1, 43: -1, 44: -1, 45: '45', 46: -1, 47: -1, 48: -1, 49: -1, 50: '50', 51: -1, 52: -1, 53: -1, 54: -1, 55: -1, 56: -1, 57: -1, 58: -1, 59: -1, 60: -1, 61: -1, 62: -1, 63: -1, 64: -1, 65: -1, 66: -1, 67: -1, 68: -1, 69: -1, 70: -1, 71: -1, 72: -1, 73: -1, 74: -1, 75: -1, 76: -1, 77: -1, 78: -1, 79: -1, 80: -1, 81: -1, 82: -1, 83: -1, 84: -1, 85: -1, 86: -1, 87: -1, 88: -1, 89: -1, 90: -1, 91: -1, 92: -1, 93: -1, 94: -1, 95: -1, 96: -1, 97: -1, 98: -1, 99: -1}
>
> \# 文字の出現頻度を数える
>
> {'L': 1, 'o': 7, 'r': 5, 'e': 10, 'm': 10, ' ': 19, 'i': 13, 'p': 3, 's': 7, 'u': 5, 'd': 3, 'l': 5, 't': 7, 'a': 12, ',': 3, 'c': 5, 'q': 1, 'n': 3, 'b': 1, 'v': 3, '.': 1}
>
> \# 文字でソート
>
> [(' ', 19), (',', 3), ('.', 1), ('L', 1), ('a', 12), ('b', 1), ('c', 5), ('d', 3), ('e', 10), ('i', 13), ('l', 5), ('m', 10), ('n', 3), ('o', 7), ('p', 3), ('q', 1), ('r', 5), ('s', 7), ('t', 7), ('u', 5), ('v', 3)]
>
> \# 多い順にソート
>
> [(' ', 19), ('i', 13), ('a', 12), ('e', 10), ('m', 10), ('o', 7), ('s', 7), ('t', 7), ('r', 5), ('u', 5), ('l', 5), ('c', 5), ('p', 3), ('d', 3), (',', 3), ('n', 3), ('v', 3), ('L', 1), ('q', 1), ('b', 1), ('.', 1)]

<a id="markdown-タプル" name="タプル"></a>

## タプル

<a id="markdown-タプルを生成" name="タプルを生成"></a>

### タプルを生成

タプルは変更不可

```py
# 空のタプル
empty = ()

# 1要素のタプルを宣言するときは後ろにカンマをつける
t = 'hoge',
t = 'hoge'  # カンマをつけないとただの変数

t = 'foo', 'bar', 123, 456

# デバッグ表示
print(str(t))
print('%s' % (t,)) # print('%s' % t)とするとTypeError: not all arguments converted during string formatting

t[2]

# リストからタプルを生成
print(tuple([1, 2, 3]))  # リストからタプル
print(list((1, 2, 3))  # タプルからリスト
```

> ('foo', 'bar', 123, 456)
>
> ('foo', 'bar', 123, 456)

> 123

> (1, 2, 3)
>
> [1, 2, 3]

<a id="markdown-タプルの反復処理" name="タプルの反復処理"></a>

### タプルの反復処理

<a id="markdown-インデックスを取得-2" name="インデックスを取得-2"></a>

#### インデックスを取得

```py
t = tuple(range(5, 10))
for (index, item) in enumerate(t):
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

<a id="markdown-タプルの入れ子" name="タプルの入れ子"></a>

### タプルの入れ子

```py
t = t, ('piyo', 789)
print(t)
```

> (('foo', 'bar', 123, 456), ('piyo', 789))

<a id="markdown-多重タプルをフラット化flatten" name="多重タプルをフラット化flatten"></a>

#### 多重タプルをフラット化(flatten)

<a id="markdown-2-重タプル" name="2-重タプル"></a>

##### 2 重タプル

```py
t = ((3, 1, 4), (1, 5, 9), (2, 6, 5))
print(t)

res = [ f for i in t for flattfen in i ]
print(tuple(res))
# or
res = ()
for rows in t:
    res = res + rows

print(res)
```

<a id="markdown-多重タプル" name="多重タプル"></a>

##### 多重タプル

```py
#TODO
```

<a id="markdown-シーケンス・アンパッキング" name="シーケンス・アンパッキング"></a>

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

<a id="markdown-タプルの内包表記" name="タプルの内包表記"></a>

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

<a id="markdown-セット" name="セット"></a>

## セット

<a id="markdown-セットを生成" name="セットを生成"></a>

### セットを生成

重複する要素があれば削除される

```py
s1 = {'ab', 'cd', 'ab', 'cd'}
print(s1)

ls2 = ['ab', 'cd', 'ef', 'cd']
s2 = set(ls2)
print(s2)
```

> {'ab', 'cd'}
>
> {'ef', 'ab', 'cd'}

<a id="markdown-セットの要素の存在チェック" name="セットの要素の存在チェック"></a>

### セットの要素の存在チェック

```py
s1 = {'ab', 'cd', 'ab', 'cd'}
print('ab' in s1)
```

> True

<a id="markdown-セットの要素を追加する" name="セットの要素を追加する"></a>

### セットの要素を追加する

```py
s1 = {'ab', 'cd'}
s1.add('yz')
print(s1)
```

> {'ab', 'yz', 'cd'}

<a id="markdown-セットの演算" name="セットの演算"></a>

### セットの演算

```py
s1 = {'ab', 'cd'}
s1 = {'ef', 'ab', 'cd'}

print(s1)
print(s2)
print(s1 - s2)
print(s1 | s2)
print(s1 & s2)
print(s1 ^ s2)
```

> {'ab', 'cd'}
>
> {'ef', 'ab', 'cd'}
>
> set()
>
> {'ab', 'cd', 'ef'}
>
> {'ab', 'cd'}
>
> {'ef'}

<a id="markdown-順序つき辞書ordereddict" name="順序つき辞書ordereddict"></a>

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

<a id="markdown-制御構文" name="制御構文"></a>

# 制御構文

<a id="markdown-if" name="if"></a>

## if

```py
if x < 0:
    print('N')
elif x == 0: # else if
    print('0')
else:
    print('P')
```

<a id="markdown-for" name="for"></a>

## for

```py
for i in range(3):
    j = i + 1
    print(' ' + str(i) + ' ,')

for i in range(5, 8):
    j = i + 1
    print(' ' + str(i) + ' ,')

# Pythonではループ変数やループ内で定義された変数を、ループの外でも参照できる
print(', ' + str(i) + ' ' + str(j))
```

<a id="markdown-forリストを与える場合" name="forリストを与える場合"></a>

### for(リストを与える場合)

```py
l = ['foo', 'bar', 123, 456]
for x in l:
    print(str(x))
```

<a id="markdown-forタプルを与える場合" name="forタプルを与える場合"></a>

### for(タプルを与える場合)

```py
t = ('foo', 'bar', 123, 456)
for x in t:
    print(str(x))
```

<a id="markdown-for辞書を与える場合" name="for辞書を与える場合"></a>

### for(辞書を与える場合)

```py
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
```

<a id="markdown-for試行回数を与える場合" name="for試行回数を与える場合"></a>

### for(試行回数を与える場合)

```py
for i in range(4):
    print(i)    # 0 1 2 3
for i in range(5, 21, 5):
    print(i)    # 5 10 15 20
```

<a id="markdown-for-文の-else-節" name="for-文の-else-節"></a>

### for 文の else 節

```py
for i in range(5):
    print(i)
else:
    # ループを抜けたときに実行される
    print('else')
```

> 0
>
> 1
>
> 2
>
> 3
>
> 4
>
> else

```py
for i in (0, 1, 2):
    print(i)
```

> 0
>
> 1
>
> 2

```py
for k in {'k1': 1, 'k2': 2, 'k3': 3}:
    print(k)
```

> k1
>
> k2
>
> k3

```py
for c in '012':
    print(c)
```

> 0
>
> 1
>
> 2

```py
for line in open('grammer.py', encoding='utf8'):
    print(line)
    # 1行ずつ標準出力
```

```py
# keyとvalueを一緒に取得する
for k, v in enumerate(['v1', 'v2', 'v3']):
    print(k, v)
```

> 0 v1
>
> 1 v2
>
> 2 v3

```py
# 途中でループから脱出
for i in range(5):
    if i > 3:
        break
    print(i)
```

> 0
>
> 1
>
> 2
>
> 3

<a id="markdown-スキップするcontinue" name="スキップするcontinue"></a>

### スキップする(continue)

```py
for i in range(5):
    if i == 3:
        continue
    print(i)
```

> 0
>
> 1
>
> 2
>
> 4

<a id="markdown-itertools" name="itertools"></a>

### itertools

```py
import itertools
for x, y,z in itertools.product(range(10), range(10), range(10)):
  print('%d,%d,%d' % (x,y,z))
```

```
0,0,0
0,0,1
0,0,2
0,0,3
0,0,4
0,0,5
0,0,6
0,0,7
0,0,8
0,0,9
0,1,0
0,1,1
0,1,2
0,1,3
0,1,4
0,1,5
0,1,6
0,1,7
0,1,8
0,1,9
0,2,0
0,2,1
0,2,2
0,2,3
0,2,4
0,2,5
0,2,6
0,2,7
0,2,8
0,2,9
0,3,0
0,3,1
0,3,2
0,3,3
0,3,4
0,3,5
0,3,6
0,3,7
0,3,8
0,3,9
0,4,0
0,4,1
0,4,2
0,4,3
0,4,4
0,4,5
0,4,6
0,4,7
0,4,8
0,4,9
0,5,0
0,5,1
0,5,2
0,5,3
0,5,4
0,5,5
0,5,6
0,5,7
0,5,8
0,5,9
0,6,0
0,6,1
0,6,2
0,6,3
0,6,4
0,6,5
0,6,6
0,6,7
0,6,8
0,6,9
0,7,0
0,7,1
0,7,2
0,7,3
0,7,4
0,7,5
0,7,6
0,7,7
0,7,8
0,7,9
0,8,0
0,8,1
0,8,2
0,8,3
0,8,4
0,8,5
0,8,6
0,8,7
0,8,8
0,8,9
0,9,0
0,9,1
0,9,2
0,9,3
0,9,4
0,9,5
0,9,6
0,9,7
0,9,8
0,9,9
1,0,0
1,0,1
1,0,2
1,0,3
1,0,4
1,0,5
1,0,6
1,0,7
1,0,8
1,0,9
1,1,0
1,1,1
1,1,2
1,1,3
1,1,4
1,1,5
1,1,6
1,1,7
1,1,8
1,1,9
1,2,0
1,2,1
1,2,2
1,2,3
1,2,4
1,2,5
1,2,6
1,2,7
1,2,8
1,2,9
1,3,0
1,3,1
1,3,2
1,3,3
1,3,4
1,3,5
1,3,6
1,3,7
1,3,8
1,3,9
1,4,0
1,4,1
1,4,2
1,4,3
1,4,4
1,4,5
1,4,6
1,4,7
1,4,8
1,4,9
1,5,0
1,5,1
1,5,2
1,5,3
1,5,4
1,5,5
1,5,6
1,5,7
1,5,8
1,5,9
1,6,0
1,6,1
1,6,2
1,6,3
1,6,4
1,6,5
1,6,6
1,6,7
1,6,8
1,6,9
1,7,0
1,7,1
1,7,2
1,7,3
1,7,4
1,7,5
1,7,6
1,7,7
1,7,8
1,7,9
1,8,0
1,8,1
1,8,2
1,8,3
1,8,4
1,8,5
1,8,6
1,8,7
1,8,8
1,8,9
1,9,0
1,9,1
1,9,2
1,9,3
1,9,4
1,9,5
1,9,6
1,9,7
1,9,8
1,9,9
2,0,0
2,0,1
2,0,2
2,0,3
2,0,4
2,0,5
2,0,6
2,0,7
2,0,8
2,0,9
2,1,0
2,1,1
2,1,2
2,1,3
2,1,4
2,1,5
2,1,6
2,1,7
2,1,8
2,1,9
2,2,0
2,2,1
2,2,2
2,2,3
2,2,4
2,2,5
2,2,6
2,2,7
2,2,8
2,2,9
2,3,0
2,3,1
2,3,2
2,3,3
2,3,4
2,3,5
2,3,6
2,3,7
2,3,8
2,3,9
2,4,0
2,4,1
2,4,2
2,4,3
2,4,4
2,4,5
2,4,6
2,4,7
2,4,8
2,4,9
2,5,0
2,5,1
2,5,2
2,5,3
2,5,4
2,5,5
2,5,6
2,5,7
2,5,8
2,5,9
2,6,0
2,6,1
2,6,2
2,6,3
2,6,4
2,6,5
2,6,6
2,6,7
2,6,8
2,6,9
2,7,0
2,7,1
2,7,2
2,7,3
2,7,4
2,7,5
2,7,6
2,7,7
2,7,8
2,7,9
2,8,0
2,8,1
2,8,2
2,8,3
2,8,4
2,8,5
2,8,6
2,8,7
2,8,8
2,8,9
2,9,0
2,9,1
2,9,2
2,9,3
2,9,4
2,9,5
2,9,6
2,9,7
2,9,8
2,9,9
3,0,0
3,0,1
3,0,2
3,0,3
3,0,4
3,0,5
3,0,6
3,0,7
3,0,8
3,0,9
3,1,0
3,1,1
3,1,2
3,1,3
3,1,4
3,1,5
3,1,6
3,1,7
3,1,8
3,1,9
3,2,0
3,2,1
3,2,2
3,2,3
3,2,4
3,2,5
3,2,6
3,2,7
3,2,8
3,2,9
3,3,0
3,3,1
3,3,2
3,3,3
3,3,4
3,3,5
3,3,6
3,3,7
3,3,8
3,3,9
3,4,0
3,4,1
3,4,2
3,4,3
3,4,4
3,4,5
3,4,6
3,4,7
3,4,8
3,4,9
3,5,0
3,5,1
3,5,2
3,5,3
3,5,4
3,5,5
3,5,6
3,5,7
3,5,8
3,5,9
3,6,0
3,6,1
3,6,2
3,6,3
3,6,4
3,6,5
3,6,6
3,6,7
3,6,8
3,6,9
3,7,0
3,7,1
3,7,2
3,7,3
3,7,4
3,7,5
3,7,6
3,7,7
3,7,8
3,7,9
3,8,0
3,8,1
3,8,2
3,8,3
3,8,4
3,8,5
3,8,6
3,8,7
3,8,8
3,8,9
3,9,0
3,9,1
3,9,2
3,9,3
3,9,4
3,9,5
3,9,6
3,9,7
3,9,8
3,9,9
4,0,0
4,0,1
4,0,2
4,0,3
4,0,4
4,0,5
4,0,6
4,0,7
4,0,8
4,0,9
4,1,0
4,1,1
4,1,2
4,1,3
4,1,4
4,1,5
4,1,6
4,1,7
4,1,8
4,1,9
4,2,0
4,2,1
4,2,2
4,2,3
4,2,4
4,2,5
4,2,6
4,2,7
4,2,8
4,2,9
4,3,0
4,3,1
4,3,2
4,3,3
4,3,4
4,3,5
4,3,6
4,3,7
4,3,8
4,3,9
4,4,0
4,4,1
4,4,2
4,4,3
4,4,4
4,4,5
4,4,6
4,4,7
4,4,8
4,4,9
4,5,0
4,5,1
4,5,2
4,5,3
4,5,4
4,5,5
4,5,6
4,5,7
4,5,8
4,5,9
4,6,0
4,6,1
4,6,2
4,6,3
4,6,4
4,6,5
4,6,6
4,6,7
4,6,8
4,6,9
4,7,0
4,7,1
4,7,2
4,7,3
4,7,4
4,7,5
4,7,6
4,7,7
4,7,8
4,7,9
4,8,0
4,8,1
4,8,2
4,8,3
4,8,4
4,8,5
4,8,6
4,8,7
4,8,8
4,8,9
4,9,0
4,9,1
4,9,2
4,9,3
4,9,4
4,9,5
4,9,6
4,9,7
4,9,8
4,9,9
5,0,0
5,0,1
5,0,2
5,0,3
5,0,4
5,0,5
5,0,6
5,0,7
5,0,8
5,0,9
5,1,0
5,1,1
5,1,2
5,1,3
5,1,4
5,1,5
5,1,6
5,1,7
5,1,8
5,1,9
5,2,0
5,2,1
5,2,2
5,2,3
5,2,4
5,2,5
5,2,6
5,2,7
5,2,8
5,2,9
5,3,0
5,3,1
5,3,2
5,3,3
5,3,4
5,3,5
5,3,6
5,3,7
5,3,8
5,3,9
5,4,0
5,4,1
5,4,2
5,4,3
5,4,4
5,4,5
5,4,6
5,4,7
5,4,8
5,4,9
5,5,0
5,5,1
5,5,2
5,5,3
5,5,4
5,5,5
5,5,6
5,5,7
5,5,8
5,5,9
5,6,0
5,6,1
5,6,2
5,6,3
5,6,4
5,6,5
5,6,6
5,6,7
5,6,8
5,6,9
5,7,0
5,7,1
5,7,2
5,7,3
5,7,4
5,7,5
5,7,6
5,7,7
5,7,8
5,7,9
5,8,0
5,8,1
5,8,2
5,8,3
5,8,4
5,8,5
5,8,6
5,8,7
5,8,8
5,8,9
5,9,0
5,9,1
5,9,2
5,9,3
5,9,4
5,9,5
5,9,6
5,9,7
5,9,8
5,9,9
6,0,0
6,0,1
6,0,2
6,0,3
6,0,4
6,0,5
6,0,6
6,0,7
6,0,8
6,0,9
6,1,0
6,1,1
6,1,2
6,1,3
6,1,4
6,1,5
6,1,6
6,1,7
6,1,8
6,1,9
6,2,0
6,2,1
6,2,2
6,2,3
6,2,4
6,2,5
6,2,6
6,2,7
6,2,8
6,2,9
6,3,0
6,3,1
6,3,2
6,3,3
6,3,4
6,3,5
6,3,6
6,3,7
6,3,8
6,3,9
6,4,0
6,4,1
6,4,2
6,4,3
6,4,4
6,4,5
6,4,6
6,4,7
6,4,8
6,4,9
6,5,0
6,5,1
6,5,2
6,5,3
6,5,4
6,5,5
6,5,6
6,5,7
6,5,8
6,5,9
6,6,0
6,6,1
6,6,2
6,6,3
6,6,4
6,6,5
6,6,6
6,6,7
6,6,8
6,6,9
6,7,0
6,7,1
6,7,2
6,7,3
6,7,4
6,7,5
6,7,6
6,7,7
6,7,8
6,7,9
6,8,0
6,8,1
6,8,2
6,8,3
6,8,4
6,8,5
6,8,6
6,8,7
6,8,8
6,8,9
6,9,0
6,9,1
6,9,2
6,9,3
6,9,4
6,9,5
6,9,6
6,9,7
6,9,8
6,9,9
7,0,0
7,0,1
7,0,2
7,0,3
7,0,4
7,0,5
7,0,6
7,0,7
7,0,8
7,0,9
7,1,0
7,1,1
7,1,2
7,1,3
7,1,4
7,1,5
7,1,6
7,1,7
7,1,8
7,1,9
7,2,0
7,2,1
7,2,2
7,2,3
7,2,4
7,2,5
7,2,6
7,2,7
7,2,8
7,2,9
7,3,0
7,3,1
7,3,2
7,3,3
7,3,4
7,3,5
7,3,6
7,3,7
7,3,8
7,3,9
7,4,0
7,4,1
7,4,2
7,4,3
7,4,4
7,4,5
7,4,6
7,4,7
7,4,8
7,4,9
7,5,0
7,5,1
7,5,2
7,5,3
7,5,4
7,5,5
7,5,6
7,5,7
7,5,8
7,5,9
7,6,0
7,6,1
7,6,2
7,6,3
7,6,4
7,6,5
7,6,6
7,6,7
7,6,8
7,6,9
7,7,0
7,7,1
7,7,2
7,7,3
7,7,4
7,7,5
7,7,6
7,7,7
7,7,8
7,7,9
7,8,0
7,8,1
7,8,2
7,8,3
7,8,4
7,8,5
7,8,6
7,8,7
7,8,8
7,8,9
7,9,0
7,9,1
7,9,2
7,9,3
7,9,4
7,9,5
7,9,6
7,9,7
7,9,8
7,9,9
8,0,0
8,0,1
8,0,2
8,0,3
8,0,4
8,0,5
8,0,6
8,0,7
8,0,8
8,0,9
8,1,0
8,1,1
8,1,2
8,1,3
8,1,4
8,1,5
8,1,6
8,1,7
8,1,8
8,1,9
8,2,0
8,2,1
8,2,2
8,2,3
8,2,4
8,2,5
8,2,6
8,2,7
8,2,8
8,2,9
8,3,0
8,3,1
8,3,2
8,3,3
8,3,4
8,3,5
8,3,6
8,3,7
8,3,8
8,3,9
8,4,0
8,4,1
8,4,2
8,4,3
8,4,4
8,4,5
8,4,6
8,4,7
8,4,8
8,4,9
8,5,0
8,5,1
8,5,2
8,5,3
8,5,4
8,5,5
8,5,6
8,5,7
8,5,8
8,5,9
8,6,0
8,6,1
8,6,2
8,6,3
8,6,4
8,6,5
8,6,6
8,6,7
8,6,8
8,6,9
8,7,0
8,7,1
8,7,2
8,7,3
8,7,4
8,7,5
8,7,6
8,7,7
8,7,8
8,7,9
8,8,0
8,8,1
8,8,2
8,8,3
8,8,4
8,8,5
8,8,6
8,8,7
8,8,8
8,8,9
8,9,0
8,9,1
8,9,2
8,9,3
8,9,4
8,9,5
8,9,6
8,9,7
8,9,8
8,9,9
9,0,0
9,0,1
9,0,2
9,0,3
9,0,4
9,0,5
9,0,6
9,0,7
9,0,8
9,0,9
9,1,0
9,1,1
9,1,2
9,1,3
9,1,4
9,1,5
9,1,6
9,1,7
9,1,8
9,1,9
9,2,0
9,2,1
9,2,2
9,2,3
9,2,4
9,2,5
9,2,6
9,2,7
9,2,8
9,2,9
9,3,0
9,3,1
9,3,2
9,3,3
9,3,4
9,3,5
9,3,6
9,3,7
9,3,8
9,3,9
9,4,0
9,4,1
9,4,2
9,4,3
9,4,4
9,4,5
9,4,6
9,4,7
9,4,8
9,4,9
9,5,0
9,5,1
9,5,2
9,5,3
9,5,4
9,5,5
9,5,6
9,5,7
9,5,8
9,5,9
9,6,0
9,6,1
9,6,2
9,6,3
9,6,4
9,6,5
9,6,6
9,6,7
9,6,8
9,6,9
9,7,0
9,7,1
9,7,2
9,7,3
9,7,4
9,7,5
9,7,6
9,7,7
9,7,8
9,7,9
9,8,0
9,8,1
9,8,2
9,8,3
9,8,4
9,8,5
9,8,6
9,8,7
9,8,8
9,8,9
9,9,0
9,9,1
9,9,2
9,9,3
9,9,4
9,9,5
9,9,6
9,9,7
9,9,8
9,9,9
```

<a id="markdown-while" name="while"></a>

## while

```py
i = 0
while i < 10:
    i += 1
    if i == 3:
        continue
    print(i)
else:
    print('-1')
```

> 1
>
> 2
>
> 4
>
> 5
>
> 6
>
> 7
>
> 8
>
> 9
>
> 10
>
> -1

<a id="markdown-try例外処理" name="try例外処理"></a>

## try(例外処理)

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

<a id="markdown-評価" name="評価"></a>

## 評価

<a id="markdown-eval" name="eval"></a>

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
result = eval('a + b', {'a': 1, 'b': 2})
print(result)
result = eval('a + b', {'a': 3, 'b': 4}, {'a': 1, 'b': 2})
print(result)
```

> 3
>
> 3

```py
result = eval(compile('1 + 2', '<string>', 'eval'))
print(result)
```

> 3

<a id="markdown-exec" name="exec"></a>

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

<a id="markdown-グローバル名前空間の参照・変更を制限" name="グローバル名前空間の参照・変更を制限"></a>

### グローバル名前空間の参照・変更を制限

```py
exec('import os;os.system("echo foobar")', {}, {})

exec('import os;os.system("echo foobar")', {'__builtins__':None}, {})
```

> foobar
>
> ImportError: **import** not found

<a id="markdown-assertアサーション" name="assertアサーション"></a>

## assert(アサーション)

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

<a id="markdown-del" name="del"></a>

## del

オブジェクトを削除

```py
s = 'foo'
i = [1, 2, 3]
b = Bar()
del s, i, b
```

<a id="markdown-exitプログラム実行を終了" name="exitプログラム実行を終了"></a>

## exit(プログラム実行を終了)

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

>

<a id="markdown-pass" name="pass"></a>

## pass

空の関数や空の型を定義する

```py
def empty_func():
    pass


class EmptyClass:
    pass
```

<a id="markdown-with" name="with"></a>

## with

with ブロックが終了するとオブジェクトの終了処理が自動的に呼ばれる

```py
with open(filepath, 'w') as f:
    pass
```

<a id="markdown-複数の-with-をまとめる" name="複数の-with-をまとめる"></a>

### 複数の with をまとめる

入力ファイルと出力ファイルを同時に開く場合など、複数の with ブロックによってネストが深くなってしまうのを防ぐために、「,」で区切って 1 つの with ブロックにまとめることができる

```py
with open(filepath1, 'r') as f1:
    with open(filepath2, 'w') as f2:
        pass

with open(filepath1, 'r') as f1, with open(filepath2, 'w') as f2:
    pass
```

<a id="markdown-関数" name="関数"></a>

# 関数

<a id="markdown-引数なし" name="引数なし"></a>

## 引数なし

```py
# 定義
def func1():
    print('hello')

# 呼出
func1()
```

<a id="markdown-引数あり" name="引数あり"></a>

## 引数あり

```py
# 定義
def func2(arg):
    print(arg)

# 呼出
func2('hello')
```

<a id="markdown-既定値を持つ引数あり" name="既定値を持つ引数あり"></a>

## 既定値を持つ引数あり

```py
# 定義
def func3(arg='bye'):
    print(arg)

# 呼出
func3()
func3(arg='hi')
```

<a id="markdown-戻り値あり" name="戻り値あり"></a>

## 戻り値あり

```py
# 定義
def func4(arg):
    return arg

# 呼出
print(func4('hello'))
```

<a id="markdown-docstring-あり" name="docstring-あり"></a>

## docstring あり

```py
# 定義
def func5():
    '''helloと表示する関数'''
    print('hello')

# 呼出
func5()
```

<a id="markdown-ヘルプを表示" name="ヘルプを表示"></a>

### ヘルプを表示

```py
help(func5)
```

<a id="markdown-タプルと辞書を受け取る" name="タプルと辞書を受け取る"></a>

## タプルと辞書を受け取る

```py
# 定義
def func_vl(arg, *t, **d):
    for val in t:
        print(val)
    keys = sorted(d.keys())
    for val in keys:
        print(val)

# 呼出
func_vl('foobar',
        't1',
        't2',
        dk1='dv1',
        dk2='dv2',
        dk3='dv3')
```

<a id="markdown-引数のアンパック" name="引数のアンパック"></a>

## 引数のアンパック

```py
args = [1, 5]
list(range(*args))

list(range(1, 5))   # と同じ
```

<a id="markdown-関数オブジェクト" name="関数オブジェクト"></a>

## 関数オブジェクト

<a id="markdown-関数を変数に代入" name="関数を変数に代入"></a>

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

<a id="markdown-io" name="io"></a>

# I/O

<a id="markdown-コマンドライン引数" name="コマンドライン引数"></a>

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

<a id="markdown-標準入力" name="標準入力"></a>

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

<a id="markdown-無限ループをキー入力で抜ける" name="無限ループをキー入力で抜ける"></a>

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

<a id="markdown-標準出力" name="標準出力"></a>

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

<a id="markdown-末尾に改行文字をつけずに出力する" name="末尾に改行文字をつけずに出力する"></a>

### 末尾に改行文字をつけずに出力する

```py
print('Hello Python!', end='');print('Hello Python!', end='')
```

> Hello Python!Hello Python!

<a id="markdown-pprintでデータ出力の整然化" name="pprintでデータ出力の整然化"></a>

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

<a id="markdown-標準出力の内容をファイルに書き出す" name="標準出力の内容をファイルに書き出す"></a>

### 標準出力の内容をファイルに書き出す

<a id="markdown-stdout" name="stdout"></a>

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

<a id="markdown-print" name="print"></a>

#### print()

```py
with open('./path/to/file.txt', 'w') as f:
    print('contents', file=f)
```

<a id="markdown-環境変数" name="環境変数"></a>

## 環境変数

<a id="markdown-環境変数の読み書き" name="環境変数の読み書き"></a>

### 環境変数の読み書き

<a id="markdown-環境変数の読み出し" name="環境変数の読み出し"></a>

#### 環境変数の読み出し

<a id="markdown-一覧の取得" name="一覧の取得"></a>

##### 一覧の取得

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

<a id="markdown-環境変数の存在チェック" name="環境変数の存在チェック"></a>

##### 環境変数の存在チェック

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

<a id="markdown-キーを指定して値を取得" name="キーを指定して値を取得"></a>

##### キーを指定して値を取得

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

<a id="markdown-環境変数の書き込み" name="環境変数の書き込み"></a>

#### 環境変数の書き込み

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

<a id="markdown-環境変数の削除" name="環境変数の削除"></a>

#### 環境変数の削除

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

<a id="markdown-env-ファイルに記述した設定値を環境変数に設定" name="env-ファイルに記述した設定値を環境変数に設定"></a>

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

<a id="markdown-ハッシュ" name="ハッシュ"></a>

## ハッシュ

<a id="markdown-文字列からハッシュを取得" name="文字列からハッシュを取得"></a>

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

<a id="markdown-巨大なデータのハッシュを取得" name="巨大なデータのハッシュを取得"></a>

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

<a id="markdown-ファイルのハッシュを取得" name="ファイルのハッシュを取得"></a>

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

<a id="markdown-巨大なファイルのハッシュを取得" name="巨大なファイルのハッシュを取得"></a>

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

<a id="markdown-ローカルファイル" name="ローカルファイル"></a>

## ローカルファイル

<a id="markdown-パス文字列の操作" name="パス文字列の操作"></a>

### パス文字列の操作

```py
import os

# パス文字列を組み立てる
print(os.path.sep)

joined = os.path.join('.', 'test' + '-' + 'join', 'test.txt')
print(joined)

# ファイル名を取得する
bname = os.path.basename('./test-join/test.txt')
print(bname)

# ディレクトリ名を取得する
dname = os.path.dirname('./test-join/test.txt')
print(dname)

# ファイル名とディレクトリ名のペアを取得する
dname, bname = os.path.split('./test-join/test.txt')
print(dname, bname)

# 拡張子を取得する
root, ext = os.path.splitext('./test-join/test.txt')
print(root, ext)
spltext = os.path.splitext('./test-join/test.txt')
print(spltext[0], spltext[1])

# 絶対パスを取得する
absp = os.path.abspath('./test-join/test.txt')
print(absp)
if os.path.isabs(absp): # パス文字列が絶対パスか検査する
    print('ABSPATH')

# パス文字列がシンボリックリンクか検査する
absp = os.path.abspath('./test-join/test.txt')
os.path.islink(path)

# パス文字列がマウントポイントか検査する
absp = os.path.abspath('./test-join/test.txt')
os.path.ismount(path)

# 2つのパス間の相対パスを取得する
relp = os.path.relpath(absp, '.')
print(relp)

# 共通パス(階層単位／文字単位)を取得する
paths = [
    os.path.abspath('./test-join/test1.txt'),
    os.path.abspath('./test-join/test2.txt'),
]
cmnpath = os.path.commonpath(paths)
print(cmnpath)
cmnprefix = os.path.commonprefix(paths)
print(cmnprefix)


# ドライブレターを取得する
drive, tail = os.path.splitdrive(absp)
print(drive[0])
print(os.path.samefile(os.path.join(drive, tail), absp))
```

> \# パス文字列を組み立てる
>
> /
>
> './test-join/test.txt'
>
> \# ファイル名を取得する
>
> test.txt
>
> \# ディレクトリ名を取得する
>
> ./test-join
>
> \# ファイル名とディレクトリ名のペアを取得する
>
> ./test-join test.txt
>
> \# 拡張子を取得する
>
> ./test-join/test .txt
>
> \# 絶対パスを取得する
>
> '/mnt/c/Users/y/Documents/GitHub/Python-cheatsheet/test-join/test.txt'
>
> ABSPATH
>
> \# パス文字列がシンボリックリンクか検査する
>
> False
>
> \# パス文字列がマウントポイントか検査する
>
> False
>
> \# 2 つのパス間の相対パスを取得する
>
> test-join/test.txt'
>
> \# 共通パス(階層単位／文字単位)を取得する
>
> C:\Users\y\Documents\GitHub\Python-cheatsheet\test-join
>
> C:\Users\y\Documents\GitHub\Python-cheatsheet\test-join\test
>
> \# ドライブレターを取得する
>
> C
>
> True

<a id="markdown-複数のパスが同一のファイルを示しているか検査" name="複数のパスが同一のファイルを示しているか検査"></a>

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

<a id="markdown-パス文字列を正規化する不要な区切り文字--の除去　／　-windows-環境での大文字小文字の置換スラッシュとバックスラッシュの置換" name="パス文字列を正規化する不要な区切り文字--の除去　／　-windows-環境での大文字小文字の置換スラッシュとバックスラッシュの置換"></a>

#### パス文字列を正規化する(不要な区切り文字、 `..` の除去　／　 Windows 環境での大文字小文字の置換、スラッシュとバックスラッシュの置換)

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

<a id="markdown-ホームディレクトリのパスを取得" name="ホームディレクトリのパスを取得"></a>

#### ホームディレクトリのパスを取得

```py
import os.path

filepath = os.path.join('~', 'path', 'to', 'file.txt')
path  = os.path.expanduser(filepath)
print(path)
```

> C:\Users\y\path\to\file.txt

<a id="markdown-環境変数を取得" name="環境変数を取得"></a>

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

<a id="markdown-親ディレクトリのパスを取得" name="親ディレクトリのパスを取得"></a>

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

<a id="markdown-シンボリックリンクのパスを正規化" name="シンボリックリンクのパスを正規化"></a>

#### シンボリックリンクのパスを正規化

```py
import os

os.path.realpath(__file__)
```

<a id="markdown-linux-上で-windows-形式のパスを操作" name="linux-上で-windows-形式のパスを操作"></a>

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

<a id="markdown-カレントディレクトリ" name="カレントディレクトリ"></a>

### カレントディレクトリ

[python3md-cwd.py](python3md-cwd.py)

```py
import os


CURRENT_DIRECTORY = os.getcwd()
os.chdir(CURRENT_DIRECTORY)
```

<a id="markdown-スクリプトファイルのパスを取得" name="スクリプトファイルのパスを取得"></a>

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

<a id="markdown-ファイル・フォルダを存在チェック" name="ファイル・フォルダを存在チェック"></a>

### ファイル・フォルダを存在チェック

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

<a id="markdown-ファイル・フォルダの一覧を取得" name="ファイル・フォルダの一覧を取得"></a>

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


DIRPATH = os.getcwd() # '/mnt/c/Users/y/Documents/GitHub/Python-cheatsheet'
os.chdir(DIRPATH)

DIRPATH = '.'
DIRPATH = os.path.join(DIRPATH, 'test-glob') # './test-glob'
DIRPATH += '' if DIRPATH.endswith(os.path.sep) else os.path.sep # './test-glob/'
```

<a id="markdown-直下のファイル・フォルダ一覧を取得" name="直下のファイル・フォルダ一覧を取得"></a>

#### 直下のファイル・フォルダ一覧を取得

```py
dirs = glob(os.path.join(DIRPATH, '*'), recursive=True)
# または dirs = glob(os.path.join(DIRPATH, '*'), recursive=False) も同じ
```

> [
>
> './test-glob/test-glob-1',
>
> './test-glob/test-glob-2',
>
> './test-glob/test-glob-3.dat'
>
> ]

```py
dirs = glob(os.path.join(DIRPATH, '**'), recursive=False)
```

> [
>
> './test-glob/test-glob-1',
>
> './test-glob/test-glob-2',
>
> './test-glob/test-glob-3.dat'
>
> ]

<a id="markdown-直下のファイル一覧を取得" name="直下のファイル一覧を取得"></a>

#### 直下のファイル一覧を取得

```py
dirs = glob(os.path.join(DIRPATH, '*.*'), recursive=True)
```

> ['./test-glob/test-glob-3.dat']

```py
[f for f in glob(os.path.join(DIRPATH, '*')) if os.path.isfile(f)]
```

> [
>
> './test-glob/test-glob-3.dat'
>
> ]

<a id="markdown-直下のフォルダ一覧を取得" name="直下のフォルダ一覧を取得"></a>

#### 直下のフォルダ一覧を取得

```py
[f for f in glob(os.path.join(DIRPATH, '*')) if os.path.isdir(f)]
```

> [
>
> './test-glob/test-glob-1',
>
> './test-glob/test-glob-2'
>
> ]

<a id="markdown-再帰的にファイル・フォルダ一覧を取得-⇒-_recursive_-が-_true_-かつパスに-_\\_" name="再帰的にファイル・フォルダ一覧を取得-⇒-_recursive_-が-_true_-かつパスに-_\\_"></a>

#### 再帰的にファイル・フォルダ一覧を取得 ⇒ _recursive_ が _True_ かつ、パスに _\*\*_

```py
dirs = glob(os.path.join(DIRPATH, '**'), recursive=True)
```

> [
>
> './test-glob/',
>
> './test-glob/test-glob-1',
>
> './test-glob/test-glob-1/test-glob-1-1',
>
> './test-glob/test-glob-1/test-glob-1-1/test-glob-1-1-1.dat',
>
> './test-glob/test-glob-1/test-glob-1-1/test-glob-1-1-2.dat',
>
> './test-glob/test-glob-1/test-glob-1-2.dat',
>
> './test-glob/test-glob-2',
>
> './test-glob/test-glob-2/test-glob-2-2.dat',
>
> './test-glob/test-glob-3.dat'
>
> ]

<a id="markdown-python34-以前で再帰的にファイル・フォルダ一覧を取得" name="python34-以前で再帰的にファイル・フォルダ一覧を取得"></a>

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

> [
>
> './test-glob',
>
> './test-glob/test-glob-3.dat',
>
> './test-glob/test-glob-1',
>
> './test-glob/test-glob-1/test-glob-1-2.dat',
>
> './test-glob/test-glob-1/test-glob-1-1',
>
> './test-glob/test-glob-1/test-glob-1-1/test-glob-1-1-1.dat',
>
> './test-glob/test-glob-1/test-glob-1-1/test-glob-1-1-2.dat',
>
> './test-glob/test-glob-2',
>
> './test-glob/test-glob-2/.test-glob-2-1.dat',
>
> './test-glob/test-glob-2/test-glob-2-2.dat'
>
> ]

<a id="markdown-再帰的にフォルダ一覧を取得-⇒-パスの末尾が-_ospathsep_" name="再帰的にフォルダ一覧を取得-⇒-パスの末尾が-_ospathsep_"></a>

#### 再帰的にフォルダ一覧を取得 ⇒ パスの末尾が _os.path.sep_

```py
[f for f in glob(os.path.join(DIRPATH, '**'), recursive=True) if os.path.isdir(f)]
```

> [
>
> './test-glob/',
>
> './test-glob/test-glob-1',
>
> './test-glob/test-glob-1/test-glob-1-1',
>
> './test-glob/test-glob-2'
>
> ]

```py
dirs = glob(os.path.join(DIRPATH, '**' + os.path.sep), recursive=True)
```

> [
>
> './test-glob/',
>
> './test-glob/test-glob-1/',
>
> './test-glob/test-glob-1/test-glob-1-1/',
>
> './test-glob/test-glob-2/'
>
> ]

<a id="markdown-再帰的にファイル一覧を取得" name="再帰的にファイル一覧を取得"></a>

#### 再帰的にファイル一覧を取得

```py
dirs = glob(os.path.join(DIRPATH, os.path.join('**', '*.*')), recursive=True)
```

> [
>
> './test-glob/test-glob-3.dat',
>
> './test-glob/test-glob-1/test-glob-1-2.dat',
>
> './test-glob/test-glob-1/test-glob-1-1/test-glob-1-1-1.dat',
>
> './test-glob/test-glob-1/test-glob-1-1/test-glob-1-1-2.dat',
>
> './test-glob/test-glob-2/test-glob-2-2.dat'
>
> ]

<a id="markdown-ワイルドカードを利用" name="ワイルドカードを利用"></a>

#### ワイルドカードを利用

```py
dirs = glob(os.path.join(DIRPATH, os.path.join('**', '*-[0-1].???')), recursive=True)
```

> [
>
> './test-glob/test-glob-1/test-glob-1-1/test-glob-1-1-1.dat'
>
> ]

<a id="markdown-正規表現を利用" name="正規表現を利用"></a>

#### 正規表現を利用

```py
import re

dirs = [p for p in glob.glob(os.path.join(DIRPATH, os.path.join('**', '*.*')), recursive=True) if re.search('test-glob(-1){3}.dat', p)]
```

<a id="markdown-ファイル情報を取得" name="ファイル情報を取得"></a>

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

<a id="markdown-ファイルを作成" name="ファイルを作成"></a>

### ファイルを作成

<a id="markdown-touch" name="touch"></a>

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

<a id="markdown-既存のファイルがある場合はバックアップを作成して再作成" name="既存のファイルがある場合はバックアップを作成して再作成"></a>

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

<a id="markdown-フォルダを作成" name="フォルダを作成"></a>

### フォルダを作成

<a id="markdown-既存のフォルダがある場合はバックアップを作成して再作成" name="既存のフォルダがある場合はバックアップを作成して再作成"></a>

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

<a id="markdown-ファイルをコピー" name="ファイルをコピー"></a>

### ファイルをコピー

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

# ファイル→ファイル (同名のファイルが既に存在すれば上書き)
result_path = shutil.copy(srcpath, dstpath)
print(result_path)

dst1 = os.path.join(os.path.dirname(dstpath), 'test-copy2')
result_path = shutil.copy(srcpath, dst1)
print(result_path)

# ファイル→フォルダ (同名のファイルが既に存在すればエラー)
#  コピー先として指定されたディレクトリが予め存在し、その中に同名の既存ファイルが存在しなければコピーされる
dst2 = os.path.join(os.path.dirname(dstpath), 'test-copy2/') # dst1との差異は、末尾の'/'のみ
os.makedirs(dst2, exist_ok=True) # 予めディレクトリを作成しておかないとIsADirectoryError

dst_file_path = os.path.join(os.path.dirname(dst2), os.path.basename(srcpath))
if os.path.exists(dst_file_path):
    os.remove(dst_file_path)

result_path = shutil.copy(srcpath, dst2)
print(result_path)

# ファイル→ファイル (ファイル情報を保持)
result_path = shutil.copy2(srcpath, dstpath)
print(result_path)

result_path = shutil.copy2(srcpath, dst2) # 予めディレクトリを作成しておかないとIsADirectoryError
print(result_path)
```

> \# ファイル → ファイル (同名のファイルが既に存在すれば上書き)
>
> ./test-copy2.txt

> \# ファイル → ファイル (同名のファイルが既に存在すれば上書き)
>
> ./test-copy2.txt
>
> ./test-copy2

> \# ファイル → フォルダ (同名のファイルが既に存在すればエラー)
>
> ./test-copy2/test-copy1.txt

> \# ファイル → ファイル (ファイル情報を保持)
>
> ./test-copy2.txt
>
> ./test-copy2/test-copy1.txt

<a id="markdown-フォルダをコピー" name="フォルダをコピー"></a>

### フォルダをコピー

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

<a id="markdown-ファイルをリネーム" name="ファイルをリネーム"></a>

### ファイルをリネーム

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

os.rename(srcpath, dstpath)
glob('./test-rename/**', recursive=True)

touch(srcpath)
glob('./test-rename/**', recursive=True)

os.rename(srcpath, dstpath) # dstpathのファイルが既に存在すると、上書きされる
glob('./test-rename/**', recursive=True)
```

> ['./test-rename/', './test-rename/file2.txt']
>
> ['./test-rename/', './test-rename/file1.txt', './test-rename/file2.txt']
>
> ['./test-rename/', './test-rename/file2.txt'] \# dstpath のファイルが既に存在すると、上書きされる

<a id="markdown-フォルダをリネーム" name="フォルダをリネーム"></a>

### フォルダをリネーム

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

<a id="markdown-ファイルを移動" name="ファイルを移動"></a>

### ファイルを移動

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

<a id="markdown-フォルダを移動" name="フォルダを移動"></a>

### フォルダを移動

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

<a id="markdown-ファイルを削除" name="ファイルを削除"></a>

### ファイルを削除

<a id="markdown-特定のファイルを削除" name="特定のファイルを削除"></a>

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

<a id="markdown-ファイルを検索して削除" name="ファイルを検索して削除"></a>

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

<a id="markdown-フォルダを削除" name="フォルダを削除"></a>

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

<a id="markdown-タイプ別のファイル読み書き" name="タイプ別のファイル読み書き"></a>

### タイプ別のファイル読み書き

<a id="markdown-zip-ファイル" name="zip-ファイル"></a>

#### ZIP ファイル

<a id="markdown-zip-ファイル圧縮" name="zip-ファイル圧縮"></a>

##### ZIP ファイル圧縮

<a id="markdown-shutil-を使ってフォルダごと圧縮" name="shutil-を使ってフォルダごと圧縮"></a>

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

<a id="markdown-個別にファイルを追加して圧縮ファイルを作成" name="個別にファイルを追加して圧縮ファイルを作成"></a>

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



with zipfile.ZipFile(archive_path, 'w', compression=zipfile.ZIP_DEFLATED) as z:
    z.write(srcdpath1, arcname=srcdpath1)
    z.write(srcdpath2, arcname=srcdpath2)
    z.write(srcfpath1, arcname=srcfpath1)

with zipfile.ZipFile(archive_path) as zip_contents:
    print(zip_contents.namelist())

# 既存の圧縮ファイルがある場合は圧縮ファイル自体が上書きされる
with zipfile.ZipFile(archive_path, 'w', compression=zipfile.ZIP_DEFLATED) as z:
    z.write(srcdpath1, arcname=srcdpath1)
    z.write(srcdpath2, arcname=srcdpath2)
    z.write(srcfpath2, arcname=srcfpath2)

with zipfile.ZipFile(archive_path) as zip_contents:
    print(zip_contents.namelist())

# 既存の圧縮ファイルに、ファイルを追加する
with zipfile.ZipFile(archive_path, 'a', compression=zipfile.ZIP_DEFLATED) as z:
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

<a id="markdown-zip-ファイル解凍" name="zip-ファイル解凍"></a>

##### ZIP ファイル解凍

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

<a id="markdown-ログファイルテキストファイル・追記" name="ログファイルテキストファイル・追記"></a>

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

<a id="markdown-設定ファイルconfigparser" name="設定ファイルconfigparser"></a>

#### 設定ファイル(configparser)

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

<a id="markdown-テキストファイル" name="テキストファイル"></a>

#### テキストファイル

<a id="markdown-モード" name="モード"></a>

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

<a id="markdown-文字コードの推測" name="文字コードの推測"></a>

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

<a id="markdown-エラーハンドラ" name="エラーハンドラ"></a>

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

<a id="markdown-cchardet-モジュールを使用" name="cchardet-モジュールを使用"></a>

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

<a id="markdown-読み込み" name="読み込み"></a>

##### 読み込み

<a id="markdown-単一の文字列として読み込みr-読み取り" name="単一の文字列として読み込みr-読み取り"></a>

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

<a id="markdown--shift-jis" name="-shift-jis"></a>
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

<a id="markdown--utf-8-bom-なし" name="-utf-8-bom-なし"></a>
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
﻿あいうえお8XkfWDHyFdcB52MbTNNswDnFRAsZdEgRmmsaNktD
かきくけこxahfE6WkxNFpU-4KgnJ4jS2jZUyWf9spDbKRaFyC
```

<a id="markdown--utf-8-bom-あり" name="-utf-8-bom-あり"></a>
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

<a id="markdown-1-行ずつ読み込みr-読み取り" name="1-行ずつ読み込みr-読み取り"></a>

###### 1 行ずつ読み込み(r: 読み取り)

```py
import os
with open(os.path.join('test-fileio', 'inpututf8.txt'), 'r', encoding='utf_8') as file:
    string = file.readline()
    while string:
        print(string)
        string = file.readline()
```

<a id="markdown-リストへ格納r-読み取り" name="リストへ格納r-読み取り"></a>

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

<a id="markdown-書き込み" name="書き込み"></a>

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

<a id="markdown-単一の文字列として書き込みx-新規作成" name="単一の文字列として書き込みx-新規作成"></a>

###### 単一の文字列として書き込み(x: 新規作成)

```py
import os
string = 'foobar\nhoge\n'
with open(os.path.join('test-fileio', 'outpututf8.txt'), 'x', encoding='utf_8') as file:
    file.write(string)
```

> 11

<a id="markdown-リストを書き込みx-新規作成" name="リストを書き込みx-新規作成"></a>

###### リストを書き込み(x: 新規作成)

```py
import os
lst = ['foobar', 'hoge']
with open(os.path.join('test-fileio', 'outpututf8.txt'), 'x', encoding='utf_8') as file:
    file.writelines(lst) # 要素間には空白文字等は挿入されない
```

<a id="markdown-単一の文字列として書き込みw-新規作成／上書き" name="単一の文字列として書き込みw-新規作成／上書き"></a>

###### 単一の文字列として書き込み(w: 新規作成／上書き)

```py
import os
string = 'foobar\nhoge\n'
with open(os.path.join('test-fileio', 'outpututf8.txt'), 'w', encoding='utf_8') as file:
    file.write(string)
```

> 11

<a id="markdown-既存ファイルが存在するときに上書きするか確認する" name="既存ファイルが存在するときに上書きするか確認する"></a>

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

<a id="markdown-リストを書き込みw-新規作成／上書き" name="リストを書き込みw-新規作成／上書き"></a>

###### リストを書き込み(w: 新規作成／上書き)

```py
import os
lst = ['foobar', 'hoge']
with open(os.path.join('test-fileio', 'outpututf8.txt'), 'w', encoding='utf_8') as file:
    file.writelines(lst) # 要素間には空白文字等は挿入されない
```

<a id="markdown-単一の文字列として書き込みa-追記" name="単一の文字列として書き込みa-追記"></a>

###### 単一の文字列として書き込み(a: 追記)

```py
import os
string = 'foobar\nhoge\n'
with open(os.path.join('test-fileio', 'outpututf8.txt'), 'a', encoding='utf_8') as file:
    file.write(string)
```

<a id="markdown-リストを書き込みa-追記" name="リストを書き込みa-追記"></a>

###### リストを書き込み(a: 追記)

```py
import os
lst = ['foobar', 'hoge']
with open(os.path.join('test-fileio', 'outpututf8.txt'), 'a', encoding='utf_8') as file:
    file.writelines(lst) # 要素間には空白文字等は挿入されない
```

<a id="markdown-csv-ファイル" name="csv-ファイル"></a>

#### CSV ファイル

<a id="markdown-読み込み-1" name="読み込み-1"></a>

##### 読み込み

Windows 環境の場合は、明示的に UTF-8 を指定しないと SJIS として読み書きされる

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

<a id="markdown-メモリ上の-csv-文字列の読み込み" name="メモリ上の-csv-文字列の読み込み"></a>

###### メモリ上の CSV 文字列の読み込み

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

<a id="markdown-書き込み-1" name="書き込み-1"></a>

##### 書き込み

<a id="markdown-上書き" name="上書き"></a>

###### 上書き

```py
import csv
with open(os.path.join('test-fileio', 'outpututf8.csv'), 'w', encoding='utf_8', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['foo', 'bar', 'hoge'])
    spamwriter.writerow(['foo', 'bar', 'hoge'])
```

> 14
>
> 14

<a id="markdown-追記" name="追記"></a>

###### 追記

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

<a id="markdown-json-ファイル" name="json-ファイル"></a>

#### JSON ファイル

<a id="markdown-jsontool" name="jsontool"></a>

##### json.tool

```sh
$ python -m json.tool inpututf8.json
```

<a id="markdown-ファイルから読み込み" name="ファイルから読み込み"></a>

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

<a id="markdown-スクリプトを書かずjsontool-で解析する" name="スクリプトを書かずjsontool-で解析する"></a>

###### スクリプトを書かず、json.tool で解析する

```sh
$ python -m json.tool ./test-fileio/inpututf8.json
```

<a id="markdown-文字列から読み込み" name="文字列から読み込み"></a>

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

<a id="markdown-文字列から読み込み順序を保つ" name="文字列から読み込み順序を保つ"></a>

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

decoder = json.JSONDecoder(object_pairs_hook=collections.OrderedDict)
print(decoder.decode(json_str))
```

> OrderedDict([('key1', 'val1'), ('key2', 'val2')])

<a id="markdown-要素の読み込み" name="要素の読み込み"></a>

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

<a id="markdown-要素の検索" name="要素の検索"></a>

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

<a id="markdown-書き込み-2" name="書き込み-2"></a>

##### 書き込み

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

<a id="markdown-ini-ファイル" name="ini-ファイル"></a>

#### ini ファイル

<a id="markdown-ファイルから読み込み-1" name="ファイルから読み込み-1"></a>

##### ファイルから読み込み

- settings.ini

```ini
[DEFAULT]
host = fuga

[db]
user = foobar
password = hogepiyo
```

- app.py

```py
import configparser
import os

ini = configparser.ConfigParser()
ini.read(os.path.join('test-fileio', 'settings.ini'), 'UTF-8')

print(ini['db']['user'])
print(ini['db']['password'])

print(ini.get('db', 'user'))
print(ini.get('db', 'password'))

print(ini['db']['host'])
```

> ['test-fileio\\settings.ini'] # ini.read() の戻り値

> foobar
>
> hogepiyo

> foobar
>
> hogepiyo

> fuga

<a id="markdown-tsv-ファイル" name="tsv-ファイル"></a>

#### TSV ファイル

<a id="markdown-メモリ上の-tsv-文字列の読み込み" name="メモリ上の-tsv-文字列の読み込み"></a>

###### メモリ上の TSV 文字列の読み込み

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

<a id="markdown-xml-ファイル" name="xml-ファイル"></a>

#### XML ファイル

<a id="markdown-ファイルから読み込み-2" name="ファイルから読み込み-2"></a>

##### ファイルから読み込み

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

<a id="markdown-文字列から読み込み-1" name="文字列から読み込み-1"></a>

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

<a id="markdown-書き込み-3" name="書き込み-3"></a>

##### 書き込み

<a id="markdown-arff-ファイル" name="arff-ファイル"></a>

#### ARFF ファイル

<a id="markdown-読み込み-2" name="読み込み-2"></a>

##### 読み込み

```py
import arff
data = arff.load(open('test.arff', 'rb'))
```

<a id="markdown-書き込み-4" name="書き込み-4"></a>

##### 書き込み

```py

import arff
arff.dumps(data)
```

<a id="markdown-ネットワーク" name="ネットワーク"></a>

## ネットワーク

<a id="markdown-url-文字列の操作" name="url-文字列の操作"></a>

### URL 文字列の操作

<a id="markdown-url-エンコーディング" name="url-エンコーディング"></a>

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

<a id="markdown-変換対象の文字の違いと利用する関数" name="変換対象の文字の違いと利用する関数"></a>

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

<a id="markdown-url-の一部の要素に日本語が含まれている場合" name="url-の一部の要素に日本語が含まれている場合"></a>

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

<a id="markdown-url-文字列のパース" name="url-文字列のパース"></a>

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

<a id="markdown-url-文字列の組み立て" name="url-文字列の組み立て"></a>

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

<a id="markdown-リクエストを送信" name="リクエストを送信"></a>

### リクエストを送信

`urllib` モジュールではなく `Requests` モジュールを利用する場合、以下のコマンドでインストールする

```sh
$ pip install requests
```

<a id="markdown-コンテンツを文字列として取得" name="コンテンツを文字列として取得"></a>

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

<a id="markdown-文字コードを指定" name="文字コードを指定"></a>

#### 文字コードを指定

<a id="markdown-特定の文字コードshift-jisを指定" name="特定の文字コードshift-jisを指定"></a>

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

<a id="markdown-コンテンツの内容から文字コードを推定する" name="コンテンツの内容から文字コードを推定する"></a>

##### コンテンツの内容から文字コードを推定する

<a id="markdown-chardet-による推定" name="chardet-による推定"></a>

###### chardet による推定

```py
import requests
url = 'http://www.soumu.go.jp/'
response = requests.get(url)
if response.status_code == 200:
    response.encoding = response.apparent_encoding
    print(response.text)
```

<a id="markdown-cchardet-による推定chardet-よりも高速" name="cchardet-による推定chardet-よりも高速"></a>

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

<a id="markdown-コンテンツをテンポラリファイルとして取得" name="コンテンツをテンポラリファイルとして取得"></a>

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

<a id="markdown-バイナリファイルを保存" name="バイナリファイルを保存"></a>

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

<a id="markdown-画像ファイルの保存" name="画像ファイルの保存"></a>

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

<a id="markdown-大容量ファイルの保存" name="大容量ファイルの保存"></a>

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

<a id="markdown-get" name="get"></a>

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

print(r.encoding)  # 文字エンコードの確認
r.encoding = 'Shift-JIS'  # 文字コードの設定(変更)
print(r.text)  # 変更後のエンコーディングが使用される

# リダイレクト禁止
import requests
url = 'http://httpbin.org/get'
r = requests.get(url, allow_redirects=True)
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

<a id="markdown-post" name="post"></a>

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

<a id="markdown-フォーム送信multipart-エンコード" name="フォーム送信multipart-エンコード"></a>

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

<a id="markdown-put" name="put"></a>

#### PUT

```py
import requests
url = 'http://httpbin.org/put'
r = requests.put(url)
```

<a id="markdown-delete" name="delete"></a>

#### DELETE

```py
import requests
url = 'http://httpbin.org/delete'
r = requests.delete(url)
```

<a id="markdown-head" name="head"></a>

#### HEAD

```py
import requests
url = 'http://httpbin.org/get'
r = requests.head(url)
```

<a id="markdown-http-ヘッダ" name="http-ヘッダ"></a>

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

<a id="markdown-basic-認証" name="basic-認証"></a>

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

<a id="markdown-応答ヘッダ・リダイレクト先-url" name="応答ヘッダ・リダイレクト先-url"></a>

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

<a id="markdown-セッション" name="セッション"></a>

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

<a id="markdown-cookie" name="cookie"></a>

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

<a id="markdown-例外処理とレスポンスコード" name="例外処理とレスポンスコード"></a>

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

<a id="markdown-クラス" name="クラス"></a>

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

<a id="markdown-オブジェクトの文字列表現" name="オブジェクトの文字列表現"></a>

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

<a id="markdown-オブジェクトの属性の参照と存在チェック" name="オブジェクトの属性の参照と存在チェック"></a>

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

<a id="markdown-クラスの継承" name="クラスの継承"></a>

## クラスの継承

```py
class MySubClass(MyClass):
    def Calc(self):  # オーバーロード
        print('sub  a')
```

<a id="markdown-多重継承" name="多重継承"></a>

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

<a id="markdown-モジュール" name="モジュール"></a>

# モジュール

<a id="markdown-モジュールの読み込み" name="モジュールの読み込み"></a>

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

<a id="markdown-推奨される読み込み順序" name="推奨される読み込み順序"></a>

### 推奨される読み込み順序

1. 標準ライブラリ
2. サードパーティライブラリ
3. ローカルライブラリ（自作のライブラリ）

<a id="markdown-外部スクリプトの読み込み" name="外部スクリプトの読み込み"></a>

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

<a id="markdown-一時的にモジュール検索パスを追加" name="一時的にモジュール検索パスを追加"></a>

## 一時的にモジュール検索パスを追加

```py
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
```

<a id="markdown-恒久的にモジュール検索パスを追加" name="恒久的にモジュール検索パスを追加"></a>

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

<a id="markdown-pydoc" name="pydoc"></a>

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

<a id="markdown-ロギング" name="ロギング"></a>

# ロギング

logging ライブラリを利用する

```py
import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(filename)s %(lineno)d %(funcName)s %(message)s")
logger = logging.getLogger(__name__)

logger.debug("message")
logger.info("message")
logger.warning("message")
logger.error("message")
logger.critical("message")
```

<a id="markdown-ファイル出力" name="ファイル出力"></a>

## ファイル出力

```py
import logging
import os

LOG_DIR = 'logfile'
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(filename=os.path.join(LOG_DIR, 'logger.log'), level=logging.INFO, format="%(asctime)s %(levelname)s %(filename)s %(lineno)d %(funcName)s %(message)s")
logger = logging.getLogger(__name__)

logger.info("message")
```

<a id="markdown-エラーメッセージ" name="エラーメッセージ"></a>

# エラーメッセージ

<a id="markdown-シンタックスハイライト" name="シンタックスハイライト"></a>

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

---

Copyright (c) 2019 YA-androidapp(https://github.com/YA-androidapp) All rights reserved.
