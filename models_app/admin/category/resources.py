from django.contrib import admin

from models_app.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_filter = ('name', 'created_at')
    list_display = [
        "id",
        "name",
        "description",
        "created_at",
        "updated_at",
    ]
    list_display_links = (
        "id",
        "name",
    )
    ordering = ("id", "created_at", "updated_at")
