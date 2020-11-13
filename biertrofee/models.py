from django.db import models

DEFAULT_PLAYER_ID = 1

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=64, primary_key=True)

    def __str__(self):
        return self.name

class TeamName(models.Model):
    name = models.CharField(max_length=64)
    abbreviation = models.CharField(max_length=3)
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="player", default=DEFAULT_PLAYER_ID)

    def __str__(self):
        return self.name

class Poul(models.Model):
    name = models.CharField(max_length=1)

    def __str__(self):
        return self.name    

class Team(models.Model):
    team = models.ForeignKey(TeamName, on_delete=models.CASCADE, related_name="team")
    poule = models.ForeignKey(Poul, on_delete=models.CASCADE, related_name="poule", default=DEFAULT_PLAYER_ID)
    points = models.IntegerField(default=0)
    goals = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.team}-poule"

class Match(models.Model):
    home = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="home")
    away = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="away")
    home_score = models.IntegerField(default=0)
    away_score = models.IntegerField(default=0)
    

    def __str__(self):
        return f"{self.home} - {self.away}"

    
