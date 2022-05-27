import datetime
from django.test import TestCase
from wagtail.models import Page

from apps.seasons.models import Game, Season, Round


class TestSeasonModel(TestCase):
    def setUp(self):
        self.root_page = Page.objects.get(slug='root')

    def test_season_page_can_be_created(self):
        new_season = Season(title='New Season', slug='new-season')
        self.root_page.add_child(instance=new_season)
        new_season.save()

        db_instance = Season.objects.get(id=new_season.id)

        self.assertEqual(db_instance.title, new_season.title)

    def test_string_repr_of_season_page(self):
        new_season = Season(title='nice string', slug='nice-slug')

        self.assertEqual(str(new_season), 'nice string')


class TestRoundModel(TestCase):
    def setUp(self):
        self.root_page = Page.objects.get(slug='root')
        self.season = Season(title='New Season', slug='new-season')
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


class TestGameModel(TestCase):
    def setUp(self):
        self.root_page = Page.objects.get(slug='root')
        self.season = Season(title='New Season', slug='new-season')
        self.root_page.add_child(instance=self.season)
        self.season.save()
        self.round = Round(
            title='Round 1',
            start_date=datetime.datetime(2020, 1, 2, 12),
            end_date=datetime.datetime(2020, 1, 2, 12),
            slug='round-one',
        )
        self.season.add_child(instance=self.round)
        self.round.save()

    def test_game_page_can_be_created(self):
        new_game = Game(
            title='Game 1',
            slug='game-one',
        )
        self.round.add_child(instance=new_game)
        new_game.save()

        db_instance = Game.objects.last()

        self.assertEqual(new_game, db_instance)

    def test_string_repr_of_game_page(self):
        new_round = Game(
            title='Game 1',
            slug='game-one',
        )
        self.round.add_child(instance=new_round)
        new_round.save()

        self.assertEqual(str(new_round), 'Game 1')
