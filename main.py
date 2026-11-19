from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


product = input("Enter product link = ")

options = Options()
options.add_argument("--headless=new")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36")

driver = webdriver.Chrome(options=options)

try:
    driver.get(product)
    time.sleep(3)
    titles = driver.find_element(By.CLASS_NAME, "pdp-mod-product-badge-title")
    prices = driver.find_element(By.CLASS_NAME,  "pdp-product-price")

    print(f" NAME = {titles.text} ")
    print(f"PRICE = {prices.text} ")

finally:
    driver.quit()



