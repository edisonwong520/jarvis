# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver import ChromeOptions
import os
import urllib.request
import urllib.parse
import re

# 不同的chrome版本对应不同的chromedriver版本
driver_version = {"69": "2.41", "68": "2.40", "67": "2.40", "66": "2.40", "65": "2.38",
                  "64": "2.37", "63": "2.36", "62": "2.34", "61": "2.33", "60": "2.33",
                  "59": "2.32", "58": "2.29", "57": "2.28", "56": "2.27", "55": "2.25",
                  "54": "2.27", "53": "2.25", "52": "2.24", "51": "2.23", "50": "2.21",
                  "49": "2.22", "48": "2.20", "47": "2.19", "46": "2.18", "45": "2.13",
                  "44": "2.19", "43": "2.17", "42": "2.15", "41": "2.13", "40": "2.12"}


# mac chrome driver 驱动下载
def dl_driver_mac():
    print("--------------缺少驱动，将自动下载驱动--------------")
    request = urllib.request.Request('http://npm.taobao.org/mirrors/chromedriver/')
    response = urllib.request.urlopen(request)
    html = response.read()
    pat = re.compile(r'/mirrors/chromedriver/(.+?)/')
    result = pat.findall(str(html))
    flag = 0
    # 获得版本数组
    # 想了想可以用xpath快速匹配的，但觉得安装第三方模块也需要时间
    version = get_version_mac()
    if int(version[0]) <= 69:
        chrome_version = driver_version[version[0]]
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


def get_version_mac():
    cmd = r'/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --version'
    re = os.popen(cmd).read().strip()
    version = re.split(" ")[2].split(".")
    return version


def get_browser():
    cur_path_list = os.getcwd().split("/")[:-1]
    cur_path = "/".join(cur_path_list) + "/dependencies/chromedriver/chromedriver"
    ind = cur_path.index("Jarvis")
    cur_path =cur_path[:ind+6]+"/dependencies/chromedriver/chromedriver"
    # if it does have a diver,so download one
    if not os.path.exists(cur_path):
        print("下载地址"+cur_path)
        dl_driver_mac()

    """mac下手动填写Chrome位置"""

    opts = ChromeOptions()
    opts.add_experimental_option("detach", True)

    driver = webdriver.Chrome(executable_path=cur_path, options=opts)

    return driver
