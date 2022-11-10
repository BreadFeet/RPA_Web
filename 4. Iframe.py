# iframe : html 코드에서 하나의 완성된 <html></html>를 갖는 틀
# xpath를 구할 때 /html/body/iframe/...으로 찾을 수 없어서 다른 방법을 써야 한다

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio")

driver.switch_to.frame("iframeResult")       # frame id를 이용해서 전환
elmt = driver.find_element_by_xpath('//*[@id="male"]')    # 성공
elmt.click()

driver.switch_to.default_content()      # 상위로 빠져나옴
# elmt = driver.find_element_by_xpath('//*[@id="male"]')    # 실패
# elmt.click()

time.sleep(5)           # 5초 대기
driver.quit()