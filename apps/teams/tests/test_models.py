from django.test import TestCase
from wagtail.images.models import Image
from wagtail.images.tests.utils import get_test_image_file

from apps.teams.models import Team


class TestTeamModel(TestCase):
    def setUp(self):
        self.test_image = Image.objects.create(title='New Image', file=get_test_image_file())

    def test_model_can_be_created(self):
        new_team = Team.objects.create(name='new team', image=self.test_image)

        db_model = Team.objects.get(id=new_team.id)

        self.assertEqual(new_team.id, db_model.id)

    def test_string_repr_capitalize_name(self):
        new_team = Team.objects.create(name='new team', image=self.test_image)

        db_model = Team.objects.get(id=new_team.id)

        self.assertEqual(str(db_model), 'New Team')
