# MatchingStrangers
Given a list of people with avaliable times and dining halls, how do you efficiently and reliably match everyone in groups of 4.
This code was used for the several dining for 4 strangers event held at UCLA for around 80 people.

Rundown of algorithm:
Each person has an "availability number" corresponding to their dining halls * times
The algorithm puts people in groups in ascending order based on their number
  prioritizes unfinished groups
  new groups are created in the most popular time slots left to have the best chance of being completed
