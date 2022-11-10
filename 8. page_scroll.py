# 동적 페이지: 스크롤 다운할 수록 계속 페이지가 로딩되는 것
# 처음에 뜨는 html 코드에는 마지막 상품 정보는 없을 수 있음

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://shopping.naver.com/')

# 검색창에 무선마우스 입력
elmt = driver.find_element_by_name('query')
elmt.send_keys('무선마우스')
time.sleep(3)

# 검색 클릭
elmt = driver.find_element_by_xpath('//*[@id="autocompleteWrapper"]/a[2]')
elmt.click()

## 스크롤
# 1. 지정한 위치로 스크롤 내리기
driver.execute_script('window.scrollTo(0, 1080)')    # 자바스크립트 실행; 모니터 해상도 기준 제일 아래까지 내림
time.sleep(2)
driver.execute_script('window.scrollTo(0, 2160)')   

# 2. 화면 가장 아래로 스크롤 내리기(End)
# driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')

# 3. 페이지가 바뀌지 않을 때까지 계속 내리기
# interval = 2     # 2초마다 스크롤 내리기
# # 현재 문서의 높이를 가져오기
# prev_height = driver.execute_script('return document.body.scrollHeight')

# while True :     # 무한 반복
#     # 가장 아래로 스크롤 내리기
#     driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
#     time.sleep(interval)     # 페이지 대기
    
#     # 바뀐 문서 높이 불러오기
#     cur_height = driver.execute_script('return document.body.scrollHeight')

#     if cur_height == prev_height :
#         break     # 스크롤 다운해도 늘어난 페이지가 없는 경우, 반복문 탈출
    
#     prev_height = cur_height

# # 4. 페이지 맨 위로 올리기(Home)
# driver.execute_script('window.scrollTo(0,0)')


time.sleep(5)
driver.quit()
