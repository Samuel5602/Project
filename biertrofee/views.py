from django.shortcuts import render

from . import util

from .models import Player, TeamName, Poul, Team

# Create your views here.
def index(request):
    return render(request, "biertrofee/index.html")

def players(request):
    return render(request, "biertrofee/players.html", {
        "players": Player.objects.all()
    })

def player(request, player):
    player_name = Player.objects.get(pk=player)
    teams = TeamName.objects.filter(player=player_name)
    return render(request, 'biertrofee/player.html', {
        "teams": teams,
        "player": player
    })

def poules(request):
    return render(request, "biertrofee/poules.html", {
        "poules": Poul.objects.all()
    })

def poule(request, id):
    teams = Team.objects.filter(poule=id)
    return render(request, 'biertrofee/poule.html', {
        "teams": teams,
        "poule": Poul.objects.get(pk=id)
    })

def matches(request, id):
    matches = util.create_matches(Team.objects.filter(poule=id))
    return render(request, "biertrofee/matches.html", {
        "matches": matches,
        "poule": Poul.objects.get(pk=id)
    })