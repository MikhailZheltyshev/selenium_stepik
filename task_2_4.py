import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)

WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '10000 RUR')
    )

browser.find_element_by_id("book").click()
browser.find_element_by_id('answer').send_keys(calc(browser.find_element_by_id('input_value').text))
browser.find_element_by_id('solve').click()

browser.quit()