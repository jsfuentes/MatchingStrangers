# MatchingStrangers
Problem:
This code was needed for the several Dinner for 4 Strangers events held at UCLA for around 80 people. Given a list of people with avaliable times and dining halls, how do you efficiently and reliably match everyone in groups of 4?


Overview of algorithm:
Each person has an "availability number" corresponding to their dining halls * times
The algorithm puts people in groups in ascending order based on their number
  prioritizes unfinished groups(you can create empty groups before running the algorithm that will be filled)
  new groups are created in the most popular time slots left to have the best chance of being completed
