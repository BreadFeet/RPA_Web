from selenium import webdriver
import time

## 1. 구글 검색으로 w3schools 접속
driver = webdriver.Chrome()
driver.get('http://google.com')

# w3schools 검색
elmt = driver.find_element_by_name('q')
elmt.click()
elmt.send_keys('w3schools')
elmt.send_keys('\ue007')     # enter키 누름

# 첫번째 검색 결과 클릭 - 에러 많이 남
driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div/div[1]/a').click()

## 2. 화면 중간 LEARN HTML 클릭
driver.find_element_by_link_text('LEARN HTML').click()

## 3. 화면에서 HOW TO 클릭
driver.find_element_by_link_text('HOW TO').click()

## 4. 좌측 메뉴에서 Contact Form 클릭 - 시간 걸림!
# elmt = driver.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[116]')
# elmt = driver.find_element_by_link_text('Contact Form')
elmt = driver.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[text()="Contact Form"]')
elmt.click()

# 스크롤 해서 클릭하기
# from selenium.webdriver.common.action_chains import ActionChains
# ActionChains(driver).move_to_element(elmt).click().perform()

## 5. Form 작성
name = "카츄"
surname = "피"
country = "Canada"
sub = "퀴즈 완료하였습니다."

# 중간으로 스크롤 다운
driver.execute_script('window.scrollTo(0, 400)')

# 이름 넣기
elmt = driver.find_element_by_id('fname')
elmt.send_keys(name)

# 성 넣기
elmt = driver.find_element_by_id('lname')
elmt.send_keys(surname)

# 나라 옵션 지정하기
# driver.find_element_by_xpath('//*[@id="country"]/option[text()="Canada"]').click()  # 큰 따옴표 사용!
driver.find_element_by_xpath('//*[@id="country"]/option[text()="{}"]'.format(country)).click()

# 내용 작성
elmt = driver.find_element_by_xpath('//*[@id="main"]/div[3]/textarea')
elmt.send_keys(sub)

## 6. 5초 대기 후 submit 버튼 클릭
time.sleep(5)
driver.find_element_by_xpath('//*[@id="main"]/div[3]/a').click()

## 7. 5초 대기 후 브라우저 종료
time.sleep(5)
driver.quit()