from django.urls import path

from api.views.category import CategoryListView

urlpatterns = [
    path("categories/", CategoryListView.as_view()),
]

