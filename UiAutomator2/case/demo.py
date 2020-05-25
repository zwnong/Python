# coding utf-8
import uiautomator2 as u2

device = u2.connect('127.0.0.1:21503')
device_package_name = 'com.smile.gifmaker'

size = device.window_size()
str_size = str(size)

a = str_size.strip('()').split(',')

print(a[1])






