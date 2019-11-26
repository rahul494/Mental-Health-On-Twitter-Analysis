#!/usr/bin/python

#######
# This Pythons script serves as a Mapper for the Docker HDFS MapReduce stage. It is used to map the top words by score.
#######

import csv, sys, re

keywords = ['abuse', 'eatingdisorders', 'nostigma', 'presspause', 'addiction', 'endthestigma', 'nostigmas', 'mentalhealthmatters', 'alzheimers', 'IAmStigmaFree', '1SmallAct', 'ocd', 'anxiety', 'mentalhealth', 'psychology', 'suicideprevention', 'bipolar', 'pts', 'mhchat', 'therapy', 'bpd', 'anxiety', 'schizophrenia', 'trauma', 'Operationalstress', 'therapy', 'ptsd', 'mhsm', 'endthestigma', 'psychology', 'worldmentalhealthday', 'trauma', 'AA', 'schizophrenia', 'stress', 'spsm', 'mentalhealthmatters', 'stigma', 'wellbeing', 'alcoholism', 'mentalhealthawareness', 'stopsuicide', 'adhd', 'depressed', 'mentalillness', 'suicide', 'bpd', 'depression', 'MH', 'shellshock']

sums = {}
data = csv.reader(iter(sys.stdin.readline,''))
for row in data:
    for word in row[1].split():
        word = re.sub(r'(\[)|(\])|(\')|(,)','',word)
        if word not in keywords:
            print(word + "\t1")