#!/usr/bin/env python3
## create file object in "r"ead mode
line = 0

configfile = open("vlanconfig.cfg", "r")
## readlines() creates a list by reading target
## file line by line
configfile_lines = configfile.readlines()

    for line in configfile
        linecount += 1
    else
        print("The number of lines is", line)

## file was just auto closed (no more indenting)

## each item of the list now has the "\n" characters back
#print(configfile)
configfile.close()

