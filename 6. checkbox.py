from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_checkbox")

# driver.switch_to.frame("iframeResult")
# elmt = driver.find_element_by_xpath('//*[@id="vehicle1"]')

# # 선택여부 확인하고 클릭하기
# if elmt.is_selected() == False :    # 선택 안되어 있는 경우
#     print("선택 안됨 --> 선택하기")
#     elmt.click()
# else :
#     print("선택됨 --> 아무것도 하지 않음")

# time.sleep(5)

# if elmt.is_selected() == False :    # 선택 안되어 있는 경우
#     print("선택 안됨 --> 선택하기")
#     elmt.click()
# else :
#     print("선택됨 --> 아무것도 하지 않음")

# driver.close()


## Element 다르게 불러오는 방법
from selenium.webdriver.common.by import By

driver.switch_to.frame("iframeResult")
# elmt = driver.find_element(By.XPATH, '//*[@id="vehicle1"]')
elmt = driver.find_element(By.ID, 'vehicle1')
elmt.click()