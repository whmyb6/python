#!/usr/bin/python
# -*- coding: UTF-8 -*-

import io
import os
import shutil
#import subprocess,psutil
import time
import sys
import chardet

# 功能：将当前目录的字目录中的文件，移动到当前目录下=====
# 当前目录设置
# 全局变量 ================
root_path =r'J:\OK-2018\AAAA系列'
#path = r'J:\OK-2017\OK\JP\AAAAA @@@@@@@@'

def sys_encoding_decoding():
    '''
    *首先要搞清楚，字符串在Python内部的表示是unicode编码，因此，在做编码转换时，通常需要以unicode作为中间编码，
    即先将其他编码的字符串解码（decode）成unicode，再从unicode编码（encode）成另一种编码。
    decode的作用是将其他编码的字符串转换成unicode编码，如str1.decode('gb2312')，表示将gb2312编码的字符串str1转换成unicode编码。
    encode的作用是将unicode编码转换成其他编码的字符串，如str2.encode('gb2312')，表示将unicode编码的字符串str2转换成gb2312编码。
    总得意思:想要将其他的编码转换成utf-8必须先将其解码成unicode然后重新编码成utf-8,它是以unicode为转换媒介的
    如：s='中文'
    如果是在utf8的文件中，该字符串就是utf8编码，如果是在gb2312的文件中，则其编码为gb2312。这种情况下，要进行编码转换，都需要先用
    decode方法将其转换成unicode编码，再使用encode方法将其转换成其他编码。通常，在没有指定特定的编码方式时，都是使用的系统默认编码创建的代码文件。
    如下：
    s.decode('utf-8').encode('utf-8')
    decode():是解码
    encode()是编码
    isinstance(s,unicode):判断s是否是unicode编码，如果是就返回true,否则返回false*
    chardet入门
    模块介绍
        Chardet：通用字符编码检测器，Python版本：需要Python 2.6,2.7或3.3+。
         检测字符集范围：
        ASCII，UTF-8，UTF-16（2种变体），UTF-32（4种变体）
        Big5，GB2312，EUC-TW，HZ-GB-2312，ISO-2022-CN（繁体中文和简体中文）
        EUC-JP，SHIFT_JIS，CP932，ISO-2022-JP（日文）
        EUC-KR，ISO-2022-KR（韩文）
        KOI8-R，MacCyrillic，IBM855，IBM866，ISO-8859-5，windows-1251（西里尔文）
        ISO-8859-5，windows-1251（保加利亚语）
        ISO-8859-1，windows-1252（西欧语言）
        ISO-8859-7，windows-1253（希腊语）
        ISO-8859-8，windows-1255（视觉和逻辑希伯来语）
        TIS-620（泰国语）


    '''
    '''
        s='中文'
        s=s.decode('utf-8')           #将utf-8编码的解码成unicode
        print isinstance(s,unicode)   #此时输出的就是True
        s=s.encode('utf-8')           #又将unicode码编码成utf-8
        print isinstance(s,unicode)   #此时输出的就是False
    '''
    print sys.getdefaultencoding()

    s='中文'
    if isinstance(s,unicode):   #如果是unicode就直接编码不需要解码
        print s.encode('utf-8')      # unicode -> utf8
    else:
        print s.decode('utf-8').encode('gb2312')  #utf8->unicode->gb2312

    print sys.getdefaultencoding()    #获取系统默认的编码
    reload(sys)
    sys.setdefaultencoding('utf8')    #修改系统的默认编码
    print sys.getdefaultencoding()

#  转化绝对路径为相对路径格式=========
def getRootDict(currpath):
    strpath = ""
    for ch in currpath:
        if ch =="\\":
            strpath =strpath+"..\\"
    return strpath

# 获取时间标志
def getTime():
    #获得当前时间时间戳
    now = int(time.time())
    #转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S"
    timeStruct = time.localtime(now)
    strTime = time.strftime("%Y%m%d_%H%M%S", timeStruct)
    print(strTime)
    return strTime



# 利用windows cmd 判断文件是否存在！
def fileExists(filename):
    if os.path.isdir(filename):
        return  False
    return os.path.exists(filename)
    '''
    #filename = unicode(filename, "gb18030")
    res = os.system("dir " +filename )           # 新开的窗口会自动关闭，
    if(res ==0 ):
        return True
    else:
        return False
    '''

# 利用 windows cmd 执行 BAT 命令
def execBatfile(filename):
    print(filename)
    #os.system("cmd/c start")
    #os.system("start cmd /k echo Hello, World!")     # cmd /k 新开的窗口不关闭
    os.system("start cmd /c " +filename)            # cmd /c 新开的窗口会自动关闭，
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
# 处理 文件名 含有？的情况，可能为目录
def chuliErrordictory(sourcefile,root_path):
    moveCmd = ""
    print(format('sourcedir = %s') % sourcefile.decode(encoding='gbk'))  # GBK-->UNICODE
    i = sourcefile.find('?')
    if i > -1:
        currpath = sourcefile[:i] + "*"
        moveCmd = 'cd "' + currpath + '"\n'
        r_path = getRootDict(currpath)
        print chardet.detect(currpath)

        print(format('   Curr path = %s  ') % (currpath)).decode(encoding='gbk')  # GBK-->UNICODE   root_path))   ##.decode('EUC-JP'
        print(format('   Root path = %s ') % (root_path))
        # os.chdir(currpath.decode(encoding='gbk'))

        moveCmd = moveCmd + 'move *.* ' + r_path + "\n"
        moveCmd = moveCmd + "cd " + root_path.decode(encoding='utf8').encode('mbcs') + "\n"  ##使用Python把UTF8转ANSI编码 utf8->unicode->mbcs
        # 返回 windows 的 cmd 命令
    return moveCmd

#  遍历目录，进行文件的移动
def doWorkDict(home_path):
    print os.getcwd()  # 获取当前工作目录路径
    curr_poject_home = os.getcwd()
    myrootpath = home_path.decode(encoding='utf8')  ##utf8字符串解码（decode）成unicode
    cmdfile = r'movefile.bat'
    os.chdir(myrootpath)
    print os.getcwd().decode(encoding='gbk')

    if os.path.exists(cmdfile):
        os.remove(cmdfile)
    '''
    dirs = os.listdir( '.\\1pondo' )
    for filed in dirs:
       #print (filed).decode(encoding='gbk')
       if os.path.isdir(os.path.join('.\\1pondo', filed)):
           print (filed).decode(encoding='gbk')
    '''

    for root, dirs, files in os.walk('.',topdown=True ):
        #print(format('root = %s')%root).decode(encoding='gbk')
        #for name in dirs:
        #    print(format('dirs = %s') % name).decode(encoding='gbk')
        for name in files:
            #print(format('filename = %s') % os.path.join(root, name)).decode(encoding='gbk')
            moveCmd = ""
            if root != '.': ##处理子目录下的文件===
                print(format('filename = %s') % os.path.join(root, name)).decode(encoding='gbk')
                sourcefile =(os.path.join(root, name))

                if fileExists(name):   #如果当前目录下，存在相同名称的文件，修改目标文件名（增加时间标记），防止覆盖 ===
                    i= name.rfind('.')
                    if i > -1 :
                        name = name[:i] + getTime() + name[i:]
                    else:
                        name = name+"_" + getTime()
                    moveCmd = 'move "' + sourcefile + '" "' +name +'"'
                else:
                    # 判断 文件名 含有？的错误情况，日语环境， 出现目录中无法识别的字符 识别为？ =====
                    #sourcedir = os.path.join(path,name)
                    moveCmd = chuliErrordictory(sourcefile,root_path)
                moveCmd = moveCmd +  'move "' + sourcefile + '" .'
                newfile = (os.path.join('.',name))
                try:
                    shutil.move(sourcefile, newfile)  # 执行命令，移动文件到新路径
                    print("Finish Move file ! ")
                except:
                    #对无法移动的文件，写入 bat 文件 ===
                    with open(cmdfile, 'a+') as f:
                        f.write(moveCmd + '\n')  # 加\n换行显示
            else:  ## 处理 当前目录下的异常文件名======
                sourcefile = (os.path.join(root, name))
                moveCmd = chuliErrordictory(sourcefile, root_path)
                if len(moveCmd) > 0:
                    # 保存到 bat 文件
                    with open(cmdfile, 'a+') as f:
                        f.write(moveCmd + '\n')  # 加\n换行显示





    # 存在 bat文件，通过 cmd 执行 bat文件
    if os.path.exists(cmdfile):
        with open(cmdfile, 'a+') as f:
    #        f.write('echo move file\n')
            f.write( 'pause\n')  # 加\n换行显示
        print('请执行:' + root_path + '\\'+  cmdfile + " !!")
        execBatfile( cmdfile)
    os.chdir(curr_poject_home)  # 返回当前目录==
    print(format( "返回主目录 = %s"% curr_poject_home ))

# ================main ==================
if __name__ == '__main__':
    print('sys.getfilesystemencoding:',sys.getfilesystemencoding())
    print( 'sys.getdefaultencoding:',sys.getdefaultencoding())
    print('sys.stdin.encoding:',sys.stdin.encoding)
    print('sys.stdin.encoding:',sys.stdout.encoding)

    doWorkDict(root_path)
    #myrootpath= unicode(root_path, "utf8")  # 处理中文目录名称 ====


###+=========================================