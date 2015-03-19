from __future__ import unicode_literals
# -*- coding: utf-8 -*-
import unittest
import time
from selenium import webdriver
'''
import os
from easyprocess import EasyProcess
from pyvirtualdisplay import Display
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui as ui
'''
####################################################################################################
__author__ = 'LOKIEC'
__project__= 'Pajacyk'
####################################################################################################
####################################################################################################
class Pajacyk(unittest.TestCase):

    def setUp(self):
        #self.browser = webdriver.Firefox()
        self.chrome_driver = webdriver.Chrome()

    # because it is a unit test we need to start method name with 'test' so here we have: test_pajacyk_click()
    def test_pajacyk_click(self):
        pajacyk_homepage = "http://www.pajacyk.pl/"
        #browser = self.browser
        #browser.get(pajacyk_homepage)
        chrome_browser = self.chrome_driver
        chrome_browser.set_window_size(1280, 720)
        chrome_browser.get(pajacyk_homepage)
        click_it = chrome_browser.find_element_by_class_name("paj-click")
        click_it.click()
        time.sleep(5)
        #click_it.click()

    def tearDown(self):
        self.chrome_driver.quit()
####################################################################################################
####################################################################################################
#script execution by running it as unit test - running our test suite
if __name__ == "__main__":
    unittest.main()
