from django.contrib import admin

from models_app.models import Theme
from models_app.models import Coloring


class ListColorings(admin.StackedInline):
    model = Coloring
    readonly_fields = ('id', 'created_at', 'updated_at',)
    fieldsets = [
        ("Information", {'fields': ['name', 'image', 'updated_at', 'created_at', ]}),
    ]
    extra = 0


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_filter = ('name', 'created_at')
    inlines = (ListColorings,)
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
    readonly_fields = ("rating", )
    ordering = ("id", 'category', "created_at", "updated_at")
