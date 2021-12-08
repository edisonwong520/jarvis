## Introdution
Jarvis：An intelligent assistant based voice control on Mac OS.  
中文版贾维斯Jarvis语音助手(电脑版Siri)  


## Functions
- Auto play music
- Auto download music
- Weather broadcast
- Simple caculator
- Road guide (base on GaodeMap)  
- Web search (base on Baidu)
- Timer
- Auto reboot/shutdown computer
- Translate (Chinese to English)

Note:  
Only base on Mac OS currently , maybe the windows version will be developed in the future. 


## Runtime
- Language： python3
- OS： Mac OS
- Web browser： Google Chrome

## Usage
`git clone git@github.com:edisonwong520/jarvis.git`  
`cd jarvis`  
`pip install -r requirements.txt`  
`python __main__.py`   
  
  
After run Jarvis ,you can say:  
  
  
`贾维斯，来一首易燃易爆炸`  
`从机场到医院开车怎么走`  
`计时器1分20秒`  
`1分20秒后自动重启`  
`翻译今天天气不错`

## Notice
- If error in installing PyAudio in Mac happends , make sure run `brew install portaudio` 
- Web broswer depends on selenium , so the program will install chrome driver automatically.(Maybe the code isn't elegent enough currently)


## Reference  
Auto download music：https://github.com/ligongcheng/qq_music_downloader  
Timer：https://github.com/zhanzecheng/Time_NLP    

Thanks for the program/author above. If there is any infringement, please contact me.  
感谢以上作者，非商业用途，如有侵权，请告知我，及时删除  
