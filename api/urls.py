from django.urls import path

from api.views.theme import ThemeListCreateView, ThemeListByCategoryView, ThemeListBySearchView, ThemePopularListView
from api.views.category import CategoryListView
from api.views.coloring import ColoringListCreateView, ColoringDetailView, ColoringDownloadView, ColoringAllDetailView

urlpatterns = [
    # Category
    path("categories/", CategoryListView.as_view()),
    path("categories/<int:id>/themes/", ThemeListByCategoryView.as_view()),

    # Theme
    path('themes/', ThemeListCreateView.as_view()),
    path('themes/populars/', ThemePopularListView.as_view()),
    path('themes/<int:id>/colorings/', ColoringListCreateView.as_view()),

    # Coloring
    path('colorings/', ColoringAllDetailView.as_view()),
    path('colorings/<int:id>/', ColoringDetailView.as_view()),
    path('colorings/<int:id>/download/', ColoringDownloadView.as_view()),

    # Search
    path('search/', ThemeListBySearchView.as_view()),

]
