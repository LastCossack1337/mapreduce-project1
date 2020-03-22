#!/usr/bin/python

from operator import itemgetter
import sys

for line in sys.stdin:
    vehiclecolor = line.split(",")[33].strip()
    vehiclecolor = vehiclecolor.strip("Vehicle Color")

    if vehiclecolor:
        issuecolor = str(vehiclecolor)
        print("%s\t%s" % (issuecolor, 1))
