#import 라이브러리&모듈
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys
import sys
import csv

url = "https://news.naver.com/main/ranking/popularMemo.naver"

driver = wd.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)

act = ActionChains(driver)
#JTBC분석
list_of_Publish = driver.find_elements(By.CSS_SELECTOR , "div.rankingnews_box")
for temp_list in list_of_Publish:
    신문사id = temp_list.find_element(By.TAG_NAME , "a").get_attribute('href')
    if("437" in 신문사id):
        print("JTBC를 분석중입니다.")
        JTBC = ["JTBC:"]
        rankingnewslist = temp_list.find_element(By.CSS_SELECTOR , "ul.rankingnews_list")
        news = rankingnewslist.find_elements(By.TAG_NAME , "li")
        for typicalnews in news:
            time.sleep(5)
            aTag = typicalnews.find_element(By.TAG_NAME , "a")
            href = aTag.get_attribute('href')
            driver.execute_script('window.open("https://google.com");')
            time.sleep(1)
            driver.switch_to.window(driver.window_handles[-1])
            driver.get(href)
            time.sleep(2)
            comments = driver.find_element(By.ID , "comment_count")
            num_comments = comments.text
            set = href + num_comments
            title = driver.find_element(By.ID , "title_area").text
            JTBC.append(title)
            JTBC.append(num_comments)
            driver.close()
            driver.switch_to.window(driver.window_handles[-1])
            time.sleep(1)
        time.sleep(2)
#중앙일보 분석
    elif("025" in 신문사id):
        print("중앙일보를 분석중입니다.")
        중앙일보 = ["중앙일보:"]
        rankingnewslist = temp_list.find_element(By.CSS_SELECTOR , "ul.rankingnews_list")
        news = rankingnewslist.find_elements(By.TAG_NAME , "li")
        for typicalnews in news:
            time.sleep(5)
            aTag = typicalnews.find_element(By.TAG_NAME , "a")
            href = aTag.get_attribute('href')
            driver.execute_script('window.open("https://google.com");')
            time.sleep(1)
            driver.switch_to.window(driver.window_handles[-1])
            driver.get(href)
            time.sleep(2)
            comments = driver.find_element(By.ID , "comment_count")
            num_comments = comments.text
            set = href + num_comments
            title = driver.find_element(By.ID , "title_area").text
            중앙일보.append(title)
            중앙일보.append(num_comments)
            driver.close()
            driver.switch_to.window(driver.window_handles[-1])
            time.sleep(1)
        time.sleep(2)
#조선일보 분석
    elif("023" in 신문사id):
        print("조선일보를 분석중입니다.")
        조선일보 = ["조선일보:"]
        rankingnewslist = temp_list.find_element(By.CSS_SELECTOR , "ul.rankingnews_list")
        news = rankingnewslist.find_elements(By.TAG_NAME , "li")
        for typicalnews in news:
            time.sleep(5)
            aTag = typicalnews.find_element(By.TAG_NAME , "a")
            href = aTag.get_attribute('href')
            driver.execute_script('window.open("https://google.com");')
            time.sleep(1)
            driver.switch_to.window(driver.window_handles[-1])
            driver.get(href)
            time.sleep(2)
            comments = driver.find_element(By.ID , "comment_count")
            num_comments = comments.text
            set = href + num_comments
            title = driver.find_element(By.ID , "title_area").text
            조선일보.append(title)
            조선일보.append(num_comments)
            driver.close()
            driver.switch_to.window(driver.window_handles[-1])
            time.sleep(1)
        time.sleep(2)
#동아일보 분석
    elif("020" in 신문사id):
        print("동아일보를 분석중입니다.")
        동아일보 = ["동아일보:"]
        rankingnewslist = temp_list.find_element(By.CSS_SELECTOR , "ul.rankingnews_list")
        news = rankingnewslist.find_elements(By.TAG_NAME , "li")
        for typicalnews in news:
            time.sleep(5)
            aTag = typicalnews.find_element(By.TAG_NAME , "a")
            href = aTag.get_attribute('href')
            driver.execute_script('window.open("https://google.com");')
            time.sleep(1)
            driver.switch_to.window(driver.window_handles[-1])
            driver.get(href)
            time.sleep(2)
            comments = driver.find_element(By.ID , "comment_count")
            num_comments = comments.text
            set = href + num_comments
            title = driver.find_element(By.ID , "title_area").text
            동아일보.append(title)
            동아일보.append(num_comments)
            driver.close()
            driver.switch_to.window(driver.window_handles[-1])
            time.sleep(1)
        time.sleep(2)
#한겨래 분석
    elif("028" in 신문사id):
        print("한겨래신문을 분석중입니다.")
        한겨래 = ["한겨래:"]
        rankingnewslist = temp_list.find_element(By.CSS_SELECTOR , "ul.rankingnews_list")
        news = rankingnewslist.find_elements(By.TAG_NAME , "li")
        for typicalnews in news:
            time.sleep(5)
            aTag = typicalnews.find_element(By.TAG_NAME , "a")
            href = aTag.get_attribute('href')
            driver.execute_script('window.open("https://google.com");')
            time.sleep(1)
            driver.switch_to.window(driver.window_handles[-1])
            driver.get(href)
            time.sleep(2)
            comments = driver.find_element(By.ID , "comment_count")
            num_comments = comments.text
            set = href + num_comments
            title = driver.find_element(By.ID , "title_area").text
            한겨래.append(title)
            한겨래.append(num_comments)
            driver.close()
            driver.switch_to.window(driver.window_handles[-1])
            time.sleep(1)
        time.sleep(2)
#kbs
    elif("056" in 신문사id):
        print("kbs를 분석중입니다.")
        kbs = ["kbs:"]
        rankingnewslist = temp_list.find_element(By.CSS_SELECTOR , "ul.rankingnews_list")
        news = rankingnewslist.find_elements(By.TAG_NAME , "li")
        for typicalnews in news:
            time.sleep(5)
            aTag = typicalnews.find_element(By.TAG_NAME , "a")
            href = aTag.get_attribute('href')
            driver.execute_script('window.open("https://google.com");')
            time.sleep(1)
            driver.switch_to.window(driver.window_handles[-1])
            driver.get(href)
            time.sleep(2)
            comments = driver.find_element(By.ID , "comment_count")
            num_comments = comments.text
            set = href + num_comments
            title = driver.find_element(By.ID , "title_area").text
            kbs.append(title)
            kbs.append(num_comments)
            driver.close()
            driver.switch_to.window(driver.window_handles[-1])
            time.sleep(1)
        time.sleep(2)
#sbs
    elif("055" in 신문사id):
        print("sbs를 분석중입니다.")
        sbs = ["sbs:"]
        rankingnewslist = temp_list.find_element(By.CSS_SELECTOR , "ul.rankingnews_list")
        news = rankingnewslist.find_elements(By.TAG_NAME , "li")
        for typicalnews in news:
            time.sleep(5)
            aTag = typicalnews.find_element(By.TAG_NAME , "a")
            href = aTag.get_attribute('href')
            driver.execute_script('window.open("https://google.com");')
            time.sleep(1)
            driver.switch_to.window(driver.window_handles[-1])
            driver.get(href)
            time.sleep(2)
            comments = driver.find_element(By.ID , "comment_count")
            num_comments = comments.text
            set = href + num_comments
            title = driver.find_element(By.ID , "title_area").text
            sbs.append(title)
            sbs.append(num_comments)
            driver.close()
            driver.switch_to.window(driver.window_handles[-1])
            time.sleep(1)
        time.sleep(2)
#매일경제
    elif("009" in 신문사id):
        print("매일경제를 분석중입니다.")
        매일경제 = ["매일경제:"]
        rankingnewslist = temp_list.find_element(By.CSS_SELECTOR , "ul.rankingnews_list")
        news = rankingnewslist.find_elements(By.TAG_NAME , "li")
        for typicalnews in news:
            time.sleep(5)
            aTag = typicalnews.find_element(By.TAG_NAME , "a")
            href = aTag.get_attribute('href')
            driver.execute_script('window.open("https://google.com");')
            time.sleep(1)
            driver.switch_to.window(driver.window_handles[-1])
            driver.get(href)
            time.sleep(2)
            comments = driver.find_element(By.ID , "comment_count")
            num_comments = comments.text
            set = href + num_comments
            title = driver.find_element(By.ID , "title_area").text
            매일경제.append(title)
            매일경제.append(num_comments)
            driver.close()
            driver.switch_to.window(driver.window_handles[-1])
            time.sleep(1)
        time.sleep(2)
#ytn
    elif("052" in 신문사id):
        print("ytn을 분석중입니다.")
        ytn = ["ytn:"]
        rankingnewslist = temp_list.find_element(By.CSS_SELECTOR , "ul.rankingnews_list")
        news = rankingnewslist.find_elements(By.TAG_NAME , "li")
        for typicalnews in news:
            time.sleep(5)
            aTag = typicalnews.find_element(By.TAG_NAME , "a")
            href = aTag.get_attribute('href')
            driver.execute_script('window.open("https://google.com");')
            time.sleep(1)
            driver.switch_to.window(driver.window_handles[-1])
            driver.get(href)
            time.sleep(2)
            comments = driver.find_element(By.ID , "comment_count")
            num_comments = comments.text
            set = href + num_comments
            title = driver.find_element(By.ID , "title_area").text
            ytn.append(title)
            ytn.append(num_comments)
            driver.close()
            driver.switch_to.window(driver.window_handles[-1])
            time.sleep(1)
        time.sleep(2)
    else:
        print("기타 뉴스는 분석하지 않습니다.")


print("JTBC:" , JTBC)
print("중앙일보:" , 중앙일보)
print("조선일보:" , 조선일보)
print("동아일보:" , 동아일보)
print("한겨래:" , 한겨래)
print("kbs:" , kbs)
print("sbs:" , sbs)
print("ytn:" , ytn)
print("매일경제:" , 매일경제)

final_set = []
final_set.append(JTBC)
final_set.append(중앙일보)
final_set.append(조선일보)
final_set.append(동아일보)
final_set.append(한겨래)
final_set.append(kbs)
final_set.append(sbs)
final_set.append(ytn)
final_set.append(매일경제)

f = open("C:/Users/Me/Desktop/KFCW2V/ranking_news/rank.csv" , 'w' , newline='')
data = final_set
writer = csv.writer(f)
writer.writerows(data)
f.close()