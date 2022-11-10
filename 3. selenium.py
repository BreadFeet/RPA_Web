# chrome version 확인: 주소창에 chrome://version
# chromedriver 검색해서 window 버전 다운로드 후, 현재 작업 디렉토리로 옮김

from selenium import webdriver

# Chromedriver의 경우, 사용하는 chrome의 버전에 맞게 계속 다시 다운받아야 함!
# browser = webdriver.Chrome("chromedriver.exe")   # 브라우저를 핸들링 할 수 있게 함
browser = webdriver.Chrome('8.RPA_HTML/chromedriver.exe')     # 현재 작업 디렉토리에 드라이버가 있는 경우, 경로를 지정하지 않아도 알아서 찾음
# browser.get("http://naver.com")          # 해당 url로 이동


# elmt = browser.find_element_by_link_text("카페")   # '카페'텍스트의 링크를 찾음
# print(elmt)
# a = elmt.get_attribute("href")      # 링크 내 속성을 가져옴
# print(a)
# b = elmt.get_attribute("class")
# print(b)
# c = elmt.get_attribute("data-clk")
# print(c)
# elmt.click()
# browser.back()     # 뒤로 가기
# browser.forward()  # 앞으로 가기
# browser.refresh()


# 검색창 찾기
# elmt = browser.find_element_by_id("query")    # html id가 query임
# print(elmt)
# elmt.send_keys("인기검색어")     # 글자 입력

# # 키보드로 엔터 입력하기
# from selenium.webdriver.common.keys import Keys
# elmt.send_keys(Keys.ENTER)

# # html a 태그 가져오기
# elmt = browser.find_element_by_tag_name("a")    # 페이지의 첫번째 a 태그를 가져옴
# print(elmt)
# a = elmt.get_attribute("href")
# print(a)

# elmts = browser.find_elements_by_tag_name("div")   # 페이지의 모든 div 태그를 가져옴
# print(elmts)

# for e in elmts :
#     b = e.get_attribute("id")
#     print(b)


# name 정보로 element 가져오기
browser.get("http://daum.net") 
elmt = browser.find_element_by_name("q")    # name: 검색창 태그의 attribute 중 name

elmt.send_keys("나도코딩")
elmt.send_keys("나도코딩")   # 기존 글자 뒤에 추가 입력됨
elmt.clear()     # 글자 지움
elmt.send_keys("나도코딩")

# 검색 버튼 클릭 - Xpath 이용(따옴표 사용 주의)
elmt = browser.find_element_by_xpath('//*[@id="daumSearch"]/fieldset/div/div/button[2]')
elmt.click()

# 화면 스크린샷
browser.save_screenshot('scrshot.png')

# 페이지 소스코드
print(browser.page_source)

# 브라우저 종료
browser.close()      # 현재 탭만 종료
browser.quit()       # 전체 창 종료