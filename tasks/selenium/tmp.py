#!/usr/bin/env python
from time import sleep
import unittest
from selenium import webdriver
from selenium.common.exceptions import *
class TestHomepage(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        
    def testTitle(self):
        self.form_page = "https://www.youtube.com/watch?v=yo6kyyX0nBI"
        self.browser.get(self.form_page)
        # date_8[date][yy]: 1992
        # try:
        # //*[@id="main"]/div[2]/a[2]
        #     self.browser.find_element_by_id("masthead-search-term").send_keys("pardesiyon se na ankhiya milana\n")
        #     self.browser.find_element_by_id("search-btn").click()
        # except NoSuchElementException:
        #     print "element error"
        sleep(3)
    # def tearDown(self):
    #     self.browser.quit()


if __name__ == '__main__':
    unittest.main()
