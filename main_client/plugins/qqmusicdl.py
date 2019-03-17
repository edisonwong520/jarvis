import urllib.parse
from urllib.parse import quote
import string
import re
import os
import requests

headers = {'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; vivo x5s l Build/LMY48Z)',
           'Referer': 'https://y.qq.com/portal/profile.html'}

qq_re = re.compile(r'(\w+)\.html')

size_list = ['size_128mp3', 'size_320mp3', 'size_ape', 'size_flac']

dl = True

down_type = 'size_flac'


def download(single_info, down_path):
    if not dl:
        return
    if not os.path.exists(down_path):
        os.makedirs(down_path)

    if down_type not in size_list:
        print('输入格式错误')
    length = len(single_info['link_info'])
    try:
        url = single_info['link_info'][down_type]['link']
    except:
        url = single_info['link_info'][size_list[length - 1]]['link']
    type = re.search(r'(mp3|ape|flac)', url).group(0)
    song_name = single_info['song_name'] + '-' + single_info['singer_name'] + '.' + type
    song_path = down_path + '/' + song_name
    if os.path.exists(song_path):
        getsize = os.path.getsize(song_path)
        if getsize == 0:
            os.remove(song_path)
        else:
            print('already exist:{0} skip'.format(song_name))
            return

    print('start download:', song_name)
    with requests.get(url, headers=headers, stream=True) as r:
        with open(song_path, mode='wb') as f:
            f.write(r.content)
    print('download success')
    os.system("say '下载成功'")


def get_key():
    uin = '1008611'
    guid = '1234567890'
    getVkeyUrl = 'https://c.y.qq.com/base/fcgi-bin/fcg_music_express_mobile3.fcg?g_tk=0&loginUin={uin}&hostUin=0&format=' \
                 'json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0&cid=205361747&uin={uin}&songmid=' \
                 '003a1tne1nSz1Y&filename=C400003a1tne1nSz1Y.m4a&guid={guid}'
    url = getVkeyUrl.format(uin=uin, guid=guid)
    try:
        r = requests.get(url, headers=headers)
        json = r.json()
        vkey = json['data']['items'][0]['vkey']
        if len(vkey) == 112:
            return vkey
    except:
        pass
    return None


def get_link(media_mid, vkey):
    type_info = [['M500', 'mp3'], ['M800', 'mp3'], ["A000", 'ape'], ['F000', 'flac']]
    dl_url = 'http://streamoc.music.tc.qq.com/{prefix}{media_mid}.{type}?vkey={vkey}&guid=1234567890&uin=1008611&fromtag=8'
    dl = []
    for item in type_info:
        s_url = dl_url.format(prefix=item[0], media_mid=media_mid, type=item[1], vkey=vkey)
        dl.append(s_url)
    return dl


def get_single_info(songmid, vkey, do=True):
    info_url = 'https://c.y.qq.com/v8/fcg-bin/fcg_play_single_song.fcg?songmid={songmid}&tpl=yqq_song_detail&format=json' \
               '&callback=getOneSongInfoCallback&g_tk=5381&jsonCallback=getOneSongInfoCallback&loginUin=0&hostUin=0&format' \
               '=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0'
    url = info_url.format(songmid=songmid)
    try:
        r = requests.get(url=url, headers=headers)
        json = r.json()
        music_info = json['data'][0]['file']
        media_mid = json['data'][0]['file']['media_mid']
        song_name = json['data'][0]['name']
        singer_name = json['data'][0]['singer'][0]['name']
        album_name = json['data'][0]['album']['name']
        single_info = {'singer_name': singer_name, 'song_name': song_name, 'album_name': album_name,
                       'media_mid': media_mid}
        song_link = get_link(media_mid, vkey)
        link_info = {}
        for i in range(0, 4):
            s = format(music_info[size_list[i]] / 1024 / 1024)
            if s == '0.0':
                continue
            link_info[size_list[i]] = {'size': s, 'link': song_link[i]}
        single_info['link_info'] = link_info

        cur_path_list = os.getcwd().split("/")[:-1]
        down_path = "/".join(cur_path_list) + "/download/songs"
        print("下载地址为："+down_path)
        os.system("mkdir -p {}".format(down_path))

        try:
            if do:
                download(single_info, down_path)

        except:
            os.system("say '下载失败'")
            print('download fail')
        return single_info
    except:
        pass
    return None


def run(driver,args):
    songname = args[0]
    url = "https://c.y.qq.com/soso/fcgi-bin/client_search_cp?&lossless=0&flag_qc=0&p=1&n=20&w={0}".format(songname)
    s = quote(url, safe=string.printable)
    reponse = urllib.request.urlopen(s)
    data = bytes.decode(reponse.read())

    # find the top one song id
    pat = re.compile(r'"songmid":"(.+?)"')
    result = pat.search(data).group()
    song_id = result.split('"')[-2]

    os.system("say '正在为您下载'")
    v_key = get_key()
    get_single_info(song_id, v_key)
