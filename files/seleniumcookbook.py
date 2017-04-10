from selenium import webdriver
browser = webdriver.Chrome(executable_path="C:\\Users\\Steve\\Desktop\\temp\\chromedriver\\chromedriver.exe")
browser.get('https://automatetheboringstuff.com')
elem = browser.find_element_by_css_selector('body > div.main > div:nth-child(1) > div:nth-child(3) > a')
print(elem.text)
elem.click()