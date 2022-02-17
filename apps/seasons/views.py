from django.views.generic import DetailView

from apps.seasons.models import SeasonPage


class SeasonView(DetailView):
    model = SeasonPage
    template_name = 'seasons/seasonpage_detail.html'
