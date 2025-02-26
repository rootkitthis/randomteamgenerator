import random

#function that takes list of anames and splits them into a specified number of teams
def splitTeams(names, numberOfTeams):
    random.shuffle(names) #randomizes list of names

    teams = [] #emply list to store number of teams

    #creates an empty lists for each team
    for i in range(numberOfTeams):
        teams.append([])

    teamIndex = 0

    #loops through each name in fanodm name list and adds it to a team
    for i in range(len(names)):
        teams[teamIndex].append(names[i])
        teamIndex += 1

        if teamIndex == numberOfTeams:
            teamIndex = 0
    return teams #returns the list of teams with their assgined names that were randomized

names = []  #Creates an empty list to store names of people
numberOfPeople = int(input("Enter the Number of People to Choose from:  ")) # Gets the number of people to assign to teams from user input

print(f'Enter the names of {numberOfPeople} people') # Prompts user to enter the names of the people

#For loop that takes user input for names and stores in names variable
for i in range(numberOfPeople):
    name = input(f"Name {i+1}: ") 
    names.append(name) 

numberOfTeams = int(input("Enter the number of teams you want to split the people into: ")) # Ask for the number of teams


# Check if number of teams is valid and prints error if innvalid. 
#if not invalid runs main logic 
if numberOfTeams <= 0 or numberOfTeams > numberOfPeople:
    print("Invalid number of teams. Please enter a number between 1 and the number of people.")
else:
    teams = splitTeams(names, numberOfTeams)  # Split the names into the specified number of teams

    # Prints names in an easy to read table
    print(f"\n{'Name':<20}{'Team':<10}")
    print("-" * 30)

    teamNumber = 1  # Start team number count at 1

    #Nested For Loop that iterates over teams list and names list and prints them
    for team in teams:
        for name in team:
            print(f"{name:<20}{'Team ' + str(teamNumber):<10}")
        teamNumber += 1
