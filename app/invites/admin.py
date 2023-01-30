from django.apps import apps
from django.contrib import admin

from . import models


@admin.register(models.Invite)
class InviteAdmin(admin.ModelAdmin):
    list_display = ['name', 'confirmed', 'total_confirmed', 'id']
    ordering = ['confirmed', 'name']


app_models = apps.get_app_config('invites').get_models()

for model in app_models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
