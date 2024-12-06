import pandas as pd
import numpy as np
# Pandas 数据结构 - Series
"""
pandas.Series(data=None, index=None, dtype=None, name=None, copy=False, fastpath=False)

    data：Series 的数据部分，可以是列表、数组、字典、标量值等。如果不提供此参数，则创建一个空的 Series。
    index：Series 的索引部分，用于对数据进行标记。可以是列表、数组、索引对象等。如果不提供此参数，则创建一个默认的整数索引。
    dtype：指定 Series 的数据类型。可以是 NumPy 的数据类型，例如 np.int64、np.float64 等。如果不提供此参数，则根据数据自动推断数据类型。
    name：Series 的名称，用于标识 Series 对象。如果提供了此参数，则创建的 Series 对象将具有指定的名称。
    copy：是否复制数据。默认为 False，表示不复制数据。如果设置为 True，则复制输入的数据。
    fastpath：是否启用快速路径。默认为 False。启用快速路径可能会在某些情况下提高性能。
"""

"""创建Series"""
# a = [1, 2, 3]
# myvar = pd.Series(a)  # 如果没有指定索引，索引值就从 0 开始
# print(myvar)
# print(myvar[0])
#
#
# a1 = ["Google", "Runoob", "Wiki"]
# myvar1 = pd.Series(a1, index = ["x", "y", "z"])  # 指定索引index = []
# print(myvar1)
# print(myvar1["y"])
# print(myvar1[1]) # 使用默认的所应也可以


# sites = {1: "Google", 2: "Runoob", 3: "Wiki"}
#
# myvar = pd.Series(sites, index = [1, 2])
# myvar1 = pd.Series(sites, index = [2,3],name="RUNOOB-Series-TEST")
# print(myvar)
# print(myvar1)

# 使用列表创建 Series
# s = pd.Series([1, 2, 3, 4])
# 使用 NumPy 数组创建 Series
# s = pd.Series(np.array([1, 2, 3, 4]))
# 使用字典创建 Series
# s = pd.Series({'a': 1, 'b': 2, 'c': 3, 'd': 4})

"""基本操作"""
# 指定索引创建 Series
s = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])

# 获取值
# value = s[2]  # 获取索引为2的值
# print(value)
# print(s['a'])  # 返回索引标签 'a' 对应的元素

# 获取多个值
# subset = s[1:4]  # 获取索引为1到4的值 包含后面
# subset = s['b':'d']  # 获取索引为1到4的值 包含后面
# print(subset)

# 使用自定义索引
# value = s['b']  # 获取索引为'b'的值

# 索引和值的对应关系
# for index, value in s.items():
#     print(f"Index: {index}, Value: {value}")


# # 使用切片语法来访问 Series 的一部分
# print(s['a':'c'])  # 返回索引标签 'a' 到 'c' 之间的元素
# print(s[:3])  # 返回前三个元素

# 为特定的索引标签赋值
# s['a'] = 10  # 将索引标签 'a' 对应的元素修改为 10
# print(s)

# 通过赋值给新的索引标签来添加元素
# s['e'] = 5  # 在 Series 中添加一个新的元素，索引标签为 'e'
# print(s)

# 使用 del 删除指定索引标签的元素。在同一个Series上删除
# del s['a']  # 删除索引标签 'a' 对应的元素
# print(s)

# 使用 drop 方法删除一个或多个索引标签，并返回一个新的 Series。
# s_dropped = s.drop(['b'])  # 返回一个删除了索引标签 'b' 的新 Series
# print(s_dropped)

"""基本运算"""
# 算术运算
# result = s * 2  # 所有元素乘以2
# print(result)

# 过滤
# filtered_series = s[s > 2]  # 选择大于2的元素
# print(filtered_series)
# result = np.sqrt(s)  # 对每个元素取平方根
# print(result)

"""计算统计数据：使用 Series 的方法来计算描述性统计。"""
# print(s.sum())  # 输出 Series 的总和
# print(s.mean())  # 输出 Series 的平均值
# print(s.max())  # 输出 Series 的最大值
# print(s.min())  # 输出 Series 的最小值
# print(s.std())  # 输出 Series 的标准差

"""Series属性和方法"""
# # 获取索引
# index = s.index
#
# # 获取值数组
# values = s.values
#
# # 获取描述统计信息
# stats = s.describe()
#
# # 获取最大值和最小值的索引
# max_index = s.idxmax()
# min_index = s.idxmin()
#
# # 其他属性和方法
# print(s.dtype)   # 数据类型
# print(s.shape)   # 形状
# print(s.size)    # 元素个数
# print(s.head())  # 前几个元素，默认是前 5 个
# print(s.tail())  # 后几个元素，默认是后 5 个
# print(s.sum())   # 求和
# print(s.mean())  # 平均值
# print(s.std())   # 标准差
# print(s.min())   # 最小值
# print(s.max())   # 最大值

"""转换数据类型：使用 astype 方法将 Series 转换为另一种数据类型。"""
# s = s.astype('float64')  # 将 Series 中的所有元素转换为 float64 类型