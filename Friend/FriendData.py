import csv
import random

from Constants import numberOfFriends, numberOfUsers, dateRange, DataOutput

# used to ensure repeated relationships do not happen
#   person 1 cannot be friends with person 2 twice
relationships = set()


class Relationship:
    def __init__(self, personID, myFriend):
        self.personID = personID
        self.myFriend = myFriend

    # To string methods
    def __str__(self):
        return "(" + str(self.personID) + "->" + str(self.myFriend) + ")"
    def __repr__(self):
        return str(self)

    # Equality operations to work with sets
    def __hash__(self):
        return hash((self.personID, self.myFriend))
    def __eq__(self, other):
        return isinstance(other, Relationship) \
               and other.myFriend == self.myFriend \
               and  other.personID == self.personID


# idea from https://stackoverflow.com/questions/29938804/generate-random-sentences-in-python
noun = ["They", "These two"]
wayToMeet = ["met eachother in", "have been friends since", "have a mutual friend from", "played sports together in", "had class together in"]
place = ["college", "highschool", "graduate school", "primary school" ]

def generateRandomFriendDescriptor():
    randNoun = random.randint(0, len(noun) - 1)
    randWayToMeet = random.randint(0, len(wayToMeet) -1)
    randPlace = random.randint(0, len(place) - 1)
    return noun[randNoun] + " " + wayToMeet[randWayToMeet] + " " + place[randPlace]

def generateFriendsCSV():
    # open/create myFriends file
    print("Generating Friend Data...\n")
    with open(DataOutput +'friends.csv', 'w', newline='') as friend :
        # setup file writer
        friendFieldNames = ['FriendRel', 'PersonID', 'MyFriend', 'DateofFriendship', 'Desc']
        friendWriter = csv.DictWriter(friend, fieldnames=friendFieldNames)
        # create random users
        for relationshipNumber in range(numberOfFriends) :
            if (relationshipNumber+1) % 100 == 0:
                print("\rPercent Complete "+str( ((relationshipNumber+1) / numberOfFriends) * 100 ) + "%", end =" ")
            friendWriter.writerow(generateFriend(relationshipNumber + 1))

def generateFriend(id):
    formatStr = "{0:<10}" # use this string to set the format for the strings, this sets is to be 20 characters long I think
    personID = random.randint(1, numberOfUsers)
    myFriend = random.randint(1, numberOfUsers)
    desc = generateRandomFriendDescriptor()
    relationshipsLength = len(relationships)
    dateOfFriendship = random.randint(1, dateRange)

    while len(relationships) == relationshipsLength:
        if myFriend != personID :
            relationships.add(Relationship(personID, myFriend))
        myFriend = random.randint(1, numberOfUsers)


    return {'FriendRel': id, 'PersonID': personID, 'MyFriend': myFriend, 'DateofFriendship': dateOfFriendship, 'Desc': desc}


if __name__ == '__main__':
    generateFriendsCSV()