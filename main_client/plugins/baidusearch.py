# -*- coding: utf-8 -*-

from urllib.parse import quote
import string
import os


def run(driver, args):
    key = args[0]
    url = "https://www.baidu.com/s?wd={}".format(key)
    url_str = quote(url, safe=string.printable)
    os.system("""open -a "Google Chrome" "{}" """.format(url_str))
