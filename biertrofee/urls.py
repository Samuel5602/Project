from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("players", views.players, name="players"),
    path("players/<str:player>", views.player, name="player"),
    path("poules", views.poules, name="poules"),
    path("poules/<int:id>", views.poule, name="poule"),

    path("poules/<int:id>/matches", views.matches, name="matches")
]