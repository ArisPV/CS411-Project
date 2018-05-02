from collections import Counter
import datetime
import numpy as np
from api_main import api_main
import itertools
import operator

#from db import output_db




import json


def goForItBaby():

    
    #try:
    JSON_File = open("access_token.json","r")
    print("")
    images = api_main(JSON_File)
    print("\n\n\n\ngoForItBaby is done getting images")
        

    print(images)
    sortedByLikes = sorted(images,key=lambda l:l[2], reverse=True)
    best_hastags = []

    times = []
    for i in range(len(images)):

        date = datetime.datetime.fromtimestamp(int(sortedByLikes[i][1]))
        hour = date.hour
        minute = date.minute
        if minute >= 10: finalTime = hour + 1
        else: finalTime = hour
        times += [finalTime]

    #print(times)


    hist = np.histogram(times, bins=list(range(0, 25)))


    for i in range(len(images)):
        best_hastags += sortedByLikes[i][3]
    best_hastag_counts = Counter(best_hastags)


    #return str(list(hist[0]))

    best_hastag_counts = dict(best_hastag_counts)

    timesHistogramValues = hist[0]
    timesHistogramBins   = hist[1]

    bestTimesIndexes = timesHistogramValues.argsort()[-3:][::-1]
    bestTimesString =   str(timesHistogramBins[bestTimesIndexes[0]]) + " - " + str(timesHistogramBins[bestTimesIndexes[0] + 1]) + ", " + \
                        str(timesHistogramBins[bestTimesIndexes[1]]) + " - " + str(timesHistogramBins[bestTimesIndexes[1] + 1]) + " and "+ \
                        str(timesHistogramBins[bestTimesIndexes[2]]) + " - " + str(timesHistogramBins[bestTimesIndexes[2] + 1]) 
    



    li = [(value,key) for key, value in best_hastag_counts.items()]
    li.sort()
    m = 5
    best5hastags = str([k for v, k in li[-m:]])


    googleResults = []
    for image in sortedByLikes:
        googleResults += image[-1]

    print(googleResults)
    res1 = most_common(googleResults)
    googleResults = list(filter(lambda a: a != res1, googleResults))
    print(res1)



    res2 = most_common(googleResults)
    googleResults = list(filter(lambda a: a != res2, googleResults))

    res3 = most_common(googleResults)
    googleResults = list(filter(lambda a: a != res3, googleResults))

    mostCommonGogleResults = [res1,res2,res3]
    print(mostCommonGogleResults)



    #flattened_list = [y for x in list_of_lists for y in x]




    return (best5hastags,bestTimesString,mostCommonGogleResults) #dictionary with key as hastag and val as number of occurance






def most_common(L):
  # get an iterable of (item, iterable) pairs
  SL = sorted((x, i) for i, x in enumerate(L))
  # print 'SL:', SL
  groups = itertools.groupby(SL, key=operator.itemgetter(0))
  # auxiliary function to get "quality" for an item
  def _auxfun(g):
    item, iterable = g
    count = 0
    min_index = len(L)
    for _, where in iterable:
      count += 1
      min_index = min(min_index, where)
    # print 'item %r, count %r, minind %r' % (item, count, min_index)
    return count, -min_index
  # pick the highest-count/earliest item
  return max(groups, key=_auxfun)[0]

