#!/usr/bin/python

import sys

for line in sys.stdin:
    line = line.split(",")
    vehiclecolor = line[33]
    try:
        issuecolor = str(vehiclecolor)
        print (("%s\t%s") % (issuecolor, 1))
    except ValueError:
        continue
