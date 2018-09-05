from selenium import webdriver
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome()
browser.get("https://google.com")

search_field = browser.find_element_by_css_selector("input[name='q']")
search_field.send_keys("selenium browser automation")
#I need to get out of the search bar but don't want to press enter.
search_field.send_keys(Keys.TAB)

search_btn = browser.find_element_by_css_selector("input[name='btnK']")
search_btn.click()
