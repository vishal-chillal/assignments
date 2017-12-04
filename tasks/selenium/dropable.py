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
        try:
            self.browser.close()
        except:
            pass
        exit(0)

    def testTitle(self):
        self.form_page = "http://demoqa.com/droppable"
        try:
            self.browser.get(self.form_page)
            self.drag = self.browser.find_elements_by_class_name("ui-draggable")
            self.drop_reject = self.browser.find_element_by_id("droppableaccept")
        except NoSuchElementException as e:
            self.errorHandling(e)
        except Exception as e:
            self.errorHandling(e)

        for i in self.drag:
            try:
                self.acn = ActionChains(self.browser)
                self.acn.click_and_hold(i)
                self.acn.move_to_element(self.drop)
                self.acn.click()
                self.acn.perform()
            except Exception as e:
                self.errorHandling(e)

        
            try:
                if self.drop.text == "Dropped!":
                    errorHandling( "Well Done...!")
                    break

                else:
                    print "Do it again"
            except Exception as e:
                errorHanding(e)
                

t = TestHomepage()

