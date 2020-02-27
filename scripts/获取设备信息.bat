@echo off
echo=>1.txt

@echo 查看固件版本号inside.id
@echo off
adb shell getprop ro.build.inside.id

echo.
@echo 查看固件版本号mask.id（固件后缀有三种类型stable、daily和_I）
@echo off 
adb shell getprop ro.build.mask.id 


echo.
@echo 机器编码
@echo off 
adb shell getprop ro.meizu.hardware.version

echo.
@echo 查看安全补丁日期
@echo off 
adb shell getprop ro.build.version.security_patch

echo.
@echo 查看手机型号
@echo off 
adb shell getprop ro.meizu.product.model

echo.
@echo 查看kernel内核版本号
@echo off 
adb shell cat /proc/version

echo.
@echo 查看flyme版本号
@echo off 
adb shell getprop ro.build.display.id


echo.
@echo 查看手机序列号（SN）
@echo off 
adb shell getprop ro.serialno

echo.
@echo 查看手机IMEI号
@echo off 
adb shell getprop ril.gsm.imei

echo.
@echo 查看手机MEID号
@echo off 
adb shell getprop ril.cdma.meid

echo.
@echo 查看GSM基带版本
@echo off 
adb shell getprop gsm.version.baseband

echo.
@echo 查看手机版本，联通还是移动
@echo off 
adb shell cat /proc/lk_info/sw_version

echo.
@echo 查看手机是否加密
@echo off 
adb shell cat proc/lk_info/sec


@echo off
获取设备信息/all>1.txt
pause