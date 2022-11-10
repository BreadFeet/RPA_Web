# handle: 열려있는 여러 브라우저를 관리하는 것

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.minimize_window()

# 첫번째 웹사이트 불러오기 - 첫번째 handle
driver.get('https://www.w3schools.com/tags/att_input_type_radio.asp')
cur_handle = driver.current_window_handle
print(cur_handle)     # 실행 때마다 값 계속 변한다!

# 'Try it Yourself' 버튼 클릭
driver.find_element_by_xpath('//*[@id="main"]/div[2]/a').click()

# 모든 handle 정보
handles = driver.window_handles
for handle in handles :
    print(handle)
    time.sleep(3)
    driver.switch_to.window(handle)    # 각 handle로 이동
    print(driver.title)    # 각 handle의 브라우저 제목 표기
    print()     # 한 줄 띄움

# 이동한 브라우저에서 종료
# driver.close()

# 이전 핸들로 돌아와서 창 끄기
driver.switch_to.window(cur_handle)
driver.get('http://naver.com')    # 브라우저 컨트롤 확인

time.sleep(5)
driver.quit()

