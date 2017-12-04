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
        # self.browser.close()
        return

    def testTitle(self):
        self.form_page = "http://amazon.in"
        try:
            self.browser.get(self.form_page)
            # self.drag = self.browser.find_element_by_id("draggable")
            a = self.browser.find_element_by_xpath("//*[contains(text(), 'Sign in')]")
            a.click()

        except NoSuchElementException as e:
            self.errorHandling(e)
        except Exception as e:
            self.errorHandling(e)

        sleep(5)
        try:
            # self.p = self.browser.find_element_by_xpath("//*[@name='password']")
            self.u = self.browser.find_element_by_xpath('//*[@id="ap_email"]')
            self.u.send_keys("vishal_k3g@yahoo.com")
            self.p = self.browser.find_element_by_xpath('//*[@id="ap_password"]')
            self.p.send_keys("Indianairforce&777")

            self.login = self.browser.find_elements_by_xpath("//*[contains(text(), 'Login')]")[1]
            self.login.click()

        except Exception as e:
            self.errorHandling(e)
t = TestHomepage()

