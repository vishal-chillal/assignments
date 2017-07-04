import unittest, time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_form_filling(self):
        browser = self.driver
        form_page = "http://toolsqa.com/automation-practice-form/"
        browser.get(form_page)
        assert "Demo" in browser.title

        browser.find_element_by_name("firstname").send_keys("vishal")
        browser.find_element_by_name("lastname").send_keys("chillal")
        browser.find_element_by_id("sex-0").click()
        browser.find_element_by_id("exp-0").click()
        browser.find_element_by_id("profession-1").click()
        browser.find_element_by_id("tool-1").click()
        browser.find_element_by_id("tool-2").click()
        continent = Select(browser.find_element_by_id("continents"))
        continent.select_by_visible_text('Antartica')

        browser.find_element_by_id("submit").click()

        wait = WebDriverWait( browser, 5 )
        print browser.current_url

        try:
            page_loaded = wait.until_not(
                lambda browser: browser.current_url == form_page
            )
        except TimeoutException:
            self.fail( "Loading timeout expired" )
 

    def tearDown(self):
        time.sleep(3)
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
