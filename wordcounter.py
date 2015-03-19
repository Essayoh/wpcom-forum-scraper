import glob
import os
import csv

# wordcount={}

#next iteration: date ranges
#print ("What date would you like to count? Please use YYYY-MM-DD format.")
#user_date = raw_input()

#for name in glob.glob(("data/"+user_date+"*.txt")):
#    print name
 
file=open("sample.txt","r+")
wordcount={}
for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
for k,v in wordcount.items():
    print k, v

writer = csv.writer(ofile, dialect = 'excel')

for items in wordcount:
    for k,v in items.items():
        writer.writerow([k,v])