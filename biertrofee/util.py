from .models import Player, TeamName, Poul, Team, Match

def create_matches(teams, poule):
    for team1 in teams:
        for team2 in teams:
            if team1 is not team2:
                temp = Match(home=team1, away=team2, poule=poule)
                temp.save()

def fix_score(home, away, match):
    pass