# coding = utf-8
"""
@All-project: Selenium
@author: ZWNONG
@file: 前程无忧.py
@time: 2020-08-03 20:26:58
"""
import os
import time

from selenium import webdriver

# 自动化爬取前程无忧 python工程师职位
from selenium.webdriver.support.wait import WebDriverWait

path_browser_driver = r'D:\Google\Chrome\Application\chromedriver.exe'
driver = webdriver.Chrome(executable_path=path_browser_driver)
driver.get("http://51job.com")
driver.implicitly_wait(10)
time.sleep(2)
WebDriverWait(driver, 3, 1).until(lambda x: x.find_element_by_xpath('//*[@id="kwdselectid"]')).send_keys("python")
# 选择城市方案：把已经在选中的城市点一遍
# 根据css表达式 查找选中的城市  表达式：em[class=on] 在div里面查找  div有id 用#表示id: #work_position_click_ip_location em[class=on]
driver.find_element_by_xpath('//*[@id="work_position_click"]/em').click()
# 在div中查找已经被选中的城市 css表达式：#work_position_click_ip_location em[class=on]
eles = driver.find_elements_by_css_selector('#work_position_click_ip_location em[class=on]')
# 逐个点击
for ele in eles:
    ele.click()
# 点击我们需要查找的城市
driver.find_element_by_id('work_position_click_center_right_list_category_000000_030200').click()
# 点击确定
driver.find_element_by_id('work_position_click_bottom_save').click()
# 点击搜索
driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/button').click()

# 查找所有的工作
jobs = driver.find_elements_by_css_selector('div[class=j_joblist]  div[class=e]')
for job in jobs:
    job_name = job.find_element_by_tag_name('span')
    print(job_name)
    # company_name = job.find_element_by_tag_name('div[class=er]').text
    # print(company_name)
    f = [f.text for f in job_name]
    print(' | '.join(f))





















