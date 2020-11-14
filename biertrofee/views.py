from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse

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
    return render(request, "biertrofee/matches.html", {
        "matches": Match.objects.filter(poule=id),
        "poule": Poul.objects.get(pk=id)
    })

def score(request, id):
    if request.method == "POST":
        home_score = request.POST["home_score"]
        away_score = request.POST["away_score"]
        match = request.POST["match"]
        util.fix_score(home_score, away_score, match)
        return HttpResponseRedirect(reverse("matches", args=[id]))


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

def create_matches(request):
    for i in range(1, len(Poul.objects.all())+1):
        util.create_matches(Team.objects.filter(poule=i), Poul.objects.get(id=i))
    return render(request, "biertrofee/config.html")