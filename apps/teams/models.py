from django.db import models
from wagtail.admin.panels import FieldPanel


class Team(models.Model):
    name = models.CharField(max_length=264)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
    )

    panels = [FieldPanel('name'), FieldPanel('image')]

    def __str__(self):
        return f'{self.name.title()}'

    def save(self, *args, **kwargs):
        if self.image:
            self.image.get_rendition('fill-32x32')
        super().save(*args, **kwargs)
