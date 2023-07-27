from django.urls import path

from api.views.theme import ThemeListView, ThemeListByCategoryView, ThemeListBySearchView, ThemePopularListView
from api.views.category import CategoryListView
from api.views.coloring import ColoringListView, ColoringDownloadView

urlpatterns = [
    # Category
    path("categories/", CategoryListView.as_view()),
    path("categories/<int:id>/themes/", ThemeListByCategoryView.as_view()),

    # Theme
    path('themes/', ThemeListView.as_view()),
    path('themes/populars/', ThemePopularListView.as_view()),
    path('themes/<int:id>/colorings/', ColoringListView.as_view()),


    path('colorings/<int:id>/download/', ColoringDownloadView.as_view()),

    # Search
    path('search/', ThemeListBySearchView.as_view()),

]
