```python
import os, sys, requests
from selenium import webdriver

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time


def translate(browser):
    wait = WebDriverWait(browser, 10)  # 等待加载10s

    url = 'https://translate.google.com.hk/?hl=en&tab=rT&sl=en&tl=zh-CN&op=translate'
    browser.get(url)

    input = wait.until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[1]/span/span/div/textarea')))
    time.sleep(3)
    input.send_keys('hello world')

    output = wait.until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[2]/div[5]/div/div[1]')))
    time.sleep(3)
    print(output)
    print(output.get_attribute("innerText"))
    

if 1:
    # Not work
    #chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_argument("--disable-popup-blocking")

    #browser = webdriver.Chrome(options=chrome_options)
    browser = webdriver.Chrome()

    browser.maximize_window()  # 最大化窗口
    wait = WebDriverWait(browser, 10)  # 等待加载10s

    # txtTemp, btnSubmit
    translate(browser)

# pass!
if 0:
    driver = webdriver.Chrome()
    driver.get("http://www.python.org")
    assert "Python" in driver.title
    elem = driver.find_element_by_name("q")
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)
    print (driver.page_source)

```