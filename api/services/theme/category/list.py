import json

from django.core.paginator import Paginator
from service_objects.services import ServiceWithResult

from conf.settings.rest_framework import REST_FRAMEWORK
from models_app.models import Theme
from django import forms


class ThemeListByCategoryService(ServiceWithResult):
    id = forms.IntegerField()
    page = forms.IntegerField(required=False, min_value=1)
    per_page = forms.IntegerField(required=False, min_value=1)

    def process(self):
        self._paginated_themes()
        return self

    def _paginated_themes(self):
        page = self.cleaned_data.get("page") or 1
        paginator = Paginator(
            self._colorings,
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
    def _colorings(self):
        return Theme.objects.filter(category_id=self.cleaned_data["id"]).order_by("-updated_at")
