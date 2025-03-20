from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
from konlpy.tag import Okt
from PIL import Image
import numpy as np
import sys

#사용자 정의 가능한 정보 입력
least_num = int(input("워드 클라우드 단어 최소 빈도를 정수로 입력하시오.:"))
directory = input("데이터의 주소를 입력해 주세요.(파일단위입니다.):")
temp_save_dirc = input("완성된 워드클라우드가 저장될 주소를 입력해 주세요.:")

#파일 주소 처리
empty_list = []
empty_str = ""
for i in directory:
    if(i == "\\"):
        i = '/'
        empty_list.append(i)
    else:
        empty_list.append(i)
real_dirc = empty_str.join(empty_list)


#저장 주소 처리
save_empty_list = []
save_empty_str = ""
for i in temp_save_dirc:
    if(i == "\\"):
        i = '/'
        save_empty_list.append(i)
    else:
        save_empty_list.append(i)
real_save_dirc = save_empty_str.join(save_empty_list)
real_save_dirc = real_save_dirc + "/Word_cloud.png"

#matplotlib 대화형 모드 켜기
plt.ion()

#워드클라우드의 기본 데이터 위치 설정
with open(real_dirc, 'r', encoding='utf-8') as f:
    text = f.read()
# OKT 사전 설정
okt = Okt()

#명사만 추출
nouns = okt.nouns(text)

# 단어의 길이가 1개인 것은 제외
words = [n for n in nouns if len(n) > 1]

# 위에서 얻은 words를 처리하여 단어별 빈도수 형태의 딕셔너리 데이터를 구함
c = Counter(words)

#각 단어의 빈도수 확인
print(c)

#최소 빈도수 처리
key = list(c.keys())
for a in key:
    if(c[a] < least_num):
        del c[a]

#빈도수가 맞지 않을 시 프로그램을 종료
if(len(c) == 0):
    print("최소 빈도수가 너무 큽니다. 다시 설정해 주세요.")
    print("프로그램을 종료합니다.")
    sys.exit()

#워드클라우드 만들기
wc = WordCloud(background_color="white" ,  font_path=r"C:/Windows/Fonts/malgun.ttf", width=600, height=600, scale=2.0, max_font_size=250)
gen = wc.generate_from_frequencies(c)
plt.figure()
plt.imshow(gen)

#파일로 저장 
wc.to_file(real_save_dirc)