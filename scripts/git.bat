@echo off
echo github uploading...
d:
cd D:\Git\Python
git add -A
set a=%date:~0,4%%date:~5,2%%date:~8,2%%h%%time:~3,2%%time:~6,2%
git commit -a -m "updateSomethings%a%"
git push origin master
pause