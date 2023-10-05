from apps.categories.models import Category
from django.contrib import admin


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "group")


admin.site.register(Category, CategoryAdmin)
