from django.contrib import admin

from models_app.models import Coloring


@admin.register(Coloring)
class ColoringAdmin(admin.ModelAdmin):
    list_filter = ("type", "created_at")
    list_display = [
        "id",
        "name",
        "image",
        "type",
        "theme",
        "created_at",
        "updated_at",
    ]
    readonly_fields = ["id", "created_at", "updated_at"]
    list_display_links = (
        "id",
        "name",
    )
    ordering = ("id", "theme", "created_at", "updated_at")
