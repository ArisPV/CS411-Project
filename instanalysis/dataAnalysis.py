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
    sortedByLikes = sorted(images,key=lambda l:l[2], reverse=True) #sort the imges by number of likes
    best_hastags = []

    times = []
    for i in range(len(images)): #convert unixtime to hour of day

        date = datetime.datetime.fromtimestamp(int(sortedByLikes[i][1]))
        hour = date.hour
        minute = date.minute
        if minute >= 10: finalTime = hour + 1
        else: finalTime = hour
        times += [finalTime]

    #print(times)


    hist = np.histogram(times, bins=list(range(0, 25)))#create histogram for hours of days as buckets



    for i in range(len(images)): #find most common hastags used
        best_hastags += sortedByLikes[i][3]
    best_hastag_counts = Counter(best_hastags)


    #return str(list(hist[0]))

    best_hastag_counts = dict(best_hastag_counts)

    timesHistogramValues = hist[0]
    timesHistogramBins   = hist[1]
 
    bestTimesIndexes = timesHistogramValues.argsort()[-3:][::-1] #get best 3 buckets from histogram
    bestTimesString =   str(timesHistogramBins[bestTimesIndexes[0]]) + " - " + str(timesHistogramBins[bestTimesIndexes[0] + 1]) + ", " + \
                        str(timesHistogramBins[bestTimesIndexes[1]]) + " - " + str(timesHistogramBins[bestTimesIndexes[1] + 1]) + " and "+ \
                        str(timesHistogramBins[bestTimesIndexes[2]]) + " - " + str(timesHistogramBins[bestTimesIndexes[2] + 1]) 
    


    #find most succesfull 5 hastags
    li = [(value,key) for key, value in best_hastag_counts.items()]
    li.sort()
    m = 5
    best5hastags = str([k for v, k in li[-m:]])


    googleResults = []
    for image in sortedByLikes:
        googleResults += image[-1]




    #get 3 res as googles best maches in most liked images
    res1 = most_common(googleResults)
    googleResults = list(filter(lambda a: a != res1, googleResults))
    print(res1)

    res2 = most_common(googleResults)
    googleResults = list(filter(lambda a: a != res2, googleResults))

    res3 = most_common(googleResults)
    googleResults = list(filter(lambda a: a != res3, googleResults))

    mostCommonGogleResults = [res1,res2,res3]
    print(mostCommonGogleResults)





    #return all findings
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

