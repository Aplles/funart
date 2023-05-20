from django.urls import path
from api.views.theme import ThemeListView

from api.views.category import CategoryListView

urlpatterns = [
    path("categories/", CategoryListView.as_view()),

    # Theme
    path('theme/', ThemeListView.as_view()),
]
