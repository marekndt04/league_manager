from django.test import TestCase
from wagtail.models import Page

from apps.seasons.models import SeasonPage


class TestSeasonModel(TestCase):
    def setUp(self):
        self.root_page = Page.objects.get(slug='root')

    def test_season_page_can_be_created(self):
        new_season = SeasonPage(title='New Season', slug='new-season')
        self.root_page.add_child(instance=new_season)
        new_season.save()

        db_instance = SeasonPage.objects.get(id=new_season.id)

        self.assertEqual(db_instance.title, new_season.title)

    def test_string_repr_of_season_page(self):
        new_season = SeasonPage(title='nice string', slug='nice-slug')

        self.assertEqual(str(new_season), 'nice string')
