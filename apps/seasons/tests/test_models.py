import datetime
from django.test import TestCase
from wagtail.models import Page

from apps.seasons.models import Round, SeasonPage


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


class TestRoundModel(TestCase):
    def setUp(self):
        self.root_page = Page.objects.get(slug='root')
        self.season = SeasonPage(title='New Season', slug='new-season')
        self.root_page.add_child(instance=self.season)
        self.season.save()

    def test_round_page_can_be_created(self):
        new_round = Round(
            title='Round 1',
            start_date=datetime.datetime(2020, 1, 2, 12),
            end_date=datetime.datetime(2020, 1, 2, 12),
            slug='round-one',
        )
        self.season.add_child(instance=new_round)
        new_round.save()

        db_instance = Round.objects.last()

        self.assertEqual(new_round, db_instance)

    def test_string_repr_of_round_page(self):
        new_round = Round(
            title='Round 1',
            start_date=datetime.datetime(2020, 1, 2, 12),
            end_date=datetime.datetime(2020, 1, 2, 12),
            slug='round-one',
        )
        self.season.add_child(instance=new_round)
        new_round.save()

        self.assertEqual(str(new_round), 'Round 1')
