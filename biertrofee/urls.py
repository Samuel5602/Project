from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("players", views.players, name="players"),
    path("players/<str:player>", views.player, name="player"),
    path("poules", views.poules, name="poules"),
    path("poules/<int:id>", views.poule, name="poule"),

    path("poules/<int:id>/matches", views.matches, name="matches"),
    path("poules/<int:id>/matches/score", views.score, name="score"),

    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("config", views.config, name="config"),
    path("login/create_matches", views.create_matches, name="create_matches"),
    path("login/reset", views.reset, name="reset")
]