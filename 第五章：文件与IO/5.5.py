#文件不存在才能写入，你想像一个文件中写入数据，但是前提必须是这个文件在文件系统上不存在。 也就是不允许覆盖已存在的文件内容。
#可以在 open() 函数中使用 x 模式来代替 w 模式的方法来解决这个问题。比如：
with open('test.txt','wt') as f:
    f.write('Hello\n')
# with open('test.txt','xt') as f:
#     f.write('Hello\n')

#这一小节演示了在写文件时通常会遇到的一个问题的完美解决方案(不小心覆盖一个已存在的文件)。 一个替代方案是先测试这个文件是否存在，像下面这样：
import os
if not os.path.exists('test.txt'):
    with open('test.txt','wt') as f:
        f.write('Hello\n')
else:
    print('File already exists!')

'''
显而易见，使用x文件模式更加简单。要注意的是x模式是一个Python3对open()函数特有的扩展。
在Python的旧版本或者是Python实现的底层C函数库中都是没有这个模式的。
'''





