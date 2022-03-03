import http

from django.test import TestCase
from django.urls import reverse
from wagtail.core.models import Page

from apps.seasons.models import SeasonPage


class TestSeasonView(TestCase):
    def setUp(self):
        self.root_page = Page.objects.get(slug='root')
        self.season_1 = SeasonPage(title='New Season', slug='new-season')
        self.season_2 = SeasonPage(title='Newest Season', slug='newest-season')
        self.root_page.add_child(instance=self.season_1)
        self.root_page.add_child(instance=self.season_2)
        self.season_1.save()
        self.season_2.save()

    def test_view_returns_http_ok_for_existing_season_object(self):
        self.url = reverse('season-view')
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_view_returns_last_season_in_context(self):
        self.url = reverse('season-view')
        response = self.client.get(self.url)

        self.assertEqual(response.context['object_list'].title, self.season_2.title)
