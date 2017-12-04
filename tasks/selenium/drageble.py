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

    def errorHandling(self, errorMsg):
        print errorMsg
        self.browser.close()
        exit(0)

    def testTitle(self):
        self.form_page = "http://demoqa.com/draggable/"
        try:
            self.browser.get(self.form_page)
            self.drag = self.browser.find_element_by_id("draggable")
        except NoSuchElementException as e:
            self.errorHandling(e)
        finally:
            pass
         
        sleep(3)
        try:
            self.acn = ActionChains(self.browser)
            self.acn.click_and_hold(self.drag)
            self.acn.move_by_offset(100.0, 200.0)# xoffset, yoffset
            self.acn.click()
            self.acn.perform()
        except Exception as e:
            self.errorHandling(e)



        # this part is not propperly working.......
        try:
            self.browser.find_element_by_id("ui-id-5").click()
        except NoSuchElementException as e:
            self.errorHandling(e)

        try:
            a = self.browser.find_elements_by_xpath("//*[contains(text(), 'Item')]")
        except NoSuchElementException as e:
            self.errorHandling(e)

        try:
            self.acn.drag_and_drop_by_offset(a[0], a[-1].location["y"]+10, a[-1].location["x"])
            self.acn.perform()
        except Exception as e:
            self.errorHandling(e)


t = TestHomepage()

