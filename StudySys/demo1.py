import sys

print("The list of command line arguments:\n", sys.argv) # 命令行参数列表
# sys.exit(0)  #退出程序，正常退出时exit(0)

print('该电脑的系统是%s'%sys.platform) # 看系统
print(sys.byteorder) # “byteorder”即“字节序”，指的是在计算机内部存储数据时，数据的低位字节存储在存储空间中的高位还是低位。
print('获取Python解释程序的版本信息%s' % sys.version)
print('当前运行的 Python 解释器对应的可执行程序所在的绝对路径是%s' % sys.executable)
print('sys.getsizeof()返回的是作用对象所占用的字节数,例如1返回%s' % sys.getsizeof(1))

"sys.ps1和sys.ps2,这两个属性中，sys.ps1代表的是一级提示符，也就是进入 Python 交互界面之后就会出现的那一个>>>；而第二个sys.ps2则是二级提示符，是在同一级内容没有输入完，换行之后新行行首的提示符...。当然，两个属性都是字符串。"

sys.exit(0)  #退出程序，正常退出时exit(0)