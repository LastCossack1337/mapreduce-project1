#!/usr/bin/python

from operator import itemgetter
import sys

for line in sys.stdin:
    vehiclecolor = line.split(",")[33].strip()

    if vehiclecolor:
        issuecolor = str(vehiclecolor)
        issuecolor == "Vehicle Color"
        continue
    else:

        print("%s\t%s" % (issuecolor, 1))
