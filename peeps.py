import random
#person with first and last name in name and time list
class Person:
    def __init__(self,names,times):
        self.name = names
        self.times = times
    def amount_of_times(self):
        return len(self.times)

class Group(object):
    def __init__(self, time):
        self.people = []
        self.time = time

    def size(self):
        return len(self.people)


# structure for availbaility list
class Availability(object):
    def __init__(self,time):
        self.time = time
        self.amount = 0

# global availability list, list of availabilities
# 5pm,6pm and 7pm respectively
availability_list = [Availability(5), Availability(6), Availability(7)]

# global list of people , sorted by the number of available times
people_list = []

#global list of groups
group_list = []

#populates possible times list
def gettimes():
    times = [5,6,7]
    return times

#todo: make first names all uppercase or last names capitalized then lowercase
#populates potential first name list
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

#populates last name list
def getlast():
    namesDoc = open("lastNames.txt","r")
    names = []
    for line in namesDoc:
        line = line[:-1]#creates a substring
        line = line.split("\t")
        names.append(line[0])
    print(names)
    return names

#creates random people with random names and random times
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
        while rand2 == rand1: #ensures unique random time
            rand2 = random.randint(0, len(timeList) - 1)
        if random.randint(0,1) == 0: #50% chance to have 2 times
            times.append(timeList[rand2])
            rand3 = rand1
            while rand3 == rand1 or rand3 == rand2:
                rand3 = random.randint(0, len(timeList) - 1)
            if random.randint(0,1) == 0: #50% chance to have 3 if already has 2
               times.append(timeList[rand3])
        name = name + " " + surname
        print(name)
        print(times)
        x = Person(name, times)
        people.append(x)
    return people

def createAtyList(peeps):
    for peep in peeps: #for each person
        for time in peep.times: #for each time they are available
            for a in availability_list:
                if a.time == time:
                    a.amount = a.amount + 1

def insert_into_groups(person):
    unfinished_group_list = []
    # check if there are any unfinished groups
    for group in group_list:
        # skip full groups
        if (group.size() == 4):
            continue

        # if there is an unfinished one
        if (group.size() < 4):
            # if the group's time coincides with the person's time
            for time in person.times:
                if (group.time == time):
                    # add it to the unfinished gruop list
                    unfinished_group_list.append(group)
                    #  break this loop
                    break

    # if there are unfinished groups
    if (len(unfinished_group_list) != 0):
        # find the one with least availbable people
        chosen_group = unfinished_group_list[0]
        for group in unfinished_group_list:
            if (availability_list[group.time-5].amount < availability_list[chosen_group.time-5].amount):
                chosen_group = group

        # put the person in that one
        chosen_group.people.append(person)
    # no unfinished groups
    else:
        # figure out which availbailities match the persons time
        possibile_availabilities = []
        for availability in availability_list:
            if availability.time in person.times:
                possibile_availabilities.append(availability)

        # get the max availability out of all possibile
        max_availability = possibile_availabilities[0]
        for availability in possibile_availabilities:
            if (availability.amount > max_availability.amount):
                max_availability = availability

        # add person to new group with time with max availability
        new_group = Group(max_availability.time);
        new_group.people.append(person)
        group_list.append(new_group)

#todo: sort peeps by len(times) in ascending order
peeps = getPeople(12)
createAtyList(peeps)
for peep in peeps:
    insert_into_groups(peep)
counter = 0
for group in group_list:
    print ("GROUP ", counter, " at ", group.time, " has ")
    counter = counter + 1
    for peep in group.people:
        print(peep.name, "who had times", peep.times)



