"""
This scrapes data from a product inputted by the user into a csv file
"""
# imports
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import time
import pandas

# This is the eBay URL
LINK = "https://www.ebay.com/"

# This is the product you want to find on eBay
search_item = input("Enter an item to collect data on: ")

# This ensures the browser stays open until you close it
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# This opens chrome and enters the specified URL
driver.get(LINK)
# This stops the code for 5 seconds allowing all page elements to be loaded
time.sleep(5)

# This looks for the search bar element, clicks on it, types in your search input and searches eBay for it.
search_bar = driver.find_element(By.ID, "gh-ac")
search_bar.click()
search_bar.send_keys(search_item)
search_bar.send_keys(Keys.ENTER)
time.sleep(5)
# lst_of_result = driver.find_element(By.CSS_SELECTOR, "#srp-river-results > ul")
# This is a python list that contains all the results and their details
# res = lst_of_result.find_elements(By.CSS_SELECTOR, "li.s-item__pl-on-bottom")
# print(results)

# Loop through each result to get its details. This method requires longer line of code
# But I can make it shorter using list comprehension
# for result in results:
#     product_name = result.find_element(By.CSS_SELECTOR, "div.s-item__title > span")
#     product_price = result.find_element(By.CSS_SELECTOR, 'span.s-item__price')
#     product_shipping_fee = result.find_element(By.CSS_SELECTOR, 'span.s-item__shipping.s-item__logisticsCost')
#     product_image = result.find_element(By.TAG_NAME, "img").get_attribute('src')
# print(product_name.text)
# print(product_price.text)
# print(product_shipping_fee.text)
# print(product_image)

# LIST COMPREHENSION METHOD
# Storing the data in a csv file which is practically a spreadsheet

# product_dict = {
#     "Product Name": [result.find_element(By.CSS_SELECTOR, "div.s-item__title > span").text for result in res],
#     "Product Price": [result.find_element(By.CSS_SELECTOR, 'span.s-item__price').text for result in res],
#     "Image Link": [result.find_element(By.TAG_NAME, "img").get_attribute('src') for result in res]
# }

# product_data = pandas.DataFrame(product_dict)
# product_data.to_csv(f"{search_item} eBay data.csv", index=False)
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

# This closes the browser
# driver.quit()
