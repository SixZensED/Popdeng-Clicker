from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://popdeng.click/')
element = driver.find_element(By.TAG_NAME, 'body')
actions = ActionChains(driver)

def auto_clicker(clicks_per_second, duration):
    start_time = time.time()
    clicks = 0
    max_clicks = clicks_per_second * duration
    while clicks < max_clicks and time.time() - start_time < duration:
        actions.move_to_element(element)
        for _ in range(10000):
            actions.click()
        actions.perform()
        clicks += 10000

auto_clicker(clicks_per_second=300, duration=9e9)
driver.quit()
