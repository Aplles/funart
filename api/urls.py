from django.urls import path
from api.views.theme import ThemeListView
from api.views.coloring import ColoringListView
from api.views.category import CategoryListView

urlpatterns = [
    path("categories/", CategoryListView.as_view()),

    # Theme
    path('themes/', ThemeListView.as_view()),
    path('themes/<int:id>/colorings/', ColoringListView.as_view()),
]
