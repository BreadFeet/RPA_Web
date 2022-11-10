from selenium import webdriver
import time

driver = webdriver.Chrome('C:/Users/sori-/Desktop/DS_webscraping/chromedriver.exe')
driver.maximize_window()    # 창 최대화
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio")

driver.switch_to.frame("iframeResult")   # frame 전환
elmt = driver.find_element_by_xpath('//*[@id="male"]')   # male radio 버튼 찾기

# 선택여부 확인 후 선택하기
if elmt.is_selected() == False :    # 선택이 안되어 있는 경우
    print("선택이 안되어 있음 --> 선택하기")
    elmt.click()
else :    # 선택이 되어 있는 경우
    print("선택되어 있음 --> 아무것도 안함")

time.sleep(5)            # 화면에서 직접 female을 클릭하고 아래 확인함

if elmt.is_selected() == False :    # 선택이 안되어 있는 경우
    print("선택이 안되어 있음 --> 선택하기")
    elmt.click()
else :    # 선택이 되어 있는 경우
    print("선택되어 있음 --> 아무것도 안함")

driver.quit()
