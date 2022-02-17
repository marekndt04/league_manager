import http

from django.test import TestCase
from django.urls import reverse
from wagtail.core.models import Page

from apps.seasons.models import SeasonPage


class TestSeasonView(TestCase):
    def setUp(self):
        self.root_page = Page.objects.get(slug='root')

    def test_view_returns_http_ok_for_existing_object(self):
        new_season = SeasonPage(title='New Season', slug='new-season')
        self.root_page.add_child(instance=new_season)
        new_season.save()

        self.url = reverse('season-view', args=[new_season.id])
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_view_returns_http_not_found_for_unexisting_object(self):
        self.url = reverse('season-view', args=[666])
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, http.HTTPStatus.NOT_FOUND)
