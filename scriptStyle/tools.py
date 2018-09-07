from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import alert_is_present
from selenium.webdriver.support.select import Select

browser = webdriver.Chrome()
browser.get("https://techstepacademy.com/training-ground")
print("I have arrived")

btn_one = browser.find_element_by_id("b1")
btn_one.click()
WebDriverWait(browser, 10).until(alert_is_present())
print("An alert appeared")
alert_btn1 = browser.switch_to.alert
alert_btn1.accept()

sel = browser.find_element_by_id('sel1')
my_select = Select(sel)

my_select.select_by_visible_text("Battlestar Galactica")
my_select.select_by_index(0)
my_select.select_by_value("second")
print(my_select.first_selected_option.text)

browser.quit()
