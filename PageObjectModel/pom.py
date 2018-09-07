from selenium import webdriver

class TrainingGroundPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://techstepacademy.com/training-ground'

    def go(self):
        self.driver.get(self.url)

    def type_into_input_field(self, text):
        text_input = self.driver.find_element_by_id('ipt1')
        text_input.clear()
        text_input.send_keys(text)
        return None

    def get_intput_text(self):
        text_input = self.driver.find_element_by_id('ipt1')
        elem_text = text_input.get_attribute('value')
        return elem_text

    def click_button_1(self):
        button = self.driver.find_element_by_id('b1')
        button.click()
        return None


# Test Setup
test_value = 'it worked'
browser = webdriver.Chrome()

# Test
training_page = TrainingGroundPage(driver=browser)
training_page.go()
training_page.type_into_input_field(test_value)
txt_from_input = training_page.get_intput_text()
assert txt_from_input == test_value, f"Test Failed: Input did not match expected ({test_value})."
print("Test passed")
training_page.click_button_1()
browser.quit()
