adb shell uiautomator dump /sdcard/sc.uix
adb pull /sdcard/sc.uix C:\Users\Administrator\Desktop\scripts\uix\sc.uix
adb shell screencap -p /sdcard/sc.png
adb pull /sdcard/sc.png  C:\Users\Administrator\Desktop\scripts\png\sc.png