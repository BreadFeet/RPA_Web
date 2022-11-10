from selenium import webdriver
import time

# 원하는 폴더에 다운로드 하기
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option('prefs', {'download.default_directory':r'C:\Users\sori-\Desktop\PythonWorkSpace\8. RPA_HTML'})
# r: \가 탈출문자로 인식되지 않도록 함
# 폴더 명이 기존에 없는 폴더이면 새로 생성하여 저장

driver = webdriver.Chrome(options=chrome_options)     # 옵션 적용
driver.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_a_download')
driver.switch_to.frame('iframeResult')

# 다운로드 할 링크 클릭
elmt = driver.find_element_by_xpath('/html/body/p[2]/a')
elmt.click()


time.sleep(5)
driver.quit()
