# -*- coding: utf-8 -*-

from CmdInter import CmdClient
import Audio
import PluginsManager
import WordParse


class Jarvis():
    def __init__(self):

        self.pm = PluginsManager.Platform()
        self.action_list = self.pm.get_all_plugin()

    # def run(self):
    #     try:
    #
    #         # cmdclient = CmdClient()
    #         # while(1):
    #         #     cmdclient.onecmd("hello") #tend to speak recognize
    #         #     # cmdclient.cmdloop(intro="Hi,I'm Jarvis")
    #         #     cmdclient.onecmd("me")
    #
    #         result = Audio.listen()
    #         if result:
    #             print("识别的语句是:" + result[0])
    #
    #         # result is a tuple
    #         result = WordParse.word_parse(result[0])
    #
    #         self.findAction(result[0],result[1])
    #
    #
    #     except Exception as e:
    #         print(str(e))
    #         print("Sorry,something wrong happend")
    #         exit()

    def run(self):

        # cmdclient = CmdClient()
        # while(1):
        #     cmdclient.onecmd("hello") #tend to speak recognize
        #     # cmdclient.cmdloop(intro="Hi,I'm Jarvis")
        #     cmdclient.onecmd("me")

        # speack recognize
        result=["放一首k歌之王"]
        # result = Audio.listen()
        if result:
            print("识别的语句是:" + result[0])

        # result = ['1乘2+3']

        word = WordParse.word_parse(result[0])
        # word[1] is a tuple
        self.findAction(word[0], word[1])

    def findAction(self, keyword, args):
        if keyword not in self.action_list:
            print("Sorry,I don't understannd your command")

        else:

            plugin = self.pm.load_plugins(keyword, args)

    def getAllAct(self):
        pass
