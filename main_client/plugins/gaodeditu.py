from urllib import parse
import urllib.request
import string
import re
import os


def run(args):
    sp = args[0]
    des = args[1]
    traffic_type = args[2]

    # find starting point  longitude and latitude data
    url = "https://restapi.amap.com/v3/place/text?s=rsv3&children=&key=8325164e247e15eea68b59e89200988b&page=1&offset=10" \
          "&city=220100&language=zh_cn&callback=jsonp_723771_&platform=JS&logversion=2.0&sdkversion=1.3&appname=https%3A" \
          "%2F%2Flbs.amap.com%2Fconsole%2Fshow%2Fpicker&csid=4C38031A-B147-4B0A-963D-9A0F3413DA1F&keywords="
    url_str = parse.quote_plus(url + sp, safe=string.printable)
    reponse = urllib.request.urlopen(url_str)
    data = bytes.decode(reponse.read())
    pat = re.compile(r'"location":"(.+?)"')
    sp_location = pat.search(data).group(1)

    # des  longitude and latitude data
    url_str = parse.quote_plus(url + des, safe=string.printable)
    reponse = urllib.request.urlopen(url_str)
    data = bytes.decode(reponse.read())
    pat = re.compile(r'"location":"(.+?)"')
    des_location = pat.search(data).group(1)

    url = "https://ditu.amap.com/dir?type={}&policy=2&from[lnglat]={}&from[name]=startpoint&to[lnglat]={}&to[name]=" \
          "endpoint&src=mypage&callnative=0".format(traffic_type, sp_location.replace(",", "%2C"),
                                                    des_location.replace(",", "%2C"))

    url_str = parse.quote_plus(url, safe=string.printable)
    os.system("""open -a "Google Chrome" "{}" """.format(url_str))
    os.system("say '正在为 您显示路线'")
