#--------------------------------------------------------------------
# TODO:
#   - lowercase() the contents of an early data set to prevent dupes
#   - filter (re.sub?) non alpha-numeric from early data set.
#   - consider input/raw_input for file selection/needed top X
#--------------------------------------------------------------------

import csv, itertools

#Read the contents of 'readsample.csv' and begin splitting it
incoming_data = open('readsample.csv', 'r').read().split()
delimited_data = [item.split(',') for item in incoming_data]

#Recombine the contents of the list into one meta list
remerged = list(itertools.chain(*delimited_data))

#Count the frequency of each word, and pair it as a dict entry
wordfreq = [remerged.count(p) for p in remerged]
dictionary = dict(zip(remerged, wordfreq))

#For each pair, sort by key (wordfreq) and reverse to top-down
aux = [(dictionary[key], key) for key in dictionary]
aux.sort()
aux.reverse()

#For the top 25 entries, print them
for a in aux[:25]:
    print a
