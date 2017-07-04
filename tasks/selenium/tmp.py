#!/usr/bin/env python

import unittest
from selenium import webdriver

class TestHomepage(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        
    def testTitle(self):
        self.browser.get('http://toolsqa.com/automation-practice-form/')
        self.assertIn('Demo', self.browser.title)
        
    def automateForm(self):
        self.browser.firstname = "vishal"
        self.findElement(By.name("firstname")).sendKeys("vishal")
    # def tearDown(self):
    #     self.browser.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
