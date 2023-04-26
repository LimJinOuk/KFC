#import 라이브러리&모듈
from bs4 import BeautifulSoup as bs
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QBasicTimer

#Interface만들기
class Myapp(QMainWindow):
    #초기 설정
    def __init__(self):
        super().__init__()
        self.initUI()


    #UI설정
    def initUI(self):
        #제목 설정
        self.setWindowTitle("네이버 기사 크롤링")
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
        QLabel('기사 url.:' , self)
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
        directory = directory + "/crwalling.txt"

    #인터넷 기사 주소 저장    
    def save_URL(self):
        global real_url
        real_url = self.url.text()
        print(real_url)
    
    #버튼에 연결된 코드
    def functionStart(self):
        #크롬 드라이버 설정
        driver = wd.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get(real_url)

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
        f = open(directory , 'w' , encoding = 'utf-8')
        for data in reply:
            list(data)
            for o in data:
                f.write("%s\n" %o)
        f.close

    #프로그램을 화면 중앙에 정렬
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

#프로그램 종료
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Myapp()
    sys.exit(app.exec_())
