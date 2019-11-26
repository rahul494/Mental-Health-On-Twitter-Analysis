#######
# This Python scripts orders the MapReduce output from highest to lowest summed terms
#######

import sys, csv, os, re, math, operator, time

storage = {}

for line in sys.stdin:
    value, key = line.split()
    storage[key] = int(value)
    
sorted_storage = sorted(storage.items(), key=operator.itemgetter(1), reverse=True)

for key,value in sorted_storage:
    print(key + "," + str(value))