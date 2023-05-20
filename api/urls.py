from django.urls import path

from api.views.category import CategoryListView
from api.views.theme import ThemeListByCategoryView

urlpatterns = [
    path("categories/", CategoryListView.as_view()),
    path("categories/<int:id>/themes/", ThemeListByCategoryView.as_view()),
]

