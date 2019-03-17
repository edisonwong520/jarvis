# -*- coding: utf-8 -*-

from urllib.parse import quote
import string

def run(driver, args):
    key = args[0]
    url = "https://www.baidu.com/s?wd={}".format(key)
    url_str = quote(url, safe=string.printable)
    driver.open_website(url_str)
