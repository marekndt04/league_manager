from django.views.generic import ListView

from apps.seasons.models import SeasonPage
from apps.teams.models import Team


class SeasonView(ListView):
    template_name = 'seasons/seasonpage_detail.html'
    queryset = SeasonPage.objects.last()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teams'] = Team.objects.all()

        return context
