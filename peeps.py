import random
import operator
#person with first and last name in name and time list
class Person:
    def __init__(self,names,times,halls, number,fact,swipes):
        self.name = names
        self.times = times
        self.halls = halls
        self.number = number
        self.fact = fact
        self.swipes=swipes

    def amount_of_combos(self):
        return len(self.times)*len(self.halls)

class Group(object):
    def __init__(self, time, hall):
        self.people = []
        self.time = time
        self.hall = hall

    def size(self):
        return len(self.people)


# structure for availbaility list
class Availability(object):
    def __init__(self, time, hall):
        self.time = time
        self.hall = hall
        self.amount = 0

# global availability list, list of availabilities
# 5pm,6pm and 7pm respectively
availability_list = []

# global list of people , sorted by the number of available times
people_list = []

#global list of groups
group_list = []

#populates possible times list(MUST BE MORE THAN 3 TIMES)
def gettimes():
    times = [5,6,7,8]
    return times

#populates possible hall list
def gethalls():
    halls = ["De Neve", "Covel", "B-Plate"]
    return halls

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
    hallList = gethalls()
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
        halls = []
        rnd1 = random.randint(0, len(hallList) - 1)
        halls.append(hallList[rnd1])
        rnd2 = rnd1
        while rnd2 == rnd1:
            rnd2 = random.randint(0, len(hallList) - 1)
        if random.randint(0,1) == 0:
            halls.append(hallList[rnd2])
            rnd3 = rnd1
            while rnd3 == rnd1 or rnd3 == rnd2:
                rnd3 = random.randint(0, len(hallList) - 1)
            if random.randint(0,1) == 0:
                halls.append(hallList[rnd3])
        swipe = "#getonmylevel"
        swipeRand = random.randint(0,2)
        if swipeRand == 0:
            swipe = "im good"
        elif swipeRand == 1:
            swipe = "#thestruggle"
        name = name + " " + surname
        print(name, times, halls, swipe)
        x = Person(name, times, halls, 6616616661,"i like pie",swipe)
        people.append(x)
    return people

def createAtyList(times, halls):
    if(len(availability_list) != 0):
        print("Are you sure there bro, theres stuff in the availability list")
    for time in times:
        for hall in halls:
            x = Availability(time, hall)
            availability_list.append(x)

#make this better with if * in *
def populateAtyList(peeps):
    for peep in peeps: #for each person
        for time in peep.times: #for each time they are available
            for hall in peep.halls: #for each hall they are available
                for a in availability_list: #for each possible time
                    if a.time == time and a.hall == hall: #check to make sure its a perfect match
                        a.amount = a.amount + 1
                        #break prob good here idk python though

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
                for hall in person.halls:
                    if (group.time == time) and (group.hall == hall):
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
                if availability.hall in person.halls:
                    possibile_availabilities.append(availability)

        # get the max availability out of all possibile
        max_availability = possibile_availabilities[0]
        for availability in possibile_availabilities:
            if (availability.amount > max_availability.amount):
                max_availability = availability

        # add person to new group with time with max availability
        new_group = Group(max_availability.time, max_availability.hall);
        new_group.people.append(person)
        group_list.append(new_group)

#this method should be ran on the list of people before inserting them into groups normally
def insertSwipersAndSwipees(peeps):
    swipers = []
    swipees = []
    for peep in peeps:
        if "#thestruggle" in peep.swipes:
            swipees.append(peep)
        elif "#getonmylevel" in peep.swipes:
            swipers.append(peep)
    for needer in swipees: # for every person who needs a swipe
        foundGroup = False # at this point we have a match of times and halls
        for giver in swipers: # for every person who can give a swipe
            for neederHall in needer.halls: #for every hall the person needs a swipe
                if neederHall in giver.halls: #if the giver wants that hall
                    for neederTime in needer.times: #check every times to see matchs
                        if neederTime in giver.times:
                            for group in group_list: #check every group to see if an unfinished one that is similar exists
                                if group.time == neederTime and group.hall == neederHall and len(group.people) < 4:
                                    group.people.append(giver)
                                    group.people.append(needer)
                                    foundGroup = True
                            if not foundGroup:
                                newGroup = Group(neederTime, neederHall)
                                newGroup.people.append(giver)
                                newGroup.people.append(needer)
                            peeps.remove(giver) #remove the giver and needer from every list to avoid duplicates
                            peeps.remove(needer)
                            swipers.remove(giver)
                            swipees.remove(needer)
                            break # breaks for neederTime
                    if foundGroup:
                        break #breaks for neederHall
            if foundGroup:
                break #breaks for giver in swipers which will start at next
        if not foundGroup: #if after checking all the swpers there is no match
            for group in group_list:
                if group.hall == "Covel" and group.time == 8 and len(group.people) < 4:
                    group.people.append(needer)
                    foundGroup = True
            if not foundGroup:
                newGroup = Group(8, "Covel")
                newGroup.people.append(needer)
                foundGroup = True
            swipees.remove(needer)
            peeps.remove(needer)


def test(people):
    peeps = people
#    random.shuffle(peeps)
 #   random.shuffle(peeps)
    peeps.sort(key=operator.methodcaller("amount_of_combos"), reverse=False)
    insertSwipersAndSwipees(peeps)
    createAtyList(gettimes(), gethalls())
    populateAtyList(peeps)
    for peep in peeps:
        insert_into_groups(peep)
    counter = 0
    unfinished = []
    for group in group_list:
        print("GROUP ", counter, " at ", group.hall, group.time, ":")
        counter = counter +1
        if group.size() < 4:
            unfinished.append(group)
        for peep in group.people:
            print(peep.name, "had times: ", peep.times, "and halls: ", peep.halls, peep.swipes)
    for group in unfinished:
        print("INCOMPELTE GROUP at ", group.hall, group.time, ":")
        for peep in group.people:
            print(peep.name, "had times: ", peep.times, "and halls: ", peep.halls, peep.swipes)

test(getPeople(10))

