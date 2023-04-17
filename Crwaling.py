#import 라이브러리&모듈
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time


#크롬 드라이버 설정
driver = wd.Chrome(service=Service(ChromeDriverManager().install()))
#드라이버에게 실행할 url입력
url = "https://n.news.naver.com/article/comment/055/0001050468"
driver.get(url)
#드라이버 액터 설정
act = ActionChains(driver)


#더보기 누르기
while(True):
    try:
        더보기 = driver.find_elements(By.CSS_SELECTOR , 'a.u_cbox_btn_more')
        act.click(더보기)
        
    except:
        print("더보기 완료")
        break



reviews = driver.find_elements(By.CSS_SELECTOR , 'span.u_cbox_contents')
reviews = [reviews.text for reviews in reviews]

up = driver.find_elements(By.CSS_SELECTOR,'em.u_cbox_cnt_recomm')
up = [up.text for up in up]

down = driver.find_elements(By.CSS_SELECTOR,'em.u_cbox_cnt_unrecomm')
down = [down.text for down in down]

reply = list(zip(reviews , up , down))
print(reply)

f = open("C:/Users/Me/Desktop/KFCW2V/comments_crwalling/crawlling.txt" , 'w')
for data in reply:
    list(data)
    for o in data:
        f.write("%s\n" %o)

f.close