#import glob #for searching multiple dates eventually
import os
import csv
from time import strftime
import string

#next iteration: date ranges
print ("What date would you like to count? Please use YYYY-MM-DD format.")
user_date = raw_input()

#for name in glob.glob(("data/"+user_date+"*.txt")):
#    print name

#future iteration: strip out commonly used words
#probably a library for that
 
file = open(os.path.join("data/", user_date + ".txt"), "r")

file = file.read().translate(string.maketrans("",""), string.punctuation)


wordcount={}
for word in file.split():
    if word.lower() not in wordcount:
        wordcount[word.lower()] = 1
    else:
        wordcount[word.lower()] += 1

print wordcount 

#csv_file = open(user_date + ".csv", "w")

#writer = csv.writer(csv_file)

#for items in wordcount:
#    for k,v in wordcount.items():
#        writer.writerow([k,v])
#print("Wordcount for " + user_date + " has been exported to " + user_date + ".csv" )