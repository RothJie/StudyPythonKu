import time
from datetime import date,datetime

"""
time.time(): 返回自纪元（1970年1月1日00:00:00 UTC）以来的秒数，通常称为Unix时间戳。
time.localtime(): 返回一个表示本地时间的time.struct_time对象。
time.gmtime(): 返回一个表示协调世界时（UTC）的time.struct_time对象。
"""
now = time.time()
# print(now) # 可以获取时间戳   date.fromtimestamp(time.time()) 可以返回具体时间

# print(time.localtime())
# print(time.gmtime())

# 格式化本地时间
# formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) #需要传入一个时间元组
# print("北京时间:", formatted_time)
# print("北京时间：",datetime.now().strftime("%Y年%m月%d日 %H时%M分%S秒"))

# print("开始休眠...")
# time.sleep(2)  # 休眠2秒
# print("休眠结束!")

# 获取10秒后的时间戳
# print(now + 10)
# 获取10秒前的时间戳
# print(now-10)

# 计算一段程序所需时间
# start_time = time.time()
# for i in range(400):
#     print("已经完成%s了！" % i)
#
# end_time = time.time()
# execution_time = end_time - start_time
# print(execution_time)

# 定时器(每隔一定时间执行一次任务)
# 你可以使用 time.sleep()和一个循环来创建一个简单的定时器。
# def timer_task():
#     print("定时任务执行中...")
# while True:
#     timer_task()
#     time.sleep(5)  # 每5秒执行一次


