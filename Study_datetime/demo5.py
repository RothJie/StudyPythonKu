from datetime import datetime
import pytz

Beijin_time = datetime.now()
tz_BJ = pytz.timezone('Asia/Shanghai')
print("北京时间：",Beijin_time.strftime("%Y年%m月%d日 %H时%M分%S秒"))

tz_NY = pytz.timezone('America/New_York') # 时区
New_York_time = datetime.now(tz_NY) # 时间
print("纽约时间：",New_York_time.strftime("%Y年%m月%d日 %H时%M分%S秒")) # 格式化时间

tz_London = pytz.timezone('Europe/London')
London_time = datetime.now(tz_London)
print("伦敦时间：", London_time.strftime("%Y年%m月%d日 %H时%M分%S秒"))

# 计算时差：
# 一种方法是将两个时间都转换为 UTC 时间，然后计算差值。
beijin_utc = Beijin_time.astimezone(pytz.utc)  # 传入pytz.utc
newyork_utc = New_York_time.astimezone(pytz.utc)

sub_time = (newyork_utc-beijin_utc).total_seconds() / 3600
print(sub_time)
