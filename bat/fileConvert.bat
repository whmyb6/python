@Rem ======== a.txt ==========
@Rem a1 a2 a3 a4 a5 a6 a7 a8
@Rem b1 b2 b3 b b b b b
@Rem c1 c2 c3 c c c c c
@Rem -------------------------

@Rem ======== b.txt ===============
@Rem 27850 3758 5739 22253 28262
@Rem 15464 30413 30033 24543 24661
@Rem 1853 8091 23919 17560 19680
@Rem 23470 21890 23992 27313 32488
@Rem 19728 19875 10358 26951 15913
@Rem ------------------------------

@Rem ====== 使文本内容纵列按横向显示 ===========
	@echo off&setlocal enabledelayedexpansion
	echo "使文本内容纵列按横向显示"
	:loop
	set /a n+=1
	for /f "tokens=%n%" %%a in (a.txt) do (
		set /a m+=1
		echo %%a
		call set .!n!=%%.!n!%% %%a
	)
	if !n! lss 3 goto loop
	set .
	pause

@Rem ======= 对文本行的数字排序的代码 ===========
	@echo off
	echo "对文本行的数字排序的代码"
	for /f "delims=" %%a in (b.txt) do (
		setlocal enabledelayedexpansion
		for %%i in (%%a) do (
		set "str=0000000000%%i"
		set #!str:~-10!=%%i
		)
		for /f "tokens=2 delims==" %%i in ('set #') do set var=!var! %%i
	    echo !var!
	    endlocal
	)
	pause
	