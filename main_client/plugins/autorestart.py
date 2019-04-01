import os


def run(driver, args):
    time_dict = args[0]
    sec_count = int(time_dict["daysdelta"]) * 24 * 3600 + int(time_dict["hour"]) * 3600 + int(
        time_dict["minute"]) * 60 + int(time_dict["second"])
    time_word = ""
    if int(time_dict["hour"]) != 0:
        time_word += "{}小时".format(time_dict["hour"])
    if int(time_dict["minute"]) != 0:
        time_word += "{}分".format(time_dict["minute"])
    if int(time_dict["second"]) != 0:
        time_word += "{}秒".format(time_dict["second"])

    cur_path_list = os.getcwd().split("/")[:-1]
    bash_path = "/".join(cur_path_list) + "/main_client/run_bash/"

    cmd = "#!/bin/sh\n" \
          "seconds_left={}\n" \
          "while [ $seconds_left -gt 0 ];do\n" \
          "sleep 1\n" \
          "seconds_left=$(($seconds_left - 1))\n" \
          "done\n" \
          "say '您设定的{}自动重启时间到了！正在为您自动重启'\n".format(sec_count, time_word)
    long_cmd= """osascript -e 'tell app """+r"""\"System Events\" to restart' """
    os.system("mkdir -p {}".format(bash_path))
    os.system("echo '{}'>{}restart.sh ".format(cmd, bash_path))
    os.system("""echo "{}">>{}autorestart.sh """.format(long_cmd,bash_path))
    os.system("nohup bash {}autorestart.sh &".format(bash_path))
    print("自动重启设定好了")
    os.system("say '自动重启设定好了' ")
