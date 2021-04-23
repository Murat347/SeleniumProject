# 04/15/2021
# Finding elements
# by name,
#  by id (fastest if the element ID is unique)
# by class name,
# by link text, by partical link text

# by xpath (customizable, flexible, element hierarchy can be used better),
# by css selector (customizable, flexible),

# Functions from selenium
# flind_element_by_id(id)

# start the browser
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from utilities import *

driver = webdriver.Chrome()
# implicit wait is defined once you start the browser and this will apply all find element steps
driver.implicitly_wait(5)
driver.maximize_window()

def open_website(url):
    time.sleep(3)
    """open the website and click "No, thanks!" button"""
    try:
        driver.get(url)
        print(f"Title of the page 1: {driver.title}")
        # time.sleep(10) # one way of holding the execution and to wait for something
        print("now clicking the 'No, thanks!' button..")
        driver.find_element_by_link_text('No, thanks!').click()
    except NoSuchElementException as err:
        print(f"pop did not appear this time .\n {err}")


def back_forward():
    img1 = f'./../screenshots/{get_str_seconds()}_datapage.png'
    img2 = f'./../screenshots/{get_str_seconds()}_seleniumdemo.png'

    driver.back()
    time.sleep(5)
    print(f"Title of the page 2: {driver.title}")

    driver.forward()
    print(f"Title of the page 3: {driver.title}")
    driver.get_screen





def get_total_input_fields():
    # find the "Enter message" imput box
    # enter the "20" text in a
    # enter the "30" text in b
    # find the "Enter a" input box
    # find the "Enter b" input box
    driver.find_element_by_id('sum1').send_keys("20")
    avalue_input = driver.find_element_by_id('sum1')
    bvalue_input = driver.find_element_by_id('sum2')
    bvalue_input.send_keys("30")
    # find the "Get total" button, then click on that button
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sum_button = driver.find_element_by_xpath("//button[text()='Get total']")
    #driver.execute_script("arguments[0].scrollIntoView();", sum_button)
    #sum_button = driver.find_element_by_class_name("btn btn-default")
    sum_button.click()
    driver.get_screenshot_as_file(f'screenshots/{get_str_seconds()}_result.png')
    #time.sleep(5)
    driver.close()
    driver.quit()

def close_browser():
    driver.close()
    driver.quit()

def checkbpx_test():
    # todo: code here
    pass
    # fine the element to check and click
    # find the message elements and get text
    # verify the checkbox is checked

print("Execution strarting...")
# Scenario 1: variables
url_inputs = "https://www.seleniumeasy.com/test/basic-first-form-demo.html"
open_website(url_inputs)
back_forward()
get_total_input_fields()
close_browser()

# Scenario 2:
url_checkbox = "https://www.seleniumeasy.com/test/basic-first-form-demo.html"
open_website(url_checkbox)
close_browser()

print("Steps are completed")


# Scenario 3; working with multiple elements, ecomerse webstite
# go to this website: http://automationpractice.com/index.php
# find the element by id 'search_query_top'
# search for address (hit enter or click on search button)
# get the list of products and get the text out of each product
#   use find elements to find products listed, this returns a list of 'products'
#   loop through this list and use element.txt
# check the count of products
#   we have a list of elements, len(products)
# click on the last product
#   products[-1]
