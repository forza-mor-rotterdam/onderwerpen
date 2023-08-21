from apps.categories.models import Category
from django.contrib import admin


class CategoryAdmin(admin.ModelAdmin):
    ...


admin.site.register(Category, CategoryAdmin)
