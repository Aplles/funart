from django.urls import path

from api.views.category import CategoryListView
from api.views.coloring import ThemeListView

urlpatterns = [
    path("categories/", CategoryListView.as_view()),
    path("categories/<int:id>/themes/", ThemeListView.as_view()),
]

