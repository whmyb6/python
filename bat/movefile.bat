@Rem
@Rem =============================================================================================================
@Rem ！！！！！  注意：执行bat 文件，使用 ANSI 编码格式 ！！！！！！！！！！
@Rem 功能：利用批处理移动一个文件夹及其子文件夹里面的某一格式的全部文件到另一个文件夹。
@Rem 批处理当中的 for 循环的结构：for /r %%a in (*.txt) do move %%a C:\Users\CSDN\Desktop

@Rem %%a 为变量，/r 为递归方式，in 与 do 之间一定要有 ()。
@Rem
@Rem for 循环的工作流程：查找当前文件夹及其子文件夹里面的 txt 文件，找到后把文件路径赋值给变量 %%a，然后执行 do 后面的语句，直到遍历完全部文件。
@Rem =================================================================================================================

@echo on
set work_path="J:\OK-2018\最新合集"
for /R %work_path% %%s in (.,*) do (
echo %%s
move "%%s" "%work_path%"
)
pause