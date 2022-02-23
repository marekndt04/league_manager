from django.test import TestCase
from wagtail.images import get_image_model

from ..models import Team


class TestTeamModel(TestCase):
    def setUp(self):
        self.test_image_1 = get_image_model()

    def test_smth(self):
        new_team = Team.objects.create(name='new team', image=self.test_image_1)

        db_model = Team.objects.get(id=new_team.id)

        self.assertAlmostEqual(new_team.id, db_model.id)
