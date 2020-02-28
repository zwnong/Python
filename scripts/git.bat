@echo off
echo github uploading...
d:
cd Git\Learnning-Python
git add -A
git commit -a -m "updateSomethings"
git push origin appium
pause