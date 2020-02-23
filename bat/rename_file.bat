@Rem
@Rem =========================================================================================================================================
@Rem ！！！！！  注意：执行bat 文件，使用 ANSI 编码格式 ！！！！！！！！！！
@Rem 功能：利用批处理移动当前目录下及子目录下的文件自动添加000000。
@Rem 批处理当中的 for 循环的结构：for /r %%a in (*.txt) do move %%a C:\Users\CSDN\Desktop

@Rem %%a 为变量，/r 为递归方式，in 与 do 之间一定要有 ()。
@Rem
@Rem for 循环的工作流程：查找当前文件夹及其子文件夹里面的 txt 文件，找到后把文件路径赋值给变量 %%a，然后执行 do 后面的语句，直到遍历完全部文件。
@Rem ==========================================================            ====================================================================
@Rem |                                                        |
@Rem |          Author: whm           date :2020-02-23        |
@Rem |                              update :2020-02-23        |
@Rem ==========================================================
@Rem


@Rem setlocal enabledelayedexpansion  @Rem ##注意：打开此选项对目录名，含有！！！的无法，会丢失信息，造成异常处理！



@echo off
	set /p input=提示：当前目录下及子目录下的文件头自动添加0，输入(y/n)：
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

	set filepath=%cd%
    set zero_str=000000000

	del temp.txt
	del temp_bat.bat

	setlocal enabledelayedexpansion
	set /A maxlen = 0

	@Rem :: 读取当前目录及子目录下的所有文件 =====
	for /r "%filepath%" %%s in (*) do (
	   @Rem 读取目录地址
	   set mfilepath=%%~dps
	   @Rem 读取文件名称
	   set mfilename=%%~nxs

	   @Rem 发现新的目录文件======
	   if not "!filepath!" == "!mfilepath!" (
	        @Rem 如果maxlen >0，说明上个目录存在文件，需要对上个目录中的文件名进行处理
			@Rem 处理带格式的临时文件，生成批命令文件
			echo maxlen=!maxlen!  !mfilepath!
            if !maxlen! GTR 0 (
			   for /f  "tokens=1,2 delims=@" %%i in (temp.txt) do (
				   @Rem echo %%i,%%j
				   @Rem 如果文件头含有数字，,以数字开始，就进行处理，生成rename命令===
				   echo %%i | findstr /b [^0-9] >nul &&(
						if !maxlen! gtr %%j (
							@Rem 计算需要重复的0的个数
							set /A replacenum=!maxlen!-%%j
							@Rem echo !replacenum! %%j !maxlen!
							@Rem 生成新文件名头
							call set newfilename=%%zero_str:~0,!replacenum!%%
							@Rem echo "!newfilename!"
							echo rename "%%i" "!newfilename!%%i" >> temp_bat.bat

						)

				   ) || (
						@Rem 如果文件头，不含有数字，无需处理直接保存===
						echo %%i >> temp_bat.bat
				   )

			   )
			)
			@Rem 重新建立标记
	        del temp.txt
			set /A maxlen = 0

			@Rem 生成新的目录文件
			echo cd "!mfilepath!" >> temp.txt
			set filepath=!mfilepath!
			echo #####!filepath! #####
	   )


	   @Rem echo !mfilepath!  %%s
	   @Rem 判断文件名格式为 . 分割，且文件头为数字 ， 把文件名及文件头的长度以 文件名 @ 头长度 保存到临时文件
	   @Rem 计算 文件头的最大长度
	   for /f  "tokens=1 delims=." %%i in ("!mfilename!") do (
			@Rem echo %%i
			set curr_head=%%i
			call :strLen curr_head,strlen
			@Rem echo 'strlen=' !strlen!

			@Rem 如果文件头含有数字就进行处理===
			@Rem 查找当前目录中文件头的长度的最大值，保存到 maxlen
			@Rem 保存当前的文件名和文件头长度，到临时文件temp.txt, 格式：文件名@长度
			echo !curr_head! | findstr /b [^0-9] >nul && (
				if !strlen! gtr !maxlen! set /A maxlen=!strlen!
				echo !mfilename!@!strlen! >> temp.txt
			)
			@Rem echo 'maxlen= ' !maxlen!
	   )
	)
   echo '============'

   @Rem 处理带格式的临时文件，生成批命令文件===
   for /f  "tokens=1,2 delims=@" %%i in (temp.txt) do (
       @Rem echo %%i,%%j
	   @Rem 如果文件头含有数字,以数字开始，就进行处理===
	   echo %%i | findstr /b [^0-9] >nul &&(
			if !maxlen! gtr %%j (
				@Rem 计算需要重复的0的个数
			    set /A replacenum=!maxlen!-%%j
				echo !replacenum! %%j !maxlen!
				@Rem 生成新文件名头
				call set newfilename=%%zero_str:~0,!replacenum!%%
				echo rename "%%i" "!newfilename!%%i" >> temp_bat.bat

			)

	   ) || (
	        @Rem 如果文件头，不含有数字，无需处理直接保存=====
			echo %%i >> temp_bat.bat
	   )

   )
   del temp.txt
   endlocal
   echo .
   echo .
   echo ********************************************************************
   echo .
   echo .
   echo                            提示：
   echo .
   echo      生成 %cd%\temp_bat.bat 批处理文件
   echo .    运行bat文件，即可执行!
   echo .
   echo .
   echo ********************************************************************
   echo .
   echo .
   pause
goto :eof

 @Rem :: 计算字符串长度 =====
 @Rem :: call :strLen（函数名） str(字符串) strlen(返回值）
 :strLen
	 setlocal enabledelayedexpansion
	 set /A len=0
	 :strLen_Loop
			if not "!%1:~%len%!"=="" set /A len+=1  & goto :strLen_Loop
	 (endlocal & set %2=%len%)

 :end