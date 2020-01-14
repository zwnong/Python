
@echo off
echo adb wait-for-deveces
adb remount
echo 选择填充内容:
:MAIN
echo ------------------------------
echo (1)filled ROM
ECHO (2)filled RAM  #需root
echo ------------------------------
set /p UserSelection="请输入选择(1/2):"
if "%UserSelection%" == "1" (goto ROM
        )else(
		    if "%UserSelection%" == "2"(goto RAM
		        )else(
			    echo 您输入有误，请重新输入！
		        goto MAIN
		    )
		)
:ROM
echo 手机剩余内存为(Avail)：
adb shell df -h /data/media
set FilePath=/sdcard/TempFolder/
set /p FileSize=请指定文件大小(M:):
set /p NumberOfFiles=请输入创建的文件数量:
set a=0
if not exist %FilePath% adb shell mkdir %FilePath%
:begin
set /a a+=1
echo 正在创建中，请稍后...
adb shell dd if=/dev/zero of=%FilePath%%FileName%%a% bs=1048576 count=%FileSize%
if %a% == %NumberOfFiles% goto end
goto begin
:end
echo ---------------------------------------------
echo 文件已经在 %FilePath% 创建完成
echo ---------------------------------------------
pause
goto exist

:RAM
REM : 找到剩余的可利用的RAM
echo 目前剩余的内存为(KB):
adb shell "cat /proc/meminfo | grep MemAvailable"
ping -n 3 127.1>nul
REM :将 mem_occupy 文件push 到bin目录下
adb push mem_occupy /system/bin/
ping -n 2 127.1>nul
REM :给mem_occupy增加最大的权限
adb shell chmod 777 /system/bin/mem_occupy
set /p times=      请设置RAM的大小(M)：
echo 测试过程中请勿拔出USB线，如果测试完毕请使用Ctrl+C来停止运行！
adb shell mem_occupy %times%
pause
goto exist
