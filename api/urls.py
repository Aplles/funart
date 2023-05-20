from django.urls import path
from api.views.theme import ThemeListView

urlpatterns = [
    # Theme
    path('theme/', ThemeListView.as_view()),
]
