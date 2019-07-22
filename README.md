## 简介
中文版贾维斯Jarvis语音助手  （电脑加强版Siri，已自动播放下载音乐/天气播报/问路导航/计时器）  
Jarvis--A very intelligent assistant based voice control


## 已实现的功能
- 功能1:自动放歌
- 功能2:自动下载歌
- 功能3:天气播报
- 功能4:计算器
- 功能5:问路导航（高德地图）  
- 功能6:百度搜索  
- 功能7:计时器功能（闹钟）
- 功能8:自动关机/重启(也可以自动设定时间)
- 功能9:翻译（中文转英文）


其余功能正在开发中，欢迎提建议  
英文版也许会开发，windows版本的也许也会开发，目前只适配Mac  
未来会与图灵机器人结合起来，深度开发  


## 运行要求
- 语言： python3
- 系统： Mac OS
- 浏览器： Google Chrome

## 用法
获取源码：`git clone git@github.com:edisonwong520/jarvis.git`  
进入源码目录： `cd jarvis`  
安装依赖： `pip install -r requirements.txt`  
运行Jarvis：  `python __main__.py`  


然后对着Jarvis发布命令，比如你可以说  
`贾维斯，来一首易燃易爆炸`  
`从机场到医院开车怎么走`  
`计时器1分20秒`  
`1分20秒后自动重启`  
`翻译今天天气不错`

## 备注
- 安装PyAudio出错的，需要先在Mac命令行运行brew install portaudio
- 打开浏览器部分要用到selenium,目前的解决办法是自动下载对应的驱动，解压，新开一个chrome，然后完成对应的浏览器操作,目前还没找到能复用已开的Chrome的方法，不够优雅-。- 


## 参考  
自动下载歌代码参考：https://github.com/ligongcheng/qq_music_downloader  
计时器功能代码参考：https://github.com/zhanzecheng/Time_NLP   
感谢以上作者，非商业用途,如有侵权,请告知我,及时删除  
