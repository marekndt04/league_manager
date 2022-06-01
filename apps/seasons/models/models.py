from django.db import models
from django.forms import ValidationError
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, InlinePanel


class Season(Page):
    subpage_types = ['seasons.Round']


class Round(Page):
    parent_page_types = ['seasons.Season']
    subpage_types = ['seasons.Game']

    start_date = models.DateField('Start Date')
    end_date = models.DateField('End Date')

    content_panels = Page.content_panels + [
        FieldPanel('start_date'),
        FieldPanel('end_date'),
    ]


class Game(Page):
    parent_page_types = ['seasons.Round']

    panels = [InlinePanel(relation_name='gameteam_set', heading='Game Teams', min_num=2, max_num=2)]
    content_panels = Page.content_panels + panels

    def clean(self):
        super().clean()
        try:
            game_team_1 = self.gameteam_set.all()[0]
            game_team_2 = self.gameteam_set.all()[1]
        except IndexError:
            return
        if game_team_1.team == game_team_2.team:
            raise ValidationError('Teams can not be duplicated')
        if game_team_1.host and game_team_2.host:
            raise ValidationError('Host value can not be duplicated')


class SeasonTeamPoints(models.Model):
    season = models.ForeignKey('seasons.Season', on_delete=models.CASCADE)
    team = models.ForeignKey('teams.Team', on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    goals_scored = models.IntegerField(default=0)
    goals_lost = models.IntegerField(default=0)
