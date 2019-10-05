#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
for root, dirs, files in os.walk(r'J:\OK-2017\OK\JP', topdown=True):
    #print(format('root = %s')%root)
    for name in files:
        print(format('filename = %s') % os.path.join(root, name))
    for name in dirs:
        print(format('dir = %s') % os.path.join(root, name)).decode(encoding='gbk')