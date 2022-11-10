from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('https://flight.naver.com/flights/')
driver.maximize_window()

## 3월 27일 시드니-인천 항공권 찾기

# 편도 클릭
driver.find_element_by_link_text('편도').click()

# 출발지 클릭 - 시드니 설정
driver.find_element_by_xpath('//*[@id="l_1"]/div/div[1]/a[2]').click()
elmt = driver.find_element_by_xpath('//*[@id="l_1"]/div/div[1]/div[1]/input')
elmt.send_keys('syd')
time.sleep(3)
elmt.send_keys(Keys.ARROW_DOWN)
elmt.send_keys(Keys.ENTER)

# 도착지 클릭 - 인천 설정
driver.find_element_by_xpath('//*[@id="l_1"]/div/div[2]/a[2]').click()
elmt = driver.find_element_by_xpath('//*[@id="l_1"]/div/div[2]/div[1]/input')
elmt.send_keys('icn')
time.sleep(3)
elmt.send_keys(Keys.ARROW_DOWN)
elmt.send_keys(Keys.ENTER)

# 가는날 클릭 - 3월 27일
driver.find_element_by_link_text('가는날 선택').click()
# 다음 달로 달력 넘김
driver.find_element_by_link_text('다음달').click()
# 2/27, 3/27 두개 중 두번째 것 클릭
driver.find_elements_by_link_text('27')[1].click()

# 항공권 선택 클릭
driver.find_element_by_link_text('항공권 검색').click()

# # 첫번째 결과 출력
# elmt = driver.find_element_by_xpath('//*[@id="content"]/div[3]/div[1]/div[7]/ul/li[1]')
# print(elmt.text)    # text 부분만 출력 
# # 결과) 로딩 기다리지 않으면 출력이 안됨. 화면이 로딩중이라 element가 없다고 인식됨 


## 화면 로딩 기다리기
# 1. 
# time.sleep(10)

# 2.
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
    
try :
    elmt = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[3]/div[1]/div[7]/ul/li[1]')))
    print(elmt.text)      # xpath로 찾은 값이 element가 됨
except :
    print("Element를 찾는데 실패하였습니다.")


time.sleep(5)
driver.quit()

