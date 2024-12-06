"""Pandas JSON"""

# import pandas as pd
#
# df = pd.read_json('demo5dir_read_json.json')
# print(df.to_string())


# # 当然也可以直接加载Json字符串
# import pandas as pd
# data =[
#     {
#       "id": "A001",
#       "name": "菜鸟教程",
#       "url": "www.runoob.com",
#       "likes": 61
#     },
#     {
#       "id": "A002",
#       "name": "Google",
#       "url": "www.google.com",
#       "likes": 124
#     },
#     {
#       "id": "A003",
#       "name": "淘宝",
#       "url": "www.taobao.com",
#       "likes": 45
#     }
# ]
# df = pd.DataFrame(data)
# print(df)


# import pandas as pd
# URL = 'https://static.jyshare.com/download/sites.json'  # 通过连接可以直接的到的json也可以直接读
# df = pd.read_json(URL)
# print(df)


# # 假设有一组内嵌的 JSON 数据文件 demo5contain_json.json
# import pandas as pd
# import json
# '''这种读取方法的到的数据并不是我们想要的'''
# # df = pd.read_json('demo5contain_json.json')
# # print(df)
#
# # 使用 Python JSON 模块载入数据
# with open('demo5contain_json.json','r') as f:
#     data = json.loads(f.read())
# # # 展平数据 使用到 json_normalize() 方法将内嵌的数据完整的解析出来：
# # df_nested_list = pd.json_normalize(data, record_path =['students'])
#
# # 显示结果还没有包含 school_name 和 class 元素，如果需要展示出来可以使用 meta 参数来显示这些元数据：
# df_nested_list = pd.json_normalize(data,
#                                    record_path=['students'],
#                                    meta=['school_name','class'])
# print(df_nested_list.to_string())


# 下面尝试读取更加复杂的文件
# import pandas as pd
# import json
# # 使用 Python JSON 模块载入数据
# with open('demo5more_json.json', 'r') as f:
#     data = json.loads(f.read())
# df = pd.json_normalize(
#     data,
#     record_path=['students'], # 记录内容主要的
#     meta=[
#         'class',
#         ['info', 'president'],
#         ['info', 'contacts', 'tel']
#     ]
# )
# print(df.to_string())


# # 读取内嵌数据中的一组数据
# # 以下是实例文件 demo5contain_json.json，我们只读取内嵌中的 math 字段：
# # 首先安装 pip install glom
# import pandas as pd
# from glom import glom
# df = pd.read_json('demo5contain_json.json')
# data = df['students'].apply(lambda row: glom(row, 'grade.chemistry'))
# print(data)