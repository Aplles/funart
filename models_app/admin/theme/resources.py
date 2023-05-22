from django.contrib import admin

from models_app.models import Theme
from models_app.admin.coloring.resources import ColoringInline


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_filter = ('name', 'created_at')
    list_display = [
        "id",
        "name",
        "description",
        "rating",
        'image',
        'category',
        "created_at",
        "updated_at",
    ]
    list_display_links = (
        "id",
        "name",
    )
    ordering = ("id", 'category', "created_at", "updated_at")
    inlines = [ColoringInline,]
