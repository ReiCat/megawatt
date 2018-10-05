from django.contrib import admin
from django.urls import include, path

from apps.sites.views import SitesView

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Site
    path(r'', SitesView.as_view(), name='home'),
    path(r'', include('apps.sites.urls'))
]