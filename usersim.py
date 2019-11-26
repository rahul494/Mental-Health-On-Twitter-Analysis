#######
# This python script calculates the similarity between two .txt files containing the top $LIMIT words of users claiming certain mental illnesses/exerpeicnes. For example, compaing users top words who have claimed suicidal and comparing users top words who have claimed depressed.
#######

import sys, csv, os, re, math, operator, time

storage1 = []
storage2 = []

i = 1
limit = 100
for line in open(sys.argv[1]):
    key, value = line.split(",")
    if i <= limit:
        storage1.append(key)
        i = i + 1
    
j = 1
for line in open(sys.argv[2]):
    key, value = line.split(",")
    if j <= limit:
        storage2.append(key)
        j = j + 1
        

listIntersection = (len(set(storage1) & set(storage2)))
listUnion = (len(set(storage1) | set(storage2)))

print("The similar between user types is: " + str(listIntersection/listUnion))