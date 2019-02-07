import time
sleep_s = int(input("How many minutes to sleep?\n"))*60
print('Set alarm on: ' + str(time.ctime(int(time.time()) + sleep_s))[11:16])
