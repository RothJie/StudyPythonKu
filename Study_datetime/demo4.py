"""
strftime()方法是在date、datetime和time类下面定义的。
该方法根据给定的日期、日期时间或时间对象创建格式化的字符串。

strptime()方法从一个给定的字符串(表示日期和时间)创建一个datetime对象

"""
from datetime import date,datetime,time
from time import strptime

"""
%Y -年[0001，...，2018，2019，...，9999]

%m -月[01，02，...，11，12]

%d -天[01，02，...，30，31]

%H -小时[00，01，...，22，23

%M -分钟[00，01，...，58，59]

%S -秒[00，01，...，58，59]
"""

# n = datetime.now()
# print(n)
# print(n.strftime("%Y~%m~%d %H:%S:%M"))

date_string = "21 July, 2018"
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)

"""
# %Y  Year with century as a decimal number.
# %m  Month as a decimal number [01,12].
# %d  Day of the month as a decimal number [01,31].
# %H  Hour (24-hour clock) as a decimal number [00,23].
# %M  Minute as a decimal number [00,59].
# %S  Second as a decimal number [00,61].
# %z  Time zone offset from UTC.
# %a  Locale's abbreviated weekday name.
# %A  Locale's full weekday name.
# %b  Locale's abbreviated month name.
# %B  Locale's full month name.
# %c  Locale's appropriate date and time representation.
# %I  Hour (12-hour clock) as a decimal number [01,12]. 
# %p Locale's equivalent of either AM or PM.
# Other codes may be available on your platform. See documentation for 
# the C library strftime function.
常见的日期字符串格式：
'06-Feb-19 00:00:00' -----> "%d-%b-%y %H:%M:%S"
'2019/02/06 00:00:00'----->"%Y/%m/%d %H:%M:%S"
'2019-01-29 23:40:00'-----> "%Y-%m-%d %H:%M:%S"
以及自己按照上述格式自己定义自己需要的时间字符串格式
"""
