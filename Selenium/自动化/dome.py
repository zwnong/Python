# coding = utf-8
"""
@project: Selenium
@author: ZWNONG
@file: dome.py
@time: 2020-08-03 23:18:01
"""
from selenium import webdriver
path_browser_driver = r'D:\Google\Chrome\Application\chromedriver.exe'
driver = webdriver.Chrome(executable_path=path_browser_driver)
driver.get("https://jobs.51job.com/guangzhou/72712060.html?s=01&t=0")
driver.implicitly_wait(10)
