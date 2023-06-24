from django.contrib import admin

from models_app.models import Theme, Coloring


class ColoringInline(admin.TabularInline):
    model = Coloring
    extra = 10


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_filter = ('name', 'created_at')
    list_display = [
        "id",
        "name",
        "description",
        "rating",
        'image',
        "created_at",
        "updated_at",
    ]
    list_display_links = (
        "id",
        "name",
    )
    ordering = ("id", 'category', "created_at", "updated_at")
    filter_horizontal = ['category', ]
    inlines = [ColoringInline, ]

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.all().distinct('id')