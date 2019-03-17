# -*- coding: utf-8 -*-
import os
import urllib.request
import time
import urllib.parse
from urllib.parse import quote
import string
import re

# 不同的chrome版本对应不同的chromedriver版本
driver_version = {"69": "2.41", "68": "2.40", "67": "2.40", "66": "2.40", "65": "2.38",
                  "64": "2.37", "63": "2.36", "62": "2.34", "61": "2.33", "60": "2.33",
                  "59": "2.32", "58": "2.29", "57": "2.28", "56": "2.27", "55": "2.25",
                  "54": "2.27", "53": "2.25", "52": "2.24", "51": "2.23", "50": "2.21",
                  "49": "2.22", "48": "2.20", "47": "2.19", "46": "2.18", "45": "2.13",
                  "44": "2.19", "43": "2.17", "42": "2.15", "41": "2.13", "40": "2.12"}


def get_version_mac():
    cmd = r'/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --version'
    re = os.popen(cmd).read().strip()
    version = re.split(" ")[2].split(".")
    return version


# mac chrome driver 驱动下载
def dl_driver_mac():
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


def run(driver, args):
    songname = args[0]

    cur_path_list = os.getcwd().split("/")[:-1]
    cur_path = "/".join(cur_path_list) + "/dependencies/chromedriver/chromedriver"

    # if it does have a diver,so download one
    if not os.path.exists(cur_path):
        dl_driver_mac()

    # qqmusic API
    """https://c.y.qq.com/soso/fcgi-bin/client_search_cp?&lossless=0&flag_qc=0&p=1&n=20&w="""

    url = "https://c.y.qq.com/soso/fcgi-bin/client_search_cp?&lossless=0&flag_qc=0&p=1&n=20&w={0}".format(songname)
    s = quote(url, safe=string.printable)
    reponse = urllib.request.urlopen(s)
    data = bytes.decode(reponse.read())

    # find the top one song id
    pat = re.compile(r'"songmid":"(.+?)"')
    result = pat.search(data).group()
    song_id = result.split('"')[-2]

    os.system("say '正在为您播放'")
    song_url = "https://y.qq.com/n/yqq/song/{0}.html".format(song_id)

    driver.open_website(song_url)

    # driver.get("https://y.qq.com/portal/player.html")
    time.sleep(0.7)
    driver.find_element_by_class_name("mod_btn_green__icon_play")
