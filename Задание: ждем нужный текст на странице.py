import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
browser = webdriver.Chrome()
try:
    browser.get('http://suninjuly.github.io/explicit_wait2.html')
    WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    browser.find_element_by_id('book').click()
    browser.find_element_by_id('answer').send_keys(str(math.log(abs(12 * math.sin(int(browser.find_element_by_id('input_value').text))))))
    browser.find_element_by_id('solve').click()
    print(browser.switch_to.alert.text.split(':')[-1])
finally:
    time.sleep(5)
    browser.quit()
    
