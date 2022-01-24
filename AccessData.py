# AccessId: unique sequential number (integer) from 1 to 10,000,000
# ByWho: References the Id of the person who has accessed the Facebook page
# WhatPage: References the Id of the page that was accessed
# TypeOfAccess: text  of  characters  of  length  between  20  and  50  explaining  if  just
# viewed, left a note, added a friendship, etc.
# AccessTime: random number between 1 and 1,000,000 (or epoch time)
import math
import random
import csv

numberOfAccess = 200
numberOfUsers = 20000
maxTime = 1000000
accessTypeOptions = ['viewed', 'left a note', 'sent a message']

def accessCVS():
    # initialize random seed
    random.seed(100)
    # open/create myPage file
    with open('accessLog.csv', 'w', newline='') as myPage :
        # setup file writer
        myPageFieldNames = ['ID', 'ByWho', 'WhatPage', 'TypeOfAccess', 'AccessTime']
        myPageWriter = csv.DictWriter(myPage, fieldnames=myPageFieldNames)
        # create random users
        for accessNumber in range(numberOfAccess) :
            myPageWriter.writerow(generateAccessRow(accessNumber+1)) # add 1 to start enumeration at 1


def generateAccessRow(id):
    formatStr = "{0:<20}" # use this string to set the format for the strings, this sets is to be 20 characters lon
    byWho = math.trunc(random.random() * numberOfUsers)
    whatPage = math.trunc(random.random() * numberOfUsers)
    while byWho == whatPage: # keep retrying until pages are different
        math.trunc(random.random() * numberOfUsers)
    typeOfAccess = formatStr.format(random.choice(accessTypeOptions))
    time = math.ceil(random.random() * maxTime)
    return {'ID': id, 'ByWho': byWho, 'WhatPage': whatPage, 'TypeOfAccess': typeOfAccess, 'AccessTime':time}

if __name__ == '__main__':
    accessCVS()
