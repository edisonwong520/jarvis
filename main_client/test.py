import os


def run(driver, args):
    time_dict = args
    sec_count = int(time_dict["daysdelta"]) * 24 * 3600 + int(time_dict["hour"]) * 3600 + int(
        time_dict["minute"]) * 60 + int(time_dict["second"])
    cmd = "#!/bin/sh\n" \
          "seconds_left={}\n" \
          "while [ $seconds_left -gt 0 ];do\n" \
          "sleep 1\n" \
          "seconds_left=$(($seconds_left - 1))\n" \
          "done\n" \
          "say '计时器时间到了！'".format(sec_count)

    os.system("echo '{}'>timer.sh &&nohup bash timer.sh &".format(cmd))
    print("计时器已经设定好了")
    os.system("say '计时器已经设定好了' ")

a={'year': 0, 'month': 0, 'day': 0, 'daysdelta': 0, 'hour': 0, 'minute': 0, 'second': 20}
run(a,a)