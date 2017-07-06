from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# driver = webdriver.Firefox()
driver = webdriver.Chrome(executable_path = '/usr/local/bin/chromedriver')
driver.get("http://toolsqa.com/automation-practice-form/")
# assert "Demo" in driver.title
# elem = driver.find_element_by_name("firstname")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()
