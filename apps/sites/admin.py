from django.contrib import admin
from apps.sites.models import Site, Value


class ValueAdminInline(admin.StackedInline):
    model = Value
    extra = 1


class SiteAdmin(admin.ModelAdmin):
    inlines = [ValueAdminInline]


admin.site.register(Site, SiteAdmin)
