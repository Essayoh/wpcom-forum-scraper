import os
import csv
from time import strftime
from string import punctuation

stop_words = [ "a", "i", "it", "am", "at", "on", "in", "to", "too", "very", "of", "from", "here", "even", "the", "but", "and", "is", "my", "them", "then", "this", "that", "than", "though", "so", "are", "you", "for", "with", "if", "can" ]

print ("What date would you like to count? Please use YYYY-MM-DD format.")
user_date = raw_input()
 
file = open(os.path.join("data/", user_date + ".txt"), "r")

file = file.read().lower()

for p in list(punctuation):
	file = file.replace(p,'')

file = ' '.join([word for word in file.split() if word not in stop_words])

wordcount={}

for word in file.split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1

csv_file = open(os.path.join("csv_output/", user_date + ".csv"), "w")

writer = csv.writer(csv_file)

for k,v in wordcount.items():
	writer.writerow([k,v])

print("Wordcount for " + user_date + " has been exported to " + user_date + ".csv" )