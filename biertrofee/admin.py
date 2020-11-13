from django.contrib import admin

from .models import Player, TeamName, Poul, Team, Match

# Register your models here.
admin.site.register(Player)
admin.site.register(TeamName)
admin.site.register(Poul)
admin.site.register(Team)
admin.site.register(Match)