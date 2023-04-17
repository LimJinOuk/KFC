#import 라이브러리&모듈
from bs4 import BeautifulSoup as bs
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys


#크롬 드라이버 설정
driver = wd.Chrome(service=Service(ChromeDriverManager().install()))
#드라이버에게 실행할 url입력
url = "url을 입력."
driver.get(url)
#드라이버 액터 설정
act = ActionChains(driver)
#더보기 누른 횟수
count = 0


#더보기 누르고 그 횟수를 저장하기. 만약 더보기가 끝났다면 몇번의 더보기 수행을 통해 끝났는지 출력하기.
while(True):
    try:
        count += 1
        time.sleep(3)
        element = driver.find_element(By.CSS_SELECTOR , 'a.u_cbox_btn_more')
        element.send_keys('\n')
    except:
        print("더보기 완료 총 %d회의 더보기를 수행했습니다." %count)
        break


#reviews 변수에 댓글을 저장
reviews = driver.find_elements(By.CSS_SELECTOR , 'span.u_cbox_contents')
reviews = [reviews.text for reviews in reviews]

#up변수에 공감수를 저장
up = driver.find_elements(By.CSS_SELECTOR,'em.u_cbox_cnt_recomm')
up = [up.text for up in up]

#down변수에 비공감 수를 저장
down = driver.find_elements(By.CSS_SELECTOR,'em.u_cbox_cnt_unrecomm')
down = [down.text for down in down]

#댓글, 공감 수, 비공감 수를 합침.
reply = list(zip(reviews , up , down))

#reply를 txt파일로 작성하는 과정.
f = open("C:/Users/Me/Desktop/KFCW2V/comments_crwalling/crawlling.txt" , 'w' , encoding = 'utf-8')
for data in reply:
    list(data)
    for o in data:
        f.write("%s\n" %o)

f.close
