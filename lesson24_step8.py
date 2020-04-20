from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    element =WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"),"$100"))
    button = browser.find_element_by_id("book")
    button.click()

    btn = browser.find_element_by_id("solve")
    browser.execute_script("return arguments[0].scrollIntoView({block: 'center'});", btn)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    inputY = browser.find_element_by_id("answer")
    inputY.send_keys(y)

    btn.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
