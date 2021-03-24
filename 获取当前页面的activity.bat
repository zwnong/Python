@echo off
adb shell dumpsys window |findstr mCurrent
pause