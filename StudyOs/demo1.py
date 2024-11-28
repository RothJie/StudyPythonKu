"""
os，语义操作系统，所以该模块就是操作系统相关的功能了，用于处理文件和目录这些我们日常手动需要做的操作。

比如新建文件夹、获取文件列表、删除某个文件、获取文件大小、重命名文件、获取文件修改时间等，该模块就包含了大量的操作系统操作函数，精选常用的进行解析，希望对大家有所帮助。
"""

#加载
import os

# t = os.name  #显示当前使用的平台，'nt'表示Windows，'posix' 表示Linux
# print(t)

# path = os.getcwd() # 返回当前进程的工作目录。
# print(path)

# os.chdir('D:\网易有道\Dict') # 更改当前目录到新的目录'D:\网易有道\Dict'

# os.mkdir(r'C:\Users\Administrator\Desktop\test\demo2',mode=0o777) # 创建文件夹
# os.mkdir(r'C:\Users\Administrator\Desktop\test\demo4',mode=0o777) # 创建文件夹

# files = os.listdir(r'C:\Users\Administrator\Desktop\test') # 列出目录下的所有文件和文件夹
# print(files)  # 返回列表

# os.remove(r'C:\Users\Administrator\Desktop\test\demo3\f.txt')  # 用于删除文件夹中的文件

# os.rename(r'C:\Users\Administrator\Desktop\test\demo',
#           r'C:\Users\Administrator\Desktop\test\form1') # 命名文件或目录,能对相应的文件进行重命名


# f = os.open(r'C:\Users\Administrator\Desktop\test\demo1\01.txt',os.O_RDWR|os.O_CREAT )
# os.write(f,b'This is a world of all compete')
# os.close(f)
# f = open(r'C:\Users\Administrator\Desktop\test\demo1\01.txt','r')
# print(f.read())
# f.close()

# info = os.stat(r'C:\Users\Administrator\Desktop\test')
# print(info)

# print(os.sep) # 显示当前平台下路径分隔符,在 POSIX 上是 '/'，在 Windows 上是 '\'



# path = '.'
# path = r'C:\Users\Administrator\Desktop\test\demo1\02.txt'
path = r'C:\Users\Administrator\Desktop\test'
# print(os.path.abspath(path))  # 返回文件的绝对路径
# print(os.path.basename(path)) #描述：返回文件名，纯粹字符串处理逻辑，路径错误也可以
# print(os.path.dirname(path)) #描述：返回文件路径

# print(os.path.exists(path))  # 判断文件path是否存在，存在返回Ture,否则返回False
# os.path.lexists() #描述：路径存在则返回True，路径损坏也返回True， 不存在，返回 False。

# os.path.getatime()
# 描述：返回最近访问时间（浮点型秒数），从新纪元到访问时的秒数。

# os.path.getmtime()
# 描述：返回最近文件修改时间，从新纪元到访问时的秒数。

# os.path.getctime()
# 描述：返回文件 path 创建时间，从新纪元到访问时的秒数。

# print(os.path.getsize(path))
# 描述：返回文件大小，如果文件不存在就返回错误

#文件不存在 返回False 是文件夹返回False 只有是文件时返回True
# print(os.path.isfile(path))
#文件不存在 返回False 是文件返回False 只有是文件夹时返回True
# print(os.path.isdir(path))

# new_path = os.path.normpath('c:/windows/System32/Temp/')  # 描述：规范path字符串形式
# print(new_path)

# print(os.path.split(path))
# 描述：把路径分割成 dirname 和 basename，返回一个元组

# print(os.path.splitext(path))
# 描述：分割路径，返回路径名和文件扩展名的元组

for file in os.walk(path):  # 遍历path，进入每个目录都调用visit函数
    print(file)
