from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import time
import pandas

LINK = "https://www.ebay.com/"

search_item = input("Enter an item to collect data on: ")
driver = webdriver.Chrome()
driver.get(LINK)
time.sleep(5)

search_bar = driver.find_element(By.ID, "gh-ac")
search_bar.click()
search_bar.send_keys(search_item)
search_bar.send_keys(Keys.ENTER)
time.sleep(5)

old_dict = {}


def tryagain():
    global old_dict

    try:
        next_page = driver.find_element(By.CLASS_NAME, 'pagination__next')
        next_page.send_keys(Keys.ENTER)
    except TimeoutException:
        driver.quit()
    else:
        list_of_result = driver.find_element(By.CSS_SELECTOR, "#srp-river-results > ul")
        results = list_of_result.find_elements(By.CSS_SELECTOR, "li.s-item__pl-on-bottom")
        products_dict = {
            "Product Name": [result.find_element(By.CSS_SELECTOR, "div.s-item__title > span").text for result in
                             results],
            "Product Price": [result.find_element(By.CSS_SELECTOR, 'span.s-item__price').text for result in results],
            "Image Link": [result.find_element(By.TAG_NAME, "img").get_attribute('src') for result in results]
        }
        if old_dict == products_dict:
            driver.quit()
        else:
            df = pandas.DataFrame(products_dict)
            df.to_csv(f'{search_item} eBay data.csv', mode='a', index=False, header=False)
            old_dict = products_dict
            print(old_dict)
            tryagain()


tryagain()
