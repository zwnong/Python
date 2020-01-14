@echo off
title 手机录屏
color 0a
echo recording...
adb shell screenrecord --time-limit 180 /sdcard/record.mp4
pause
echo 将录屏文件保存到D盘！！！
adb pull /sdcard/record.mp4 D:\%date:~,4%%date:~5,2%%date:~8,2%%time:~0,2%%time:~3,2%%time:~6,2%.mp4
pause