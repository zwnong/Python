@echo off
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