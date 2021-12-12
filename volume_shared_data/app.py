#!/usr/local/bin/python3
import sys
import os
from time import sleep

FILE = "/data/file.txt"
DOCKER = int(sys.argv[1])

x = 5  # container 1 wakes up every x seconds
y = 8  # container 2 wakes u pevery y seconds
m = 12  # container 1 increases value by m
n = 18  # container 2 increases value by n

if DOCKER == 1:
    while True:
        with open(FILE, 'a+') as f:
            f.flush()
            f.seek(0)
            try:
                last_line = f.readlines()[-1]
                current_num = int(last_line.strip('\n'))
                line = current_num + m
            except Exception as e:
                line = m
            to_write = str(line) + "\n"
            f.write(to_write)
        sleep(x)

elif DOCKER == 2:
    while True:
        with open(FILE, 'a+') as f:
            f.flush()
            f.seek(0)
            try:
                last_line = f.readlines()[-1]
                current_num = int(last_line.strip('\n'))
                line = current_num + n
            except Exception as e:
                line = n
            to_write = str(line) + "\n"
            f.write(to_write)
        sleep(y)

else:
    print("WRONG INPUT!")
