"""
Pandas 数据结构 - DataFrame
DataFrame 是 Pandas 中的另一个核心数据结构，用于表示二维表格型数据。
DataFrame 是一个表格型的数据结构，它含有一组有序的列，每列可以是不同的值类型（数值、字符串、布尔型值）。
DataFrame 既有行索引也有列索引，它可以被看做由 Series 组成的字典（共同用一个索引）。
DataFrame 提供了各种功能来进行数据访问、筛选、分割、合并、重塑、聚合以及转换等操作。
"""

"""
DataFrame 构造方法如下：
pandas.DataFrame(data=None, index=None, columns=None, dtype=None, copy=False)
参数说明：
data：DataFrame 的数据部分，可以是字典、二维数组、Series、DataFrame 或其他可转换为 DataFrame 的对象。如果不提供此参数，则创建一个空的 DataFrame。
index：DataFrame 的行索引，用于标识每行数据。可以是列表、数组、索引对象等。如果不提供此参数，则创建一个默认的整数索引。
columns：DataFrame 的列索引，用于标识每列数据。可以是列表、数组、索引对象等。如果不提供此参数，则创建一个默认的整数索引。
dtype：指定 DataFrame 的数据类型。可以是 NumPy 的数据类型，例如 np.int64、np.float64 等。如果不提供此参数，则根据数据自动推断数据类型。
copy：是否复制数据。默认为 False，表示不复制数据。如果设置为 True，则复制输入的数据。
"""

# import pandas as pd

# data = [['Google', 10], ['Runoob', 12], ['Wiki', 13]]
# # 创建DataFrame 按行创建结构
# df = pd.DataFrame(data, columns=['Site', 'Age'])
#
# # 使用astype方法设置每列的数据类型
# df['Site'] = df['Site'].astype(str)
# df['Age'] = df['Age'].astype(float)
# print(df)

# import pandas as pd
# data = {'Site':['Google', 'Runoob', 'Wiki'], 'Age':[10, 12, 13]}
#按列创建结构
# df = pd.DataFrame(data)
# print (df)


# import numpy as np
# import pandas as pd
# # 创建一个包含网站和年龄的二维ndarray
# ndarray_data = np.array([
#     ['Google', 10],
#     ['Runoob', 12],
#     ['Wiki', 13]
# ])
# # 使用DataFrame构造函数创建数据帧
# df = pd.DataFrame(ndarray_data, columns=['Site', 'Age'])
# # 打印数据帧
# print(df)


import pandas as pd
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
# # 数据载入到 DataFrame 对象
df = pd.DataFrame(data)
# # 返回第一行
# print(df.loc[0])
# # 返回第二行
# print(df.loc[1])

"""DataFrame 的属性和方法"""
# print(df.shape)     # 形状
# print(df.columns)   # 列名
# print(df.index)     # 索引
# print(df.head())    # 前几行数据，默认是前 5 行
# print(df.tail())    # 后几行数据，默认是后 5 行
# print(df.info())    # 数据信息
# print(df.describe())# 描述统计信息
# print(df.mean())    # 求平均值
# print(df.sum())     # 求和

"""访问 DataFrame 元素
访问列：使用列名作为属性或通过 .loc[]、.iloc[] 访问，也可以使用标签或位置索引。。"""

"""修改 DataFrame"""
# df['Column1'] = [10, 11, 12]  #修改列数据,直接对列进行赋值。
# df['NewColumn'] = [100, 200, 300] # 添加新列：给新列赋值。
'''添加新行：使用 loc、append 或 concat 方法。'''
# 使用 loc 为特定索引添加新行
# df.loc[3] = [13, 14, 15, 16]
# 使用 append 添加新行到末尾
# new_row = {'Column1': 13, 'Column2': 14, 'NewColumn': 16}
# df = df.append(new_row, ignore_index=True)

"""删除 DataFrame 元素"""
# df_dropped = df.drop('Column1', axis=1) # 删除列：使用 drop 方法。
# df_dropped = df.drop(0)  # 删除索引为 0 的行

"""DataFrame 的索引操作"""
# df_reset = df.reset_index(drop=True)  # 重置索引
# df_set = df.set_index('Column1') # 设置索引

# df[df['Column1'] > 2]  # 使用布尔表达式：根据条件过滤 DataFrame。

"""DataFrame 的合并与分割"""
# 合并：使用 concat 或 merge 方法。
# 纵向合并
# pd.concat([df1, df2], ignore_index=True)
# 横向合并
# pd.merge(df1, df2, on='Column1')

# 分割：使用 pivot、melt 或自定义函数。
# 长格式转宽格式
# df_pivot = df.pivot(index='Column1', columns='Column2', values='Column3')

# 宽格式转长格式
# df_melt = df.melt(id_vars='Column1', value_vars=['Column2', 'Column3'])