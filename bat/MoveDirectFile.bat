@Rem
@Rem =========================================================================================================================================
@Rem ！！！！！  注意：执行bat 文件，使用 ANSI 编码格式 ！！！！！！！！！！
@Rem 功能：利用批处理移动到work_path主目录下的一级子文件夹中的下级子目录里面的全部文件到一级子目录下。
@Rem 批处理当中的 for 循环的结构：for /r %%a in (*.txt) do move %%a C:\Users\CSDN\Desktop

@Rem %%a 为变量，/r 为递归方式，in 与 do 之间一定要有 ()。
@Rem
@Rem for 循环的工作流程：查找当前文件夹及其子文件夹里面的 txt 文件，找到后把文件路径赋值给变量 %%a，然后执行 do 后面的语句，直到遍历完全部文件。
@Rem
@Rem setlocal已经达到最大递归层解决方式：
@Rem 在程序的有效处添加endlocal，终止递归。然后在下面再加一条setlocal，重启递归，即可防止递归最大层。
@Rem ==========================================================            ====================================================================
@Rem |                                                        |
@Rem |          Author: whm           date :2019-10-07        |
@Rem |                              update :2020-07-24        |
@Rem ==========================================================
@Rem

@echo off
@Rem setlocal enabledelayedexpansion  @Rem ##注意：打开此选项对目录名，含有！！！的无法，会丢失信息，造成异常处理！

set curr_path=%~dp0
set curr_disk=%~d0
echo curr_path = %curr_path%
echo curr_disk = %curr_disk%

@Rem set work_path="D:\Program Files\JiJiDown\Download\IBM 开放技术微讲堂 超级账本Fabric v1.4 LTS系列课程"
@Rem set work_path=J:\OK-2017\OK\US\


@echo off
    echo *****************************************************************
    echo     提示：  存在风险，移动当前目录 %curr_path%
	echo     下的一级子目录中的子目录里面的全部文件,到一级子目录下！
	set /p input =.        确认，请输入(y/n):
	echo %input%
	if "%input%"=="y" (
		echo ok
	) else (
		if "%input%"=="Y" (
			echo ok
		) else (
		  goto :eof
		)
	)



@Rem 保存当前目录以供 POPD 命令使用，然后改到指定的path 目录
pushd %work_path%




del temp.txt

for /D %%p in (*) do (
@Rem 保目录名保存到 临时文件，加入？号，便于 分解
	echo "%%~fp" >> temp.txt
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
 set curr_do_path=%curr_work_path:~1,-1%

 @Rem set curr_do_path=%curr_work_path:^(=%
 @Rem set curr_do_path=%curr_work_path:^)=%
 call :strLen curr_do_path,strlen

 @Rem set curr_do_path=%curr_do_path:\=%
 echo %curr_do_path%

 echo curr_do_path length=%strlen%

 setlocal enabledelayedexpansion
 echo %curr_work_path%
 for /R %curr_work_path% %%s in (*) do (
	@Rem echo %%s
	@Rem echo %YYYYmmdd%
	@Rem echo %hhmiss%

	@Rem 取出文件的硬盘+path 信息

	@Rem ::echo filepath=%%~dps  curr_work_path=%curr_work_path:~0,-1%\"

	set mfilepath=%%~dps
	@Rem set mfilepath=!mfilepath:^(=!
	@Rem set mfilepath=!mfilepath:^)=!

	@Rem set filepath=!filepath:\=!
	echo mfilepath=!mfilepath! f=%%~dps curr_do_path="%curr_do_path%"

	@Rem call echo ffff=%%mfilepath:%curr_do_path%=%%
    @Rem call set addname=%%mfilepath:%curr_do_path%=%%
	@Rem set addname=!addname:~1!
	@Rem set addname=!addname:\=_!
	call set addname=%%mfilepath:~%strlen%%%
	set addname=!addname:~1!
	set addname=!addname:\=_!
	echo addname=!addname!


	@Rem ::set filen=!filepath:~%strlen%!
	@Rem ::echo !filen!

	@Rem 判断是否为相同目录，文件所在目录与主目录不一致，则进行移动文件的操作。
	@Rem :: %curr_work_path:~0,-1%\"  （说明：删除curr_work_path的最后一个字符,并增加 \ 和 ” 两个字符）
	if not "%%~dps"==%curr_work_path:~0,-1%\" (

		@Rem 关闭变量延迟 ,防止 sfile 无法处理感叹号！！
		endlocal
		set sfile="%%s"


		setlocal enabledelayedexpansion

		set YYYYmmdd=%date:~0,4%%date:~5,2%%date:~8,2%
		set hhmiss=%time:~0,2%%time:~3,2%%time:~6,2%

		if exist %curr_work_path%\!addname!%%~ns%%~xs (
			echo ^^!^^!发现存在同名文件,修改目标文件名称:!sfile!
			echo 修改文件名为:!addname!%%~ns!YYYYmmdd!_!hhmiss!%%~xs
			move !sfile! %curr_work_path%\"!addname!%%~ns!YYYYmmdd!_!hhmiss!%%~xs"
			) else (
			echo source file=!sfile!
			set dfile=%curr_work_path%\"!addname!%%~ns%%~xs"
			echo move file to:!dfile!
			@Rem move "%%s" %curr_work_path%\"!addname!%%~ns%%~xs"
			move !sfile! !dfile!

			)
    )
 )
 endlocal
 goto :end

 @Rem :: 计算字符串长度 =====
 @Rem :: call :strLen（函数名） str(字符串) strlen(返回值）
 :strLen
 setlocal enabledelayedexpansion
 :strLen_Loop
	if not "!%1:~%len%!"=="" set /A len+=1  & goto :strLen_Loop
 (endlocal & set %2=%len%)


:end

