from django.db import models


class Team(models.Model):
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
    )
