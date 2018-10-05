from django.urls import path
from apps.sites.views import SitesView, SiteDetailView, SummaryView, SummaryAverageView


urlpatterns = [
    path(r'sites/', SitesView.as_view(), name='sites'),
    path(r'sites/<int:site_id>/', SiteDetailView.as_view(), name='sites'),
    path(r'summary/', SummaryView.as_view(), name='summary'),
    path(r'summary-average/', SummaryAverageView.as_view(), name='summary-average'),
]
