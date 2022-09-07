import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)

button = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

if button == True:

    btn = browser.find_element(By.ID, "book")
    btn.click()

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

x = browser.find_element(By.ID, "input_value").text

y = calc(x)

inputField = browser.find_element(By.ID, "answer")
inputField.send_keys(y)


submitButton = browser.find_element(By.ID, "solve")
submitButton.click()

time.sleep(10)
browser.quit()