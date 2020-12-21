from selenium import webdriver

browser = webdriver.Firefox(executable_path='C:\\Users\\dsmidoda\\Downloads\\geckodriver-v0.28.0-win64\\geckodriver.exe')
browser.get('http://localhost:8000')

assert 'Django' in browser.title
