# 日付型

# 本日(日付のみ)
import datetime
today = datetime.date.today()
print(today.year)
print(today.month)
print(today.day)
print(today.weekday())  # 0:月曜; 6:日曜
print(today.isoweekday())  # 1:月曜; 7:日曜

# 現在日時(日付と時刻)
from datetime import datetime as dt
print(dt.now())
print(dt.today())

today = dt.today()
print(today.year)
print(today.month)
print(today.day)

# 1日後
from datetime import datetime, timedelta
today = datetime.today()
today + timedelta(days=1)    # 1日後
today.replace(day=25)  # 置換

# 任意の日時を生成
import datetime
d = datetime.datetime(2018, 1, 23, 4, 56, 7)

# 任意の時刻を生成
import datetime
t = datetime.time(4, 56, 7)


# 変換

# 書式指定子: http://docs.python.jp/3/library/datetime.html#strftime-and-strptime-behavior

# 文字列型→日付型
from datetime import datetime as dt
dt_str = '2017-10-01 12:34:56'
dt_datetime = dt.strptime(dt_str, '%Y-%m-%d %H:%M:%S')

from pytz import timezone
from dateutil import parser
utc = "Sun Jan 1 01:23:45 +0000 2017"
utc_d = parser.parse(utc)
jst = utc_d.astimezone(timezone('Asia/Tokyo'))
print(jst)

# 日付型→文字列型
from datetime import datetime as dt
now_datetime = dt.now()
now_str = now_datetime.strftime('%Y/%m/%d %H:%M:%S')

print(now_datetime.isoformat())  # ISO形式

# タイムゾーンの変更
# UTC→JST
from pytz import timezone
from datetime import datetime
utc = datetime.now(timezone('UTC'))
print(utc)
jst = utc.astimezone(timezone('Asia/Tokyo'))
print(jst)

# 無指定→UTC
# 無指定→JST
from pytz import timezone
from datetime import datetime
now = datetime.now()
print(now)
utc = timezone('UTC').localize(now)
print(utc)
jst = timezone('Asia/Tokyo').localize(now)
print(jst)

# 日時の比較
import datetime
d1 = datetime.datetime(2016, 12, 31, 23, 59, 59)
d2 = datetime.datetime(2016, 1, 1, 0, 0, 0)
td = d1 - d2
# datetime.timedelta(365, 86399)
print(td)
print(td.days)
print(td.seconds)

# 日時の比較
import datetime
d1 = datetime.date(2016, 12, 31)
d2 = datetime.date(2016, 1, 1)
print(d2 < d1)  # True
print(d2 > d1)  # False
print(d1 == d2)  # False
