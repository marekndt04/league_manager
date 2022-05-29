import datetime
from django.forms import ValidationError
from django.test import TestCase
from wagtail.models import Page

from apps.seasons.models import Game, Season, Round
from apps.seasons.models.orderables import GameTeam
from apps.teams.models import Team


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
        self.team_1 = Team.objects.create(name='Team 1')
        self.team_2 = Team.objects.create(name='Team 2')

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

    def test_game_page_has_related_teams(self):
        new_game = Game(
            title='Game 1',
            slug='game-one',
        )
        self.round.add_child(instance=new_game)
        new_game.save()
        team_1 = Team.objects.create(name='Team 1')
        team_2 = Team.objects.create(name='Team 2')
        game_team_1 = GameTeam.objects.create(page=new_game, team=team_1, goals=3, host=True)
        game_team_2 = GameTeam.objects.create(page=new_game, team=team_2, goals=2, host=False)

        db_instance = Game.objects.last()

        self.assertIn(game_team_1, db_instance.gameteam_set.all())
        self.assertIn(game_team_2, db_instance.gameteam_set.all())

    def test_game_page_cant_be_save_with_one_team(self):
        new_game = Game(
            title='Game 1',
            slug='game-one',
        )
        self.round.add_child(instance=new_game)
        new_game.save()
        game_team_1 = GameTeam.objects.create(page=new_game, team=self.team_1, goals=3, host=True)
        game_team_2 = GameTeam.objects.create(page=new_game, team=self.team_2, goals=2, host=False)

        db_instance = Game.objects.last()

        self.assertIn(game_team_1, db_instance.gameteam_set.all())
        self.assertIn(game_team_2, db_instance.gameteam_set.all())

    def test_clean_model_raises_error_with_duplicated_teams(self):
        new_game = Game(
            title='Game 1',
            slug='game-one',
        )
        self.round.add_child(instance=new_game)
        new_game.save()
        GameTeam.objects.create(page=new_game, team=self.team_1, goals=3, host=True)
        GameTeam.objects.create(page=new_game, team=self.team_1, goals=2, host=False)

        with self.assertRaises(ValidationError):
            new_game.clean()

    def test_clean_model_raises_error_with_duplicated_host_values(self):
        new_game = Game(
            title='Game 1',
            slug='game-one',
        )
        self.round.add_child(instance=new_game)
        new_game.save()
        GameTeam.objects.create(page=new_game, team=self.team_1, goals=3, host=True)
        GameTeam.objects.create(page=new_game, team=self.team_2, goals=2, host=True)

        with self.assertRaises(ValidationError):
            new_game.clean()
