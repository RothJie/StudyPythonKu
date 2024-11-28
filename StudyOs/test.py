import os

os.chdir(r'C:\Users\Administrator\Desktop\test')

li = os.listdir(('./'))

# print(os.path.exists('./demo4'))
for i in li:
    path =f'./{i}'
    isFile = os.path.isfile(path)
    # print(isFile)
    # isDir = os.path.isdir(path)
    if isFile:
        print(os.path.splitext(path))
    else:
        print(os.path.abspath(path))





# print(os.stat('./Study_math.py'))
# print(os.getcwd())
