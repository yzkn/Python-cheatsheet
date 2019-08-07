


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
