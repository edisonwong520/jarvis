# -*- coding: utf-8 -*-
from selenium import webdriver
# from selenium.webdriver import ChromeOptions
import os
import urllib.request
import urllib.parse
import re
import subprocess
from selenium.webdriver.chrome.options import Options


class Chrome():
    def __init__(self):
        self.driver = self.get_driver()
        self.driver_version = {"69": "2.41", "68": "2.40", "67": "2.40", "66": "2.40", "65": "2.38",
                               "64": "2.37", "63": "2.36", "62": "2.34", "61": "2.33", "60": "2.33",
                               "59": "2.32", "58": "2.29", "57": "2.28", "56": "2.27", "55": "2.25",
                               "54": "2.27", "53": "2.25", "52": "2.24", "51": "2.23", "50": "2.21",
                               "49": "2.22", "48": "2.20", "47": "2.19", "46": "2.18", "45": "2.13",
                               "44": "2.19", "43": "2.17", "42": "2.15", "41": "2.13", "40": "2.12"}

    def dl_driver_mac(self):
        os.system("say '缺少驱动，将为您自动下载驱动'")
        print("--------------缺少驱动，将自动下载驱动--------------")
        request = urllib.request.Request('http://npm.taobao.org/mirrors/chromedriver/')
        response = urllib.request.urlopen(request)
        html = response.read()
        pat = re.compile(r'/mirrors/chromedriver/(.+?)/')
        result = pat.findall(str(html))
        flag = 0
        # 获得版本数组
        # 想了想可以用xpath快速匹配的，但觉得安装第三方模块也需要时间
        version = self.get_version_mac()
        if int(version[0]) <= 69:
            chrome_version = self.driver_version[version[0]]
        else:
            chrome_version = version[0] + '.' + version[1] + '.' + version[2]

        for item in result:
            if chrome_version in item:
                flag = item
                break

        cur_path_list = os.getcwd().split("/")[:-1]
        cur_path = "/".join(cur_path_list) + "/dependencies/chromedriver"

        """http://npm.taobao.org/mirrors/chromedriver/72.0.3626.69/chromedriver_mac64.zip"""
        print("--------------正在下载驱动--------------")
        # create the dir
        os.system("mkdir -p {0}".format(cur_path))
        os.system(
            "cd {0}&&curl -O -L http://npm.taobao.org/mirrors/chromedriver/{1}/chromedriver_mac64.zip".format(cur_path,
                                                                                                              flag))
        print("\n--------------驱动下载成功--------------")
        os.system("cd {0}&&unzip -o chromedriver_mac64.zip".format(cur_path))
        print("\n--------------驱动解压成功--------------")
        return cur_path

    def get_version_mac(self):
        cmd = r'/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --version'
        re = os.popen(cmd).read().strip()
        version = re.split(" ")[2].split(".")
        return version

    def open_new_tab(self, url):
        self.driver.execute_script("window.open('{}');".format(url))

    def open_website(self, url):
        self.driver.get(url)

    def close(self):
        self.driver.quit()

    def find_element_by_class_name(self, name):
        self.driver.find_element_by_class_name(name).click()

    def get_driver(self):

        cur_path_list = os.getcwd().split("/")[:-1]
        cur_path = "/".join(cur_path_list) + "/dependencies/chromedriver/chromedriver"

        if not os.path.exists(cur_path):
            self.dl_driver_mac()

        cur_path_list = os.getcwd().split("/")[:-1]
        cur_path = "/".join(cur_path_list) + "/config/"
        cmd = '/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-' \
              'dir="{}" '.format(cur_path)
        subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

        chrome_options = Options()
        chrome_options.debugger_address = "127.0.0.1:9222"

        cur_path_list = os.getcwd().split("/")[:-1]
        cur_path = "/".join(cur_path_list) + "/dependencies/chromedriver/chromedriver"

        driver = webdriver.Chrome(cur_path, options=chrome_options)
        cmd = """ osascript -e 'tell application "System Events" to keystroke "h" using {command down}' """
        os.system(cmd)
        return driver
