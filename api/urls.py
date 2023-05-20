from django.urls import path

from api.views.theme import ThemeListView
from api.views.category import CategoryListView
from api.views.theme import ThemeListByCategoryView
from api.views.coloring import ColoringListView, ColoringListBySearchView

urlpatterns = [
    # Category
    path("categories/", CategoryListView.as_view()),
    path("categories/<int:id>/themes/", ThemeListByCategoryView.as_view()),

    # Theme
    path('themes/', ThemeListView.as_view()),
    path('themes/<int:id>/colorings/', ColoringListView.as_view()),

    # Search
    path('search/', ColoringListBySearchView.as_view()),
]
