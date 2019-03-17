# -*- coding: utf-8 -*-
from selenium import webdriver
# from selenium.webdriver import ChromeOptions
import os
import urllib.request
import urllib.parse
import re
import subprocess
from selenium.webdriver.chrome.options import Options


class Safari():
    def __init__(self):
        self.driver = self.get_driver()

    def open_new_tab(self, url):
        self.driver.execute_script("window.open('{}');".format(url))

    def open_website(self, url):
        self.driver.get(url)

    def close(self):
        self.driver.quit()

    def find_element_by_class_name(self, name):
        self.driver.find_element_by_class_name(name).click()

    def get_driver(self):
        driver = webdriver.Safari()
        cmd = """ osascript -e 'tell application "System Events" to keystroke "h" using {command down}' """
        os.system(cmd)
        return driver
