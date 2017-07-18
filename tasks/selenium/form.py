import os, ConfigParser
from time import sleep
import random
from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
from selenium.webdriver.common.action_chains import ActionChains
class SeleniumFormAutomation(object):
    '''class for reg form filling by selenium automation'''
    def __init__(self):
        conf = ConfigParser.ConfigParser()
        conf_file_name = "./conf.csv"
        section = "config"
        self.browser = webdriver.Firefox()
        self.form_page = "http://demoqa.com/registration/"

        self.ConfigSectionMap(section, conf, conf_file_name)
        self.test_form_filling()
        
    def ConfigSectionMap(self, section, Config, conf_file_name):
        '''read config file,and create a dictionary containing user details '''
        dict1 = {}
        Config.read(conf_file_name)
        options = Config.options(section)

        for option in options:
            try:
                dict1[option] = Config.get(section, option)
            except:
                print("exception on %s!" % option)
                dict1[option] = None
        self.detail_info = dict1

    def test_form_filling(self):
        ''' function to fill and submit the form '''
        self.browser.get(self.form_page)
        assert "Demo" in self.browser.title
        remaining_list = []
        for entry in self.detail_info:
            try:
                self.browser.find_element_by_name(entry).send_keys(self.detail_info[entry])
            except NoSuchElementException:
                remaining_list.append(entry)
            except Exception as FileNotFound:
                print FileNotFound
        try:

            self.browser.find_element_by_id("profile_pic_10").send_keys(os.getcwd()+"/profile.jpg")
            self.browser.find_element_by_id("confirm_password_password_2").send_keys(self.detail_info["password"])
            year = Select(self.browser.find_element_by_id("yy_date_8"))
            year.select_by_visible_text('1992')
            country = Select(self.browser.find_element_by_id("dropdown_7"))
            country.select_by_value('India')
            status = self.browser.find_elements_by_name("radio_4[]")
            for i in status:
                if i.get_attribute("value") in remaining_list:
                    i.click()
            hobby_list = self.browser.find_elements_by_name("checkbox_5[]")
            for i in hobby_list:
                if i.get_attribute("value") in remaining_list:
                    i.click()
            self.browser.find_element_by_name("pie_submit").click()
            self.test_check_submission()

        except NoSuchElementException as e:
            print e
        except KeyError as e:
            print "Key Error :",e
            
        
    def test_check_submission(self):
        ''' in this function we can check the aftersubmit oprations '''
        sleep(3) # wait for reload the page.

        # try:
        #     error_list = self.browser.find_elements_by_class_name("legend_txt")
        #     # finding that if there are any required fields in the form
        #     # for errors in error_list:
        #     #     print errors.text
        #     print "Errors are:\n", error_list
        #     self.tearDown()
        # except NoSuchElementException:
        #     pass

        try:
            login_error = self.browser.find_element_by_class_name("piereg_login_error")
            if "Username " in login_error.text:
                # IF USERNAME ALREADY EXISTS, THEN ADD NEW INTEGER TO THE END
                print "username error"
                self.detail_info["username"] += str(random.randint(0,10))
                self.test_form_filling()
        
            elif "E-mail" in login_error.text:
                # IF EMAIL ADDRESS IS ALREADY EXISTS, HANDLED IT HERE
                print "email error"
                email = self.detail_info["e_mail"].split("@")
                email[0] += chr(random.randint(65,90))
                self.detail_info["e_mail"] = "@".join(email)
                self.test_form_filling()

        except NoSuchElementException:
            # IF CODE ENTERS HERE MEANS NO ERROR MESSAGE ARRIVED
            try:
                login_msg = self.browser.find_element_by_class_name("piereg_message").text
                # FINDING FOR SUCCESSFUL LOGIN
                if "Thank" in login_msg:
                    print "success"
                    for key, value in self.detail_info.items():
                        print key, "\t", value
            except NoSuchElementException:
                # FIND THINGS WHICH ARE UNHANDLED
                print "find the error ;-) "

            except TypeError as e:
                print e

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    tmp = SeleniumFormAutomation()

