#!/usr/bin/python

from operator import itemgetter
import sys

# Dictionary with all the colors that you have identified so far
color_dict = {
    "BLACK":["BLK","BLACK","BLA","BK"],
    "WHITE":["WHITE","WHT","WHIT","WH","WT"],
    "GRAY":["GRAY","GR","GY","GRY"]
}

for line in sys.stdin:
    vehiclecolor = line.split(",")[33].strip()
    vehiclecolor = vehiclecolor.strip("Vehicle Color")

    if vehiclecolor:
        testcolor = str(vehiclecolor).upper()
        issuecolor = testcolor
        for k,v in color_dict.items():
            if testcolor in v:
                issuecolor = k
        print("%s\t%s" % (issuecolor, 1))
