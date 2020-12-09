#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 18 11:33:14 2020

@author: gavin
"""

import time
import requests
from selenium import webdriver
keywords=["female",'women',"sexism"]
weburl="https://www.wsj.com/search?query={word}&page={page}"
executable_path='/Users/gavin/opt/anaconda3/chromedriver'
options=webdriver.ChromeOptions()
options.add_argument('--headless') #headless mode// 無頭模式_規避chrome bug#
driver=webdriver.Chrome(options=options,executable_path=executable_path)
for word in keywords:
    file=open(f"wsj_{word}",'w',encoding="utf-8") #創建抓取結果文件
    page=1
    while True:
        url=weburl.format(word=keywords, page=page)
        driver.get(url)
        time.sleep(5)
        #XML Path Language#
        line=driver.find_elements_by_xpath("//article//h3/a")
        if len(line)==0:
            break
        print(f"keyword:{word} page:{page}")
        for e in line:
            headline=e.text
            file.write(headline+"\n")
            file.flush()
        page+=1
driver.quit()