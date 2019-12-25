from enum import Enum
import hashlib
import csv

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

class Person:
    def __init__(self, firstName, lastName, status):
        self.firstName = firstName
        self.lastName = lastName
        self.status = status

naughtNiceList = NaughtNiceList(2019)

people = []
niceSum = 0
naughtySum = 0

with open('nameList.csv', newline='') as nameList:
    nameReader = csv.reader(nameList, delimiter=',', quotechar='"')
    rowCount = 0
    for row in nameReader:
        if rowCount > 0:
            firstName = row[0]
            lastName = row[1]
            status = naughtNiceList.checkList(firstName, lastName)
            if status == ListStatus.NICE:
                niceSum += 1
            elif status == ListStatus.NAUGHTY:
                naughtySum += 1
            people.append(Person(firstName, lastName, status))
        rowCount += 1

print(f"Number of nice: {niceSum}, naughty: {naughtySum}")