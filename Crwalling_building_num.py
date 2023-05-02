#import 라이브러리&모듈
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys
import sys
from PyQt5.QtWidgets import *
import requests

class naverland(QMainWindow):
    #초기 설정
    def __init__(self):
        super().__init__()
        self.initUI()

 #UI설정
    def initUI(self):
        #제목 설정
        self.setWindowTitle("네이버 부동산 크롤링")
        #하단 바에 상태 표시
        self.statusBar().showMessage('Ready')
        #입력기 설정
        self.addQLineEdit()

        #버튼
        btn1 = QPushButton('시작', self)
        btn1.setCheckable(True)
        btn1.toggle()
        vbox = QVBoxLayout()
        vbox.addWidget(btn1)
        self.setLayout(vbox)

        #버튼 연결
        btn1.clicked.connect(self.functionStart)
        #ui보이기
        self.resize(500, 350)
        self.center()
        self.show()


    #텍스트 입력(여기서는 주소와 디렉토리)
    def addQLineEdit(self):
        QLabel('파일이 저장될 위치.:' , self)
        QLabel('네이버 부동산 url.:' , self)
        QLabel('입력 횟수 설정' , self)
        self.able_label = QLabel('' , self)
        #input directory
        self.dt_entry = QLineEdit(self)
        self.dt_entry.move(130,45)
        self.dt_entry.setPlaceholderText('파일이 저장될 위치')
        self.dt_entry.textChanged.connect(self.save_DT)
        #inputURL
        self.url = QLineEdit(self)
        self.url.move(130 , 75)
        self.url.setPlaceholderText('URL입력:')
        self.url.textChanged.connect(self.save_URL)
        #num
        self.num = QLineEdit(self)
        self.num.move(130,105)
        self.num.setPlaceholderText('더보기 횟수 입력.:')
        self.num.textChanged.connect(self.savenum)

    #횟수 저장
    def savenum(self):
        global realnum
        realnum = self.num.text()
    
    #디렉토리 저장
    def save_DT(self):
        #주소 전처리
        temp_list = []
        second_directory = ''
        for temp in self.dt_entry.text():
            if temp == '\\':
                temp = '/'
                temp_list.append(temp)
            else:
                temp_list.append(temp)
        #주소 저장
        global directory
        directory = second_directory.join(temp_list)
        directory = directory + "/crwalling_land.txt"
        print(directory)

    #인터넷 기사 주소 저장    
    def save_URL(self):
        global real_url
        real_url = self.url.text()
        print(real_url)

    #버튼에 연결된 코드
    #버튼에 연결된 코드
    def functionStart(self):
          #크롬 드라이버 설정
        driver = wd.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get(real_url)

        #드라이버 액터 설정
        act = ActionChains(driver)

        #더보기 누른 횟수
        count = 0
        #더보기 실행
        times = 1
        el = driver.find_element(By.CSS_SELECTOR , "span.text")
        time.sleep(2)
        el.click()
        ele = driver.find_element(By.TAG_NAME , "body")
        element = driver.find_elements(By.CSS_SELECTOR , "span.text")
        while(True):
            time.sleep(0.5)
            element = driver.find_elements(By.CSS_SELECTOR , "span.text")
            if(int(realnum) == 1):
                break
            elif(count == int(realnum) -1):
                break
            elif(count < int(realnum) -1):
                try:
                    if(count == 0):
                        act.move_to_element(element[19]).perform()
                        ele.send_keys(Keys.PAGE_DOWN)
                        count += 1
                        times += 1
                        time.sleep(1.5)
                    else:
                        act.move_to_element(element[19 * times + (times - 1)]).perform()
                        ele.send_keys(Keys.PAGE_DOWN)
                        count += 1
                        times += 1
                        time.sleep(1.5)
                except:
                    break
        print("총 %d번의 더보기를 수행했습니다." %(count+1))
        
        #파일 작성
        name = driver.find_elements(By.CSS_SELECTOR , 'span.text')
        name = [name.text for name in name]

        price = driver.find_elements(By.CSS_SELECTOR , 'div.price_line')
        price = [price.text for price in price]

        info = driver.find_elements(By.CSS_SELECTOR , 'span.spec')
        info = [info.text for info in info]

        cp_titel = driver.find_elements(By.CSS_SELECTOR , 'em.title')
        cp_titel = [cp_titel.text for cp_titel in cp_titel]

        cp_data = driver.find_elements(By.CSS_SELECTOR , 'em.data')
        cp_data = [cp_data.text for cp_data in cp_data]

        result = list(zip(name, price , info))

        f = open(directory , 'w' , encoding= 'utf-8')
        for data in result:
            list(data)
            for i in data:
                f.write("%s\n" %i)
        f.close
        print("파일 작성을 완료했습니다.")
    
    #프로그램을 화면 중앙에 정렬
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    #프로그램 종료
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = naverland()
    sys.exit(app.exec_())
