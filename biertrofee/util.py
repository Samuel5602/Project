from .models import Player, TeamName, Poul, Team, Match

def create_matches(teams):
    Match.objects.all().delete()
    for team1 in teams:
        for team2 in teams:
            if team1 is not team2:
                temp = Match(team1, team2)
                temp.save()