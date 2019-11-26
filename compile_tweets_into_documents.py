#######
# This python script compiles all the tweets of a user seperated by row into one block of text in a singular row and writes it onto a .CSV
#######

import sys, csv, os, re, math, operator

tweets_per_user = ""
user = ""
prev_user = ""

data = csv.reader(iter(sys.stdin.readline,''))
first = True
with open('filtered_document_per_abused_user.csv', 'w') as csvStorage:
    csv_writer = csv.writer(csvStorage)
    # For every row in the original .CSV file
    for row in data:
        if first: # To start off.
            first = False
            user = row[0]
            tweets_per_user = row[1]
        else:
            prev_user = user
            user = row[0]
            if user != prev_user: # Start a new set of compiled tweet strings and append the old users one to the .CSV file
                csv_writer.writerow([prev_user, tweets_per_user])
                tweets_per_user = row[1]
            else:   # Continuously compile the tweets if the same user
                tweets_per_user = tweets_per_user + " " + row[1]

    