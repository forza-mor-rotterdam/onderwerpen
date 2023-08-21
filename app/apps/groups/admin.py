from apps.groups.models import Group
from django.contrib import admin


class GroupAdmin(admin.ModelAdmin):
    ...


admin.site.register(Group, GroupAdmin)
