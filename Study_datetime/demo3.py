"""timedelta对象表示两个日期或时间之间的时差。"""
from datetime import timedelta,date,datetime

# t1 = date(year = 2018, month = 7, day = 12)
# t2 = date(year = 2017, month = 12, day = 23)
# t3 = t1 - t2
# print("t3 =", t3)
#
# t4 = datetime(year = 2018, month = 7, day = 12, hour = 7, minute = 9, second = 33)
# t5 = datetime(year = 2019, month = 6, day = 10, hour = 5, minute = 55, second = 13)
# t6 = t4 - t5
# print("t6 =", t6)
#
# print("type of t3 =", type(t3))
# print("type of t6 =", type(t6))


# t1 = timedelta(weeks = 2, days = 5, hours = 1, seconds = 33)
# t2 = timedelta(days = 4, hours = 11, minutes = 4, seconds = 54)
# t3 = t1 - t2
#
# print("t3 =", t3)
# print("t1 =", t1)

# t1 = timedelta(seconds = 33)
# t2 = timedelta(seconds = 54)
# t3 = t1 - t2
# print("t3 =", t3)
# print("t3 =", abs(t3))

# t = timedelta(days = 5, hours = 1, seconds = 33, microseconds = 233423)
# print("total seconds =", t.total_seconds())