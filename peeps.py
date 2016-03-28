import random
class Person:
    def _init_(self,names,times):
        self.name = names
        self.times = times

def gettimes():
    timesDoc = open("times.txt","r")
    times = []
    for line in timesDoc:
        line = line[:-1]#creates a substring without end line character
        times.append(line)
    print(times)
    return times

def getfirst():
    namesDoc = open("names.txt","r")
    names = []
    for line in namesDoc:
        line = line[:-1]#creates a substring
        strList = line.split("\t")
        strList.remove(strList[0])
        names.extend(strList)
    print(names)
    return names

def getlast():
    namesDoc = open("lastNames.txt","r")
    names = []
    for line in namesDoc:
        line = line[:-1]#creates a substring
        line = line.split("\t")
        names.append(line[0])
    print(names)
    return names

def getPeople(numOfPeeps):
    timeList = gettimes()
    firstNames = getfirst()
    lastNames = getlast()
    people = []
    for i in range(0, numOfPeeps):
        name = firstNames[random.randint(0, len(firstNames) - 1)]
        surname = lastNames[random.randint(0, len(lastNames) - 1)]
        times = []
        rand1 = random.randint(0, len(timeList) - 1)
        times.append(timeList[rand1])
        rand2 = rand1
        while rand2 == rand1:
            rand2 = random.randint(0, len(timeList) - 1)
        if random.randint(0,1) == 0:
            times.append(timeList[rand2])
            rand3 = rand1
            while rand3 == rand1 or rand3 == rand2:
                rand3 = random.randint(0, len(timeList) - 1)
            if random.randint(0,1) == 0:
               times.append(timeList[rand3])
        name = name + " " + surname
        print(name)
        print(times)
        x = Person(name, times)
        people.append(x)

print(random.randint(0, 10))
getPeople(10)
