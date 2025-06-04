from django.urls import path
from .views import (
    RedirectView, CreateShortLinkView, ListShortLinksView,
    DeactivateLinkView, StatsView
)

urlpatterns = [
    path('<str:short_id>/', RedirectView.as_view()),
    path('api/create/', CreateShortLinkView.as_view()),
    path('api/list/', ListShortLinksView.as_view()),
    path('api/deactivate/<str:short_id>/', DeactivateLinkView.as_view()),
    path('api/stats/', StatsView.as_view()),
]
