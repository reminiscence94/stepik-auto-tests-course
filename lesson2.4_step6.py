from selenium import webdriver
import time

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/cats.html"
browser.get(link)

browser.implicitly_wait(0.5)

browser.find_element_by_id("button")

browser.quit()

