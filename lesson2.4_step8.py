from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"
browser.get(link)

button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
browser.find_element_by_tag_name('button').click()

def calc(x):
    return str(math.log(abs(12*math.sin(x))))

x_element = browser.find_element_by_id('input_value')
x = x_element.text

y = calc(int(x))

input01 = browser.find_element_by_id('answer')
input01.send_keys(y)

button2 = browser.find_element_by_id('solve')
button2.click()

time.sleep(10)


browser.quit()