from django.urls import path
from apps.seasons.views import SeasonView

urlpatterns = [path('', SeasonView.as_view(), name='season-view')]
