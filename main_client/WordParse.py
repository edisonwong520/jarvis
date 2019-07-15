# -*- coding: utf-8 -*-
import datetime
import re
import json
import sys

# please add all the plugin into the func_dict
func_dict = ["parse_calculator", "parse_song", "parse_weather", "parse_ditu", "parse_baidusearch", "parse_timer",
             "parse_shutdown", "parse_restart", "parse_baidutranslate"]


class WordParse():
    # start point to parse
    def word_parse(self, data):
        data = data.replace("贾维斯", "")

        for func_name in func_dict:
            result = getattr(self, func_name)(data)
            if result:
                return result
        return ()

    def parse_baidutranslate(self, data):
        pat = re.compile(r"^翻译(.*)")
        if not pat.findall(data):
            return
        arg0 = pat.findall(data)[0]
        # return (pluginname,(word,origin_language,destination_language))
        return ("baidutranslate", (arg0, "zh", "en"))

    # sub parse function is belowed
    def parse_ditu(self, data):
        bus = ["公交", "巴士"]
        walk = ["走路", "走路", "步行", "走"]
        car = ["开车", "坐车"]
        flag = False

        pat = re.compile(r"(.*?)从(.*)到(.*)")

        # quit
        if not pat.findall(data):
            return
        arg0 = pat.findall(data)[0][0]
        arg1 = pat.findall(data)[0][1]
        arg2 = pat.findall(data)[0][2]

        # usually the result is ('', '大学', '机场开车怎么走') so just judge the arg1 and arg2

        if len(arg1) != 0 and len(arg2) != 0:
            flag = True
        if not flag:
            return ()

        # set the default traffic type
        traffic_type = "car"

        # judge the arg0
        for item in bus:
            if item in arg0:
                traffic_type = "bus"
                break
        for item in walk:
            if item in arg0:
                traffic_type = "walk"
                break
        for item in car:
            if item in arg0:
                traffic_type = "car"
                break

        sp_location = arg1

        des_str = arg2
        des_str = des_str.replace("怎么走", "")
        des_str = des_str.replace("怎么去", "")
        des_location = des_str

        # judge the arg2
        for item in bus:
            if item in des_str:
                traffic_type = "bus"
                n = des_str.index(item)
                des_location = des_str[:n]
                break
        for item in walk:
            if item in des_str:
                traffic_type = "walk"
                n = des_str.index(item)
                des_location = des_str[:n]
                break
        for item in car:
            if item in des_str:
                traffic_type = "car"
                n = des_str.index(item)
                des_location = des_str[:n]
                break

        return ("gaodeditu", (sp_location, des_location, traffic_type))

    def parse_song(self, data):
        # play music or download music

        # key word that storage
        key_play = ["放一首", "来一首", "放"]
        key_dl = ["下一首", "下载"]

        for item in key_play:
            if item in data:
                index = data.find(item) + len(item)
                songname = data[index:]

                return ("qqmusic", (songname,))
        for item in key_dl:
            if item in data:
                index = data.find(item) + len(item)
                songname = data[index:]
                return ("qqmusicdl", (songname,))
        return ()

    def parse_weather(self, data):
        key = ["天气"]

        flag = False
        l = []

        today = datetime.date.today()
        tomorrow = today + datetime.timedelta(days=1)
        after_tomorrow = today + datetime.timedelta(days=2)
        # parse_weather(today)

        days = {"今": today.strftime("%Y-%m-%d"), "明": tomorrow.strftime("%Y-%m-%d"),
                "后": after_tomorrow.strftime("%Y-%m-%d")}
        for item in key:
            if item in data:
                flag = True
                break
        if flag:
            for day in days.keys():
                if day in data:
                    l.append(days[day])

        # l example: ('2019-03-16', '2019-03-18')
        if not l:
            return ()
        else:
            return ("weather", tuple(l))

    def parse_calculator(self, data):
        key = ["+", "-", "*", "/", "加", "减", "乘", "除"]
        flag = False
        for item in key:
            if item in data:
                flag = True
                break
        if not flag:
            return ()

        data = data.replace("加", "+").replace("减", "-").replace("乘", "*").replace("除", "/").replace("等于", "")
        data = data.replace("一", "1").replace("二", "2").replace("三", "3").replace("四", "4").replace("五", "5")
        data = data.replace("六", "6").replace("七", "7").replace("八", "8").replace("九", "9").replace("零", "0")
        return ("calculator", (data,))

    def parse_baidusearch(self, data):
        str = data
        flag = False
        if "百度" in data:
            flag = True
        if not flag:
            return ()
        key = ["搜", "搜索", "百度", "百度一下"]
        for item in key:
            str = str.replace(item, "")
        return ("baidusearch", (str,))

    def parse_timer(self, data):
        flag = False
        term = ["计时", "倒数", "闹钟"]
        for i in term:
            if i in data:
                flag = True
        if not flag:
            return ()

        from time_parse import TimeNormalizer
        tn = TimeNormalizer.TimeNormalizer()
        time_dict = tn.parse(data)
        time_dict = json.loads(time_dict)
        if time_dict and time_dict["type"] == "timedelta":
            # timedelta is a dict
            timedelta = time_dict["timedelta"]
            return ("timer", (timedelta,))
        else:
            return ()

    def parse_shutdown(self, data):
        if "关机" not in data and "关电" not in data:
            return ()
        from time_parse import TimeNormalizer
        tn = TimeNormalizer.TimeNormalizer()
        time_dict = tn.parse(data)
        time_dict = json.loads(time_dict)
        if time_dict and time_dict["type"] == "timedelta":
            # timedelta is a dict
            timedelta = time_dict["timedelta"]

            return ("autoshutdown", (timedelta,))
        else:
            return ()

    def parse_restart(self, data):
        if "重启" not in data and "重新启动" not in data:
            return ()
        from time_parse import TimeNormalizer
        tn = TimeNormalizer.TimeNormalizer()
        time_dict = tn.parse(data)
        time_dict = json.loads(time_dict)

        if time_dict and time_dict["type"] == "timedelta":
            # timedelta is a dict
            timedelta = time_dict["timedelta"]

            return ("autorestart", (timedelta,))
        else:
            return ()
