from enum import Enum
import hashlib

class ListStatus(Enum):
    NAUGHTY = 0,
    NICE = 1

class NaughtNiceList:
    year = 1975

    def __init__(self, year):
        self.year = year
    
    def checkList(self, firstName, lastName):
        lookUp = str(self.year) + firstName + lastName
        hashLookUp = hashlib.md5(lookUp.encode()).hexdigest()
        isNice = int(hashLookUp, 16)%2 == 1
        return ListStatus.NICE if isNice else ListStatus.NAUGHTY

    def writeStatus(self, status):
        if status == ListStatus.NICE:
            print("You are on the nice list!")
        elif status == ListStatus.NAUGHTY:
            print("Oh no... you have been naughty.")
        else:
            print("Status could not be determined!")

naughtNiceList = NaughtNiceList(2019)

firstName = input('What is your first name?: ')
lastName = input('What is your last name?: ')

status = naughtNiceList.checkList(firstName, lastName)
naughtNiceList.writeStatus(status)
