import cmd
import os
import readline

readline.parse_and_bind('tab: complete')


class CmdClient(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = "-> "  # define command prompt

    def do_quit(self, arg):
        return True

    def do_hello(self, arg):
        print("say hello")

    def emptyline(self):
        print('Sir,what can I do for you?')

    def do_me(self, arg):
        print('iteme')

    def default(self, line):
        print("Sir,what can I do for you?")
        print(line)

    # define the shortcuts
    do_q = do_quit
