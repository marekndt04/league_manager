from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.models import Orderable


class GameTeam(Orderable):
    page = ParentalKey('seasons.Game')
    team = models.ForeignKey('teams.Team', null=True, on_delete=models.SET_NULL)
    goals = models.IntegerField()
    host = models.BooleanField()
