"""认识datetime中的date和datime两个类"""
from datetime import datetime, date

# print(dir(datetime))  # 看看datetime中有些什么
# print(dir(datetime.date))  # 看看datetime.date中有些什么
# print(dir(datetime.datetime))  # 看看datetime.date中有些什么

# print(datetime.datetime.now()) # 打印当前的精确时间，用datetime的datetime.now()方法
# print(datetime.date.today()) # 打印当前日期，用datetime的date.today()方法


# 获取年月日
# print('当前是{}年'.format(datetime.date.today().year))
# print('当前是{}月'.format(datetime.date.today().month))
# print('当前是{}日'.format(datetime.date.today().day))

# d = datetime.date(2024,3,12)
# d = datetime.date(2024,3,12)
# print(d)

# 从时间戳获得日期
# d_ = datetime.date.fromtimestamp(45613486)
# d__ = datetime.date.fromtimestamp(1576244364)
# print(d_,d__)

# n = datetime.now()
# print("年 =", n.year)
# print("月 =", n.month)
# print("日 =", n.day)
# print("时 =", n.hour)
# print("分 =", n.minute)
# print("秒 =", n.second)
# print("微秒 =", n.microsecond)
# print("时间戳 =", n.timestamp())