from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel


class Season(Page):
    subpage_types = ['seasons.Round']


class Round(Page):
    parent_page_types = ['seasons.Season']
    subpage_types = ['seasons.Game']

    start_date = models.DateField('Start Date')
    end_date = models.DateField('End Date')

    content_panels = Page.content_panels + [
        FieldPanel('start_date'),
        FieldPanel('end_date'),
    ]


class Game(Page):
    parent_page_types = ['seasons.Round']
