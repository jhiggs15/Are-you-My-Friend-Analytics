# The MyPage dataset should have the following attributes for each Facebook page:
#     ID: unique sequential number (integer) from 1 to 200,000 indicating
#       the owner of the page (there will be 200,000 lines)
# sequentially

# Name: characters  of  length  between  10  and  20  (do  not  use  commas
# inside this string)
# pip install names

# Nationality: characters  of  length  between  10  and  20  (do  not  use  commas
# inside this string)
# array of most common nationalities
# ["American", "Chinese", "German", "English", "Mexican", "Russian"]

# CountryCode: number (integer) between 1 and 50
# random number

# Hobby: sequence of characters of length between 10 and 20
# array of common hobbies
# [
import math
import random
import csv
import pandas
import names
from os.path import exists
# nationalityOptions = ["American", "Chinese", "German", "English", "Mexican", "Russian"]

numberOfUsers = 10
# both are initalized later
nationalityOptions = []
hobbyOptions = []

def myPageCSV():
    # initialize random seed
    random.seed(100)
    # open/create myPage file
    with open('myPage.csv', 'w', newline='') as myPage :
        # setup file writer
        myPageFieldNames = ['ID', 'Name', 'Nationality', 'CountryCode', 'Hobby']
        myPageWriter = csv.DictWriter(myPage, fieldnames=myPageFieldNames)
        # create random users
        for userNumber in range(numberOfUsers) :
            myPageWriter.writerow(generateMyPage(userNumber+1)) # add 1 to start enumeration at 1


# writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
# https://pypi.org/project/names/
def generateMyPage(id):
    formatStr = "{0:<10}" # use this string to set the format for the strings, this sets is to be 20 characters long I think
    name = formatStr.format(names.get_full_name())
    countryCode = math.trunc(random.random() * len(nationalityOptions))
    nationality = formatStr.format(nationalityOptions[countryCode])
    countryCode += 1 # set country code to start at 1
    hobby = formatStr.format(random.choice(hobbyOptions))
    return {'ID': id, 'Name': name, 'Nationality': nationality, 'CountryCode': countryCode, 'Hobby':hobby}

if __name__ == '__main__':
    # if files dont exist create them
    hobbyOptionsDF = pandas.read_csv("hobbies.csv")
    hobbyOptionsDF['HOBBIES'] = hobbyOptionsDF['HOBBIES'].astype('str')
    hobbyOptions = hobbyOptionsDF[(hobbyOptionsDF['HOBBIES'].str.len() <= 20)]
    hobbyOptions = hobbyOptions['HOBBIES'].array

    nationalityOptionsDF = pandas.read_csv("nationalities.csv")
    nationalityOptionsDF['Nationality'] = nationalityOptionsDF['Nationality'].astype('str')
    nationalityOptions = nationalityOptionsDF[(nationalityOptionsDF['Nationality'].str.len() <= 20)]
    nationalityOptions = nationalityOptions['Nationality'].array

    myPageCSV()