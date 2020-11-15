from .models import Player, TeamName, Poul, Team, Match


def create_matches(teams, poule):
    for team1 in teams:
        for team2 in teams:
            if team1 is not team2:
                temp = Match(home=team1, away=team2, poule=poule)
                temp.save()

def fix_score(home, away, match):
    home_team = match.home
    away_team = match.away

    home = int(home)
    away = int(away)

    dif = abs(home-away)
    if home > away:
        home_team.points += 3
        home_team.goals += dif
        away_team.goals -= dif
    elif away > home:
        away_team.points += 3
        away_team.goals += dif
        home_team.goals -= dif
    else:
        home_team.points += 1
        away_team.points += 1

    home_team.save()
    away_team.save()

    match.home_score = home
    match.away_score = away
    match.filled_in = True
    match.save()
    
def reset():
    for team in Team.objects.all():
        team.points = 0
        team.goals = 0
        team.save()
    
    for match in Match.objects.all():
        match.home_score = 0
        match.away_score = 0
        match.filled_in = False
        match.save()