'''
Given an array of pairs representing the teams that have competed against 
each other and an array containing the results of each competition, write 
a function that returns the winner of the tournament. The input arrays are 
named competitions and results, respectively. The competitions array has 
elements in the form of [homeTeam, awayTeam], where each team is a string 
of at most 30 characters representing the name of the team. The results array 
contains information about the winner of each corresponding competition in the 
competitions array. Specifically, results[i] denotes the winner of competitions[i], 
where a 1 in the results array means that the home team in the corresponding 
competition won and a 0 means that the away team won. A team receives 3 points 
if it wins and 0 points if it loses. The winner of the tournament is the team 
that receives the most amount of points.

It's guaranteed that exactly one team will win the tournament and that each 
team will compete against all other teams exactly once. It's also guaranteed 
that the tournament will always have at least two teams.

Sample input: 
    competitions = [
        ["HTML", "C#"],
        ["C#", "Python"],
        ["Python", "HTML"],
        ]
    results = [0, 0, 1]

Sample output:
    "Python"
'''


def tournamentWinner_1(competitions, results):
    # Time: O(nlog(n)) | Space: O(k) where k is the number of teams
    team_dict = {}
    for i in range(len(results)):
        if results[i] == 0:
            winning_team = competitions[i][1]
            if winning_team not in team_dict:
                team_dict[winning_team] = 3
            else:
                team_dict[winning_team] += 3

        if results[i] == 1:
            winning_team = competitions[i][0]
            if winning_team not in team_dict:
                team_dict[winning_team] = 3
            else:
                team_dict[winning_team] += 3

    team_dict = dict(
        sorted(team_dict.items(), key=lambda item: item[1], reverse=True))
    print(f'team_dict: {team_dict}')

    return next(iter(team_dict))


def tournamentWinner_2(competitions, results):
    # Time: O(n) | Space: O(k) where k is the number of teams, we have k+1 because of
    #                     adding '' at the beginning
    HOME_TEAM_WON = 1

    current_best_team = ''
    scores = {current_best_team: 0}

    for i, competition in enumerate(competitions):
        result = results[i]
        # print(f'result: {result}')

        home_team, away_team = competition

        winning_team = home_team if result == HOME_TEAM_WON else away_team
        # print(f'winning_team: {winning_team}')

        update_score(winning_team, 3, scores)

        if scores[winning_team] > scores[current_best_team]:
            current_best_team = winning_team

    return current_best_team


def update_score(winning_team, score, scores):
    if winning_team not in scores:
        scores[winning_team] = 0

    scores[winning_team] += score


### Check ###
competitions = [
    ["AlgoMasters", "FrontPage Freebirds"],
    ["Runtime Terror", "Static Startup"],
    ["WeC#", "Hypertext Assassins"],
    ["AlgoMasters", "WeC#"],
    ["Static Startup", "Hypertext Assassins"],
    ["Runtime Terror", "FrontPage Freebirds"],
    ["AlgoMasters", "Runtime Terror"],
    ["Hypertext Assassins", "FrontPage Freebirds"],
    ["Static Startup", "WeC#"],
    ["AlgoMasters", "Static Startup"],
    ["FrontPage Freebirds", "WeC#"],
    ["Hypertext Assassins", "Runtime Terror"],
    ["AlgoMasters", "Hypertext Assassins"],
    ["WeC#", "Runtime Terror"],
    ["FrontPage Freebirds", "Static Startup"]
]

results = [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0]

print(f'Best team: {tournamentWinner_1(competitions, results)}')
