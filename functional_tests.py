from selenium import webdriver

options = webdriver.ChromeOptions()
browser = webdriver.Chrome('yandexdriver.exe', options=options)
browser.get('http://localhost:8000')

assert 'Django' in browser.title

# browser.quit()