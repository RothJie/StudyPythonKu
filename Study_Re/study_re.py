import re

"""
re.match函数  语法：re.match(pattern, string, flags=0)  返回一个对象
re.match从字符串的起始位置开始匹配指定的模式. 
flags
    re.I 忽略大小写
    re.L 表示特殊字符集 \w, \W, \b, \B, \s, \S 依赖于当前环境
    re.M 多行模式
    re.S 即为 . 并且包括换行符在内的任意字符（. 不包括换行符）
    re.U 表示特殊字符集 \w, \W, \b, \B, \d, \D, \s, \S 依赖于 Unicode 字符属性数据库
    re.X 为了增加可读性，忽略空格和 # 后面的注释
"""

result = re.match('\d+',"123b jhhhj4bjn54nm mn3bn 34bn5",flags=0) # 匹配数字
resu = re.match('\d+',"sd123b jhhhj4bjn54nm mn3bn 34bn5",flags=0) # 匹配数字
print(result.group(),resu)


"""
re.search()函数 语法：re.search(pattern, string, flags=0)  返回一个对象
re.search 扫描整个字符串并返回第一个成功的匹配。
"""
print(re.search('www','www.baidu.com').group())
print(re.search('\d','www.baidu1.com').group())


"""
compile 函数
compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，re函数使用。
提前编译可减少多次正则匹配的运行时间
语法格式为：re.compile(pattern[, flags])
参数：
pattern  一个字符串形式的正则表达式
flags 可选，表示匹配模式
"""

"""
re.findall()
在字符串中找到正则表达式所匹配的[所有子串]，并返回一个列表，如果没有找到匹配的，则返回空列表
语法：
第一种：re.findall(pattern, string, flags=0)
第二种：
mat = re.compile(pattern[, flags])
mat.findall(string,pos,endpos)  #pos 可选参数，指定字符串的起始位置，默认为 0。endpos 可选参数，指定字符串的结束位置，默认为字符串的长度
"""
res =  re.findall(pattern='[0-9]*b',string="123b bjhhhj4bjn54nm mn3bn 34bn5")
print(res)

mat = re.compile("\d+")
res1 =  mat.findall("123b jhhhj4bjn54nm mn3bn 34bn5")
res2 =  mat.findall("123b jhhhj4bjn54nm mn3bn 34bn5",0,10)
print(res1,res2)

"""
re.finditer函数 re.finditer(pattern, string, flags=0)
和 findall 类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回。
"""

res_iter = re.finditer(pattern='[0-9]*b',string="123b bjhhhj4bjn54nm mn3bn 34bn5")

re_li = []
for res in res_iter:
    re_li.append(res.group())
    print(res.group())  # 返回只一个值用res.group()， 返回有多个值时用res.groups()

print(re_li)

# re_li_ = ['d%s' % i for i in res_iter]  # 这个迭代器不能用于进行列表推导式
re_li_ = ['d%s' % i.group() for i in res_iter]  # 这个迭代器不能用于进行列表推导式
print(re_li_)

"""
re.split
split 方法按照能够匹配的子串将字符串分割后返回列表，它的使用形式如下：
re.split(pattern, string[, maxsplit=0, flags=0])
"""

"""
re.sub    re模块提供了re.sub用于替换字符串中的匹配项。

语法：re.sub(pattern, repl, string, count=0, flags=0)
参数：
pattern : 正则中的模式字符串。
repl : 替换的字符串，也可为一个函数。
string : 要被查找替换的原始字符串。
count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。
flags : 编译时用的匹配模式，数字形式。

repl 参数可以是一个函数
以下实例中将字符串中的匹配的数字乘于 2：

实例： 
# 将匹配的数字乘于 2
def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)
 
s = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', double, s))   # 取不取别名均可
"""


def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)


s = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', double, s))