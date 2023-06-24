import json

from django import forms
from django.core.paginator import Paginator
from django.db.models import Q
from service_objects.services import ServiceWithResult

from conf.settings.rest_framework import REST_FRAMEWORK
from models_app.models import Theme, Coloring


class SearchServices(ServiceWithResult):
    search = forms.CharField()
    page = forms.IntegerField(required=False, min_value=1)
    per_page = forms.IntegerField(required=False, min_value=1)

    def process(self):
        self._paginated_search()
        return self

    def _paginated_search(self):
        page = self.cleaned_data.get('page') or 1
        paginator = Paginator(
            self._search,
            self.cleaned_data.get("per_page") or REST_FRAMEWORK["PAGE_SIZE"],
        )
        page_info = {
            'has_previous': paginator.get_page(page).has_previous(),
            'has_next': paginator.get_page(page).has_next(),
            'num_page': json.dumps(page),
        }
        self.result = {
            'page_info': page_info,
            'object_list': paginator.page(page).object_list,
            'page_range': json.dumps([str(p) for p in paginator.page_range]),
        }

    @property
    def _search(self):
        # themes = Theme.objects.filter(
        #     Q(name__icontains=self.cleaned_data["search"]) |
        #     Q(description__icontains=self.cleaned_data["search"]) |
        #     Q(category__name__icontains=self.cleaned_data["search"]) |
        #     Q(category__description__icontains=self.cleaned_data["search"])
        # ).order_by("id")
        return Coloring.objects.select_related('theme', 'theme__category').filter(
            Q(name__icontains=self.cleaned_data["search"]) |
            Q(theme__name__icontains=self.cleaned_data["search"]) |
            Q(theme__description__icontains=self.cleaned_data["search"]) |
            Q(theme__category__name__icontains=self.cleaned_data["search"]) |
            Q(theme__category__description__icontains=self.cleaned_data["search"])
        ).order_by("id")