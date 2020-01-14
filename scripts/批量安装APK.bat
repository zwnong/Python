@echo off
setlocal EnableDelayedExpansion
title install apks
color 0a
:::: 重启adb 保证能顺利连接  
adb kill-server  
adb start-server  
adb wait-for-device
set ApkPath=%cd%\apks
cd %ApkPath%
set count = 0
for /R %%s in (*.apk) do (
    ::要使用引号来包括apk的路径，不然adb install语法报错
    set /a count +=1
    echo 正在安装第!count!个apk:
    echo %%s
    adb install "%%s"
    echo ------------------------------------------------
)
echo ***********安装完成***********
pause

