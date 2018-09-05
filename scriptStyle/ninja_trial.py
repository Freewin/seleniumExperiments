from selenium import webdriver
import time


browser = webdriver.Chrome()
browser.get("https://techstepacademy.com/trial-of-the-stones")


# selectors
riddle_of_stone_answer = "rock"
riddle_stone_xpath_input_box = "//input[@name='r1Input']"
riddle_stone_xpath_button = "//button[@name='r1Btn']"
riddle_stone_xpath_secret_text = "//div[@id='passwordBanner']/h4"
riddle_secrets_xpath_input_box = "//input[@name='r2Input']"
riddle_secrets_xpath_button = "//button[@name='r2Butn']"
total_wealth_jessica_xpath = "//b[text()='Jessica']/../../p"
total_wealth_bernard_xpath = "//b[text()='Bernard']/../../p"
richest_merchant_xpath_input_box = "//input[@name='r3Input']"
richest_merchant_answer_box = "//button[@name='r3Butn']"
check_answer_xpath_button = "//button[@name='checkButn']"
trial_status_xpath_text = "//div[@id='trialCompleteBanner']/h4"


# Answer stone sequence
stone_input_box = browser.find_element_by_xpath(riddle_stone_xpath_input_box)
stone_input_box.send_keys(riddle_of_stone_answer)
stone_answer_btn = browser.find_element_by_xpath(riddle_stone_xpath_button)
stone_answer_btn.click()


# Get Answer from Stone sequence
secret_text = browser.find_element_by_xpath(riddle_stone_xpath_secret_text)


# Answer secrets sequence
secrets_input_box = browser.find_element_by_xpath(riddle_secrets_xpath_input_box)
secrets_input_box.send_keys(secret_text.text)
secrets_button = browser.find_element_by_xpath(riddle_secrets_xpath_button)
secrets_button.click()


# Get Merchant Wealth
jessica_total = browser.find_element_by_xpath(total_wealth_jessica_xpath).text
bernard_total = browser.find_element_by_xpath(total_wealth_bernard_xpath).text
richer_merchant = ""

if int(jessica_total) > int(bernard_total):
    richer_merchant = "Jessica"
else:
     richer_merchant = "Bernard"

merchant_input = browser.find_element_by_xpath(richest_merchant_xpath_input_box)
merchant_input.send_keys(richer_merchant)
merchant_btn = browser.find_element_by_xpath(richest_merchant_answer_box)
merchant_btn.click()


# Push Check Answer
btn_check_answer = browser.find_element_by_xpath(check_answer_xpath_button)
btn_check_answer.click()


# Get Trial Status
trial_status = browser.find_element_by_xpath(trial_status_xpath_text)
assert trial_status.text == "Trial Complete"

time.sleep(1)
browser.quit()
