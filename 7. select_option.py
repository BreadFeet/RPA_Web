from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_select")

driver.switch_to.frame('iframeResult')

# 1. element로서 cars를 찾고 4번째 옵션인 Audi를 선택
# elmt = driver.find_element_by_xpath('//*[@id="cars"]/option[4]')
# elmt.click()

# 2. Audi라는 텍스트를 통해서 옵션 선택하기
# elmt = driver.find_element_by_xpath('//*[@id="cars"]/option[text()="Audi"]')
# elmt.click()

# 3. 텍스트 일부분(ud)으로 옵션 선택하기
elmt = driver.find_element_by_xpath('//*[@id="cars"]/option[contains(text(), "ud")]')
elmt.click()



time.sleep(5)
driver.close()