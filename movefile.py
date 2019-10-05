#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import shutil
import subprocess,psutil
import time
import subprocess,time,psutil

# 功能：将当前目录的字目录中的文件，移动到当前目录下=====
# 当前目录设置
path = r'J:\OK-2017\OK\JP\大橋未久 @@@@@@@@'

def execBatfile(filename):
    print(filename)
    #filename = unicode(filename, "utf8")
    #filename ='date'
    #os.system("cmd/c start")
    #os.system("start cmd /k echo Hello, World!")     # 新开的窗口不关闭
    os.system("start cmd /c " +filename)            # 新开的窗口会自动关闭，
    #os.system("cmd/c start&&" +  filename )
    # print(res.read())
    #os.system("pause")
    '''
    proc = subprocess.Popen("cmd.exe /c" + filename,creationflags=subprocess.CREATE_NEW_CONSOLE)
    time.sleep(10)

    pobj = psutil.Process(proc.pid)
    # list children & kill them
    for c in pobj.children(recursive=True):
        c.kill()
    pobj.kill()

    p = subprocess.Popen("cmd.exe /c " + filename, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,creationflags=subprocess.CREATE_NEW_CONSOLE)
    curline = p.stdout.readline()
    while (curline != b''):
        print(' ddd: ' +curline)
        curline = p.stdout.readline()

    p.wait()
    print(p.returncode)
    '''

print os.getcwd() #获取当前工作目录路径


mypath= unicode(path, "utf8")  # 处理中文目录名称 ====
cmdfile = r'movefile.bat'
os.chdir(mypath)
print os.getcwd().decode(encoding='gbk')

if os.path.exists(cmdfile):
    os.remove(cmdfile)

for root, dirs, files in os.walk('.', topdown=True):
    #print(format('root = %s')%root).decode(encoding='gbk')
    for name in files:
        if root != '.':
            print(format('filename = %s') % os.path.join(root, name)).decode(encoding='gbk')

            sourcefile =(os.path.join(root, name))
            newfile = (os.path.join('.',name))
            moveCmd = 'move "' + sourcefile + '" .'
            print(format('movefile: %s ==> %s '%(sourcefile,newfile))).decode(encoding='gbk')
            try:
                shutil.move(sourcefile, newfile)  # 移动
            except:

                with open(cmdfile, 'a+') as f:
                    f.write(moveCmd + '\n')  # 加\n换行显示

if os.path.exists(cmdfile):
    with open(cmdfile, 'a+') as f:
#        f.write('echo move file\n')
        f.write( 'pause\n')  # 加\n换行显示
    print('请执行:' + path + '\\'+  cmdfile + " !!")

    #os.system(cmdfile)
    #os.system(path + "\\" + cmdfile)
    execBatfile( cmdfile)

#from tkinter import messagebox
#print("这是一个弹出提示框")
#messagebox.showinfo("提示", "需运行" + cmdfile)


        #break
    #for name in dirs:
    #    print(format('dir = %s') % os.path.join(root, name)).decode(encoding='gbk')