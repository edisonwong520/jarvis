import os

cur_path_list = os.getcwd().split("/")[:-1]
cur_path = "/".join(cur_path_list) + "/dependencies/chromedriver/chromedriver"

print(cur_path)