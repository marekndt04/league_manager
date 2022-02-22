from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel


class Team(models.Model):
    name = models.CharField(max_length=264)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
    )

    panels = [FieldPanel('name'), ImageChooserPanel('image')]
