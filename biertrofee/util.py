from .models import Player, TeamName, Poul, Team, Match

matches = []

def create_matches(teams):
    matches = []
    for team1 in teams:
        for team2 in teams:
            if team1 is not team2:
                matches.append((team1.team.name, team2.team.name))
    print(len(matches))
    return matches