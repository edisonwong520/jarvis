# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import re
from xpinyin import Pinyin
import datetime
import os
import socket


def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip


def time_count(func):
    def int_time(*args, **kwargs):
        start_time = datetime.datetime.now()  # 程序开始时间
        func(*args, **kwargs)
        over_time = datetime.datetime.now()  # 程序结束时间
        total_time = (over_time - start_time).total_seconds()
        print('----------本程序共运行了%s秒----------' % total_time)

    return int_time


def run(args):
    url = """http://www.ip138.com/ips138.asp?ip={0}&action=2""".format(get_host_ip())

    reponse = urllib.request.urlopen(url)
    data = reponse.read().decode('GBK')

    pat = re.compile("参考数据1：(.+?)</li>?")
    result = pat.findall(data)[0].split("  ")[0]

    if result.startswith("黑龙江") or result.startswith("内蒙古"):
        location = result[:3] + " " + result[3:]
    else:
        location = result[:2] + " " + result[2:]

    p = Pinyin()
    pinyin = []

    for item in location.split(" ")[:2]:
        pinyin.append(p.get_pinyin(item, ''))

    if "beijing" not in pinyin and "tianjin" not in pinyin:
        # weather website
        url = "http://qq.ip138.com/weather/{}.htm".format("/".join(pinyin))
    else:
        url = "http://qq.ip138.com/weather/{}".format(pinyin[0])

    reponse = urllib.request.urlopen(url)
    data = reponse.read().decode('GBK')
    pat = re.compile("'bdText':'(.+)ip138.com查询")
    result = pat.findall(str(data))[0]
    index = result.index("_")
    weather_list = result[index + 1:].split("；")

    # A dict storage today ,tomorrow ,after tomorrow weather
    # weather dict example :{'2019-3-15': '阴，19℃～16℃', '2019-3-16': '多云转阴，23℃～16℃', '2019-3-17': '阴转多云，24℃～17℃。'}
    weather = {}
    for day in weather_list:
        day1 = day.split("：")[0]
        month = day1.split("-")[1]
        if int(month) < 10:
            month_str = "0" + str(month)
        else:
            month_str = str(month)

        date = "{}-{}-{}".format(day1.split("-")[0], month_str, day1.split("-")[2])
        weather[date] = day.split("：")[1:][0]

    # ----------
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)
    after_tomorrow = today + datetime.timedelta(days=2)

    days_dict = {today.strftime("%Y-%m-%d"): "今", tomorrow.strftime("%Y-%m-%d"): "明",
                 after_tomorrow.strftime("%Y-%m-%d"): "后"}
    print("----------天气预告----------")
    for item in weather.keys():
        print(item + ': ' + weather[item])
    print("---------------------------")

    for date in args:
        os.system('say "{}天天气:{}"'.format(days_dict[date], weather[date].replace("～", "至").replace("-", "负")))

# run(('2019-03-16','2019-03-18'))
