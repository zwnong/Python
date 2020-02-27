echo.
@echo off
adb root 


@echo off
set/p save_path=ÇëÊäÈëmodem dump±£´æÂ·¾¶: 

ping 127.0.0.1 -n 2 >nul

echo.
@echo off
adb pull /data/vendor/tombstones/SDX55M  %save_path%

