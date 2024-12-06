"""Pandas CSV 文件"""

import pandas as pd

path = r"F:\罗平县3年的天气状况.csv"
df = pd.read_csv(path)

# print(df.to_string())
df['date'] = df['date'].astype('datetime64[ns]') # 将'date'列转换为日期时间类型
# df.set_index('date', inplace=True)

# print(df.head())
# df.to_csv('./罗平县3年的天气状况.csv') # 方法将 DataFrame 存储为 csv 文件

# print(df.info())

# 将'date'列转换为日期时间类型
# df['date'] = pd.to_datetime(df['date'])


"""筛选2023年6月的数据的4种方法"""
# new_df = df[(df['date'].dt.year == 2023) & (df['date'].dt.month == 6)] #布尔筛选
new_df = df.loc[(df['date'].dt.year == 2023) & (df['date'].dt.month == 2)] # .loc()
# new_df = df.query("date.dt.year == 2023 and date.dt.month == 6") # 使用query方法
# # 确定2023年6月的起始和结束日期
# start_date = '2023-06-01'
# end_date = '2023-06-30'
# new_df = df[df['date'].between(start_date, end_date)] # 使用between方法（针对日期范围）

print(new_df.to_string())