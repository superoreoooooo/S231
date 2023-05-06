import time

now = time

print("Project/Data/Logs/log_" + str(now.localtime().tm_hour) + "_" + str(now.localtime().tm_min) + "_" + str(now.localtime().tm_sec) + ".txt")