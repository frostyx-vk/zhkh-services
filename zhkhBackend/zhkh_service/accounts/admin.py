from django.contrib import admin

from accounts.models import ProfilePortal


@admin.register(ProfilePortal)
class ProfilePortalAdmin(admin.ModelAdmin):
    pass