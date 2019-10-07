@Rem
@Rem =============================================================================================================
@Rem ！！！！！  注意：执行bat 文件，使用 ANSI 编码格式 ！！！！！！！！！！
@Rem 功能：利用批处理移动到work_path主目录下的一级子文件夹中的下级子目录里面的全部文件到一级子目录下。
@Rem 批处理当中的 for 循环的结构：for /r %%a in (*.txt) do move %%a C:\Users\CSDN\Desktop

@Rem %%a 为变量，/r 为递归方式，in 与 do 之间一定要有 ()。
@Rem
@Rem for 循环的工作流程：查找当前文件夹及其子文件夹里面的 txt 文件，找到后把文件路径赋值给变量 %%a，然后执行 do 后面的语句，直到遍历完全部文件。
@Rem =================================================================================================================



@echo off
@Rem setlocal enabledelayedexpansion  ##注意：打开此选项对目录名，含有！！！的无法处理，会丢失信息，造成异常！

set curr_path=%~dp0
set curr_disk=%~d0
echo curr_path = %curr_path%
echo curr_disk = %curr_disk%

set work_path=F:\OK-2015\JP\

@Rem 保存当前目录以供 POPD 命令使用，然后改到指定的path 目录
pushd %work_path%

del temp.txt > errorlog.txt

for /D %%p in (*) do (
@Rem 保目录名保存到 临时文件，加入？号，便于 分解
	echo "%%p" >> temp.txt
)
@Rem 分解目录名，并调用函数，执行文件移动处理
for /F "delims=?" %%f in (temp.txt) do (
	call :listfile %%f
@Rem call %curr_path%listfile.bat %%f   # 调用bat文件方式
)

@Rem 更改到 PUSHD 命令存储的目录。
popd

pause
goto :end

@Rem 函数：处理当前目录下的每一个文件，移动目录的子目录下的文件，到当前目录下---
:listfile
set curr_work_path=%1%
@Rem echo %curr_work_path%
for /R %curr_work_path% %%s in (*) do (
echo %%s
move "%%s" %curr_work_path%
)
:end
