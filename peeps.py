import random
import operator
import excelParser as exPar

#person defined in excelParser-
class Group(object):
    def __init__(self, time, dining):
        self.people = []
        self.time = time
        self.dining = dining

    def size(self):
        return len(self.people)

    def  __str__(self):
        returnStr = "GROUP "
        if hasattr(self, 'counter'):
            returnStr += str(self.counter) + " "
        return returnStr + "is at %s in %s" % (self.time, self.dining)





# structure for availability list
class Availability(object):
    def __init__(self, time, dining):
        self.time = time
        self.dining = dining
        self.amount = 0

# global availability list, list of availabilities
availability_list = []

# global list of people , needs to be sorted by the number of available times
people_list = []

#global list of groups, add groups here to seed program and control time/group location if possible(Group(time, "hall"))
group_list = [Group(7, "De Neve")]

#populates possible times list(MUST BE MORE THAN 3 TIMES)
def gettimes():
    times = [5,6,7,8]
    return times

#populates possible dining list
def getdinings():
    dinings = ["De Neve", "Covel", "B-Plate", "Feast", "Rendezvous"]
    return dinings

#populates possible hall list
def gethalls():
    halls = ["Acacia", "Birch", "Canyon Point", "Cedar", "Courtside",
    "Delta Terrace", "Dogwood", "Dykstra Hall", "Evergreen", "Fir", "Gardenia",
    "Hedrick Hall", "Hedrick Summit", "Hitch", "Holly", "Rieber Hall", "Rieber Vista",
    "Rieber Terrace", "Saxon", "Sproul Cove", "Sproul Hall", "Sproul Landing", "Sunset Village"]
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

#creates random people with random names, times, halls, and dinings
def getRandoms(numOfPeeps):
    timeList = gettimes()
    firstNames = getfirst()
    lastNames = getlast()
    diningList = getdinings()
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
        dinings = []
        rnd1 = random.randint(0, len(diningList) - 1)
        dinings.append(diningList[rnd1])
        rnd2 = rnd1
        while rnd2 == rnd1:
            rnd2 = random.randint(0, len(diningList) - 1)
        if random.randint(0,1) == 0:
            dinings.append(diningList[rnd2])
            rnd3 = rnd1
            while rnd3 == rnd1 or rnd3 == rnd2:
                rnd3 = random.randint(0, len(diningList) - 1)
            if random.randint(0,1) == 0:
                dinings.append(diningList[rnd3])
        hall = hallList[random.randint(0, len(hallList) - 1)]
        name = name + " " + surname
        print(name, times, dinings, hall)
        x = Person(name, times, dinings, hall)
        people.append(x)
    return people

def createAtyList(times, dinings):
    if(len(availability_list) != 0):
        print("Are you sure there bro, theres stuff in the availability list")
    for time in times:
        for dining in dinings:
            x = Availability(time, dining)
            availability_list.append(x)

#make this better with if * in *
def populateAtyList(peeps):
    for peep in peeps: #for each person
        for time in peep.times: #for each time they are available
            for dining in peep.dinings: #for each dining they are available
                for a in availability_list: #compare to every availablity list elements
                    if a.time == time and a.dining == dining: #check to make sure its a perfect match
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
                for dining in person.dinings:
                    if (group.time == time) and (group.dining == dining):
                        # add it to the unfinished gruop list
                        unfinished_group_list.append(group)
                        #  break this loop
                        break

    # if there are unfinished groups
    if (len(unfinished_group_list) != 0):
        # find the group with someone in the same hall as you
        chosen_group = unfinished_group_list[0]
        for group in unfinished_group_list:
            for peep in group.people:
                if peep.hall == person.hall:
                    chosen_group = group
        # put the person in that one
        chosen_group.people.append(person)
    # no unfinished groups
    else:
        # figure out which availbailities match the persons time
        possibile_availabilities = []
        for availability in availability_list:
            if availability.time in person.times:
                if availability.dining in person.dinings:
                    possibile_availabilities.append(availability)

        # get the max availability out of all possibile
        max_availability = possibile_availabilities[0]
        for availability in possibile_availabilities:
            if (availability.amount > max_availability.amount):
                max_availability = availability

        # add person to new group with time with max availability
        new_group = Group(max_availability.time, max_availability.dining);
        new_group.people.append(person)
        group_list.append(new_group)

def main():
    peeps = exPar.excel_to_personlist()
    peeps.sort(key=operator.methodcaller("amount_of_combos"), reverse=False)
    createAtyList(gettimes(), getdinings())
    populateAtyList(peeps)
    for peep in peeps:
        insert_into_groups(peep)
    counter = 0
    unfinished = []
    groupDoc = open("groups.txt","w")
    for group in group_list:
        #adds # to group for easier identification
        group.counter = counter
        groupDoc.write(group.__str__() + "\n")
        counter = counter + 1
        if group.size() < 4:
            unfinished.append(group)
        for peep in group.people:
            groupDoc.write(peep.__str__() + "\n")
    groupDoc.write("UNFINISHED GROUPS" + "\n")
    for group in unfinished:
        groupDoc.write(group.__str__() + "\n")
        for peep in group.people:
            groupDoc.write(peep.__str__() + "\n")

if __name__ == "__main__":
    main()
