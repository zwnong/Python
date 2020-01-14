@echo off
color 0a
echo root
adb reboot bootloader
timeout 15
fastboot oem root
fastboot reboot
pause