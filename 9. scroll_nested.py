# 페이지 전체가 아닌, 페이지 안의 일부 영역을 스크롤 하는 경우
from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.get('https://www.w3schools.com/html/')
driver.maximize_window()

time.sleep(3)

# 특정 영역(HTML Tag List) 스크롤
elmt = driver.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[61]')

# 1. ActionChain - 간단한 동작들을 순서대로 저장하고 수행
# from selenium.webdriver.common.action_chains import ActionChains
# actions = ActionChains(driver)
# actions.move_to_element(elmt).perform()

# 2. 좌표 정보 얻는 메소드를 사용하면 스크롤이 되는 점을 이용하는 방법
# xy = elmt.location_once_scrolled_into_view    # () 안씀
# print('type:', type(xy))    # dict
# print('value:', xy)         # {'x': 0, 'y': 122}
elmt.click()


# time.sleep(5)
# driver.quit()