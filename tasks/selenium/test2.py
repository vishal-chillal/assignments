import unittest, time, os
from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

class SeleniumFormAutomation(unittest.TestCase):

    def setUp(self):
        
        self.driver = webdriver.Firefox()
        # self.driver = webdriver.Chrome()
        self.firstname = "vishal"
        self.lastname = "chillal"
        self.form_page = "http://toolsqa.com/automation-practice-form/"

    def test_form_filling(self):
        ''' function to fill and submit the form. '''
        browser = self.driver
        browser.get(self.form_page)
        assert "Demo" in browser.title
        browser.find_element_by_name("firstname").send_keys(self.firstname)
        browser.find_element_by_name("lastname").send_keys(self.lastname)
        browser.find_element_by_id("sex-0").click()
        browser.find_element_by_id("exp-0").click()
        
        calander = browser.find_element_by_id("datepicker")
        ActionChains(self.driver).move_to_element(calander).click().send_keys('01012011').perform()
        browser.find_element_by_id("datepicker").click()
        browser.find_element_by_id("profession-1").click()
        browser.find_element_by_id("photo").send_keys(os.getcwd()+"/image.png")
        browser.find_element_by_id("tool-1").click()
        browser.find_element_by_id("tool-2").click()
        
        continent = Select(browser.find_element_by_id("continents"))
        continent.select_by_visible_text('Antartica')
        
        browser.find_element_by_id("submit").click()

    def test_check_submission(self):
        ''' in this function we can check the aftersubmit oprations.'''
        wait = WebDriverWait( self.driver, 5 )
        url = self.driver.current_url

        try:
            page_loaded = wait.until_not(
                lambda browser: self.driver.current_url == self.form_page
            )
        except TimeoutException:
            self.fail( "Loading timeout expired" )

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
