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

    home = int(float(home))
    away = int(float(away))

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
    match.save()
    