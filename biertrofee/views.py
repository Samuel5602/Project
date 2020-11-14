from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

from . import util

from .models import Player, TeamName, Poul, Team, Match

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
    util.create_matches(Team.objects.filter(poule=id))
    return render(request, "biertrofee/matches.html", {
        "matches": Match.objects.all(),
        "poule": Poul.objects.get(pk=id)
    })

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, "biertrofee/config.html")
        else:
            return render(request, "biertrofee/index.html", {
                "message": "Invalid credentials."
            })
    return render(request, "biertrofee/index.html")

def config(request):
    pass

def logout_view(request):
    logout(request)
    return render(request, "biertrofee/index.html")