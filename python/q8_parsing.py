#The football.csv file contains the results from the English Premier League. 
# The columns labeled 'Goals' and 'Goals Allowed' contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in 'for' and 'against' goals.

# The below skeleton is optional.  You can use it or you can write the script with an approach of your choice.


import csv

class Season:
    teams = []
    data = []
    def __init__(self, fname):
        with open(fname) as data:
                reader = csv.DictReader(data)
                for row in reader:
                    self.teams.append(row['Team'])
                    self.data.append(row)

    def get_min_score_difference_team(self):
        scoreDiff = []
        for tName in self.teams:
            tData = self.get_team(tName)
            teamScoreDiff = abs(int(tData['Goals']) - int(tData['Goals Allowed']))
            scoreDiff.append(teamScoreDiff)
        return self.teams[scoreDiff.index(min(scoreDiff))]

    def get_team(self, team_name):
        return self.data[self.teams.index(team_name)]

fname = 'football.csv'
season = Season(fname)
print season.get_min_score_difference_team()
