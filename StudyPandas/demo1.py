import pandas as pd

"""
Pandas 是 Python 语言的一个扩展程序库，用于数据分析。
Pandas 名字衍生自术语 "panel data"（面板数据）和 "Python data analysis"（Python 数据分析）。
Pandas 是一个开放源码、BSD 许可的库，提供高性能、易于使用的数据结构和数据分析工具。
Pandas 一个强大的分析结构化数据的工具集，基础是 Numpy（提供高性能的矩阵运算）。
"""
# Pandas 主要引入了两种新的数据结构：DataFrame 和 Series。

# Series： 类似于一维数组或列表，是由一组数据以及与之相关的数据标签（索引）构成。
# Series 可以看作是 DataFrame 中的一列，也可以是单独存在的一维数据结构。

pd_v = pd.__version__
print(pd_v)