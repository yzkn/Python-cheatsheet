# urllib

# コンテンツを文字列として取得
import urllib.request
url = 'http://python.org/'
with urllib.request.urlopen(url) as response:
    html = response.read()

import urllib.request
url = 'http://python.org/'
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    html = response.read()

# 文字コードを指定
import urllib.request
url = 'http://python.org/'
with urllib.request.urlopen(url) as response:
    html = response.read().decode('utf-8')

# コンテンツをテンポラリファイルとして取得
import urllib.request
url = 'http://python.org/'
local_filename, headers = urllib.request.urlretrieve(url)
html = open(local_filename)

# バイナリファイルを保存
import os
import urllib.request
url = 'http://python.org/'
with urllib.request.urlopen(url) as response:
    with open(os.path.basename(url), 'wb') as localfile:
        localfile.write(response.read())

# GET
import urllib.parse
import urllib.request

url = 'http://python.org/'

params = {}
params['name'] = 'Sato'
params['location'] = 'Tokyo'
params['age'] = '30'
query = urllib.parse.urlencode(params)
url = url + '?' + query

with urllib.request.urlopen(url) as response:
    html = response.read()

# POST
import urllib.parse
import urllib.request

url = 'http://python.org/'

params = {'name': 'Sato', 'location': 'Tokyo',  'age': '30'}
query = urllib.parse.urlencode(params)
query = query.encode('ascii')

req = urllib.request.Request(url, query)
with urllib.request.urlopen(req) as response:
    html = response.read()

# HTTPヘッダ(headers引数)
import urllib.parse
import urllib.request

url = 'http://python.org/'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/xxx.xx (KHTML, like Gecko) Chrome/xx.x.xxxx.xx Safari/xxx.xx'
headers = {'User-Agent': user_agent}

params = {'name': 'Sato', 'location': 'Tokyo',  'age': '30'}
query = urllib.parse.urlencode(params)
query = query.encode('ascii')

req = urllib.request.Request(url, query, headers)
with urllib.request.urlopen(req) as response:
    html = response.read()

# HTTPヘッダ(add_header)
import urllib.parse
import urllib.request

url = 'http://python.org/'

params = {'name': 'Sato', 'location': 'Tokyo',  'age': '30'}
query = urllib.parse.urlencode(params)
query = query.encode('ascii')

req = urllib.request.Request(url, query)
req.add_header('Referer', 'http://www.python.org/')
with urllib.request.urlopen(req) as response:
    html = response.read()

# BASIC認証
import urllib.request
import urllib.request
import getpass

url = 'http://python.org/'
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

# 応答ヘッダ・リダイレクト先URL
import urllib.parse
import urllib.request

url = 'http://python.org/'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/xxx.xx (KHTML, like Gecko) Chrome/xx.x.xxxx.xx Safari/xxx.xx'
headers = {'User-Agent': user_agent}

params = {'name': 'Sato', 'location': 'Tokyo',  'age': '30'}
query = urllib.parse.urlencode(params)
query = query.encode('ascii')

req = urllib.request.Request(url, query, headers)
with urllib.request.urlopen(req) as response:
    url = response.geturl()
    headers = response.info()
    print(headers)
    # charset=req.info().get_content_charset() # 応答ヘッダから文字コードを取得してデコードする例
    # content=req.read().decode(charset)

# Cookie
import urllib
import urllib.request  # opener
import urllib.parse  # urlencode
import http
import http.cookiejar

opener = urllib.request.build_opener(
    urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))

u, p = 'id', 'pw'

url1 = 'http://python.org/?login'
url2 = 'http://python.org/?user=%s' % u

post = {
    'name': u,
    'password': p
}
data = urllib.parse.urlencode(post).encode('utf-8')

conn = opener.open(url1, data)
ofs = open('out1.html', 'w', encoding='utf-8')
ofs.write(conn.read().decode('utf-8'))
ofs.close()

conn = opener.open(url2)
ofs = open('out2.html', 'w', encoding='euc-jp')
ofs.write(conn.read().decode('euc-jp'))
ofs.close()


# 例外処理とレスポンスコード
import urllib.parse
import urllib.request
from urllib.error import URLError

url = 'http://python.org/'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/xxx.xx (KHTML, like Gecko) Chrome/xx.x.xxxx.xx Safari/xxx.xx'
headers = {'User-Agent': user_agent}

params = {'name': 'Sato', 'location': 'Tokyo',  'age': '30'}
query = urllib.parse.urlencode(params)
query = query.encode('ascii')

req = urllib.request.Request(url, query, headers)
try:
    with urllib.request.urlopen(req) as response:
        html = response.read()
except URLError as e:  # URLErrorはHTTPErrorも拾う
    print(e.code)
    print(e.read())

    if hasattr(e, 'reason'):
        print('Reason: ', e.reason)
    elif hasattr(e, 'code'):
        print('Error code: ', e.code)
else:
    pass  # リクエストに成功


# Requests

# pip install requests

# GET
import requests
url = 'http://python.org/'
requests.get(url)

# POST
import requests
url = 'http://python.org/'
requests.post(url)

# PUT
import requests
url = 'http://python.org/'
requests.put(url)

# DELETE
import requests
url = 'http://python.org/'
requests.delete(url)

# header の取得
import requests
url = 'http://python.org/'
requests.head(url)

# クエリ

# GET
import requests
url = 'http://python.org/'
payload = {'key1': 'val1', 'key2': 'val2'}
r = requests.get(url, params=payload)
print(r.url)  # 生成されたURL

# POST
import requests
url = 'http://python.org/'
payload = {'key1': 'val1', 'key2': 'val2'}
r = requests.post(url, data=payload)
print(r.url)  # 生成されたURL(POSTなのでクエリ文字列がないことを確認)

# ヘッダの追加
import requests
url = 'http://python.org/'
payload = {'key1': 'val1', 'key2': 'val2'}
headers = {'Referer', 'http://www.python.org/'}
r = requests.post(url, data=json.dumps(payload), headers=headers)

# フォーム送信(Multipartエンコード)
import requests
url = 'http://python.org/'
files = {'file': open('test.png', 'rb')}
r = requests.post(url, files=files)

import requests
url = 'http://python.org/'
files = {'file': ('test.png', open('test.png', 'rb'))}
r = requests.post(url, files=files)

import requests
url = 'http://python.org/'
files = {'file': ('test.txt', 'foobar')}
r = requests.post(url, files=files)

# 応答
import requests
url = 'http://python.org/'
r = requests.get(url)
r.headers
# r.headers['status']
# r.headers.get('status')
r.text

import requests
url = 'http://python.org/'
r = requests.get(url)
r.status_code  # レスポンスコード
r.status_code == requests.codes.ok  # 200か判定

import requests
url = 'http://python.org/'
r = requests.get(url)
r.encoding  # 文字エンコードの確認
r.encoding = 'Shift-JIS'  # 文字コードの設定(変更)
r.text  # 変更後のエンコーディングが使用される

# Cookie

# 取得
import requests
url = 'http://python.org/'
r = requests.get(url)
r.cookies['key1']  # Cookieが存在する場合は非None

# 設定
import requests
url = 'http://python.org/'
cookies = dict(key1='val1')
r = requests.get(url, cookies=cookies)

# リダイレクト禁止
import requests
url = 'http://python.org/'
r = requests.get(url, allow_redirects=True)

# タイムアウト
import requests
url = 'http://python.org/'
r = requests.get(url, timeout=1)


# 画像ファイルの保存

# pip install Image
# pip install requests
# pip install StringIO

import os
import requests
from PIL import Image
from io import BytesIO
url = 'https://www.python.org/static/img/python-logo.png'
r = requests.get(url)
i = Image.open(BytesIO(r.content))
i.save(os.path.basename(url))

# 大容量ファイルの保存
import os
import requests
url = 'https://www.python.org/static/img/python-logo.png'
res = requests.get(url, stream=True)
if res.status_code == 200:
    with open(os.path.basename(url), 'wb') as file:
        for chunk in res.iter_content(chunk_size=1024):
            file.write(chunk)

# JSON
import requests
url = 'http://python.org/path/to/json/'
r = requests.get()
r.json()

# セッション
import requests
url = 'http://python.org/path/to/json/'
session = requests.session()
auth_data = {'username': 'foo', 'password': 'bar'}
res = session.post(url, data=auth_data)
res = session.post(url, data={'key1': 'val1'})

# 例外処理とレスポンスコード
import requests
url = 'http://python.org/'
try:
    r = requests.get(url)
except requests.exceptions.RequestException as e:
    print("Error: {}".format(e))


# Copyright (c) 2017 YA-androidapp(https://github.com/YA-androidapp) All rights reserved.
