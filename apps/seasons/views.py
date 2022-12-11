from django.db.models import Prefetch
from django.views.generic import ListView
from wagtail.images import get_image_model

from apps.seasons.models import Season
from apps.teams.models import Team


class SeasonView(ListView):
    template_name = 'seasons/seasonpage_detail.html'
    queryset = Season.objects.all()

    def get_context_data(self, **kwargs):
        renditions_queryset = (
            get_image_model().get_rendition_model().objects.filter(filter_spec__in=["fill-32x32"])
        )
        context = super().get_context_data(**kwargs)
        context['teams'] = (
            Team.objects.select_related('image')
            .prefetch_related(Prefetch('image__renditions', queryset=renditions_queryset))
            .all()
        )
        return context
