# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 14:56:15 2018
抽取前50条书评并计算评分平均值
@author: JinXin
"""

import requests,re,time
from bs4 import BeautifulSoup

count = 0
i = 0
sum,count_s = 0,0

while(count<50):
    try:
        r=requests.get("https://book.douban.com/subject/19952400/comments/hot?p="+str(i+1))
    except Exception as err:
        print(err)
        break
    soup = BeautifulSoup(r.text,'lxml') #解析内容
    comments = soup.find_all('p','comment-content') #获取指定标签和属性的内容
    for item in comments:
        count+=1
        print(count,item.string)
        
        if(count==50):
            break
    
    #指定内容匹配正则表达式
    pattern = re.compile('<span class="user-stars allstar(.*?) rating"')
    p=re.findall(pattern,r.text) #使用模式匹配筛选内容(评分)
    for star in p:
        count_s += 1 #有评分的评论数量
        sum += int(star) #累加总评分
    time.sleep(5) #delay request from douban's robots.txt
    
    i+=1
if count==50:
    print(sum/count_s)
    
print(count,sum,count_s)