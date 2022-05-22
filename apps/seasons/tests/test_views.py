import http

from django.test import TestCase
from django.urls import reverse
from wagtail.models import Page

from apps.seasons.models import SeasonPage
from apps.teams.models import Team


class TestSeasonView(TestCase):
    def setUp(self):
        self.root_page = Page.objects.get(slug='root')
        self.season_1 = SeasonPage(title='New Season', slug='new-season')
        self.season_2 = SeasonPage(title='Newest Season', slug='newest-season')
        self.root_page.add_child(instance=self.season_1)
        self.root_page.add_child(instance=self.season_2)
        self.season_1.save()
        self.season_2.save()

    def setup_teams(self):
        self.team_names = ['team 1', 'team 2', 'team 3']
        for team in self.team_names:
            Team.objects.create(name=team)

    def test_view_returns_http_ok_for_existing_season_object(self):
        self.url = reverse('season-view')
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_view_returns_last_season_in_context(self):
        self.url = reverse('season-view')
        response = self.client.get(self.url)

        self.assertEqual(response.context['object_list'].title, self.season_2.title)

    def test_view_returns_teams_in_context(self):
        self.setup_teams()

        self.url = reverse('season-view')
        response = self.client.get(self.url)

        self.assertEqual(len(response.context['teams']), len(self.team_names))

    def test_view_returns_correct_team_names(self):
        self.setup_teams()

        self.url = reverse('season-view')
        response = self.client.get(self.url)

        self.assertIn(response.context['teams'][0].name, self.team_names)
        self.assertIn(response.context['teams'][1].name, self.team_names)
        self.assertIn(response.context['teams'][2].name, self.team_names)
