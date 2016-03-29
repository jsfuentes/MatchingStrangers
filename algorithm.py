class Person(object):
    def __init__(self,name,times):
        self.name = name
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
    def __init__(self,time)
        self.time = time
        self.amount = 0

# global availability list, list of availabilities
# 5pm,6pm and 7pm respectively
availability_list = [Availability(5), Availability(6), Availability(7)]

# global list of people , sorted by the number of available times
people_list = []

#global list of groups
group_list = []

# insert intoa gropup,
# priority to unfinished groups with the least availbale people
# unless no unfinished groups, in which case we
# add person to the group with most availbale people
def insert_into_groups(person):
    unfinished_group_list = []
    # check if there are any unfinished groups
    for group in group_list:
        # skip full groups
        if (group.size == 4):
            continue

        # if there is an unfinished one
        if (group.size < 4):
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
            if (availability_list[group.time-5] < availability_list[chosen_group.time-5]):
                chosen_group = group

        # put the person in that one
        chosen_group.people.insert(person)
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



# the people with one time are put into a group automatically
def one_time_selected(person):
    insert_into_groups(person)
