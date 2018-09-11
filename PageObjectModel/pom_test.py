from selenium import webdriver

from PageObjectModel.training_ground_page import TrainingGroundPage
from PageObjectModel.trial_page import TrialPage

# Test_Setup
browser = webdriver.Chrome()
test_value = "It worked"

# Trial Page
trial_page = TrialPage(driver=browser)
trial_page.go()
trial_page.stone_input.input_text("rock")
trial_page.stone_button.click()

# Training Page
trng_page = TrainingGroundPage(driver=browser)
trng_page.go()
assert trng_page.button1.text == "Button1"
trng_page.button1.click()
browser.quit()