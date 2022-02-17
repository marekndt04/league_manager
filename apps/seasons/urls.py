from django.urls import path
from apps.seasons.views import SeasonView

urlpatterns = [path('seasons/<int:pk>', SeasonView.as_view(), name='season-view')]
