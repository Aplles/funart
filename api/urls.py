from django.urls import path

from api.views.coloring import ColoringListView
from api.views.theme import ThemeListView
from api.views.category import CategoryListView
from api.views.theme import ThemeListByCategoryView

urlpatterns = [
    # Category
    path("categories/", CategoryListView.as_view()),
    path("categories/<int:id>/themes/", ThemeListByCategoryView.as_view()),

    # Theme
    path('themes/', ThemeListView.as_view()),
    path('themes/<int:id>/colorings/', ColoringListView.as_view()),
]
