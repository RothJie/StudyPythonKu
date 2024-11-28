import random
import string

print(random.random())  # 随机生成一个在0~1之间的浮点数
print(random.randint(1,60))  # 随机生成一个0~60之间的整数
print(random.uniform(5.5,8.5))  # 定制生成一个在5.5~8.5之间的浮点数或整数

# random.choice() 可以传入列表，字符串，元组
print(random.choice([456,789,123])) 
print(random.choice("gjghjkjakdbmbS"))
print(random.choice((456,4,89,78,"fajh")))

print(random.randrange(0,100,2))	# 生成从1到100的间隔为2的随机整数

# 多个字符中生成指定数量的随机字符列表：
print (random.sample('zyxwvutsrqponmlkjihgfedcba',5))

# 从a-zA-Z0-9生成指定数量的随机字符：(生成密码)
ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 6))
print (ran_str)

# 打乱排序
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
random.shuffle(items)
print(items)