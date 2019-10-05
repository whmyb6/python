#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import shutil


print os.getcwd() #获取当前工作目录路径
path = r'J:\OK-2017\OK\JP\大橋未久 @@@@@@@@'

path= unicode(path, "utf8")  # 处理中文目录名称 ====
os.chdir(path)
print os.getcwd().decode(encoding='gbk')
for root, dirs, files in os.walk('.', topdown=True):
    #print(format('root = %s')%root).decode(encoding='gbk')
    for name in files:
        print(format('filename = %s') % os.path.join(root, name)).decode(encoding='gbk')
    #for name in dirs:
    #    print(format('dir = %s') % os.path.join(root, name)).decode(encoding='gbk')