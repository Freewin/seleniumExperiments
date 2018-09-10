from selenium import webdriver

from PageObjectModel.training_ground_page import TrainingGroundPage

browser = webdriver.Chrome()
test_value = "It worked"

trng_page = TrainingGroundPage(driver=browser)
trng_page.go()
assert trng_page.button1.text == "Button1"
trng_page.button1.click()
browser.quit()