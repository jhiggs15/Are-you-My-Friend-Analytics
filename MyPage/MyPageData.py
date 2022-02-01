import csv
import random

import pandas
import names

from Constants import numberOfUsers, DataOutput


def dataframeToValidArray(fileName, columnName):
    dataframe = pandas.read_csv(fileName)
    dataframe[columnName] = dataframe[columnName].astype('str')
    filteredDataFrame = dataframe[(dataframe[columnName].str.len() <= 20)]
    return filteredDataFrame[columnName]

# Hobby csv found at https://www.kaggle.com/muhadel/hobbies
# Nationality csv found at https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/664133/CH_Nationality_List_20171130_v1.csv/preview
nationalityOptions = dataframeToValidArray("MyPage/nationalities.csv", "Nationality").sample(50).array
hobbyOptions = dataframeToValidArray("MyPage/hobbies.csv", "Hobby").array

def generateMyPageCSV():
    print("Generating MyPage Data...\n")

    # open/create myPage file
    with open(DataOutput + 'myPage.csv', 'w', newline='') as myPage :
        # setup file writer
        myPageFieldNames = ['ID', 'Name', 'Nationality', 'CountryCode', 'Hobby']
        myPageWriter = csv.DictWriter(myPage, fieldnames=myPageFieldNames)
        # create random users
        for userNumber in range(numberOfUsers) :
            if (userNumber+1) % 100 == 0:
                print("\rPercent Complete "+str( ((userNumber+1) / numberOfUsers) * 100 ) + "%", end =" ")
            myPageWriter.writerow(generateMyPage(userNumber+1)) # add 1 to start enumeration at 1

# generate a single users page
def generateMyPage(id):
    formatStr = "{0:<10}" # use this string to set the format for the strings, this sets is to be 20 characters long I think
    name = formatStr.format(names.get_full_name())
    countryCode = random.randint(0, len(nationalityOptions) - 1)  # gets a random integer that is an index to a nationality
    nationality = formatStr.format(nationalityOptions[countryCode])
    hobby = formatStr.format(random.choice(hobbyOptions))
    countryCode += 1
    return {'ID': id, 'Name': name, 'Nationality': nationality, 'CountryCode': countryCode, 'Hobby':hobby}

if __name__ == '__main__':
    generateMyPageCSV()
