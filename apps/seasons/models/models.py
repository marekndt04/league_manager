from django.db import models
from django.forms import ValidationError
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, InlinePanel

from apps.seasons.models.orderables import GameTeam


class SeasonTeamStandings(models.Model):
    season = models.ForeignKey('seasons.Season', on_delete=models.CASCADE)
    team = models.ForeignKey('teams.Team', on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    goals_scored = models.IntegerField(default=0)
    goals_lost = models.IntegerField(default=0)


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

    def save(self, clean=True, user=None, log_action=False, **kwargs):
        print('how many save')
        season_page = self.get_ancestors().exact_type(Season)[0].specific
        game_team_query = self.gameteam_set.all()

        if game_team_query:
            team_points = self._set_team_points(game_team_query)
            for idx, game_team in enumerate(game_team_query):
                if idx == 0:
                    rival_id = idx + 1
                else:
                    rival_id = idx - 1
                try:
                    standing = SeasonTeamStandings.objects.get(
                        season=season_page,
                        team=game_team.team,
                    )

                    if self._check_game_has_not_changed():
                        continue

                    standing.goals_scored = standing.goals_scored + game_team.goals
                    standing.goals_lost = (
                        standing.goals_lost + self.gameteam_set.all()[rival_id].goals
                    )
                    standing.points = standing.points + team_points[idx]
                    standing.save()

                except SeasonTeamStandings.DoesNotExist:
                    SeasonTeamStandings.objects.create(
                        season=season_page,
                        team=game_team.team,
                        goals_scored=game_team.goals,
                        goals_lost=self.gameteam_set.all()[rival_id].goals,
                        points=team_points[idx],
                    )

        return super().save(clean, user, log_action, **kwargs)

    def _set_team_points(self, game_team_query):
        game_team_1 = game_team_query[0]
        game_team_2 = game_team_query[1]

        if game_team_1.goals > game_team_2.goals:
            team_1_points = 3
            team_2_points = 0
        elif game_team_1.goals < game_team_2.goals:
            team_1_points = 0
            team_2_points = 3
        elif game_team_1.goals == game_team_2.goals:
            team_1_points = 1
            team_2_points = 1
        return team_1_points, team_2_points

    def _check_game_has_not_changed(self):
        has_not_changed = True
        for game_team in self.gameteam_set.all():
            try:
                current_game_team = GameTeam.objects.get(id=game_team.id, page_id=game_team.page_id)
                if (
                    not current_game_team.goals == game_team.goals
                    and not current_game_team.team == game_team.team
                ):
                    has_not_changed = False
            except GameTeam.DoesNotExist:
                pass

        return has_not_changed
