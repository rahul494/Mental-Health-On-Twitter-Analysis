#######
# This python script performs a TF-iDF computation to get the top 50 words of a users tweets based on the other users tweets. Document = all of the <200 Tweets collected PER USER. Collection = All of the Tweets collected.
#######

import sys, csv, os, re, math, operator, time

map_of_csv = {}
N = 0

# A function that retrieves the term frequency of a word within the tweets of users it exists in
def calculate_tf(term, tweets_of_user):
    tf = 0
    for word in tweets_of_user.split():
        if word == term:
            tf = tf + 1
    return tf

# A function that retrieves the document frequency of a word, as in how many times it amongst users
def calculate_df(term):
    df = 0
    for user in map_of_csv:
        if term in map_of_csv[user]:
            df = df + 1
    return df

# This function calculates the weight of each word using the N, TF and DF. It then sorts the words with their weights and only takes the top 50.
def get_top_words_of_user(user):
    words_and_scores = {}
    top_50_words = []
    tweets_of_user = map_of_csv[user]
    for word in tweets_of_user.split():
        tf = calculate_tf(word, tweets_of_user)
        df = calculate_df(word)
        w = (1+math.log10(tf))*(math.log10(N/df))
        words_and_scores[word] = w
    sorted_words_and_scores = sorted(words_and_scores.items(), key=operator.itemgetter(1), reverse=True)
    for i in range(0, 50):
        if len(sorted_words_and_scores) > i:
            top_50_words.append(sorted_words_and_scores[i][0])
    return top_50_words

# This portion of the script goes through the .CSV of all users tweets and calculates TF-IDF to get the top 50 words.
with open('top_abused_words_per_user_filtered.csv', 'w') as csvStorage:
    original_time = time.time()
    csv_writer = csv.writer(csvStorage)
    data = csv.reader(iter(sys.stdin.readline,''))
    for row in data:
        user = row[0]
        tweets = row[1]
        map_of_csv[user] = tweets
    i = 0
    N = len(map_of_csv)
    for user in map_of_csv:
        start_time = time.time()
        top_50_words = get_top_words_of_user(user)
        csv_writer.writerow([user, top_50_words])
        i = i + 1
        print("User: " + user + " is completed at the " + str(i) + "-th iteration.\nTime taken: " + str(time.time()-start_time) + ". \nTotal time thus far: " + str(time.time()-original_time))
        print("-------------------------------")
