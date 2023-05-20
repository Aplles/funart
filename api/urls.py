from django.urls import path
from api.views.theme import ThemeListView

from api.views.category import CategoryListView
from api.views.coloring import ColoringListView

urlpatterns = [
    # Category
    path("categories/", CategoryListView.as_view()),
    path("categories/<int:id>/themes/", ColoringListView.as_view()),

    # Theme
    path('theme/', ThemeListView.as_view()),
]
