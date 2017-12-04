#!/usr/bin/env python
from time import sleep
import unittest
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.action_chains import ActionChains
class TestHomepage():
    
    def __init__(self):
        self.browser = webdriver.Firefox()
        self.testTitle()

    def testTitle(self):
        self.form_page = "http://demoqa.com/draggable/"
        self.browser.get(self.form_page)
        
        # resizable
        self.drag = self.browser.find_element_by_id("draggable")
        print self.drag.text
        
        sleep(3)
        try:
            self.acn = ActionChains(self.browser)
            self.acn.click_and_hold(self.drag)
            self.acn.move_by_offset(100,200)# xoffset, yoffset
            self.acn.click()
            self.acn.perform()
        except Exception as e:
            print e

t = TestHomepage()
