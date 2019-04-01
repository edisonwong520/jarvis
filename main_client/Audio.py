from aip import AipSpeech
import speech_recognition as sr
import os

""" 你的 APPID AK SK """
APP_ID = '15759315'
API_KEY = 'zgQFArTgCV9V7znq0bEdGrAe'
SECRET_KEY = 'OsF4m1GsmZHp6IWdfkBXI3WchaD2cqGK'

"""
dev_pid
1536	普通话(支持简单的英文识别)	搜索模型	无标点	支持自定义词库
1537	普通话(纯中文识别)	输入法模型	有标点	不支持自定义词库
1737	英语		无标点	不支持自定义词库
1637	粤语		有标点	不支持自定义词库
1837	四川话		有标点	不支持自定义词库
1936	普通话远场	远场模型	有标点	不支持
"""

file_location = "./input_voice/"


def getAudio():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        os.system("say '请问我能为您做些什么？'")
        print("请问我能为您做些什么？")
        audio = r.listen(source)

        with open(file_location + "input.wav", "wb") as f:
            f.write(audio.get_wav_data(convert_rate=16000))
            return True

    return False


# 识别本地文件
def listen():
    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

    input_filename = file_location + "input.wav"  # 麦克风采集的语音输入
    # input_filepath = "/Users/edison/PycharmProjects/aip-python-sdk-2.0.0/Jarvis/voice/"  # 输入文件的path
    # in_path = input_filepath + input_filename

    # get the audio
    getAudio()

    os.system("say '正在识别中'")
    result = client.asr(getFileContent(input_filename), 'pcm', 16000, {
        'dev_pid': 1536,
    })

    # print(result)
    if result["err_no"] != 0:
        print("语音识别失败,错误码{}".format(result['err_no']))
        return []
    else:
        print("识别结果:" + result["result"][0])
        return result["result"]


# 读取文件
def getFileContent(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
