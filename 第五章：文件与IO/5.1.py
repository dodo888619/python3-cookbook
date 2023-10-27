#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

import sys

# 读写文本数据，你需要读写各种不同编码的文本数据，比如ASCII，UTF-8或UTF-16编码等
# 使用带有rt模式的open()函数读取文本文件。
# Read the entire file as single string
with open('file.txt', 'r', encoding='utf-8') as f:
    data = f.read()

# Iterate over the lines of the file
with open('file.txt', 'rt', encoding='utf-8') as f:
    pass
# 如果是在已存在文件中添加内容，使用模式为 at 的 open() 函数。
with open('file.txt', 'at', encoding='utf-8') as f:
    pass
# Redirected print statement


print(sys.getdefaultencoding())
with open('file.txt', 'rt', encoding='utf-8') as f2:
    data = f2.read()
# 另外一个问题是关于换行符的识别问题，在Unix和Windows中是不一样的(分别是n和rn)。
# 默认情况下，Python会以统一模式处理换行符。
# 这种模式下，在读取文本的时候，Python可以识别所有的普通换行符并将其转换为单个 \n 字符。
# 类似的，在输出时会将换行符 \n 转换为系统默认的换行符。
# 如果你不希望这种默认的处理方式，可以给 open() 函数传入参数 newline=''，就像下面这样：
# Read with disabled newline translation
with open('file.txt', 'rt', newline='') as f3:
    pass

"""
最后一个问题就是文本文件中可能出现的编码错误。 但你读取或者写入一个文本文件时，你可能会遇到一个编码或者解码错误。比如：

>>> f = open('sample.txt', 'rt', encoding='ascii')
>>> f.read()
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "/usr/local/lib/python3.3/encodings/ascii.py", line 26, in decode
        return codecs.ascii_decode(input, self.errors)[0]
UnicodeDecodeError: 'ascii' codec can't decode byte 0xc3 in position
12: ordinal not in range(128)
>>>
如果出现这个错误，通常表示你读取文本时指定的编码不正确。 你最好仔细阅读说明并确认你的文件编码是正确的(比如使用UTF-8而不是Latin-1编码或其他)。
如果编码错误还是存在的话，你可以给 open() 函数传递一个可选的 errors 参数来处理这些错误。 下面是一些处理常见错误的方法：
>>> # Replace bad chars with Unicode U+fffd replacement char
>>> f = open('sample.txt', 'rt', encoding='ascii', errors='replace')
>>> f.read()
'Spicy Jalape?o!'
>>> # Ignore bad chars entirely
>>> g = open('sample.txt', 'rt', encoding='ascii', errors='ignore')
>>> g.read()
'Spicy Jalapeo!'
>>>
如果你经常使用 errors 参数来处理编码错误，可能会让你的生活变得很糟糕。
对于文本处理的首要原则是确保你总是使用的是正确编码。当模棱两可的时候，就使用默认的设置(通常都是UTF-8)。
"""

f5 = open('file.txt', 'rt', encoding='utf-8', errors='replace')
f6 = open('file.txt', 'rt', encoding='utf-8', errors='ignore')
