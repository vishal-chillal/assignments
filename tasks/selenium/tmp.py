#!/usr/bin/env python

import unittest
from selenium import webdriver
from selenium.common.exceptions import *
class TestHomepage(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        
    def testTitle(self):
        self.form_page = "http://demoqa.com/registration/"
        self.browser.get(self.form_page)
        # date_8[date][yy]: 1992
        try:
            self.browser.find_element_by_name("date_8[date][yy]").send_keys("1993")
        except NoSuchElementException:
            print "element error"

    # def tearDown(self):
    #     self.browser.quit()


if __name__ == '__main__':
    unittest.main()
