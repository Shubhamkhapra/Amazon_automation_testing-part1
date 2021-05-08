from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')
driver.maximize_window()
driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
# assert 'Selenium Easy Demo ' in driver.title

button = driver.find_element_by_class_name('btn-default')
# print(button.get_attribute('innerHTML'))

assert 'Show Message' in driver.page_source
user_message = driver.find_element_by_id('user-message')
button1 = driver.find_element_by_css_selector('#get-input > .btn')
print(button1)
user_message.clear()
user_message.send_keys('hello this is test ')
button.click()
output_message = driver.find_element_by_id('display')
assert 'hello this is test' in output_message.text

# driver.close()
# driver.quit()
