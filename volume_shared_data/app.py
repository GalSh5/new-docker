#!/usr/local/bin/python3
# Import modules
import sys  # To get args
from time import sleep  # To sleep

FILE = "/data/file.txt"  # Datafile path
DOCKER = int(sys.argv[1])  # Get arguement

x = 5  # container 1 wakes up every x seconds
y = 8  # container 2 wakes u pevery y seconds
m = 12  # container 1 increases value by m
n = 18  # container 2 increases value by n

if DOCKER == 1:  # If container number 1
    while True:
        with open(FILE, 'a+') as f:  # Open file
            f.flush()  # Clear buffer
            f.seek(0)  # Go to start of file
            try:
                last_line = f.readlines()[-1]  # Get last line
                current_num = int(last_line.strip('\n'))
                line = current_num + m  # Set the line to write to the file
            except Exception as e:  # If file is empty
                line = m
            to_write = str(line) + "\n"
            f.write(to_write)  # Write data to file
        sleep(x)  # Sleep for x amount of time

elif DOCKER == 2:  # If container number 2
    while True:
        with open(FILE, 'a+') as f:  # Open file
            f.flush()  # Clear buffer
            f.seek(0)  # Go to start of file
            try:
                last_line = f.readlines()[-1]  # Get last line
                current_num = int(last_line.strip('\n'))
                line = current_num + n  # Set the line to write to the file
            except Exception as e:  # If file is empty
                line = n
            to_write = str(line) + "\n" 
            f.write(to_write)  # Write data to file
        sleep(y)  # Sleep for y amount of time

else:  # Else
    print("WRONG INPUT!")  # Let the user know the passed arguement was bad
