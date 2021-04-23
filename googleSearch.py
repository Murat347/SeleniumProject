from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import *

driver = webdriver.Chrome()
# or specify the path: driver = webdriver.Chrome('/path/to/chromedriver')


driver.get("https://google.com")

search_text_box = driver.find_element_by_name("q")
search_text_box.clear()
search_text_box.send_keys("python selenium integration") # typing in the search box
search_text_box.send_keys(Keys.RETURN) # hitting ENTER key
sleep(5)



search_text_box = driver.find_element_by_name("q")
search_text_box.clear() # delete everything in the search box
sleep(10)
driver.close()
print("completed!!!")

