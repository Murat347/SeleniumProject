from source.finding_elements import *

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


##########
from source.finding_elements import *

print("Execution starting ...")
# Scenario 1:
url_inputs = "https://www.seleniumeasy.com/test/basic-first-form-demo.html"

open_website(url_inputs)
back_forward()
get_total_input_fields()
# close_browser()


# Scenario 2:
url_checkbox = "https://www.seleniumeasy.com/test/basic-checkbox-demo.html"

open_website(url_checkbox)
# create steps to test checkbox using selenium
checkbox_test()
close_browser()

print("Steps are completed!")