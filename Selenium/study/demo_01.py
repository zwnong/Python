# coding = utf-8

from selenium import webdriver

# 存储浏览器驱动路劲

path_browser_driver = r'D:\Google\Chrome\Application\chromedriver.exe'
driver = webdriver.Chrome(executable_path=path_browser_driver)
url = 'http://www.sogou.com/'
driver.get(url)
