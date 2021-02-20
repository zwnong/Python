@echo off
adb shell dumpsys window | findstr mCurrentFocus
pause